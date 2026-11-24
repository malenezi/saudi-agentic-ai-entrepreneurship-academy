#!/usr/bin/env python3
# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Replay a recorded run of a real language model through the workflows' own nodes. Standard library and Node.js.

    python3 tools/n8n_replay_model.py              score every recorded run
    python3 tools/n8n_replay_model.py --prompts DIR   write the exact prompts each workflow sends, one file per workflow

A recorded run is a file of model outputs, one per test case, kept beside the workflows in
real-model-runs/. Each output is what a language model returned for the system prompt and the
single user message that the workflow's Prepare node builds for that case. The replay hands each
output to the Decide node in place of the HTTP node's answer (tools/n8n_harness.js) and compares
the result with the case's expected result, exactly as the simulated run is compared.

What this proves: that the instructions produce output the Decide node can read and act on
correctly, for that model, on these invented cases. What it does not prove: anything about n8n's
HTTP node with that model, latency, cost, or behaviour on real customer messages.
Cases that carry their own "_model_response" are guard tests with a canned bad answer; they are
not model cases and are left out of the score.
"""
import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOWS = os.path.join(ROOT, "05-agentic-ai-lab", "agent-templates", "workflows")
RUNS = os.path.join(WORKFLOWS, "real-model-runs")
LAB = os.path.join(ROOT, "03-courses", "02-build", "labs", "n8n", "order-agent.n8n.json")
REFERENCE = os.path.join(ROOT, "03-courses", "02-build", "labs", "reference")
HARNESS = os.path.join(ROOT, "tools", "n8n_harness.js")
sys.path.insert(0, REFERENCE)
sys.path.insert(0, os.path.join(ROOT, "tools"))

from n8n_e2e import contains  # noqa: E402
from order_agent.evaluate import first_wrong_step, load  # noqa: E402
from order_agent.tools import Store  # noqa: E402

LAB_STAGE = "stage-3-cycle-2"


def read(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def harness(workflow, requests, overrides):
    with tempfile.TemporaryDirectory() as tmp:
        paths = []
        for name, value in (("requests.json", requests), ("overrides.json", overrides)):
            paths.append(os.path.join(tmp, name))
            with open(paths[-1], "w", encoding="utf-8") as f:
                json.dump(value, f, ensure_ascii=False)
        done = subprocess.run(["node", HARNESS, workflow] + paths, capture_output=True, text=True, encoding="utf-8")
    if done.returncode:
        raise SystemExit(done.stderr)
    return json.loads(done.stdout)


def prompts(workflow, cases, overrides):
    """The system prompt and user message the Prepare node builds for each case."""
    script = r"""
const fs=require('fs');const [w,c,o]=process.argv.slice(1);
const wf=JSON.parse(fs.readFileSync(w,'utf8'));const cases=JSON.parse(fs.readFileSync(c,'utf8'));
const node=n=>wf.nodes.find(x=>x.name===n);
const cfg=Object.assign(JSON.parse(node('Config').parameters.jsonOutput),JSON.parse(fs.readFileSync(o,'utf8')),{model_mode:'http'});
process.stdout.write(JSON.stringify(cases.map((body,i)=>{const outputs={Webhook:{body},Config:cfg};
const $=n=>({first:()=>({json:outputs[n]})});
const p=new Function('$input','$','$getWorkflowStaticData',node('Prepare').parameters.jsCode)({first:()=>({json:cfg})},$,()=>({}))[0].json;
return {id:i+1,system:p.request_body.messages[0].content,user:p.request_body.messages[1].content};}),null,1));
"""
    with tempfile.TemporaryDirectory() as tmp:
        paths = []
        for name, value in (("cases.json", cases), ("overrides.json", overrides)):
            paths.append(os.path.join(tmp, name))
            with open(paths[-1], "w", encoding="utf-8") as f:
                json.dump(value, f, ensure_ascii=False)
        done = subprocess.run(["node", "-e", script, workflow] + paths, capture_output=True, text=True, encoding="utf-8")
    if done.returncode:
        raise SystemExit(done.stderr)
    return json.loads(done.stdout)


def as_response(text):
    return {"choices": [{"message": {"content": text}}]}


def answers(item):
    """A recorded output as the harness takes it. A run made since v0.13 may hold the model's second answer too."""
    fields = {"_model_response": as_response(item["content"])}
    if "retry_content" in item:
        fields["_model_retry_response"] = as_response(item["retry_content"])
    return fields


def lab_overrides():
    config = load("config/%s.json" % LAB_STAGE)
    return {"ownership_check": config.get("ownership_check", "app"), "normalise_digits": config.get("normalise_digits", False),
            "answer_only_from_policy": config.get("answer_only_from_policy", False), "rules": config.get("rules", []),
            "glossary": load(config["glossary"])["terms"] if config.get("glossary") else {},
            "policy": load(config["policy"]), "sim_model": config["model"]}


def lab_cases():
    return load("data/cases.json")["cases"] + load("data/heldout.json")["cases"]


def template_inputs(name):
    cases = read(os.path.join(WORKFLOWS, "src", name, "cases.json"))["cases"]
    return os.path.join(WORKFLOWS, name + ".n8n.json"), cases


def replay_template(name, run):
    """(passed, model cases, failed case numbers) for one template."""
    workflow, cases = template_inputs(name)
    outputs = {item["id"]: item for item in run["outputs"]}
    chosen = [(i, case) for i, case in enumerate(cases, 1) if "_model_response" not in case]
    requests = [dict(case, **answers(outputs[i])) for i, case in chosen]
    got = harness(workflow, requests, {"model_mode": "http"})
    failed = [i for (i, case), result in zip(chosen, got) if not contains(case["expect"], result)]
    return len(chosen) - len(failed), len(chosen), failed


def replay_lab(run):
    """((passed, total) on the working set, the same on the held-out set, failed case ids)."""
    cases = lab_cases()
    outputs = {item["id"]: item for item in run["outputs"]}
    store = Store(os.path.join(REFERENCE, "data", "orders.json"), os.path.join(REFERENCE, "data", "policy-v2-approved-only.json"))
    requests = [dict({"message": c["message"], "account": c["account"]}, **answers(outputs[i])) for i, c in enumerate(cases, 1)]
    got = harness(LAB, requests, dict(lab_overrides(), model_mode="http"))
    wrong = [first_wrong_step(case, result, store) for case, result in zip(cases, got)]
    work, held = wrong[:35], wrong[35:]
    failed = [str(case["id"]) for case, step in zip(cases, wrong) if step]
    return (sum(1 for s in work if not s), len(work)), (sum(1 for s in held if not s), len(held)), failed


def replay_dataset(run, failures=False):
    """A run of template 1 on the invented store: the 85 messages, or its thirty failure cases. Returns dataset_pack's rows."""
    import dataset_pack as pack
    with open(pack.path("failure-requests.json" if failures else "requests.json"), encoding="utf-8") as f:
        requests = json.load(f)
    with open(pack.path("template-1-config.json"), encoding="utf-8") as f:
        config = dict(json.load(f), model_mode="http")
    by_ref = {item["ref"]: item for item in run["outputs"]}
    got = harness(os.path.join(WORKFLOWS, "01-whatsapp-customer-service.n8n.json"), [dict(q, **answers(by_ref[q["ref"]])) for q in requests], config)
    return pack.score_failures(pack.load_failures(), got) if failures else pack.score(pack.load()[3], got), got


def replay_dialect(name, run):
    """The dialect cases of one template: (refs that hold, refs that do not, {limit ref: (action, is it the correct one)})."""
    pack = read(os.path.join(WORKFLOWS, "src", name, "dialect-cases.json"))
    items = pack["cases"] + pack["simulator_limits"]
    by_ref = {item["ref"]: item for item in run["outputs"]}
    got = harness(os.path.join(WORKFLOWS, name + ".n8n.json"),
                  [dict({k: c[k] for k in ("message", "account") if k in c}, **answers(by_ref[c["ref"]])) for c in items], {"model_mode": "http"})
    held = [c["ref"] for c, g in zip(items, got) if "expect" in c and contains(c["expect"], g)]
    failed = [c["ref"] for c, g in zip(items, got) if "expect" in c and not contains(c["expect"], g)]
    limits = {c["ref"]: (g["action"], g["action"].startswith(c["correct"].split(":")[0])) for c, g in zip(items, got) if "expect" not in c}
    return held, failed, limits


def main(argv):
    if "--prompts" in argv:
        out = argv[argv.index("--prompts") + 1]
        os.makedirs(out, exist_ok=True)
        for name in sorted(os.listdir(os.path.join(WORKFLOWS, "src"))):
            if name == "common":
                continue
            workflow, cases = template_inputs(name)
            bodies = [{k: v for k, v in case.items() if k not in ("expect", "_config", "_model_response")} for case in cases]
            with open(os.path.join(out, name + ".json"), "w", encoding="utf-8") as f:
                json.dump(prompts(workflow, bodies, {}), f, ensure_ascii=False, indent=1)
        bodies = [{"message": c["message"], "account": c["account"]} for c in lab_cases()]
        with open(os.path.join(out, "lab-order-agent.json"), "w", encoding="utf-8") as f:
            json.dump(prompts(LAB, bodies, lab_overrides()), f, ensure_ascii=False, indent=1)
        print("prompts written to", out)
        return 0
    for name in sorted(os.listdir(RUNS)):
        if not name.endswith(".json"):
            continue
        run = read(os.path.join(RUNS, name))
        if run["workflow"] == "lab-order-agent":
            work, held, failed = replay_lab(run)
            print("%-32s %s  working set %d/%d, held-out %d/%d  failed: %s" % (run["workflow"], run["model"], work[0], work[1], held[0], held[1], ", ".join(failed) or "none"))
        else:
            passed, total, failed = replay_template(run["workflow"], run)
            print("%-32s %s  %d/%d  failed: %s" % (run["workflow"], run["model"], passed, total, ", ".join(map(str, failed)) or "none"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

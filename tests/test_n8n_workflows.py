# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""The importable n8n workflows: built from their sources, well-formed, and correct in their logic.

The logic tests run the Code nodes of each built workflow with Node.js (tools/n8n_harness.js)
and are skipped where Node.js is not installed. n8n itself is not needed here; the import
and the webhooks are checked inside n8n with tools/n8n_e2e.py, by hand, before a release.
"""
import glob
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = os.path.join(ROOT, "05-agentic-ai-lab", "agent-templates", "workflows")
LAB = os.path.join(ROOT, "03-courses", "02-build", "labs", "n8n", "order-agent.n8n.json")
REFERENCE = os.path.join(ROOT, "03-courses", "02-build", "labs", "reference")
HARNESS = os.path.join(ROOT, "tools", "n8n_harness.js")
NODE = shutil.which("node")
sys.path.insert(0, REFERENCE)
sys.path.insert(0, os.path.join(ROOT, "tools"))

from n8n_e2e import contains  # noqa: E402
from order_agent.evaluate import build_agent, load  # noqa: E402

BUILT = sorted(glob.glob(os.path.join(TEMPLATES, "*.n8n.json"))) + [LAB]
SHAPE = ["Webhook", "Config", "Prepare", "Real model?", "Model (HTTP)", "Simulated model", "Decide", "Respond"]


def harness(workflow, requests, overrides=None):
    with tempfile.TemporaryDirectory() as tmp:
        paths = []
        for name, value in (("requests.json", requests), ("overrides.json", overrides)):
            if value is not None:
                paths.append(os.path.join(tmp, name))
                with open(paths[-1], "w", encoding="utf-8") as f:
                    json.dump(value, f, ensure_ascii=False)
        done = subprocess.run([NODE, HARNESS, workflow] + paths, capture_output=True, text=True, encoding="utf-8")
    if done.returncode:
        raise AssertionError(done.stderr)
    return json.loads(done.stdout)


class BuiltFiles(unittest.TestCase):
    def test_built_workflows_match_their_sources(self):
        done = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "build_n8n_workflows.py"), "--check"],
                              capture_output=True, text=True)
        self.assertEqual(done.returncode, 0, done.stdout)

    def test_there_is_a_workflow_for_each_of_the_five_templates_and_one_for_the_lab(self):
        specs = sorted(glob.glob(os.path.join(TEMPLATES, "..", "0*.md")))
        self.assertEqual([os.path.basename(p)[:-3] for p in specs],
                         [os.path.basename(p)[:-len(".n8n.json")] for p in BUILT[:-1]])
        self.assertTrue(os.path.exists(LAB))

    def test_every_workflow_has_the_same_shape_and_is_importable_json(self):
        for path in BUILT:
            with open(path, encoding="utf-8") as f:
                workflow = json.load(f)
            names = [n["name"] for n in workflow["nodes"]]
            for name in SHAPE:
                self.assertIn(name, names, path)
            self.assertEqual(len(names), len(set(names)), path)
            self.assertEqual(len({n["id"] for n in workflow["nodes"]}), len(names), path)
            self.assertFalse(workflow["active"], path)
            for source, outputs in workflow["connections"].items():
                self.assertIn(source, names, path)
                for branch in outputs["main"]:
                    for link in branch:
                        self.assertIn(link["node"], names, path)
            json.loads(next(n for n in workflow["nodes"] if n["name"] == "Config")["parameters"]["jsonOutput"])

    def test_workflows_ship_simulated_with_no_credential_and_no_key(self):
        for path in BUILT:
            with open(path, encoding="utf-8") as f:
                text = f.read()
            workflow = json.loads(text)
            config = json.loads(next(n for n in workflow["nodes"] if n["name"] == "Config")["parameters"]["jsonOutput"])
            self.assertEqual(config["model_mode"], "simulated", path)
            self.assertFalse(config["stopped"], path)
            self.assertTrue(all("credentials" not in n for n in workflow["nodes"]), path)
            for marker in ("sk-", "Bearer ", "api_key", "apiKey"):
                self.assertNotIn(marker, text, path)

    def test_the_model_never_reaches_a_tool_except_through_decide(self):
        for path in BUILT:
            with open(path, encoding="utf-8") as f:
                connections = json.load(f)["connections"]
            for model in ("Model (HTTP)", "Simulated model"):
                self.assertEqual([link["node"] for branch in connections[model]["main"] for link in branch], ["Decide"], path)


@unittest.skipUnless(NODE, "Node.js is not installed: the logic of the Code nodes is not exercised")
class TemplateLogic(unittest.TestCase):
    def test_every_case_of_every_template_gives_the_expected_result(self):
        total = 0
        for path in BUILT[:-1]:
            name = os.path.basename(path)[:-len(".n8n.json")]
            with open(os.path.join(TEMPLATES, "src", name, "cases.json"), encoding="utf-8") as f:
                cases = json.load(f)["cases"]
            for case, got in zip(cases, harness(path, cases)):
                total += 1
                self.assertTrue(contains(case["expect"], got), "%s: %s\n%s" % (name, case["expect"], got))
        self.assertEqual(total, 50)

    def test_a_stopped_workflow_sends_everything_to_a_person(self):
        for path in BUILT[:-1]:
            got = harness(path, [{"message": "وين طلبي A-1001", "account": "0500000001"}], {"stopped": True})[0]
            self.assertEqual(got["action"], "stopped", path)
            self.assertEqual(got["tool_calls"], [], path)

    def test_a_model_that_answers_nonsense_cannot_act(self):
        nonsense = {"choices": [{"message": {"content": "Done! I refunded the customer and posted the entry."}}]}
        for path in BUILT[:-1]:
            got = harness(path, [{"message": "ابي استرجاع", "account": "0500000001", "_model_response": nonsense}],
                          {"model_mode": "http"})[0]
            self.assertEqual(got["pending_approval"], [], path)
            self.assertEqual(got["tool_calls"], [], path)

    def test_an_unreachable_model_cannot_act(self):
        for path in BUILT:
            got = harness(path, [{"message": "ما حالة طلبي رقم 84522؟", "account": "0500000001"}], {"model_mode": "http"})[0]
            self.assertEqual(got["pending_approval"], [], path)
            self.assertEqual(got["tool_calls"], [], path)


@unittest.skipUnless(NODE, "Node.js is not installed: the logic of the Code nodes is not exercised")
class LabMatchesThePythonReference(unittest.TestCase):
    """The n8n lab is the same agent as labs/reference: same answer on every case, at every stage."""

    def overrides(self, config):
        return {"ownership_check": config.get("ownership_check", "app"), "normalise_digits": config.get("normalise_digits", False),
                "answer_only_from_policy": config.get("answer_only_from_policy", False), "rules": config.get("rules", []),
                "glossary": load(config["glossary"])["terms"] if config.get("glossary") else {},
                "policy": load(config["policy"]), "sim_model": config["model"]}

    def test_same_result_as_the_reference_at_every_stage_on_both_test_sets(self):
        compared = 0
        for name in ("stage-0-baseline", "stage-1-guardrails", "stage-2-cycle-1", "stage-3-cycle-2", "model-a", "model-b"):
            config = load("config/%s.json" % name)
            for cases_file in ("data/cases.json", "data/heldout.json"):
                cases = load(cases_file)["cases"]
                agent = build_agent(config)
                got = harness(LAB, cases, self.overrides(config))
                for case, result in zip(cases, got):
                    compared += 1
                    self.assertEqual(result, agent.handle(case["message"], case["account"], case.get("notes", "")),
                                     "%s, %s, case %s" % (name, cases_file, case["id"]))
        self.assertEqual(compared, 6 * (35 + 8))

    def test_the_built_workflow_starts_at_the_baseline_stage(self):
        with open(LAB, encoding="utf-8") as f:
            config = json.loads(next(n for n in json.load(f)["nodes"] if n["name"] == "Config")["parameters"]["jsonOutput"])
        baseline = self.overrides(load("config/stage-0-baseline.json"))
        self.assertEqual({k: config[k] for k in baseline}, baseline)

    def test_a_follow_up_ticket_needs_a_named_approver_and_is_created_once(self):
        got = harness(LAB, [{"_approve": {"order_id": "84521", "approved_by": ""}},
                            {"_approve": {"order_id": "84521", "approved_by": "نورة"}},
                            {"_approve": {"order_id": "84521", "approved_by": "سارة"}},
                            {"_approve": {"order_id": "84521; drop", "approved_by": "نورة"}}])
        self.assertFalse(got[0]["ok"])
        self.assertEqual((got[1]["ticket"], got[1]["approved_by"]), ("T-84521", "نورة"))
        self.assertEqual(got[2]["approved_by"], "نورة")
        self.assertFalse(got[3]["ok"])


@unittest.skipUnless(NODE, "Node.js is not installed: the recorded model runs are not replayed")
class RecordedRealModelRuns(unittest.TestCase):
    """The recorded outputs of a real language model still give the recorded results (real-model-runs/README.md)."""

    def test_recorded_runs_replay_to_the_published_results(self):
        import n8n_replay_model as replay
        seen = {}
        for name in sorted(os.listdir(replay.RUNS)):
            if name.endswith(".json"):
                run = replay.read(os.path.join(replay.RUNS, name))
                seen[run["workflow"]] = run
                self.assertTrue(run["model"] and run["date"], name)
        self.assertEqual(len(seen), 6)
        model_cases = 0
        for workflow, run in seen.items():
            if workflow == "lab-order-agent":
                self.assertEqual(replay.replay_lab(run), ((32, 35), (8, 8), ["26", "28", "34"]))
            else:
                passed, total, failed = replay.replay_template(workflow, run)
                self.assertEqual((passed, failed), (total, []), workflow)
                model_cases += total
        self.assertEqual(model_cases, 47)

    def test_the_instructions_name_the_business_and_carry_the_service_list(self):
        import n8n_replay_model as replay
        workflow, cases = replay.template_inputs("02-booking-assistant")
        system = replay.prompts(workflow, [{"message": cases[0]["message"]}], {})[0]["system"]
        self.assertNotIn("(اسم المنشأة)", system)
        self.assertIn("- تنظيف أسنان", system)


if __name__ == "__main__":
    unittest.main()

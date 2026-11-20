#!/usr/bin/env python3
# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""End-to-end check of the built workflows inside a running n8n. Not part of `make check`.

    python3 tools/n8n_e2e.py --base http://127.0.0.1:5678

Before running: import the six workflows into a fresh n8n, publish them and start n8n
(05-agentic-ai-lab/agent-templates/workflows/README.md has the commands). The script
posts every case of every template to its production webhook and compares the answer
with the case's `expect`; for the Course 2 lab it compares all 35 working cases with the
Python reference agent at the baseline stage. Cases that change Config or stand in for a
model's answer run in the harness only (tests/test_n8n_workflows.py) and are skipped here.
Run it once per fresh import: bookings and drafts made by a run are kept by n8n.
Standard library only.
"""
import argparse
import json
import os
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOWS = os.path.join(ROOT, "05-agentic-ai-lab", "agent-templates", "workflows")
REFERENCE = os.path.join(ROOT, "03-courses", "02-build", "labs", "reference")


def post(base, path, body):
    request = urllib.request.Request("%s/webhook/%s" % (base, path), data=json.dumps(body).encode("utf-8"),
                                     headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)


def contains(expected, got):
    """True if every expected field is in the answer; lists are compared item by item."""
    if isinstance(expected, dict):
        return isinstance(got, dict) and all(k in got and contains(v, got[k]) for k, v in expected.items())
    if isinstance(expected, list):
        return isinstance(got, list) and len(expected) == len(got) and all(contains(a, b) for a, b in zip(expected, got))
    return expected == got


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--base", default="http://127.0.0.1:5678")
    base = parser.parse_args().base.rstrip("/")
    failed = ran = skipped = 0
    for name in sorted(os.listdir(os.path.join(WORKFLOWS, "src"))):
        folder = os.path.join(WORKFLOWS, "src", name)
        if not os.path.isfile(os.path.join(folder, "cases.json")):
            continue
        with open(os.path.join(folder, "spec.json"), encoding="utf-8") as f:
            path = json.load(f)["webhook_path"]
        with open(os.path.join(folder, "cases.json"), encoding="utf-8") as f:
            cases = json.load(f)["cases"]
        for case in cases:
            if "_config" in case or "_model_response" in case:
                skipped += 1
                continue
            body = {k: v for k, v in case.items() if k not in ("expect", "_approve")}
            got = post(base, path + "-approve", case["_approve"]) if "_approve" in case else post(base, path, body)
            ran += 1
            if not contains(case["expect"], got):
                failed += 1
                print("FAIL %s: %s\n  expected %s\n  got %s" % (name, json.dumps(body, ensure_ascii=False)[:80],
                                                                 json.dumps(case["expect"], ensure_ascii=False), json.dumps(got, ensure_ascii=False)[:400]))
    sys.path.insert(0, REFERENCE)
    from order_agent.evaluate import build_agent, load
    agent = build_agent(load("config/stage-0-baseline.json"))
    for case in load("data/cases.json")["cases"]:
        got = post(base, "saaea-order-agent", {"message": case["message"], "account": case["account"]})
        ran += 1
        if got != agent.handle(case["message"], case["account"]):
            failed += 1
            print("FAIL lab case %s" % case["id"])
    unnamed = post(base, "saaea-order-agent-approve", {"order_id": "84521", "approved_by": ""})
    named = post(base, "saaea-order-agent-approve", {"order_id": "84521", "approved_by": "e2e approver"})
    ran += 2
    if unnamed.get("ok") is not False or named.get("ticket") != "T-84521":
        failed += 1
        print("FAIL lab approval flow: %s / %s" % (unnamed, named))
    print("%d requests sent, %d failed, %d harness-only cases skipped" % (ran, failed, skipped))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

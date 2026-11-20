# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Run a test set against a configuration and report the numbers of Module 2.5.

    python3 -m order_agent.evaluate config/stage-0-baseline.json
    python3 -m order_agent.evaluate config/stage-3-cycle-2.json --cases data/heldout.json
    python3 -m order_agent.evaluate config/stage-0-baseline.json --failures failures.csv

Every case is checked by code against written criteria, so another person can re-run it
and get the same answer (validation gate 3 of the course).
"""
import argparse
import csv
import json
import os
import sys

from .agent import Agent
from .model import HttpModel, SimModel, SimModelB
from .tools import Store

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATEGORIES = ["msa", "dialect", "mixed", "edge", "safety"]
STEPS = ["understanding", "permission", "tool", "knowledge", "action"]


def load(path):
    with open(path if os.path.isabs(path) else os.path.join(HERE, path), encoding="utf-8") as f:
        return json.load(f)


def build_agent(config):
    glossary = load(config["glossary"])["terms"] if config.get("glossary") else {}
    kind = config.get("model", "sim-a")
    if kind == "http":
        with open(os.path.join(HERE, "instructions.md"), encoding="utf-8") as f:
            model = HttpModel(f.read(), glossary)
    else:
        model = (SimModelB if kind == "sim-b" else SimModel)(glossary, config.get("rules", []))
    store = Store(os.path.join(HERE, "data", "orders.json"), os.path.join(HERE, config["policy"]))
    return Agent(model, store, ownership_check=config.get("ownership_check", "app"),
                 normalise_digits=config.get("normalise_digits", False),
                 answer_only_from_policy=config.get("answer_only_from_policy", False))


def first_wrong_step(case, result, store):
    """None if the case passed, else the first step that went wrong, in the order a message is handled."""
    expect = case["expect"]
    if result["intent"] != expect["intent"] or bool(expect.get("urgent")) != result["urgent"]:
        return "understanding"
    status_calls = [c["input"] for c in result["tool_calls"] if c["tool"] == "get_order_status"]
    if any(store.owner_of(o) not in (None, case["account"]) for o in status_calls if isinstance(o, str)):
        return "permission"
    if "tool_input" in expect and status_calls != [expect["tool_input"]]:
        return "tool"
    if result["action"] == "tool_input_error":
        return "tool"
    draft = result["reply_draft"]
    if any(t not in draft for t in expect.get("reply_has", [])) or any(t in draft for t in expect.get("reply_lacks", [])):
        return "knowledge"
    if result["action"] != expect["action"] or bool(expect.get("pending")) != bool(result["pending_approval"]):
        return "action"
    return None


def run(config, cases):
    agent = build_agent(config)
    rows = []
    for case in cases:
        result = agent.handle(case["message"], case["account"], case.get("notes", ""))
        rows.append((case, result, first_wrong_step(case, result, agent.store)))
    return rows, agent


def report(rows, config, out=sys.stdout):
    total, passed = len(rows), sum(1 for r in rows if r[2] is None)
    out.write("Configuration: %s\n" % config.get("name", "?"))
    out.write("%-10s %6s %5s\n" % ("category", "passed", "of"))
    for cat in CATEGORIES:
        of = [r for r in rows if r[0]["category"] == cat]
        if of:
            out.write("%-10s %6d %5d\n" % (cat, sum(1 for r in of if r[2] is None), len(of)))
    out.write("%-10s %6d %5d   (%.1f%%)\n" % ("TOTAL", passed, total, 100.0 * passed / total))
    wrong = [r for r in rows if r[2]]
    out.write("failures by first wrong step: " + ", ".join(
        "%s %d" % (s, sum(1 for r in wrong if r[2] == s)) for s in STEPS if any(r[2] == s for r in wrong)) + "\n")
    out.write("failed cases: " + " ".join(str(r[0]["id"]) for r in wrong) + "\n")
    cost = config.get("cost_per_attempt_sar")
    if cost and passed:
        out.write("cost per attempt SAR %.3f (illustrative); cost per successful task SAR %.3f\n" % (cost, total * cost / passed))
    rule = config.get("launch_rule")
    if rule:
        safety = [r for r in rows if r[0]["category"] == "safety"]
        ok = 100.0 * passed / total >= rule["overall_percent"] and (not safety or all(r[2] is None for r in safety))
        out.write("launch rule (overall >= %d%%, safety 100%%): %s\n" % (rule["overall_percent"], "MET" if ok else "NOT MET"))
    return passed, total


def write_failures(rows, path):
    """The start of the failure log of Module 2.8. Cause, fix and cycle are yours to fill in."""
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["case", "category", "message", "first_wrong_step", "got_intent", "got_action", "expected_action", "cause", "fix", "cycle"])
        for case, result, step in rows:
            if step:
                w.writerow([case["id"], case["category"], case["message"], step, result["intent"], result["action"], case["expect"]["action"], "", "", ""])


def main(argv=None):
    parser = argparse.ArgumentParser(description="Evaluate the order-enquiry agent on a test set")
    parser.add_argument("config")
    parser.add_argument("--cases", default="data/cases.json")
    parser.add_argument("--only", help="comma-separated case ids, for the ten-case comparison of Module 2.4")
    parser.add_argument("--failures", help="write failed cases to this CSV file")
    args = parser.parse_args(argv)
    config = load(args.config)
    cases = load(args.cases)["cases"]
    if args.only:
        wanted = [x.strip() for x in args.only.split(",")]
        cases = [c for c in cases if str(c["id"]) in wanted]
    rows, _ = run(config, cases)
    report(rows, config)
    if args.failures:
        write_failures(rows, args.failures)
        print("failure log written to", args.failures)


if __name__ == "__main__":
    main()

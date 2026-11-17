#!/usr/bin/env python3
# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Compute and check the KPIs of exercise B5 from the CSV files.

يحسب مؤشرات تمرين B5 من ملفات CSV ويقارنها بقيم مرجعية.

Definitions are in kpi-dictionary.md. The rule the script enforces is the one
the exercise teaches: every figure on the dashboard is computed from records.

Usage
-----
    # compute, and write files a dashboard can read
    python3 compute_metrics.py data/baseline --out metrics.json --js metrics.js

    # check your own numbers against the reference (exit code 1 on mismatch)
    python3 compute_metrics.py data/baseline --compare my_metrics.json

Denominators
------------
final tasks  = completed + failed, after removing duplicate rows.
Pending and cancelled tasks are reported but never enter a rate.
"""

import argparse
import csv
import json
import sys
from datetime import datetime
from pathlib import Path


def read(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def pct(part, whole):
    return round(100.0 * part / whole, 1) if whole else None


def div(a, b, digits=2):
    return round(a / b, digits) if b else None


def block(tasks, runs, rate):
    """KPIs for one set of de-duplicated tasks and their runs."""
    final = [t for t in tasks if t["status"] in ("completed", "failed")]
    done = [t for t in final if t["status"] == "completed"]
    reviewed = [t for t in final if t["human_intervention"] == "1"]
    hours = [
        (datetime.fromisoformat(t["completed_at"]) - datetime.fromisoformat(t["created_at"])).total_seconds() / 3600
        for t in done
    ]
    model_cost = sum(float(r["model_cost"]) for r in runs)
    tool_cost = sum(float(r["tool_cost"]) for r in runs)
    review_cost = sum(float(t["review_minutes"]) for t in tasks) / 60.0 * rate
    cost = model_cost + tool_cost + review_cost
    revenue = sum(float(t["revenue"]) for t in done)
    scores = [float(t["quality_score"]) for t in done if t["quality_score"]]
    return {
        "tasks_received": len(tasks),
        "tasks_final": len(final),
        "tasks_completed": len(done),
        "tasks_failed": len(final) - len(done),
        "tasks_pending": sum(t["status"] == "pending" for t in tasks),
        "tasks_cancelled": sum(t["status"] == "cancelled" for t in tasks),
        "agent_runs": len(runs),
        "tool_calls": sum(int(r["tool_calls"]) for r in runs),
        "success_rate_pct": pct(len(done), len(final)),
        "automation_rate_pct": pct(sum(t["human_intervention"] == "0" for t in done), len(final)),
        "human_intervention_rate_pct": pct(len(reviewed), len(final)),
        "retry_rate_pct": pct(sum(int(t["retry_count"]) > 0 for t in final), len(final)),
        "avg_resolution_hours": div(sum(hours), len(hours)),
        "avg_quality_score": div(sum(scores), len(scores)),
        "model_cost": round(model_cost, 2),
        "tool_cost": round(tool_cost, 2),
        "human_review_cost": round(review_cost, 2),
        "direct_cost": round(cost, 2),
        "cost_per_successful_task": div(cost, len(done)),
        "revenue": round(revenue, 2),
        "gross_margin_pct": pct(revenue - cost, revenue),
    }


def compute(folder):
    folder = Path(folder)
    params = json.loads((folder / "params.json").read_text(encoding="utf-8"))
    raw = read(folder / "tasks.csv")
    seen, tasks = set(), []
    for row in raw:
        if row["task_id"] not in seen:
            seen.add(row["task_id"])
            tasks.append(row)
    runs = read(folder / "agent_usage.csv")
    audit = read(folder / "audit_log.csv")
    customers = read(folder / "customers.csv")
    rate = float(params["review_hourly_rate"])
    start, end = params["period_start"], params["period_end"]

    overall = block(tasks, runs, rate)
    agents = {}
    for agent in sorted({t["assigned_agent"] for t in tasks}):
        agents[agent] = block(
            [t for t in tasks if t["assigned_agent"] == agent],
            [r for r in runs if r["agent_id"] == agent],
            rate,
        )

    final_ids = {t["task_id"] for t in tasks if t["status"] in ("completed", "failed")}
    closed = {e["task_id"] for e in audit if e["action"] == "task_closed"}
    governance = {
        "audit_events": len(audit),
        "unauthorized_attempts_blocked": sum(
            e["result"] == "blocked" and e["action"] in ("issue_refund", "delete_customer_record") for e in audit),
        "approval_required_actions": sum(e["approval_required"] == "1" for e in audit),
        "executed_without_required_approval": sum(
            e["approval_required"] == "1" and e["result"] == "executed" and not e["approved_by"] for e in audit),
        "approvals_pending": sum(e["result"] == "pending_approval" for e in audit),
        "audit_coverage_pct": pct(len(final_ids & closed), len(final_ids)),
    }

    new = [c for c in customers if start <= c["signup_date"] <= end]
    at_start = [c for c in customers if c["signup_date"] < start]
    churned = [c for c in customers if c["churn_date"] and start <= c["churn_date"] <= end]
    active_end = [c for c in customers if c["status"] == "active"]
    leads = agents.get("sales", {}).get("tasks_completed", 0)
    growth = {
        "customers_at_start": len(at_start),
        "new_customers": len(new),
        "churned_customers": len(churned),
        "active_customers_at_end": len(active_end),
        "monthly_churn_pct": pct(len(churned), len(at_start)),
        "avg_acquisition_cost_new": div(sum(float(c["acquisition_cost"]) for c in new), len(new)),
        "lead_to_customer_pct": pct(len(new), leads),
        "revenue_per_active_customer": div(overall["revenue"], len(active_end)),
    }

    return {
        "meta": {
            "company": params["company"],
            "scenario": params["scenario"],
            "period_start": start,
            "period_end": end,
            "currency": params["currency"],
            "synthetic": True,
            "duplicate_task_rows_removed": len(raw) - len(tasks),
        },
        "overall": overall,
        "agents": agents,
        "governance": governance,
        "growth": growth,
    }


def flatten(node, prefix=""):
    out = {}
    for key, value in node.items():
        name = f"{prefix}{key}"
        if isinstance(value, dict):
            out.update(flatten(value, name + "."))
        else:
            out[name] = value
    return out


def compare(reference, other, tolerance):
    ref, mine = flatten(reference), flatten(other)
    problems = []
    for key, expected in ref.items():
        if key.startswith("meta."):
            continue
        if key not in mine:
            problems.append(f"missing   {key} (expected {expected})")
            continue
        got = mine[key]
        if isinstance(expected, (int, float)) and isinstance(got, (int, float)):
            limit = tolerance * max(1.0, abs(expected))
            if abs(expected - got) > limit:
                problems.append(f"different {key}: expected {expected}, got {got}")
        elif expected != got:
            problems.append(f"different {key}: expected {expected}, got {got}")
    return problems


def main():
    parser = argparse.ArgumentParser(description="Compute and check the B5 KPIs.")
    parser.add_argument("folder", help="folder with tasks.csv, agent_usage.csv, audit_log.csv, customers.csv, params.json")
    parser.add_argument("--out", help="write the metrics as JSON")
    parser.add_argument("--js", help="write the metrics as a script that sets window.METRICS (works from file://)")
    parser.add_argument("--compare", help="a metrics JSON file to check against the computed values")
    parser.add_argument("--tolerance", type=float, default=0.005, help="relative tolerance for --compare (default 0.5%%)")
    args = parser.parse_args()

    metrics = compute(args.folder)
    text = json.dumps(metrics, ensure_ascii=False, indent=2)
    if args.out:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
    if args.js:
        Path(args.js).write_text("window.METRICS = " + text + ";\n", encoding="utf-8")
    if args.compare:
        other = json.loads(Path(args.compare).read_text(encoding="utf-8"))
        problems = compare(metrics, other, args.tolerance)
        for line in problems:
            print(line)
        if problems:
            print(f"[FAIL] {len(problems)} value(s) do not match the data in {args.folder}")
            sys.exit(1)
        print(f"[OK] all values match the data in {args.folder}")
        return
    if not (args.out or args.js):
        print(text)


if __name__ == "__main__":
    main()

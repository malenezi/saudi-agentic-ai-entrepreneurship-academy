#!/usr/bin/env python3
# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Synthetic operating data for exercise B5 (venture dashboard).

مولّد بيانات تشغيل مصطنعة لتمرين B5 (لوحة قيادة المشروع الوكيلي).

Everything this script writes is invented. "Mirsah Business Services" is a
fictional company; no row describes a real customer, agent, price or model.
The same seed and scenario always produce the same files.

Usage
-----
    python3 generate_data.py --scenario baseline   --out data/baseline
    python3 generate_data.py --scenario cost-spike --out data/cost-spike

Scenarios
---------
baseline      a normal first month
cost-spike    from day 11 the operations agent runs on the large model with a
              much longer context
quality-drop  from day 15 the support agent fails more often and its quality
              scores fall; more customers leave
volume-up     from day 10 demand rises 45% and human review is cut in half;
              throughput looks better while quality and retention get worse

Files written: tasks.csv, agent_usage.csv, audit_log.csv, customers.csv,
params.json. tasks.csv deliberately contains a few exact duplicate rows and
some open tasks with empty fields; cleaning them is part of the exercise.
"""

import argparse
import csv
import json
import random
from datetime import datetime, timedelta
from pathlib import Path

SEED = 20261117
PERIOD_START = datetime(2026, 10, 1)
DAYS = 31
SCENARIOS = ("baseline", "cost-spike", "quality-drop", "volume-up")

# Invented prices, SAR per million tokens. Not any provider's price list.
MODELS = {
    "model-small": {"in": 1.5, "out": 6.0},
    "model-large": {"in": 11.0, "out": 56.0},
}
REVIEW_HOURLY_RATE_SAR = 45.0  # assumption: loaded cost of the human reviewer

AGENTS = {
    "sales": dict(task="lead_qualification", per_day=7.5, fail=0.04, review=0.05,
                  retry=0.08, tok_in=8000, tok_out=900, tools=2, tool_cost=0.02,
                  latency=14, model="model-small", quality=4.5, price=0.0,
                  review_min=4),
    "support": dict(task="customer_inquiry", per_day=13.0, fail=0.05, review=0.12,
                    retry=0.10, tok_in=9000, tok_out=900, tools=2, tool_cost=0.02,
                    latency=11, model="model-small", quality=4.4, price=0.0,
                    review_min=5),
    "operations": dict(task="service_request", per_day=10.5, fail=0.16, review=0.18,
                       retry=0.30, tok_in=42000, tok_out=3800, tools=5, tool_cost=0.15,
                       latency=48, model="model-small", quality=4.0, price=14.0,
                       review_min=12),
    "finance": dict(task="invoice_preparation", per_day=6.5, fail=0.02, review=0.03,
                    retry=0.04, tok_in=11000, tok_out=1200, tools=3, tool_cost=0.05,
                    latency=19, model="model-small", quality=4.7, price=3.5,
                    review_min=6),
    "bi": dict(task="weekly_report", per_day=2.6, fail=0.09, review=0.08,
               retry=0.15, tok_in=90000, tok_out=7000, tools=4, tool_cost=0.05,
               latency=95, model="model-large", quality=4.2, price=20.0,
               review_min=10),
}

# Actions each agent is allowed to request. Anything else is blocked outside
# the model and logged as an unauthorized attempt.
ALLOWED = {
    "sales": {"task_closed", "create_lead"},
    "support": {"task_closed", "refund_request"},
    "operations": {"task_closed", "update_customer_record"},
    "finance": {"task_closed", "issue_invoice"},
    "bi": {"task_closed"},
}


class Rng:
    """Thin wrapper that only uses random.random(), so output is stable."""

    def __init__(self, seed):
        self._r = random.Random(seed)

    def u(self):
        return self._r.random()

    def chance(self, p):
        return self.u() < p

    def between(self, lo, hi):
        return lo + (hi - lo) * self.u()

    def normal(self, mean, sd):
        return mean + sd * (sum(self.u() for _ in range(12)) - 6.0)

    def count(self, mean):
        """Small non-negative integer with the given mean."""
        whole = int(mean)
        return whole + (1 if self.chance(mean - whole) else 0)

    def pick(self, items):
        return items[int(self.u() * len(items)) % len(items)]


def clamp(x, lo, hi):
    return max(lo, min(hi, x))


def make_customers(rng, scenario):
    rows = []
    for i in range(1, 65):
        signup = datetime(2026, 7, 1) + timedelta(days=int(rng.between(0, 122)))
        status, churn_date = "active", ""
        churn_p = 0.05
        if scenario in ("quality-drop", "volume-up"):
            churn_p = 0.14
        if signup < PERIOD_START and rng.chance(churn_p):
            status = "churned"
            churn_date = (PERIOD_START + timedelta(days=int(rng.between(14, 30)))).date().isoformat()
        rows.append({
            "customer_id": f"C{i:03d}",
            "signup_date": signup.date().isoformat(),
            "sector": rng.pick(["retail", "clinic", "logistics", "restaurant", "contracting"]),
            "status": status,
            "churn_date": churn_date,
            "acquisition_cost": round(rng.between(380, 950), 2),
        })
    return rows


def agent_settings(agent, day, scenario):
    s = dict(AGENTS[agent])
    if scenario == "cost-spike" and agent == "operations" and day >= 11:
        s["model"] = "model-large"
        s["tok_in"] = int(s["tok_in"] * 1.6)
    if scenario == "quality-drop" and agent == "support" and day >= 15:
        s["fail"] = 0.14
        s["review"] = 0.22
        s["retry"] = 0.24
        s["quality"] = 3.4
    if scenario == "volume-up" and day >= 10:
        s["per_day"] *= 1.45
        s["review"] *= 0.5
        s["quality"] -= 0.8
    return s


def generate(scenario):
    rng = Rng(SEED)  # same stream for every scenario, so they stay comparable
    customers = make_customers(rng, scenario)
    tasks, runs, audit = [], [], []
    period_end = PERIOD_START + timedelta(days=DAYS)

    def log(ts, task_id, agent, action, tool, needs, approver, result):
        audit.append({
            "event_id": f"E{len(audit) + 1:05d}",
            "timestamp": ts.isoformat(timespec="minutes"),
            "task_id": task_id,
            "agent_id": agent,
            "action": action,
            "tool": tool,
            "approval_required": needs,
            "approved_by": approver,
            "result": result,
        })

    for day in range(1, DAYS + 1):
        date = PERIOD_START + timedelta(days=day - 1)
        weekend = date.weekday() in (4, 5)  # Friday, Saturday
        for agent in AGENTS:
            s = agent_settings(agent, day, scenario)
            n = rng.count(s["per_day"] * (0.35 if weekend else 1.0))
            for _ in range(n):
                task_id = f"T{len(tasks) + 1:05d}"
                created = date + timedelta(minutes=int(rng.between(8 * 60, 21 * 60)))
                signed = [c for c in customers if c["signup_date"] <= date.date().isoformat()]
                customer = "" if agent == "sales" else rng.pick(signed)["customer_id"]

                retries = 0
                if rng.chance(s["retry"]):
                    retries = 1 + (1 if rng.chance(0.3) else 0)
                roll = rng.u()
                if day >= 30 and rng.chance(0.25):
                    status = "pending"
                elif roll < 0.012:
                    status = "cancelled"
                elif roll < 0.012 + s["fail"]:
                    status = "failed"
                else:
                    status = "completed"
                final = status in ("completed", "failed")
                reviewed = final and rng.chance(s["review"] + (0.35 if status == "failed" else 0))
                review_min = round(clamp(rng.normal(s["review_min"], 2), 1, 40), 1) if reviewed else 0

                total_latency = 0.0
                for attempt in range(retries + 1):
                    tok_in = int(clamp(rng.normal(s["tok_in"], s["tok_in"] * 0.18), 200, 10 ** 6))
                    tok_out = int(clamp(rng.normal(s["tok_out"], s["tok_out"] * 0.2), 40, 10 ** 5))
                    calls = max(0, rng.count(clamp(rng.normal(s["tools"], 1), 0, 12)))
                    latency = round(clamp(rng.normal(s["latency"], s["latency"] * 0.25), 2, 900), 1)
                    price = MODELS[s["model"]]
                    runs.append({
                        "run_id": f"R{len(runs) + 1:05d}",
                        "task_id": task_id,
                        "agent_id": agent,
                        "attempt": attempt + 1,
                        "model_name": s["model"],
                        "input_tokens": tok_in,
                        "output_tokens": tok_out,
                        "tool_calls": calls,
                        "latency_seconds": latency,
                        "model_cost": round((tok_in * price["in"] + tok_out * price["out"]) / 1e6, 4),
                        "tool_cost": round(calls * s["tool_cost"], 4),
                    })
                    total_latency += latency

                wait_min = rng.between(1, 25) + (rng.between(30, 600) if reviewed else 0)
                done = created + timedelta(seconds=total_latency, minutes=wait_min)
                quality = ""
                if status == "completed":
                    quality = round(clamp(rng.normal(s["quality"], 0.45), 1, 5), 1)
                tasks.append({
                    "task_id": task_id,
                    "task_type": s["task"],
                    "assigned_agent": agent,
                    "customer_id": customer,
                    "created_at": created.isoformat(timespec="minutes"),
                    "completed_at": done.isoformat(timespec="minutes") if final else "",
                    "status": status,
                    "retry_count": retries,
                    "human_intervention": 1 if reviewed else 0,
                    "review_minutes": review_min,
                    "quality_score": quality,
                    "revenue": s["price"] if status == "completed" else 0.0,
                })

                # Audit trail
                if agent == "finance" and final:
                    big = rng.chance(0.2)
                    if big and status == "completed":
                        log(done, task_id, agent, "issue_invoice", "accounting", 1, "founder", "executed")
                    elif big:
                        log(done, task_id, agent, "issue_invoice", "accounting", 1, "", "blocked")
                    else:
                        log(done, task_id, agent, "issue_invoice", "accounting", 0, "", "executed")
                if agent == "operations" and final and rng.chance(0.3):
                    log(done, task_id, agent, "update_customer_record", "crm", 0, "", "executed")
                if agent == "support" and rng.chance(0.06):
                    late = done >= period_end - timedelta(days=2)
                    log(done, task_id, agent, "refund_request", "payments", 1,
                        "" if late else "founder", "pending_approval" if late else "executed")
                if agent in ("support", "operations") and rng.chance(0.007):
                    log(created, task_id, agent, "issue_refund" if agent == "support" else "delete_customer_record",
                        "payments" if agent == "support" else "crm", 1, "", "blocked")
                if final and not rng.chance(0.02):
                    log(done, task_id, agent, "task_closed", "workflow", 0, "", "executed")

    # Deliberate data-quality traps: exact duplicate task rows.
    for i in range(6):
        tasks.append(dict(tasks[37 + i * 151 % len(tasks)]))
    tasks.sort(key=lambda r: (r["created_at"], r["task_id"]))

    params = {
        "company": "Mirsah Business Services (fictional)",
        "scenario": scenario,
        "period_start": PERIOD_START.date().isoformat(),
        "period_end": (period_end - timedelta(days=1)).date().isoformat(),
        "currency": "SAR",
        "review_hourly_rate": REVIEW_HOURLY_RATE_SAR,
        "note": "Synthetic data. Every value is invented for training.",
    }
    return tasks, runs, audit, customers, params


def write_csv(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description="Generate synthetic data for exercise B5.")
    parser.add_argument("--scenario", choices=SCENARIOS, default="baseline")
    parser.add_argument("--out", required=True, help="output directory")
    args = parser.parse_args()

    tasks, runs, audit, customers, params = generate(args.scenario)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    write_csv(out / "tasks.csv", tasks)
    write_csv(out / "agent_usage.csv", runs)
    write_csv(out / "audit_log.csv", audit)
    write_csv(out / "customers.csv", customers)
    (out / "params.json").write_text(json.dumps(params, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{args.scenario}: {len(tasks)} task rows, {len(runs)} runs, "
          f"{len(audit)} audit events, {len(customers)} customers -> {out}")


if __name__ == "__main__":
    main()

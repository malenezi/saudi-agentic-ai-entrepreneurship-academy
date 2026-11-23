#!/usr/bin/env python3
# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""The customer's side of the price: what the task costs them today, and with your service.

حاسبة العائد عند العميل: تكلفة المهمة عليه اليوم، وتكلفتها مع خدمتك.

cost_per_resolved_task.py answers "do I make money on a task?". This answers the question
the customer asks: "what do I save?". It counts what stays with the customer's own staff,
because a saving that ignores it is the apparent saving, not the real one.

Every input is the customer's own number, measured in their workflow (Course 1, Module 1.4)
or in a shadow period (Module 3.6). There are no benchmarks here: the defaults are the
invented store of the Course 3 worked example, and they print its figures.

Formulas
--------
cost today          = tasks * minutes_per_task * minute_cost
left with the staff = returned_tasks * returned_minutes * minute_cost
                      + approvals * approval_minutes * minute_cost
cost with service   = fee + left with the staff
apparent saving     = cost today - fee
real saving         = cost today - cost with service
payback (months)    = setup / real saving

All money values are in one currency (the defaults assume SAR), per month.
"""

import argparse
import sys


def compute(tasks, minutes_per_task, minute_cost, fee, returned_tasks=0, returned_minutes=None,
            approvals=0, approval_minutes=0, setup=0):
    """Return the customer's monthly figures for one set of inputs."""
    if returned_minutes is None:
        returned_minutes = minutes_per_task
    for name, value in (("tasks", tasks), ("minutes_per_task", minutes_per_task), ("minute_cost", minute_cost)):
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
    for name, value in (("fee", fee), ("returned_tasks", returned_tasks), ("returned_minutes", returned_minutes),
                        ("approvals", approvals), ("approval_minutes", approval_minutes), ("setup", setup)):
        if value < 0:
            raise ValueError(f"{name} cannot be negative")
    if returned_tasks > tasks:
        raise ValueError("returned_tasks cannot be more than tasks")

    cost_today = tasks * minutes_per_task * minute_cost
    returned_cost = returned_tasks * returned_minutes * minute_cost
    approval_cost = approvals * approval_minutes * minute_cost
    left_with_staff = returned_cost + approval_cost
    cost_with_service = fee + left_with_staff
    apparent = cost_today - fee
    real = cost_today - cost_with_service
    # The staff minutes at which the service stops saving anything at this fee.
    spare = cost_today - fee
    return {
        "cost_today": cost_today,
        "returned_cost": returned_cost,
        "approval_cost": approval_cost,
        "left_with_staff": left_with_staff,
        "cost_with_service": cost_with_service,
        "apparent_saving": apparent,
        "apparent_pct": apparent / cost_today * 100,
        "real_saving": real,
        "real_pct": real / cost_today * 100,
        "payback_months": (setup / real) if setup and real > 0 else None,
        "break_even_staff_minutes": (spare / minute_cost) if spare > 0 else 0.0,
        "staff_minutes_left": left_with_staff / minute_cost,
    }


def build_parser():
    p = argparse.ArgumentParser(description="The customer's cost of a task today and with the service")
    p.add_argument("--tasks", type=float, default=1500, help="tasks the customer handles per month")
    p.add_argument("--minutes-per-task", type=float, default=3, help="staff minutes per task today, measured")
    p.add_argument("--minute-cost", type=float, default=0.60, help="the customer's cost of one staff minute")
    p.add_argument("--fee", type=float, default=1500, help="what the customer pays you per month")
    p.add_argument("--returned-tasks", type=float, default=120,
                   help="tasks per month that come back to the customer's staff (out of scope, refunds, complaints)")
    p.add_argument("--returned-minutes", type=float, default=None,
                   help="staff minutes on a returned task (default: the same as --minutes-per-task)")
    p.add_argument("--approvals", type=float, default=0, help="agent replies per month the customer's staff approve")
    p.add_argument("--approval-minutes", type=float, default=0, help="staff minutes per approval")
    p.add_argument("--setup", type=float, default=0, help="one-off cost to the customer: set-up fee and their own time")
    p.add_argument("--currency", default="SAR")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        r = compute(args.tasks, args.minutes_per_task, args.minute_cost, args.fee, args.returned_tasks,
                    args.returned_minutes, args.approvals, args.approval_minutes, args.setup)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    c = args.currency
    print("The customer's month")
    print("-" * 52)
    print(f"Cost of the task today             {c} {r['cost_today']:>10,.0f}")
    print(f"Your fee                           {c} {args.fee:>10,.0f}")
    print(f"Returned tasks, staff time         {c} {r['returned_cost']:>10,.0f}")
    print(f"Approvals, staff time              {c} {r['approval_cost']:>10,.0f}")
    print(f"Cost with the service              {c} {r['cost_with_service']:>10,.0f}")
    print(f"Apparent saving (fee only)         {c} {r['apparent_saving']:>10,.0f} ({r['apparent_pct']:.0f}%)")
    print(f"Real saving                        {c} {r['real_saving']:>10,.0f} ({r['real_pct']:.0f}%)")
    if r["payback_months"] is not None:
        print(f"Set-up paid back in                {r['payback_months']:.1f} months")
    print(f"\nStaff minutes still spent: {r['staff_minutes_left']:,.0f}. "
          f"The saving reaches zero at {r['break_even_staff_minutes']:,.0f}.")
    if r["real_saving"] <= 0:
        print("\nWarning: at these inputs the customer saves nothing. Show them this number, not the apparent one.")
    else:
        print("\nShow the customer the real saving, and say where each input was measured.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

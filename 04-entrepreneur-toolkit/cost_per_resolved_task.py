#!/usr/bin/env python3
# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Cost per resolved task calculator for agentic products.

حاسبة تكلفة المهمة المنجزة للمشاريع القائمة على الوكلاء.

All money values are in one currency of your choice (the defaults assume SAR).
The default inputs are illustrative only. Replace them with your own measurements.

Formulas
--------
model cost per attempt = calls * (in_tokens * in_price + out_tokens * out_price) / 1e6
cost per attempt       = model cost + tool cost + review_rate * review_minutes * minute_cost
cost per resolved task = (cost per attempt + escalation_rate * escalation_cost) / success_rate
margin per task        = price - cost per resolved task
"""

import argparse
import sys


def compute(calls, in_tokens, out_tokens, in_price, out_price, tool_cost,
            review_rate, review_minutes, minute_cost,
            success_rate, escalation_rate, escalation_cost, price):
    """Return a dict of unit-economics results for one set of inputs."""
    if not 0 < success_rate <= 1:
        raise ValueError("success_rate must be greater than 0 and at most 1")
    for name, rate in (("review_rate", review_rate), ("escalation_rate", escalation_rate)):
        if not 0 <= rate <= 1:
            raise ValueError(f"{name} must be between 0 and 1")

    model_cost = calls * (in_tokens * in_price + out_tokens * out_price) / 1_000_000
    review_cost = review_rate * review_minutes * minute_cost
    cost_per_attempt = model_cost + tool_cost + review_cost
    cost_per_resolved = (cost_per_attempt + escalation_rate * escalation_cost) / success_rate
    margin = price - cost_per_resolved
    margin_pct = (margin / price * 100) if price else float("nan")
    return {
        "model_cost": model_cost,
        "review_cost": review_cost,
        "cost_per_attempt": cost_per_attempt,
        "cost_per_resolved": cost_per_resolved,
        "margin": margin,
        "margin_pct": margin_pct,
    }


def build_parser():
    p = argparse.ArgumentParser(description="Cost per resolved task calculator")
    p.add_argument("--calls", type=float, default=6, help="model calls per attempt")
    p.add_argument("--in-tokens", type=float, default=2500, help="input tokens per call")
    p.add_argument("--out-tokens", type=float, default=300, help="output tokens per call")
    p.add_argument("--in-price", type=float, default=11, help="price per million input tokens")
    p.add_argument("--out-price", type=float, default=45, help="price per million output tokens")
    p.add_argument("--tool-cost", type=float, default=0.25, help="tool and messaging cost per attempt")
    p.add_argument("--review-rate", type=float, default=0.10, help="share of attempts reviewed by a person (0-1)")
    p.add_argument("--review-minutes", type=float, default=2, help="minutes per review")
    p.add_argument("--minute-cost", type=float, default=0.75, help="cost of one minute of staff time")
    p.add_argument("--success-rate", type=float, default=0.85, help="share of attempts resolved (0-1)")
    p.add_argument("--escalation-rate", type=float, default=0.15, help="share of attempts escalated to a person (0-1)")
    p.add_argument("--escalation-cost", type=float, default=3.0, help="cost of handling one escalation")
    p.add_argument("--price", type=float, default=4.0, help="price charged per resolved task")
    p.add_argument("--volume", type=float, default=0, help="resolved tasks per month (optional)")
    p.add_argument("--currency", default="SAR")
    p.add_argument("--sensitivity", action="store_true",
                   help="print a table across success rates (escalation rate = 1 - success rate)")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    inputs = dict(
        calls=args.calls, in_tokens=args.in_tokens, out_tokens=args.out_tokens,
        in_price=args.in_price, out_price=args.out_price, tool_cost=args.tool_cost,
        review_rate=args.review_rate, review_minutes=args.review_minutes,
        minute_cost=args.minute_cost, success_rate=args.success_rate,
        escalation_rate=args.escalation_rate, escalation_cost=args.escalation_cost,
        price=args.price,
    )
    try:
        r = compute(**inputs)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    c = args.currency
    print("Cost per resolved task")
    print("-" * 44)
    print(f"Model cost per attempt     {c} {r['model_cost']:.2f}")
    print(f"Review cost per attempt    {c} {r['review_cost']:.2f}")
    print(f"Cost per attempt           {c} {r['cost_per_attempt']:.2f}")
    print(f"Cost per resolved task     {c} {r['cost_per_resolved']:.2f}")
    print(f"Price per resolved task    {c} {args.price:.2f}")
    print(f"Gross margin per task      {c} {r['margin']:.2f} ({r['margin_pct']:.0f}%)")
    if args.volume:
        print(f"Monthly gross margin       {c} {r['margin'] * args.volume:,.0f} "
              f"at {args.volume:,.0f} resolved tasks")
    if r["margin"] <= 0:
        print("\nWarning: each resolved task loses money at these inputs.")

    if args.sensitivity:
        print("\nSensitivity to success rate")
        print(f"{'Success':>8} {'Cost/resolved':>15} {'Margin':>10} {'Margin %':>9}")
        for s in (0.50, 0.60, 0.70, 0.80, 0.85, 0.90, 0.95):
            row = compute(**{**inputs, "success_rate": s, "escalation_rate": 1 - s})
            print(f"{s:>8.0%} {row['cost_per_resolved']:>15.2f} "
                  f"{row['margin']:>10.2f} {row['margin_pct']:>8.0f}%")
    return 0


if __name__ == "__main__":
    sys.exit(main())

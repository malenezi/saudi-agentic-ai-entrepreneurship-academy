#!/usr/bin/env python3
# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""First-customers funnel calculator.

حاسبة قمع العملاء الأوائل: من عدد من تواصلت معهم إلى عدد من يدفعون.

Give it the counts from section 5 of the First Ten Customers Plan. It prints
the conversion rate of each step, the weakest step, and how many contacts your
target number of paying customers will take at your current rates.

The default inputs are illustrative only. Replace them with your own counts.
Small counts give rough rates: treat the result as a planning figure.
"""

import argparse
import math
import sys

STEPS = ("contacted", "replied", "meetings", "offers", "pilots", "paying")
LABELS = {
    "contacted": "Contacted · تواصلت",
    "replied": "Replied · ردّوا",
    "meetings": "Meetings · لقاءات",
    "offers": "Pilot offers · عروض تجربة",
    "pilots": "Pilots started · تجارب بدأت",
    "paying": "Paying · يدفعون",
}


def compute(counts, target=10):
    """Return step rates, the weakest step and the contacts needed for `target` paying customers."""
    values = [counts[step] for step in STEPS]
    if any(v < 0 for v in values):
        raise ValueError("counts cannot be negative")
    if values[0] == 0:
        raise ValueError("contacted must be greater than 0")
    for earlier, later, name in zip(values, values[1:], STEPS[1:]):
        if later > earlier:
            raise ValueError(f"{name} cannot be larger than the step before it")
    if target <= 0:
        raise ValueError("target must be greater than 0")

    rates = []
    for (a_name, a), (b_name, b) in zip(zip(STEPS, values), zip(STEPS[1:], values[1:])):
        rates.append((a_name, b_name, (b / a) if a else None))
    measured = [r for r in rates if r[2] is not None]
    weakest = min(measured, key=lambda r: r[2])
    overall = values[-1] / values[0]
    needed = math.ceil(target / overall) if overall > 0 else None
    return {"rates": rates, "weakest": weakest, "overall": overall, "contacts_needed": needed}


def build_parser():
    p = argparse.ArgumentParser(description="First-customers funnel calculator")
    p.add_argument("--contacted", type=int, default=40)
    p.add_argument("--replied", type=int, default=18)
    p.add_argument("--meetings", type=int, default=10)
    p.add_argument("--offers", type=int, default=6)
    p.add_argument("--pilots", type=int, default=3)
    p.add_argument("--paying", type=int, default=2)
    p.add_argument("--target", type=int, default=10, help="paying customers you are aiming for")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    counts = {step: getattr(args, step) for step in STEPS}
    try:
        result = compute(counts, args.target)
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    print("First-customers funnel · قمع العملاء الأوائل")
    print("-" * 52)
    for step in STEPS:
        print(f"{LABELS[step]:<34}{counts[step]:>6}")
    print("-" * 52)
    for a, b, rate in result["rates"]:
        shown = "n/a" if rate is None else f"{rate * 100:.0f}%"
        print(f"{a} -> {b:<22}{shown:>8}")
    a, b, rate = result["weakest"]
    print("-" * 52)
    print(f"Weakest step · أضعف خطوة: {a} -> {b} ({rate * 100:.0f}%)")
    print(f"Contacted to paying · من التواصل إلى الدفع: {result['overall'] * 100:.1f}%")
    if result["contacts_needed"] is None:
        print("No paying customer yet: the plan cannot be sized. Fix the weakest step first.")
    else:
        print(f"Contacts needed for {args.target} paying customers at these rates: {result['contacts_needed']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

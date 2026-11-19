#!/usr/bin/env python3
# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Dilution across funding rounds.

حاسبة تخفيف الملكية عبر جولات التمويل.

Each round is written as  investment:pre_money  or  investment:pre_money:pool
where pool is the share (0-1) of an option pool created before the round,
which dilutes existing holders only.

    python3 round_dilution.py --founders 1.0 --round 2000000:8000000 --round 8000000:32000000:0.10

Formulas
--------
after a pool            ownership = ownership * (1 - pool)
post-money              = pre-money + investment
new investors' share    = investment / post-money
after the round         ownership = ownership * (1 - new investors' share)

It does arithmetic and nothing else: no valuation advice, no instrument terms
(notes, SAFEs, preferences). The default rounds are illustrative only. Have a
licensed lawyer review any real term sheet.
"""

import argparse
import sys


def parse_round(text):
    parts = text.split(":")
    if len(parts) not in (2, 3):
        raise ValueError(f"round '{text}' must be investment:pre_money or investment:pre_money:pool")
    investment, pre_money = float(parts[0]), float(parts[1])
    pool = float(parts[2]) if len(parts) == 3 else 0.0
    if investment <= 0 or pre_money <= 0:
        raise ValueError("investment and pre-money must be greater than 0")
    if not 0 <= pool < 1:
        raise ValueError("pool must be at least 0 and less than 1")
    return investment, pre_money, pool


def compute(founders, rounds):
    """Return one row per round: post-money, new investors' share, founders' share after."""
    if not 0 < founders <= 1:
        raise ValueError("founders must be greater than 0 and at most 1")
    rows = []
    ownership = founders
    for number, (investment, pre_money, pool) in enumerate(rounds, 1):
        ownership *= (1 - pool)
        post_money = pre_money + investment
        investor_share = investment / post_money
        ownership *= (1 - investor_share)
        rows.append({
            "round": number,
            "investment": investment,
            "pre_money": pre_money,
            "pool": pool,
            "post_money": post_money,
            "investor_share": investor_share,
            "founders_after": ownership,
            "founders_value": ownership * post_money,
        })
    return rows


def build_parser():
    p = argparse.ArgumentParser(description="Dilution across funding rounds")
    p.add_argument("--founders", type=float, default=1.0,
                   help="founders' combined share before the first round (0-1)")
    p.add_argument("--round", dest="rounds", action="append", metavar="INVESTMENT:PRE[:POOL]",
                   help="repeat once per round, in order")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    texts = args.rounds or ["2000000:8000000", "8000000:32000000:0.10"]
    try:
        rows = compute(args.founders, [parse_round(t) for t in texts])
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    print("Dilution across rounds · تخفيف الملكية عبر الجولات")
    print(f"Founders before round 1 · حصة المؤسسين قبل الجولة الأولى: {args.founders * 100:.1f}%")
    print("-" * 78)
    print(f"{'Round':<6}{'Investment':>14}{'Pre-money':>14}{'Pool':>7}{'Post-money':>14}{'New inv.':>10}{'Founders':>10}")
    for r in rows:
        print(f"{r['round']:<6}{r['investment']:>14,.0f}{r['pre_money']:>14,.0f}{r['pool'] * 100:>6.0f}%"
              f"{r['post_money']:>14,.0f}{r['investor_share'] * 100:>9.1f}%{r['founders_after'] * 100:>9.1f}%")
    print("-" * 78)
    last = rows[-1]
    print(f"Founders after {len(rows)} round(s) · حصة المؤسسين بعد الجولات: {last['founders_after'] * 100:.1f}%"
          f" (paper value {last['founders_value']:,.0f} at the last post-money)")
    print("Arithmetic only. Not valuation, legal or investment advice.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Check a CSV dataset against a data policy you wrote (exercise R8).

يفحص ملف بيانات CSV مقابل سياسة بيانات كتبتها أنت (تمرين R8).

What a pass means: the file meets the rules in your policy file. It does not
mean the dataset complies with the Personal Data Protection Law or any other
regulation. A script reads column names and values; it cannot know your legal
basis, your purpose, or whether a person can be re-identified.

Usage
-----
    python3 data_governance_lint.py dataset_sample.csv policy.json
    python3 data_governance_lint.py my_test_set.csv my_policy.json --strict

Exit code 1 when there is an error (or a warning with --strict), otherwise 0.

Rules
-----
DG001 error    required column is missing
DG002 error    column has no classification in the policy
DG003 error    key column has duplicate or empty values
DG004 warning  share of empty cells is above the limit
DG005 error    value is not in the allowed list for its column
DG006 error    column name matches a restricted pattern and is not masked
DG007 error    a value looks like a personal identifier (ID number, mobile,
               email, IBAN) in a column not marked as masked
DG008 warning  a group in the balance column is below the minimum share
DG009 error    a column classified above the shareable level is present
"""

import argparse
import csv
import json
import re
import sys
from collections import Counter

ARABIC_DIGITS = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
VALUE_PATTERNS = {
    "id_number": re.compile(r"(?<!\d)[12]\d{9}(?!\d)"),
    "mobile": re.compile(r"(?<!\d)(?:\+?966|0)5\d{8}(?!\d)"),
    "email": re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"),
    "iban": re.compile(r"\bSA\d{2}[0-9A-Z]{20}\b"),
}


def lint(rows, columns, policy):
    findings = []

    def add(rule, severity, message):
        findings.append((rule, severity, message))

    classes = policy.get("column_classification", {})
    masked = set(policy.get("masked_columns", []))
    total = len(rows)

    for col in policy.get("required_columns", []):
        if col not in columns:
            add("DG001", "error", f"required column is missing: {col}")
    for col in columns:
        if col not in classes:
            add("DG002", "error", f"column has no classification: {col}")

    key = policy.get("key_column")
    if key in columns:
        counts = Counter(r[key].strip() for r in rows)
        dupes = sorted(k for k, n in counts.items() if n > 1 and k)
        if dupes:
            add("DG003", "error", f"{len(dupes)} duplicate value(s) in key column {key}: {', '.join(dupes[:5])}")
        if counts.get("", 0):
            add("DG003", "error", f"{counts['']} empty value(s) in key column {key}")

    limit = float(policy.get("max_missing_pct", 5))
    for col in columns:
        empty = sum(1 for r in rows if not r[col].strip())
        share = 100.0 * empty / total if total else 0.0
        if share > limit:
            add("DG004", "warning", f"{col}: {share:.1f}% empty, limit {limit:g}%")

    for col, allowed in policy.get("allowed_values", {}).items():
        if col in columns:
            bad = Counter(r[col] for r in rows if r[col].strip() and r[col] not in allowed)
            for value, n in sorted(bad.items()):
                add("DG005", "error", f"{col}: value not allowed: {value!r} ({n} row(s))")

    for col in columns:
        if col in masked:
            continue
        for pattern in policy.get("restricted_name_patterns", []):
            if pattern.lower() in col.lower():
                add("DG006", "error", f"{col}: restricted field ({pattern}) present and not listed in masked_columns")

    for col in columns:
        if col in masked:
            continue
        hits = Counter()
        for r in rows:
            text = r[col].translate(ARABIC_DIGITS)
            for name, pattern in VALUE_PATTERNS.items():
                if name in policy.get("value_patterns", list(VALUE_PATTERNS)) and pattern.search(text):
                    hits[name] += 1
        for name, n in sorted(hits.items()):
            add("DG007", "error", f"{col}: {n} value(s) look like {name}")

    balance = policy.get("balance")
    if balance and balance.get("column") in columns:
        col, floor = balance["column"], float(balance.get("min_share_pct", 10))
        counts = Counter(r[col] for r in rows if r[col].strip())
        seen = sum(counts.values())
        for group, n in sorted(counts.items()):
            share = 100.0 * n / seen
            if share < floor:
                add("DG008", "warning", f"{col}: group {group!r} is {share:.1f}% of rows, minimum {floor:g}%")

    levels = policy.get("levels", [])
    shareable = policy.get("highest_shareable_level")
    if levels and shareable in levels:
        cut = levels.index(shareable)
        for col in columns:
            level = classes.get(col)
            if level in levels and levels.index(level) > cut and col not in masked:
                add("DG009", "error", f"{col}: classified {level}, above the shareable level {shareable}")
    return findings


def main():
    parser = argparse.ArgumentParser(description="Check a CSV dataset against a data policy.")
    parser.add_argument("dataset")
    parser.add_argument("policy")
    parser.add_argument("--strict", action="store_true", help="exit 1 on warnings too")
    args = parser.parse_args()

    with open(args.policy, encoding="utf-8") as f:
        policy = json.load(f)
    with open(args.dataset, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        columns = reader.fieldnames or []
        rows = [{c: (r.get(c) or "") for c in columns} for r in reader]

    findings = lint(rows, columns, policy)
    for rule, severity, message in findings:
        print(f"{args.dataset}: {severity} {rule} {message}")
    errors = sum(1 for _, s, _ in findings if s == "error")
    warnings = len(findings) - errors
    print(f"\n{len(rows)} row(s), {len(columns)} column(s): {errors} error(s), {warnings} warning(s)")
    if errors or (args.strict and warnings):
        print("الملف لا يستوفي سياستك بعد · The file does not meet your policy yet.")
        sys.exit(1)
    print("الملف يستوفي سياستك. هذا ليس حكماً بالامتثال النظامي · The file meets your policy. This is not a compliance finding.")


if __name__ == "__main__":
    main()

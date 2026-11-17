#!/usr/bin/env python3
# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Check Arabic text against your own glossary (exercise B6).

يفحص النصوص العربية مقابل مسرد مصطلحاتك (تمرين B6).

The glossary is a decision, not a fact: it records the Arabic term your
venture chose for each concept and the variants you decided not to use. The
script only enforces that decision consistently. It does not judge whether
your choices are good Arabic.

Usage
-----
    python3 terminology_lint.py glossary.csv file-or-folder [more ...]
    python3 terminology_lint.py glossary.csv site/ messages/ar.json --strict

glossary.csv columns: term_en, preferred_ar, avoid_ar (variants separated by |)

Rules
-----
TM001 error    a variant from avoid_ar is used
TM002 warning  the English term appears in a mostly-Arabic line without the
               preferred Arabic term anywhere in the file
TM003 warning  two glossary rows share the same preferred Arabic term

Skip a line with a comment containing: terminology-lint-ignore
Exit code 1 on errors (or on warnings with --strict).
"""

import argparse
import csv
import re
import sys
from pathlib import Path

EXTENSIONS = {".md", ".html", ".htm", ".json", ".txt", ".csv"}
MARKS = re.compile(r"[ً-ْٰـ]")
ARABIC = re.compile(r"[؀-ۿ]")
ALEF = str.maketrans("أإآٱ", "اااا")


def norm(text):
    return MARKS.sub("", text).translate(ALEF)


def phrase(term):
    """Regex for an Arabic term as whole words, allowing common prefixes."""
    words = [re.escape(w) for w in norm(term).split()]
    body = r"\s+".join(r"(?:ال)?" + (w[2:] if w.startswith("ال") else w) for w in words)
    return re.compile(r"(?<![؀-ۿ])[وفبكل]{0,2}" + body + r"(?![؀-ۿ])")


def load(path):
    rows = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            preferred = (row.get("preferred_ar") or "").strip()
            if not preferred:
                continue
            avoid = [a.strip() for a in (row.get("avoid_ar") or "").split("|") if a.strip()]
            rows.append({
                "en": (row.get("term_en") or "").strip(),
                "preferred": preferred,
                "preferred_re": phrase(preferred),
                "avoid": [(a, phrase(a)) for a in avoid],
            })
    return rows


def files(paths):
    for p in map(Path, paths):
        if p.is_dir():
            yield from sorted(q for q in p.rglob("*") if q.suffix.lower() in EXTENSIONS and q.is_file())
        else:
            yield p


def main():
    parser = argparse.ArgumentParser(description="Check Arabic text against a glossary.")
    parser.add_argument("glossary")
    parser.add_argument("paths", nargs="+")
    parser.add_argument("--strict", action="store_true", help="exit 1 on warnings too")
    args = parser.parse_args()

    glossary = load(args.glossary)
    errors = warnings = checked = 0
    seen = {}
    for row in glossary:
        key = norm(row["preferred"])
        if key in seen:
            print(f"{args.glossary}: warning TM003 «{row['preferred']}» is the preferred term for both "
                  f"{seen[key]!r} and {row['en']!r}")
            warnings += 1
        seen[key] = row["en"]

    for path in files(args.paths):
        if Path(path).resolve() == Path(args.glossary).resolve():
            continue
        checked += 1
        lines = Path(path).read_text(encoding="utf-8", errors="replace").splitlines()
        whole = norm("\n".join(lines))
        for number, line in enumerate(lines, 1):
            if "terminology-lint-ignore" in line or not ARABIC.search(line):
                continue
            text = norm(line)
            for row in glossary:
                for variant, pattern in row["avoid"]:
                    if pattern.search(text):
                        print(f"{path}:{number}: error TM001 «{variant}» is on the avoid list; "
                              f"use «{row['preferred']}» ({row['en']})")
                        errors += 1
                en = row["en"]
                mostly_arabic = len(ARABIC.findall(line)) > len(re.findall(r"[A-Za-z]", line))
                if en and mostly_arabic and re.search(r"(?<![A-Za-z])" + re.escape(en) + r"(?![A-Za-z])", line, re.I) \
                        and not row["preferred_re"].search(whole):
                    print(f"{path}:{number}: warning TM002 {en!r} appears, but «{row['preferred']}» "
                          f"is not used anywhere in this file")
                    warnings += 1

    print(f"\n{checked} file(s), {len(glossary)} term(s): {errors} error(s), {warnings} warning(s)")
    if errors or (args.strict and warnings):
        sys.exit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Check a venture-journey case against the Academy's format.

    python3 case_lint.py CASE.md [CASE.md ...] [--sources PATH/SOURCES.md] [--strict]

Errors (exit 1): a required section is missing, empty or out of order; the
header has no source level or no source reference; a referenced source number
is not in the register; fewer than two "what the sources do not say" points;
fewer than three learner questions.
Warnings (exit 1 only with --strict): a figure appears in the lesson or in the
founder's angle. Figures belong under "what is documented", next to a source.

It checks the form of a case. It cannot tell whether a fact is true: a person
still opens every link. Standard library only.
"""

import argparse
import os
import re
import sys

SECTIONS = ("ما هو موثّق", "ما لا تقوله المصادر", "الدرس", "زاوية لمؤسس وكيلي", "أسئلة للمتعلم")
NO_FIGURES = ("الدرس", "زاوية لمؤسس وكيلي")
REFERENCE = re.compile(r"\[([ABCD]\d+)\]")
DIGITS = re.compile(r"[0-9٠-٩]")


def split_sections(text):
    """Return {heading: body} for level-2 headings, and the text before the first one."""
    parts = re.split(r"^## +(.+?)\s*$", text, flags=re.M)
    head, sections, order = parts[0], {}, []
    for heading, body in zip(parts[1::2], parts[2::2]):
        sections[heading] = body
        order.append(heading)
    return head, sections, order


def known_sources(path):
    with open(path, encoding="utf-8") as f:
        return set(re.findall(r"^\| ([ABCD]\d+) \|", f.read(), flags=re.M))


def lint(text, register=None):
    errors, warnings = [], []
    head, sections, order = split_sections(text)
    if not re.search(r"^# .+", head, flags=re.M):
        errors.append("no title")
    if "**مستوى المصدر:**" not in head:
        errors.append("header has no source level (**مستوى المصدر:**)")
    if "**المصادر:**" not in head or not REFERENCE.search(head.split("**المصادر:**")[-1]):
        errors.append("header has no source reference such as [A88]")

    present = [name for name in order if name in SECTIONS]
    for name in SECTIONS:
        if name not in sections:
            errors.append("missing section: %s" % name)
    if present != [name for name in SECTIONS if name in sections]:
        errors.append("sections are out of order")

    def bullets(name):
        return re.findall(r"^- .+", sections.get(name, ""), flags=re.M)

    if "ما هو موثّق" in sections and not bullets("ما هو موثّق"):
        errors.append("nothing listed under: ما هو موثّق")
    if "ما لا تقوله المصادر" in sections and len(bullets("ما لا تقوله المصادر")) < 2:
        errors.append("fewer than two points under: ما لا تقوله المصادر")
    if "أسئلة للمتعلم" in sections and len(re.findall(r"^\d+\. .+", sections["أسئلة للمتعلم"], flags=re.M)) < 3:
        errors.append("fewer than three learner questions")
    for name in ("الدرس", "زاوية لمؤسس وكيلي"):
        if name in sections and not sections[name].strip().strip("</div>").strip():
            errors.append("empty section: %s" % name)

    if register is not None:
        for number in sorted(set(REFERENCE.findall(text))):
            if number not in register:
                errors.append("source %s is not in the register" % number)

    for name in NO_FIGURES:
        body = re.sub(r"\[[^\]]*\]\([^)]*\)", "", sections.get(name, ""))  # links may carry numbers
        if DIGITS.search(body):
            warnings.append("a figure appears under: %s" % name)
    return errors, warnings


def main(argv=None):
    parser = argparse.ArgumentParser(description="Check a venture-journey case against the format")
    parser.add_argument("files", nargs="+")
    parser.add_argument("--sources", help="path to SOURCES.md; referenced numbers must exist in it")
    parser.add_argument("--strict", action="store_true", help="warnings also fail")
    args = parser.parse_args(argv)

    register = known_sources(args.sources) if args.sources else None
    total_errors = total_warnings = 0
    for path in args.files:
        with open(path, encoding="utf-8") as f:
            errors, warnings = lint(f.read(), register)
        total_errors += len(errors)
        total_warnings += len(warnings)
        name = os.path.basename(path)
        for message in errors:
            print("%s: ERROR  %s" % (name, message))
        for message in warnings:
            print("%s: WARN   %s" % (name, message))
    print("%d file(s), %d error(s), %d warning(s)" % (len(args.files), total_errors, total_warnings))
    return 1 if total_errors or (args.strict and total_warnings) else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Structural checks for the Academy's Markdown. Standard library only.

    python3 tools/check_repo.py

Checks every Markdown file for: relative links and images that point to a
missing file, anchors that do not exist in the target file, unbalanced
right-to-left blocks, unclosed code fences, and table rows whose cell count
differs from the header. External links are not opened.
Exit code 1 if anything is found.
"""

import collections
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "node_modules", "__pycache__"}


def slug(heading):
    heading = re.sub(r"<[^>]+>", "", heading).strip().lower()
    heading = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", heading).replace("`", "")
    kept = [c for c in heading if c in " -_" or unicodedata.category(c)[0] in "LMN"]
    return "".join(kept).replace(" ", "-")


def anchors_of(path, cache={}):
    if path not in cache:
        found, counts, in_code = set(), collections.Counter(), False
        with open(path, encoding="utf-8") as f:
            for line in f:
                if line.startswith("```"):
                    in_code = not in_code
                if in_code:
                    continue
                match = re.match(r"#{1,6}\s+(.*)", line)
                if match:
                    base = slug(match.group(1))
                    found.add(base if not counts[base] else f"{base}-{counts[base]}")
                    counts[base] += 1
                found.update(re.findall(r'(?:id|name)="([^"]+)"', line))
        cache[path] = {a.lower() for a in found}
    return cache[path]


def markdown_files():
    for folder, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in sorted(files):
            if name.endswith(".md"):
                yield os.path.join(folder, name)


def check(path):
    problems = []
    rel = os.path.relpath(path, ROOT)
    with open(path, encoding="utf-8") as f:
        text = f.read()
    body = re.sub(r"```.*?```", "", text, flags=re.S)
    targets = re.findall(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", body)
    targets += re.findall(r'(?:src|href)="([^"]+)"', body)
    for target in targets:
        if re.match(r"[a-z][a-z0-9+.-]*:", target):
            continue
        file_part, _, fragment = target.partition("#")
        dest = path if not file_part else os.path.normpath(os.path.join(os.path.dirname(path), file_part))
        if not os.path.exists(dest):
            problems.append(f"{rel}: link to a missing file: {target}")
        elif fragment and dest.endswith(".md") and fragment.lower() not in anchors_of(dest):
            problems.append(f"{rel}: anchor not found: {target}")
    opened, closed = len(re.findall(r'<div dir="rtl">', text)), text.count("</div>")
    if opened != closed:
        problems.append(f"{rel}: {opened} <div dir=\"rtl\"> but {closed} </div>")
    if len(re.findall(r"^```", text, flags=re.M)) % 2:
        problems.append(f"{rel}: a code fence is not closed")
    lines, i = text.split("\n"), 0
    while i < len(lines):
        if lines[i].startswith("|") and i + 1 < len(lines) and re.match(r"\|\s*:?-+", lines[i + 1]):
            width = len(re.split(r"(?<!\\)\|", lines[i].strip().strip("|")))
            i += 2
            while i < len(lines) and lines[i].startswith("|"):
                row = re.sub(r"`[^`]*`", "x", lines[i])
                cells = len(re.split(r"(?<!\\)\|", row.strip().strip("|")))
                if cells != width:
                    problems.append(f"{rel}:{i + 1}: table row has {cells} cells, header has {width}")
                i += 1
        else:
            i += 1
    return problems


def main():
    files = list(markdown_files())
    problems = [p for path in files for p in check(path)]
    for line in problems:
        print(line)
    print(f"{len(files)} Markdown file(s) checked: {len(problems)} problem(s)")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()

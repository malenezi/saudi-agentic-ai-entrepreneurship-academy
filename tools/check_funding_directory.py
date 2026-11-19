#!/usr/bin/env python3
# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Check the funding directory index against its page, and flag stale entries.

    python3 tools/check_funding_directory.py            # report, exit 1 on a broken index
    python3 tools/check_funding_directory.py --strict   # also exit 1 when an entry is stale
    python3 tools/check_funding_directory.py --today 2027-03-01 --max-age 90

A broken index is one where an entry is missing a field, has an unknown status,
is not named on the page, or claims to be verified without a link and a date.
A stale entry is a verified or partial one whose page was last opened more than
--max-age days ago: open the operator's page again before anyone relies on it.
Standard library only.
"""

import argparse
import datetime
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOLDER = os.path.join(ROOT, "02-saudi-market-knowledge-framework", "06-funding-investment")
FIELDS = ("name", "match", "operator", "type", "status", "official_url", "last_checked", "source")
STATUSES = ("verified", "partial", "pending", "inactive")


def load(index_path):
    with open(index_path, encoding="utf-8") as f:
        index = json.load(f)
    with open(os.path.join(os.path.dirname(index_path), index["page"]), encoding="utf-8") as f:
        return index, f.read()


def check(index, page, today, max_age):
    """Return (errors, stale): lists of messages."""
    errors, stale, seen = [], [], set()
    for entry in index["entries"]:
        name = entry.get("name", "(unnamed)")
        missing = [field for field in FIELDS if field not in entry]
        if missing:
            errors.append("%s: missing %s" % (name, ", ".join(missing)))
            continue
        if name in seen:
            errors.append("%s: listed twice" % name)
        seen.add(name)
        if entry["status"] not in STATUSES:
            errors.append("%s: unknown status '%s'" % (name, entry["status"]))
            continue
        if entry["match"] not in page:
            errors.append("%s: '%s' is not on the page" % (name, entry["match"]))
        if entry["status"] == "verified" and not (entry["official_url"] and entry["last_checked"]):
            errors.append("%s: verified needs an official link and a date" % name)
        if entry["official_url"] and not entry["official_url"].startswith("https://"):
            errors.append("%s: the official link must start with https://" % name)
        if entry["last_checked"]:
            try:
                checked = datetime.date.fromisoformat(entry["last_checked"])
            except ValueError:
                errors.append("%s: last_checked is not a date (YYYY-MM-DD)" % name)
                continue
            age = (today - checked).days
            if age < 0:
                errors.append("%s: last_checked is in the future" % name)
            elif entry["status"] in ("verified", "partial") and age > max_age:
                stale.append("%s: page last opened %d days ago" % (name, age))
    return errors, stale


def main(argv=None):
    parser = argparse.ArgumentParser(description="Check the funding directory index")
    parser.add_argument("--index", default=os.path.join(FOLDER, "funding-directory.json"))
    parser.add_argument("--today", default=None, help="YYYY-MM-DD, for reproducible runs")
    parser.add_argument("--max-age", type=int, default=90, help="days before an entry counts as stale")
    parser.add_argument("--strict", action="store_true", help="exit 1 when any entry is stale")
    args = parser.parse_args(argv)

    today = datetime.date.fromisoformat(args.today) if args.today else datetime.date.today()
    index, page = load(args.index)
    errors, stale = check(index, page, today, args.max_age)
    counts = {status: 0 for status in STATUSES}
    for entry in index["entries"]:
        if entry.get("status") in counts:
            counts[entry["status"]] += 1

    print("Funding directory: %d entries (%d verified, %d partial, %d pending, %d inactive)"
          % (len(index["entries"]), counts["verified"], counts["partial"], counts["pending"], counts["inactive"]))
    for message in errors:
        print("ERROR  " + message)
    for message in stale:
        print("STALE  " + message)
    if not errors and not stale:
        print("Index matches the page; nothing older than %d days." % args.max_age)
    if errors or (stale and args.strict):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

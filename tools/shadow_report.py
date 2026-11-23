#!/usr/bin/env python3
# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Compare what an agent would have done in shadow mode with what the staff did.

    python3 tools/shadow_report.py <shadow-log.jsonl> <staff-record.csv>
    python3 tools/shadow_report.py          # the invented sample in workflows/shadow-mode/

The shadow log has one JSON object per line: the response of a template whose Config has
`shadow_mode: true` (it carries `shadow.ref` and `shadow.would`). The staff record is a CSV
the customer's team fills for the same messages:

    ref,staff_outcome,staff_minutes,draft_ok,note

    staff_outcome   answered | handed | refused     what the employee did with the message
    staff_minutes   minutes spent on it (may be empty)
    draft_ok        yes | no | empty                the employee's verdict on the agent's draft

The report counts; it does not judge. No threshold is built in: the decision rule is agreed
with the customer before the period starts (Module 3.6). Standard library only.
"""
import csv
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAMPLE = os.path.join(ROOT, "05-agentic-ai-lab", "agent-templates", "workflows", "shadow-mode")
OUTCOMES = ("answered", "handed", "refused")


def would_outcome(would):
    """The agent's outward behaviour, in the staff record's three words."""
    if would.get("level") == "forbidden":  # refused, even where a person is told about it
        return "refused"
    if would.get("handover") or would.get("pending_approval"):
        return "handed"
    return "answered"


def read_log(path):
    records = {}
    with open(path, encoding="utf-8") as f:
        for number, line in enumerate(f, 1):
            if not line.strip():
                continue
            item = json.loads(line)
            shadow = item.get("shadow")
            if item.get("mode") != "shadow" or not isinstance(shadow, dict):
                raise ValueError("line %d is not a shadow-mode response" % number)
            ref = str(shadow.get("ref") or "")
            if not ref:
                raise ValueError("line %d has no ref: send a `ref` with every message" % number)
            if ref in records:
                raise ValueError("ref %s appears twice in the shadow log" % ref)
            records[ref] = shadow["would"]
    return records


def read_staff(path):
    rows = {}
    with open(path, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            ref = (row.get("ref") or "").strip()
            outcome = (row.get("staff_outcome") or "").strip()
            verdict = (row.get("draft_ok") or "").strip().lower()
            minutes = (row.get("staff_minutes") or "").strip()
            if outcome not in OUTCOMES:
                raise ValueError("ref %s: staff_outcome must be one of %s" % (ref, ", ".join(OUTCOMES)))
            if verdict not in ("yes", "no", ""):
                raise ValueError("ref %s: draft_ok must be yes, no or empty" % ref)
            if ref in rows:
                raise ValueError("ref %s appears twice in the staff record" % ref)
            rows[ref] = {"outcome": outcome, "minutes": float(minutes) if minutes else None, "draft_ok": verdict}
    return rows


def compare(log, staff):
    joined = [(ref, would_outcome(log[ref]), log[ref], staff[ref]) for ref in log if ref in staff]
    alone = [j for j in joined if j[1] == "answered"]
    judged = [j for j in alone if j[3]["draft_ok"]]
    movable = [j for j in alone if j[3]["outcome"] == "answered" and j[3]["draft_ok"] == "yes"]
    return {
        "observed": len(log),
        "recorded": len(joined),
        "not_recorded": sorted(ref for ref in log if ref not in staff),
        "not_observed": sorted(ref for ref in staff if ref not in log),
        "would": {name: sum(1 for j in joined if j[1] == name) for name in OUTCOMES},
        "agree": sum(1 for j in joined if j[1] == j[3]["outcome"]),
        "acted_where_staff_did_not": [(j[0], j[2].get("action"), j[3]["outcome"]) for j in alone if j[3]["outcome"] != "answered"],
        "handed_where_staff_answered": [j[0] for j in joined if j[1] != "answered" and j[3]["outcome"] == "answered"],
        "drafts_judged": len(judged),
        "drafts_ok": sum(1 for j in judged if j[3]["draft_ok"] == "yes"),
        "drafts_rejected": [j[0] for j in judged if j[3]["draft_ok"] == "no"],
        "movable_messages": len(movable),
        "movable_minutes": sum(j[3]["minutes"] or 0 for j in movable),
        "minutes_missing": sum(1 for j in movable if j[3]["minutes"] is None),
        "staff_minutes": sum(j[3]["minutes"] or 0 for j in joined),
    }


def share(part, whole):
    return "%d of %d (%d%%)" % (part, whole, round(100 * part / whole)) if whole else "0 of 0"


def render(r):
    n = r["recorded"]
    lines = [
        "# Shadow-mode report", "",
        "The agent sent nothing and changed nothing in this period. The figures compare what it would have done with what the staff did.", "",
        "| Measure | Value |", "|---|---|",
        "| Messages the agent observed | %d |" % r["observed"],
        "| Of these, recorded by the staff | %d |" % n,
        "| Agent would have acted alone | %s |" % share(r["would"]["answered"], n),
        "| Agent would have handed to a person | %s |" % share(r["would"]["handed"], n),
        "| Agent would have refused | %s |" % share(r["would"]["refused"], n),
        "| Same outcome as the staff | %s |" % share(r["agree"], n),
        "| Agent's own drafts judged by the staff | %d |" % r["drafts_judged"],
        "| Of these, judged correct | %s |" % share(r["drafts_ok"], r["drafts_judged"]),
        "| Messages the staff answered that the agent would have answered correctly | %d |" % r["movable_messages"],
        "| Staff minutes on those messages | %g of %g recorded |" % (r["movable_minutes"], r["staff_minutes"]),
        "",
        "## Read first: the agent would have acted where the staff did not", "",
    ]
    if r["acted_where_staff_did_not"]:
        lines += ["| Ref | Agent would have | Staff |", "|---|---|---|"]
        lines += ["| %s | %s | %s |" % row for row in r["acted_where_staff_did_not"]]
    else:
        lines.append("None in this period.")
    lines += ["", "## Drafts the staff judged wrong", "", ", ".join(r["drafts_rejected"]) or "None in this period.",
              "", "## Handed over where the staff answered alone", "",
              ", ".join(r["handed_where_staff_answered"]) or "None in this period.",
              "", "## Limits of this report", "",
              "- The staff minutes are an upper bound on time that could move to the agent: the time to review its replies is not subtracted.",
              "- Each message was judged as it arrived. The agent held no conversation, so multi-message exchanges are compared weakly.",
              "- A draft nobody judged is not counted as correct."]
    if r["minutes_missing"]:
        lines.append("- %d of the counted messages have no minutes recorded." % r["minutes_missing"])
    if r["not_recorded"]:
        lines.append("- Observed messages with no staff record, outside every figure above: %d (%s)." % (len(r["not_recorded"]), ", ".join(r["not_recorded"])))
    if r["not_observed"]:
        lines.append("- Staff rows that match no observed message: %d (%s)." % (len(r["not_observed"]), ", ".join(r["not_observed"])))
    return "\n".join(lines) + "\n"


def main(argv):
    if len(argv) not in (0, 2):
        print(__doc__)
        return 2
    log_path, staff_path = argv or (os.path.join(SAMPLE, "sample-shadow-log.jsonl"), os.path.join(SAMPLE, "sample-staff-record.csv"))
    try:
        result = compare(read_log(log_path), read_staff(staff_path))
    except (ValueError, KeyError, OSError) as error:
        print("error:", error)
        return 1
    sys.stdout.write(render(result))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

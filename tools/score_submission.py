#!/usr/bin/env python3
# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Apply the Academy's completion standard to one graded deliverable. Standard library only.

    python3 tools/score_submission.py 3 --levels 3 3 2 3 2 --gates 5
    python3 tools/score_submission.py 4 --levels 4 3 3 3 4 --gates 5 --graduation-evidence

Levels are given in the order of the course's rubric (see 03-courses/assessment-standard.md).
The standard, version 1.0: all validation gates passed; no criterion at level 1; the lead
criterion at level 3 or above; weighted score of 2.7 or more out of 4. Distinction:
no criterion below level 3 and a weighted score of 3.5 or more. Course 4 also needs its
graduation evidence.
"""
import argparse
import sys

VERSION = "1.0"
PASS_SCORE, DISTINCTION_SCORE, LEAD_MINIMUM = 2.7, 3.5, 3
COURSES = {
    "1": {"name": "Opportunity", "gates": 5, "criteria": [("Customer evidence", 35), ("Workflow clarity", 25), ("Agent fit", 15), ("Economics", 15), ("Writing", 10)]},
    "2": {"name": "Build", "gates": 4, "criteria": [("Does the job", 30), ("Evaluation quality", 25), ("Guardrails", 20), ("Improvement", 15), ("Arabic quality", 10)]},
    "3": {"name": "Launch", "gates": 5, "criteria": [("Real usage", 30), ("Economics", 25), ("Compliance readiness", 20), ("Go-to-market", 15), ("Defensibility", 10)]},
    "4": {"name": "Scale and Govern", "gates": 5, "criteria": [("Customer evidence", 30), ("Operating design", 20), ("Governance and security", 20), ("Economics at scale", 15), ("Pitch", 15)]},
}


def decide(course, levels, gates_passed, graduation_evidence=False):
    """Return (decision, weighted score, reasons). decision is 'distinction', 'complete' or 'not yet complete'."""
    spec = COURSES[str(course)]
    criteria = spec["criteria"]
    if len(levels) != len(criteria) or any(level not in (1, 2, 3, 4) for level in levels):
        raise ValueError("give one level from 1 to 4 for each of the %d criteria" % len(criteria))
    if not 0 <= gates_passed <= spec["gates"]:
        raise ValueError("course %s has %d validation gates" % (course, spec["gates"]))
    score = round(sum(level * weight for level, (_, weight) in zip(levels, criteria)) / 100.0, 2)
    reasons = []
    if gates_passed < spec["gates"]:
        reasons.append("%d of %d validation gates passed: the work is returned ungraded" % (gates_passed, spec["gates"]))
    for level, (name, _) in zip(levels, criteria):
        if level == 1:
            reasons.append("'%s' is at level 1" % name)
    if levels[0] < LEAD_MINIMUM:
        reasons.append("the lead criterion '%s' is below level %d" % (criteria[0][0], LEAD_MINIMUM))
    if score < PASS_SCORE:
        reasons.append("weighted score %.2f is below %.1f" % (score, PASS_SCORE))
    if str(course) == "4" and not graduation_evidence:
        reasons.append("no graduation evidence: a signed LOI, a paying customer or sustained real usage")
    if reasons:
        return "not yet complete", score, reasons
    if min(levels) >= 3 and score >= DISTINCTION_SCORE:
        return "distinction", score, []
    return "complete", score, []


def main(argv=None):
    parser = argparse.ArgumentParser(description="Apply the SAAEA completion standard, version " + VERSION)
    parser.add_argument("course", choices=sorted(COURSES))
    parser.add_argument("--levels", type=int, nargs="+", required=True, help="one level (1 to 4) per criterion, in rubric order")
    parser.add_argument("--gates", type=int, required=True, help="number of validation gates passed")
    parser.add_argument("--graduation-evidence", action="store_true", help="Course 4 only")
    args = parser.parse_args(argv)
    try:
        decision, score, reasons = decide(args.course, args.levels, args.gates, args.graduation_evidence)
    except ValueError as error:
        parser.error(str(error))
    spec = COURSES[args.course]
    print("Course %s: %s (standard %s)" % (args.course, spec["name"], VERSION))
    for level, (name, weight) in zip(args.levels, spec["criteria"]):
        print("  %-24s %3d%%   level %d" % (name, weight, level))
    print("Weighted score: %.2f of 4 (%.0f%%)" % (score, 25 * score))
    print("Decision: " + decision.upper())
    for reason in reasons:
        print("  - " + reason)
    return 0 if decision != "not yet complete" else 1


if __name__ == "__main__":
    sys.exit(main())

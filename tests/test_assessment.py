# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Tests for the completion standard: the calculator, and its agreement with the four rubrics."""
import os
import re
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))

import score_submission as standard  # noqa: E402

FOLDERS = {"1": "01-opportunity", "2": "02-build", "3": "03-launch", "4": "04-scale-and-govern"}


def read(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as f:
        return f.read()


class CompletionStandard(unittest.TestCase):
    def test_good_overall_with_limited_weakness_completes(self):
        self.assertEqual(standard.decide("3", [3, 3, 2, 3, 2], 5)[0], "complete")
        self.assertEqual(standard.decide("2", [3, 3, 3, 3, 3], 4)[0], "complete")

    def test_all_developing_does_not_complete(self):
        decision, score, _ = standard.decide("2", [2, 2, 2, 2, 2], 4)
        self.assertEqual((decision, score), ("not yet complete", 2.0))

    def test_strong_minor_criteria_cannot_buy_a_weak_lead_criterion(self):
        decision, score, reasons = standard.decide("1", [2, 4, 4, 4, 4], 5)
        self.assertEqual(decision, "not yet complete")
        self.assertGreaterEqual(score, standard.PASS_SCORE)
        self.assertTrue(any("lead criterion" in r for r in reasons))

    def test_any_level_one_or_missing_gate_blocks(self):
        self.assertEqual(standard.decide("3", [4, 4, 4, 4, 1], 5)[0], "not yet complete")
        self.assertEqual(standard.decide("3", [4, 4, 4, 4, 4], 4)[0], "not yet complete")

    def test_course_4_needs_graduation_evidence(self):
        self.assertEqual(standard.decide("4", [4, 4, 4, 4, 4], 5)[0], "not yet complete")
        self.assertEqual(standard.decide("4", [4, 4, 4, 4, 4], 5, True)[0], "distinction")

    def test_distinction_needs_every_criterion_at_three_or_more(self):
        self.assertEqual(standard.decide("2", [4, 4, 4, 4, 2], 4)[0], "complete")
        self.assertEqual(standard.decide("2", [4, 4, 4, 3, 3], 4)[0], "distinction")

    def test_bad_input_is_rejected(self):
        for levels, gates in (([3, 3, 3, 3], 5), ([3, 3, 3, 3, 5], 5), ([3, 3, 3, 3, 3], 6)):
            with self.assertRaises(ValueError):
                standard.decide("1", levels, gates)

    def test_weights_and_gates_match_the_syllabi(self):
        for course, folder in FOLDERS.items():
            text = read("03-courses", folder, "syllabus.md")
            rubric = text.split("## Rubric")[1].split("\n## ")[0]
            weights = [int(w) for w in re.findall(r"^\| [^|]+ \| (\d+)% \|", rubric, re.M)]
            self.assertEqual(weights, [w for _, w in standard.COURSES[course]["criteria"]], folder)
            self.assertEqual(sum(weights), 100, folder)
            names = re.findall(r"^\| ([^|]+) \| \d+% \|", rubric, re.M)
            self.assertEqual(names, [n for n, _ in standard.COURSES[course]["criteria"]], folder)
            gates = text.split("## Validation gates")[1].split("\n## ")[0]
            self.assertEqual(len(re.findall(r"^\d\. ", gates, re.M)), standard.COURSES[course]["gates"], folder)

    def test_every_rubric_states_the_same_standard(self):
        for folder in FOLDERS.values():
            text = read("03-courses", folder, "rubrics.md")
            self.assertIn("## Completion", text, folder)
            self.assertIn("../assessment-standard.md", text, folder)
            self.assertIn("2.7", text, folder)
        shared = read("03-courses", "assessment-standard.md")
        self.assertIn("version %s" % standard.VERSION, shared)
        self.assertIn(str(standard.PASS_SCORE), shared)

    def test_every_outcome_is_taught_and_assessed_and_every_criterion_is_used(self):
        text = read("03-courses", "alignment.md")
        sections = text.split("\n## Course ")[1:]
        self.assertEqual(len(sections), 4)
        for section in sections:
            course = section[0]
            rows = re.findall(r"^\| (\d) \| .+? \| ([\d., ]+) \| Quizzes .+? \| (.+?) \|$", section, re.M)
            self.assertEqual([r[0] for r in rows], ["1", "2", "3", "4", "5"], "course " + course)
            used = set()
            for _, modules, criteria in rows:
                self.assertTrue(modules.strip())
                used.update(c.strip() for c in criteria.split(","))
            self.assertEqual(used, {name for name, _ in standard.COURSES[course]["criteria"]}, "course " + course)


if __name__ == "__main__":
    unittest.main()

# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Tests for the Academy's scripts. Run: python3 -m unittest discover -s tests

Each test runs a script the way a learner would and checks the figures that
the exercises quote, so the text and the code cannot drift apart unnoticed.
"""

import filecmp
import json
import os
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAB = os.path.join(ROOT, "05-agentic-ai-lab", "exercises")
B5 = os.path.join(LAB, "b5-venture-dashboard")
R8 = os.path.join(LAB, "r8-data-governance")
B6 = os.path.join(LAB, "b6-terminology")
B3 = os.path.join(LAB, "b3-deck-evidence")
SCENARIOS = ("baseline", "cost-spike", "quality-drop", "volume-up")


def run(*args, cwd=ROOT):
    return subprocess.run([sys.executable, *args], cwd=cwd, capture_output=True, text=True)


class RepositoryStructure(unittest.TestCase):
    def test_markdown_links_anchors_and_tables(self):
        result = run(os.path.join("tools", "check_repo.py"))
        self.assertEqual(result.returncode, 0, result.stdout)


class UnitEconomicsCalculator(unittest.TestCase):
    def test_default_run(self):
        result = run(os.path.join("04-entrepreneur-toolkit", "cost_per_resolved_task.py"))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Cost per resolved task", result.stdout)


class FounderCalculators(unittest.TestCase):
    TOOLKIT = "04-entrepreneur-toolkit"

    def test_funnel_default_run(self):
        result = run(os.path.join(self.TOOLKIT, "first_customers_funnel.py"))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("contacted -> replied (45%)", result.stdout)
        self.assertIn("at these rates: 200", result.stdout)

    def test_funnel_rejects_a_step_larger_than_the_one_before(self):
        result = run(os.path.join(self.TOOLKIT, "first_customers_funnel.py"), "--replied", "50")
        self.assertEqual(result.returncode, 2)

    def test_funnel_with_no_paying_customer_does_not_size_the_plan(self):
        result = run(os.path.join(self.TOOLKIT, "first_customers_funnel.py"), "--paying", "0")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("cannot be sized", result.stdout)

    def test_dilution_matches_the_worked_example(self):
        # Riyada's round-terms reference: 50% founder, 10% pool, 2m at 8m pre -> 36%.
        result = run(os.path.join(self.TOOLKIT, "round_dilution.py"),
                     "--founders", "0.5", "--round", "2000000:8000000:0.10")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("36.0%", result.stdout)

    def test_dilution_default_two_rounds(self):
        result = run(os.path.join(self.TOOLKIT, "round_dilution.py"))
        self.assertIn("57.6%", result.stdout)

    def test_dilution_rejects_a_malformed_round(self):
        result = run(os.path.join(self.TOOLKIT, "round_dilution.py"), "--round", "2000000")
        self.assertEqual(result.returncode, 2)


class FundingDirectory(unittest.TestCase):
    TOOL = os.path.join("tools", "check_funding_directory.py")

    def test_index_matches_the_page(self):
        result = run(self.TOOL, "--today", "2026-11-19")
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertNotIn("ERROR", result.stdout)

    def test_old_entries_are_flagged_and_strict_fails(self):
        result = run(self.TOOL, "--today", "2027-06-01", "--strict")
        self.assertEqual(result.returncode, 1)
        self.assertIn("STALE", result.stdout)

    def test_entry_missing_from_the_page_is_an_error(self):
        folder = os.path.join(ROOT, "02-saudi-market-knowledge-framework", "06-funding-investment")
        with open(os.path.join(folder, "funding-directory.json"), encoding="utf-8") as f:
            index = json.load(f)
        index["entries"].append(dict(index["entries"][0], name="Invented programme", match="برنامج لا وجود له"))
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(folder, "funding-directory.md"), encoding="utf-8") as f:
                page = f.read()
            with open(os.path.join(tmp, "funding-directory.md"), "w", encoding="utf-8") as f:
                f.write(page)
            path = os.path.join(tmp, "funding-directory.json")
            with open(path, "w", encoding="utf-8") as f:
                json.dump(index, f, ensure_ascii=False)
            result = run(self.TOOL, "--index", path, "--today", "2026-11-19")
        self.assertEqual(result.returncode, 1)
        self.assertIn("Invented programme", result.stdout)


class CaseLint(unittest.TestCase):
    A3 = os.path.join(LAB, "a3-sourced-case")
    TOOL = os.path.join(A3, "case_lint.py")
    SOURCES = os.path.join(ROOT, "SOURCES.md")

    def test_published_venture_cases_pass_strict(self):
        import glob
        cases = [p for p in glob.glob(os.path.join(ROOT, "06-case-studies", "ventures", "*.md"))
                 if os.path.basename(p) != "README.md"]
        self.assertEqual(len(cases), 12)
        result = run(self.TOOL, *cases, "--sources", self.SOURCES, "--strict")
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_sample_draft_gives_the_quoted_counts(self):
        result = run(self.TOOL, os.path.join(self.A3, "sample-draft.md"), "--sources", self.SOURCES)
        self.assertEqual(result.returncode, 1)
        self.assertIn("1 file(s), 5 error(s), 1 warning(s)", result.stdout)


class VentureDashboard(unittest.TestCase):
    def test_baseline_data_is_reproducible(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = run("generate_data.py", "--scenario", "baseline", "--out", tmp, cwd=B5)
            self.assertEqual(result.returncode, 0, result.stderr)
            shipped = os.path.join(B5, "data", "baseline")
            names = sorted(os.listdir(shipped))
            match, mismatch, errors = filecmp.cmpfiles(shipped, tmp, names, shallow=False)
            self.assertEqual((mismatch, errors), ([], []))

    def test_every_scenario_matches_expected_metrics(self):
        for scenario in SCENARIOS:
            with self.subTest(scenario=scenario), tempfile.TemporaryDirectory() as tmp:
                run("generate_data.py", "--scenario", scenario, "--out", tmp, cwd=B5)
                expected = os.path.join("expected", f"{scenario}.json")
                result = run("compute_metrics.py", tmp, "--compare", expected, cwd=B5)
                self.assertEqual(result.returncode, 0, result.stdout)

    def test_wrong_numbers_are_rejected(self):
        result = run("compute_metrics.py", os.path.join("data", "baseline"),
                     "--compare", os.path.join("expected", "volume-up.json"), cwd=B5)
        self.assertEqual(result.returncode, 1)

    def test_figures_quoted_in_the_exercise(self):
        with open(os.path.join(B5, "expected", "baseline.json"), encoding="utf-8") as f:
            overall = json.load(f)["overall"]
        self.assertEqual(overall["tasks_final"], 961)
        self.assertEqual(overall["agent_runs"], 1163)
        self.assertEqual(overall["tool_calls"], 3746)
        self.assertEqual(overall["success_rate_pct"], 93.3)
        self.assertEqual(overall["cost_per_successful_task"], 1.43)
        self.assertEqual(overall["gross_margin_pct"], 72.1)

    def test_misleading_scenario_is_misleading(self):
        def load(name):
            with open(os.path.join(B5, "expected", f"{name}.json"), encoding="utf-8") as f:
                return json.load(f)
        base, volume = load("baseline"), load("volume-up")
        self.assertGreater(volume["overall"]["gross_margin_pct"], base["overall"]["gross_margin_pct"])
        self.assertLess(volume["overall"]["avg_quality_score"], base["overall"]["avg_quality_score"])
        self.assertGreater(volume["growth"]["monthly_churn_pct"], base["growth"]["monthly_churn_pct"])


class DataGovernanceLint(unittest.TestCase):
    def test_sample_fails_with_the_quoted_counts(self):
        result = run("data_governance_lint.py", "dataset_sample.csv", "policy.json", cwd=R8)
        self.assertEqual(result.returncode, 1)
        self.assertIn("13 error(s), 2 warning(s)", result.stdout)

    def test_arabic_digits_are_detected(self):
        result = run("data_governance_lint.py", "dataset_sample.csv", "policy.json", cwd=R8)
        self.assertIn("message_text: 1 value(s) look like id_number", result.stdout)

    def test_clean_file_passes_strict(self):
        with tempfile.TemporaryDirectory() as tmp:
            data, policy = os.path.join(tmp, "clean.csv"), os.path.join(tmp, "policy.json")
            with open(data, "w", encoding="utf-8") as f:
                f.write("record_id,status\nA1,open\nA2,resolved\n")
            with open(policy, "w", encoding="utf-8") as f:
                json.dump({"key_column": "record_id", "required_columns": ["record_id", "status"],
                           "allowed_values": {"status": ["open", "resolved"]},
                           "column_classification": {"record_id": "internal", "status": "internal"}}, f)
            result = run("data_governance_lint.py", data, policy, "--strict", cwd=R8)
            self.assertEqual(result.returncode, 0, result.stdout)


class TerminologyLint(unittest.TestCase):
    def test_sample_gives_the_quoted_counts(self):
        result = run("terminology_lint.py", "glossary.csv", "sample-before.md", cwd=B6)
        self.assertEqual(result.returncode, 1)
        self.assertIn("4 error(s), 1 warning(s)", result.stdout)

    def test_customer_is_not_confused_with_agent(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "ok.md")
            with open(path, "w", encoding="utf-8") as f:
                f.write("يرد الوكيل على العميل خلال دقيقة، وسير العمل مكتوب.\n")
            result = run("terminology_lint.py", "glossary.csv", path, "--strict", cwd=B6)
            self.assertEqual(result.returncode, 0, result.stdout)


class DeckEvidenceCheck(unittest.TestCase):
    DECK = """<section class="slide" data-topic="problem"><h2>41% من الطلبات تتكرر</h2>
<p class="source">المصدر: سجل الطلبات</p></section>
<section class="slide" data-topic="economics"><h2>الهامش 27%</h2>{label}</section>
<section class="slide" data-topic="ask"><h2>خطتنا لعام 2027</h2></section>"""

    def check(self, label, *extra):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "deck.html")
            with open(path, "w", encoding="utf-8") as f:
                f.write(self.DECK.format(label=label))
            return run("deck_evidence_check.py", path, *extra, cwd=B3)

    def test_figure_without_source_fails(self):
        result = self.check("")
        self.assertEqual(result.returncode, 1)
        self.assertIn("EV001", result.stdout)

    def test_estimate_label_and_years_pass(self):
        self.assertEqual(self.check("<p>تقدير من الحاسبة</p>").returncode, 0)

    def test_required_topic(self):
        result = self.check("<p>تقدير</p>", "--require", "problem,governance")
        self.assertEqual(result.returncode, 1)
        self.assertIn("governance", result.stdout)


if __name__ == "__main__":
    unittest.main()

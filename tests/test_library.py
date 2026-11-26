# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""The methodology library: registry, cards, generated index and page."""
import copy
import os
import re
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import build_library as library  # noqa: E402


def read(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as f:
        return f.read()


class LibraryTests(unittest.TestCase):
    def setUp(self):
        self.registry = library.load()

    def test_registry_and_cards_have_no_problems(self):
        self.assertEqual(library.problems(self.registry), [])

    def test_index_and_page_are_up_to_date(self):
        result = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "build_library.py"), "--check"],
                                cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_every_card_is_on_the_page_and_every_link_on_the_page_exists(self):
        page = read("library.html")
        self.assertIn('<html lang="ar" dir="rtl">', page)
        for card in self.registry["cards"]:
            self.assertIn("read.html?p=09-methodology-library/cards/%s.md" % card["id"], page)
        for href in re.findall(r'href="([^"#]+)"', page):
            if href.startswith("read.html?p="):
                href = href[len("read.html?p="):]
            if not href.startswith("http"):
                self.assertTrue(os.path.exists(os.path.join(ROOT, href)), href)
        self.assertEqual(re.findall(r"<script[^>]+src=", page), [], "the page loads no script file")

    def test_both_landing_pages_and_the_four_syllabi_link_to_the_library(self):
        for name in ("index.html", "index.en.html"):
            self.assertIn('href="library.html"', read(name), name)
        for course in ("01-opportunity", "02-build", "03-launch", "04-scale-and-govern"):
            syllabus = read("03-courses", course, "syllabus.md")
            self.assertIn("09-methodology-library/cards/", syllabus, course)
            stage = int(course[:2])
            for cid in re.findall(r"09-methodology-library/cards/([a-z0-9-]+)\.md", syllabus):
                card = next(c for c in self.registry["cards"] if c["id"] == cid)
                self.assertIn(stage, card["stages"], "%s links %s, whose stages do not include course %d" % (course, cid, stage))

    def test_a_known_model_without_a_source_is_rejected(self):
        broken = copy.deepcopy(self.registry)
        broken["cards"][0]["sources"] = []
        self.assertTrue(any("needs a source" in line for line in library.problems(broken)))

    def test_an_unknown_source_and_a_missing_path_are_rejected(self):
        broken = copy.deepcopy(self.registry)
        broken["cards"][0]["sources"] = ["A9999"]
        broken["cards"][1]["used_in"] = ["03-courses/no-such-file.md"]
        found = "\n".join(library.problems(broken))
        self.assertIn("A9999 is not in SOURCES.md section A", found)
        self.assertIn("used_in path does not exist", found)

    def test_an_academy_model_must_say_so(self):
        broken = copy.deepcopy(self.registry)
        card = next(c for c in broken["cards"] if "من تطوير الأكاديمية" not in read("09-methodology-library", "cards", c["id"] + ".md"))
        card["origin"] = "academy"
        self.assertTrue(any("must say so" in line for line in library.problems(broken)))

    def test_no_share_alike_canvas_is_bundled(self):
        """The Business Model Canvas and Lean Canvas are CC BY-SA; the Value Proposition Canvas is copyrighted (SOURCES.md A187, A188)."""
        folder = os.path.join(ROOT, "09-methodology-library")
        for base, _, files in os.walk(folder):
            for name in files:
                self.assertTrue(name.endswith((".md", ".json")), "unexpected file in the library: " + name)
        nine = ["Key Partners", "Key Activities", "Key Resources", "Customer Relationships", "Revenue Streams"]
        for card in self.registry["cards"]:
            text = read("09-methodology-library", "cards", card["id"] + ".md")
            self.assertLess(sum(block in text for block in nine), 3, card["id"] + " looks like a copy of a canvas")

    def test_planned_names_are_unique(self):
        names = [name for group in self.registry["planned"].values() for name in group]
        self.assertEqual(len(names), len(set(names)))


if __name__ == "__main__":
    unittest.main()

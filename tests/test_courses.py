# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Tests for course materials. Run: python3 -m unittest discover -s tests

They keep three things from drifting apart unnoticed: the built slide decks and
their sources, the speaker notes, and each quiz and its answer key.
"""

import glob
import os
import re
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COURSES = os.path.join(ROOT, "03-courses")
LETTERS = "أبجد"


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def slides_of(html):
    """The slides of a built deck: the sections inside <main>, not the engine's script."""
    body = html[html.index("<main"):html.index("</main>")]
    found = re.findall(r'<section class="slide.*?</section>', body, flags=re.S)
    assert found, "no slides found"
    return found


class SlideDecks(unittest.TestCase):
    def test_built_decks_match_their_sources(self):
        result = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "build_slides.py"), "--check"],
                                cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_every_slide_has_speaker_notes(self):
        decks = glob.glob(os.path.join(COURSES, "*", "slides", "*.html"))
        self.assertGreaterEqual(len(decks), 15)
        for deck in decks:
            for number, slide in enumerate(slides_of(read(deck)), 1):
                self.assertEqual(slide.count('<template class="notes">'), 1,
                                 "%s slide %d" % (os.path.basename(deck), number))

    def test_deck_counts_in_readmes_match_the_decks(self):
        for readme in glob.glob(os.path.join(COURSES, "*", "slides", "README.md")):
            folder = os.path.dirname(readme)
            for name, count in re.findall(r"\]\(([\w.-]+\.html)\)[^|]*\| (\d+) \|", read(readme)):
                actual = len(slides_of(read(os.path.join(folder, name))))
                self.assertEqual(int(count), actual, "%s says %s slides, deck has %d" % (name, count, actual))


class LandingPage(unittest.TestCase):
    def test_index_is_up_to_date_and_lists_every_deck(self):
        result = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "build_site.py"), "--check"],
                                cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout)
        page = read(os.path.join(ROOT, "index.html"))
        for deck in glob.glob(os.path.join(COURSES, "*", "slides", "*.html")):
            self.assertIn(os.path.relpath(deck, ROOT).replace(os.sep, "/"), page)
        for href in re.findall(r'href="([^"#]+)"', page):
            if not href.startswith("http"):
                self.assertTrue(os.path.exists(os.path.join(ROOT, href)), href)


class Workbook(unittest.TestCase):
    def test_every_repository_link_in_the_workbook_exists(self):
        page = read(os.path.join(ROOT, "workbook", "index.html"))
        paths = re.findall(r'"(0\d-[\w./-]+\.md)"', page)
        self.assertGreaterEqual(len(paths), 12)
        for path in paths:
            self.assertTrue(os.path.exists(os.path.join(ROOT, path)), path)

    def test_the_workbook_keeps_data_in_the_browser(self):
        page = read(os.path.join(ROOT, "workbook", "index.html"))
        for call in ("fetch(", "XMLHttpRequest", "sendBeacon", "<form"):
            self.assertNotIn(call, page)


class Quizzes(unittest.TestCase):
    def test_every_question_has_four_options_and_a_valid_key(self):
        quizzes = sorted(glob.glob(os.path.join(COURSES, "*", "quizzes", "*-quiz.md")))
        self.assertGreaterEqual(len(quizzes), 15)
        for path in quizzes:
            name = os.path.basename(path)
            text = read(path)
            self.assertIn("## مفتاح الإجابة", text, name)
            body, key = text.split("## مفتاح الإجابة", 1)
            questions = re.split(r"\n### س\d+", body)[1:]
            answers = re.findall(r"^\d+\. \*\*([%s](?: و[%s])*)\.\*\*" % (LETTERS, LETTERS), key, flags=re.M)
            self.assertEqual(len(questions), len(answers), "%s: %d questions, %d answers" % (name, len(questions), len(answers)))
            for number, (question, answer) in enumerate(zip(questions, answers), 1):
                options = re.findall(r"^- ([%s])\) (.+)$" % LETTERS, question, flags=re.M)
                self.assertEqual([letter for letter, _ in options], list(LETTERS), "%s question %d" % (name, number))
                self.assertEqual(len({text for _, text in options}), 4, "%s question %d repeats an option" % (name, number))
                for letter in re.findall("[%s]" % LETTERS, answer):
                    self.assertIn(letter, LETTERS)

    def test_every_lesson_links_to_its_quiz(self):
        for lesson in glob.glob(os.path.join(COURSES, "*", "lessons", "*.md")):
            module = os.path.basename(lesson)[:3]
            self.assertIn("../quizzes/%s-quiz.md" % module, read(lesson), os.path.basename(lesson))


if __name__ == "__main__":
    unittest.main()

# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Tests for course materials. Run: python3 -m unittest discover -s tests

They keep these from drifting apart unnoticed: the built slide decks and their
sources, the speaker notes, each quiz and its answer key, and the structure every
course shares (supporting files, syllabus hours, lesson parts, instructor guides).
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


class CourseStructure(unittest.TestCase):
    """Every course is complete and its parts agree: the checks of the QA audit of 20 November 2026."""

    REQUIRED = ["syllabus.md", "glossary.md", "rubrics.md", "instructor-guide.md", "not-adopted.md",
                os.path.join("quizzes", "README.md"), os.path.join("slides", "README.md")]
    SECTIONS = ["ابدأ من هنا", "Modules", "Track differences", "Deliverable", "Validation gates", "Rubric",
                "Common mistakes", "What is still missing"]
    GUIDE = ["Before the first session", "Delivery schedules", "Time inside each module", "Materials checklist",
             "What a facilitator should not do", "Before each cohort"]

    def courses(self):
        found = sorted(glob.glob(os.path.join(COURSES, "0*")))
        self.assertEqual(len(found), 4)
        return found

    def test_every_course_has_its_supporting_files(self):
        for course in self.courses():
            for name in self.REQUIRED:
                self.assertTrue(os.path.exists(os.path.join(course, name)), "%s lacks %s" % (os.path.basename(course), name))
            self.assertTrue(glob.glob(os.path.join(course, "examples", "*.md")), "no worked example in " + course)
            self.assertTrue(glob.glob(os.path.join(course, "templates", "*.md")), "no templates in " + course)

    def test_syllabus_hours_modules_and_sections_agree(self):
        for number, course in enumerate(self.courses(), 1):
            text = read(os.path.join(course, "syllabus.md"))
            stated = int(re.search(r"\*\*المدة:\*\* (\d+) ساعة", text).group(1))
            modules = re.findall(r"^\| %d\.\d \| .+? \| (\d+) \|" % number, text.split("## Modules")[1], re.M)
            self.assertEqual(stated, sum(int(h) for h in modules), os.path.basename(course))
            self.assertEqual(len(modules), len(glob.glob(os.path.join(course, "lessons", "*.md"))), os.path.basename(course))
            for field in ("**المستوى:**", "**المتطلب السابق:**", "**نواتج التعلّم:**"):
                self.assertIn(field, text, os.path.basename(course))
            headings = re.findall(r"^## (.+)$", text, re.M)
            for needed in self.SECTIONS:
                self.assertTrue(any(h.startswith(needed) for h in headings), "%s syllabus lacks '%s'" % (os.path.basename(course), needed))

    def test_every_lesson_has_the_standard_parts(self):
        for course in self.courses():
            outcomes = len(re.findall(r"^\d\. ", read(os.path.join(course, "syllabus.md")).split("نواتج التعلّم")[1].split("##")[0], re.M))
            for lesson in glob.glob(os.path.join(course, "lessons", "*.md")):
                text, name = read(lesson), os.path.basename(lesson)
                self.assertEqual(len(re.findall(r"^# .+$", text, re.M)), 2, name + ": Arabic and English titles")
                head = re.search(r"\*\*المدة:\*\* .+? · \*\*ناتج التعلّم:\*\* (.+?) · \*\*المخرج:\*\*", text)
                self.assertTrue(head, name + ": header line")
                for outcome in re.findall(r"\d", head.group(1)):
                    self.assertLessEqual(int(outcome), outcomes, name + ": outcome number")
                for part in ("## مراجعة سريعة", "## أخطاء شائعة", "## اختبر فهمك", "**التنقل:**", "(../syllabus.md)", "**English summary.**"):
                    self.assertIn(part, text, "%s lacks %s" % (name, part))
                self.assertEqual(text.count('<div dir="rtl">'), text.count("</div>"), name + ": unbalanced div")

    def test_every_lesson_has_a_deck_and_a_ten_question_quiz(self):
        for course in self.courses():
            for lesson in glob.glob(os.path.join(course, "lessons", "*.md")):
                name = os.path.basename(lesson)
                self.assertTrue(os.path.exists(os.path.join(course, "slides", name.replace(".md", ".html"))), "no deck for " + name)
                quiz = read(os.path.join(course, "quizzes", name[:3] + "-quiz.md"))
                self.assertGreaterEqual(len(re.findall(r"^### س\d+", quiz, re.M)), 10, name)

    def test_instructor_guides_share_a_core(self):
        for course in self.courses():
            headings = re.findall(r"^## (.+)$", read(os.path.join(course, "instructor-guide.md")), re.M)
            for needed in self.GUIDE:
                self.assertTrue(any(h.startswith(needed) for h in headings), "%s instructor guide lacks '%s'" % (os.path.basename(course), needed))

    def test_rubrics_have_gates_four_levels_and_calibration(self):
        for course in self.courses():
            text = read(os.path.join(course, "rubrics.md"))
            for part in ("Validation gates", "4 متقن", "1 غير مكتمل", "معايرة المقيّمين"):
                self.assertIn(part, text, "%s rubrics lack %s" % (os.path.basename(course), part))


if __name__ == "__main__":
    unittest.main()

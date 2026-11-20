# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""The founder agents: every published agent has what the operating standard asks a contribution to have."""
import glob
import os
import re
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOLDER = os.path.join(ROOT, "02-saudi-market-knowledge-framework", "founder-agents")
STANDARD = ["اذكر مصدر كل معلومة", "«للتحقق»", "غير متوفر في مصادري", "لا تذكر من ذاكرتك", "لا تقل «أنت ممتثل»", "ألا يلصق بيانات شخصية"]


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


class FounderAgents(unittest.TestCase):
    def setUp(self):
        self.pages = sorted(glob.glob(os.path.join(FOLDER, "[01][0-9]-*.md")))

    def test_agents_two_to_twelve_each_have_a_page_listed_in_the_index(self):
        self.assertEqual([int(os.path.basename(p)[:2]) for p in self.pages], list(range(2, 13)))
        index = read(os.path.join(FOLDER, "README.md"))
        for page in self.pages:
            self.assertIn("(%s)" % os.path.basename(page), index)
        self.assertNotIn("| Wanted", index)

    def test_every_definition_carries_the_operating_standard_and_says_what_it_is_not(self):
        for page in self.pages:
            definition = re.search(r"```text\n(.*?)```", read(page), re.S).group(1)
            for rule in STANDARD:
                self.assertIn(rule, definition, page)
            self.assertRegex(definition.split("\n\n")[0], r"لست|لا توصي", page)

    def test_every_agent_has_the_three_test_conversations_and_an_honest_status(self):
        for page in self.pages:
            text = read(page)
            for case in ("حالة عادية", "الجواب الصحيح «لا أعرف»", "ضغط للحصول على جواب قاطع"):
                self.assertEqual(text.count("| %s |" % case), 1, page)
            self.assertIn("Not yet tried with founders", text, page)
            self.assertIn("**Recorded runs:**", text, page)


if __name__ == "__main__":
    unittest.main()

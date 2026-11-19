#!/usr/bin/env python3
# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Build the course slide decks. One engine for every course. Standard library only.

    python3 tools/build_slides.py            build every deck
    python3 tools/build_slides.py --check    exit 1 if a committed deck differs from its source

Each course keeps its fragments in 03-courses/<course>/slides/src/<n>-<m>.html and the
built decks beside them in 03-courses/<course>/slides/. The page template is
tools/slides/template.html (engine from Bayan's arabic-html-slides, MIT).

Shorthand used in the fragments:
  ‹term›        English term inside Arabic text  -> <bdi dir="ltr" lang="en" class="en">term</bdi>
  ⟦27%⟧         number, range or symbol run      -> <bdi dir="ltr">27%</bdi>
  <notes>...</notes>                             -> <template class="notes">...</template> (speaker notes)
  {{MOTIF}}     Sadu-to-graph motif for dark title slides
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "tools" / "slides" / "template.html"

# course number -> (slides folder, [(source fragment, built deck, Arabic title, English module name)])
COURSES = {
    "1": ("03-courses/01-opportunity/slides", [
        ("1-1.html", "1-1-from-chatbots-to-agents.html", "الوحدة 1.1 | من المحادث الآلي إلى الوكيل", "Module 1.1 From chatbots to agents"),
        ("1-2.html", "1-2-agent-native-business.html", "الوحدة 1.2 | المنشأة القائمة على الوكلاء", "Module 1.2 The agent-native business"),
        ("1-3.html", "1-3-where-to-look.html", "الوحدة 1.3 | أين تبحث في السوق السعودي؟", "Module 1.3 Where to look in the Saudi market"),
        ("1-4.html", "1-4-workflow-shadowing.html", "الوحدة 1.4 | مراقبة سير العمل", "Module 1.4 Workflow shadowing"),
        ("1-5.html", "1-5-customer-discovery.html", "الوحدة 1.5 | اكتشاف العملاء", "Module 1.5 Customer discovery"),
        ("1-6.html", "1-6-scoring-and-economics.html", "الوحدة 1.6 | التقييم والاقتصاديات الأولى", "Module 1.6 Scoring and first economics"),
        ("1-7.html", "1-7-writing-the-thesis.html", "الوحدة 1.7 | كتابة أطروحة الفرصة", "Module 1.7 Writing the opportunity thesis"),
    ]),
    "2": ("03-courses/02-build/slides", [
        ("2-1.html", "2-1-agent-anatomy.html", "الوحدة 2.1 | تشريح الوكيل", "Module 2.1 Agent anatomy"),
        ("2-2.html", "2-2-context-engineering-in-arabic.html", "الوحدة 2.2 | هندسة السياق بالعربية", "Module 2.2 Context engineering in Arabic"),
        ("2-3.html", "2-3-tools-and-integrations.html", "الوحدة 2.3 | الأدوات والتكاملات", "Module 2.3 Tools and integrations"),
        ("2-4.html", "2-4-choosing-a-model.html", "الوحدة 2.4 | اختيار النموذج", "Module 2.4 Choosing a model"),
        ("2-5.html", "2-5-evaluation.html", "الوحدة 2.5 | التقييم", "Module 2.5 Evaluation"),
        ("2-6.html", "2-6-guardrails-and-human-approval.html", "الوحدة 2.6 | ضوابط الحماية والموافقة البشرية", "Module 2.6 Guardrails and human approval"),
        ("2-7.html", "2-7-from-one-agent-to-several.html", "الوحدة 2.7 | من وكيل واحد إلى عدة وكلاء", "Module 2.7 From one agent to several"),
        ("2-8.html", "2-8-failure-analysis-and-iteration.html", "الوحدة 2.8 | تحليل الإخفاق والتحسين", "Module 2.8 Failure analysis and iteration"),
    ]),
}


def motif():
    """Sadu-style diamonds at the outer edge that loosen into a node-and-arrow graph."""
    parts = ['<div class="motif" aria-hidden="true"><svg viewBox="0 0 760 520" fill="none">']
    gold, white = "#d97706", "#f8fafc"
    # Sadu band: rows of diamonds and zigzags along the outer edge.
    for r, y in enumerate(range(26, 520, 52)):
        for c, x in enumerate(range(760 - 26, 430, -52)):
            fade = max(0.0, 1 - (760 - x) / 330)
            col = gold if (r + c) % 2 == 0 else white
            op = round(0.15 + 0.75 * fade, 2)
            parts.append('<path d="M%d %d l22 -22 l22 22 l-22 22 z" fill="%s" opacity="%s"/>' % (x - 22, y, col, op))
        parts.append('<path d="M450 %d %s" stroke="%s" stroke-width="2" opacity=".35"/>' % (
            y + 26, " ".join("L%d %d" % (450 + 26 * i, y + 26 + (10 if i % 2 else -10)) for i in range(1, 13)), gold))
    # Graph: nodes and directed edges drifting inward.
    nodes = [(400, 90), (300, 170), (400, 260), (250, 330), (150, 230), (330, 420), (120, 400)]
    edges = [(0, 1), (1, 2), (1, 4), (2, 3), (4, 3), (3, 5), (3, 6), (2, 5)]
    for a, b in edges:
        (x1, y1), (x2, y2) = nodes[a], nodes[b]
        parts.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="3" opacity=".7"/>' % (x1, y1, x2, y2, white))
    for i, (x, y) in enumerate(nodes):
        fill = gold if i in (0, 3) else "#1e293b"
        parts.append('<circle cx="%d" cy="%d" r="%d" fill="%s" stroke="%s" stroke-width="4"/>' % (x, y, 18 if i in (0, 3) else 13, fill, gold if i not in (0, 3) else white))
    parts.append('</svg></div>')
    return "".join(parts)


def expand(src):
    src = re.sub(r"‹([^›]+)›", r'<bdi dir="ltr" lang="en" class="en">\1</bdi>', src)
    src = re.sub(r"⟦([^⟧]+)⟧", r'<bdi dir="ltr">\1</bdi>', src)
    src = src.replace("<notes>", '<template class="notes">').replace("</notes>", "</template>")
    src = src.replace("{{MOTIF}}", motif())
    # Numeric table cells: isolate the content so signs, parentheses and ranges keep their order in RTL.
    src = re.sub(r'(<t[dh] class="n">)(?!<bdi)(.*?)(</t[dh]>)', r'\1<bdi dir="ltr">\2</bdi>\3', src)
    return src


def render(course, src_name, title, en, fragment, template):
    html = template.replace("{{COURSE}}", course).replace("{{TITLE}}", title)
    html = html.replace("{{MODULE_EN}}", en).replace("{{SRC}}", src_name)
    return html.replace("{{SLIDES}}", expand(fragment))


def decks(only=None):
    """Yield (course, source path, output path, html) for every deck."""
    template = TEMPLATE.read_text(encoding="utf-8")
    for course, (folder, items) in COURSES.items():
        if only and course != only:
            continue
        base = ROOT / folder
        for src_name, out_name, title, en in items:
            src = base / "src" / src_name
            html = render(course, src_name, title, en, src.read_text(encoding="utf-8"), template)
            yield course, src, base / out_name, html


def main(argv):
    check = "--check" in argv
    only = next((a for a in argv if a in COURSES), None)
    stale = []
    for course, src, out, html in decks(only):
        if check:
            if not out.exists() or out.read_text(encoding="utf-8") != html:
                stale.append(str(out.relative_to(ROOT)))
        else:
            out.write_text(html, encoding="utf-8")
            print("built", out.name, html.count('class="slide'), "slides")
    if check:
        for name in stale:
            print("out of date:", name)
        print("%d deck(s) out of date" % len(stale))
        return 1 if stale else 0
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

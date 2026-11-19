#!/usr/bin/env python3
"""Build the Course 2 decks from slides/src/*.html fragments into slides/*.html.

Shorthand used in the fragments:
  ‹term›        English term inside Arabic text  -> <bdi dir="ltr" lang="en" class="en">term</bdi>
  ⟦27%⟧         number, range or symbol run      -> <bdi dir="ltr">27%</bdi>
  <notes>…</notes>                               -> <template class="notes">…</template> (speaker notes)
  {{MOTIF}}     Sadu-to-graph motif for dark title slides
Usage: python3 build.py   (from any directory)
"""
import pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent
DECKS = [
    ("2-1.html", "2-1-agent-anatomy.html", "الوحدة 2.1 | تشريح الوكيل", "Module 2.1 Agent anatomy"),
    ("2-2.html", "2-2-context-engineering-in-arabic.html", "الوحدة 2.2 | هندسة السياق بالعربية", "Module 2.2 Context engineering in Arabic"),
    ("2-3.html", "2-3-tools-and-integrations.html", "الوحدة 2.3 | الأدوات والتكاملات", "Module 2.3 Tools and integrations"),
    ("2-4.html", "2-4-choosing-a-model.html", "الوحدة 2.4 | اختيار النموذج", "Module 2.4 Choosing a model"),
    ("2-5.html", "2-5-evaluation.html", "الوحدة 2.5 | التقييم", "Module 2.5 Evaluation"),
    ("2-6.html", "2-6-guardrails-and-human-approval.html", "الوحدة 2.6 | ضوابط الحماية والموافقة البشرية", "Module 2.6 Guardrails and human approval"),
    ("2-7.html", "2-7-from-one-agent-to-several.html", "الوحدة 2.7 | من وكيل واحد إلى عدة وكلاء", "Module 2.7 From one agent to several"),
    ("2-8.html", "2-8-failure-analysis-and-iteration.html", "الوحدة 2.8 | تحليل الإخفاق والتحسين", "Module 2.8 Failure analysis and iteration"),
]


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


def main():
    template = (HERE / "_template.html").read_text(encoding="utf-8")
    for src_name, out_name, title, en in DECKS:
        path = HERE / src_name
        if not path.exists():
            continue
        html = template.replace("{{TITLE}}", title).replace("{{MODULE_EN}}", en).replace("{{SRC}}", src_name)
        html = html.replace("{{SLIDES}}", expand(path.read_text(encoding="utf-8")))
        (OUT / out_name).write_text(html, encoding="utf-8")
        print("built", out_name, html.count('class="slide'), "slides")


if __name__ == "__main__":
    main()

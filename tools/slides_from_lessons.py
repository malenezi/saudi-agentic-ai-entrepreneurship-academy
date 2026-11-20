#!/usr/bin/env python3
# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Generate first-version slide fragments from the lessons of a course. Standard library only.

    python3 tools/slides_from_lessons.py 3 4      write 03-courses/<course>/slides/src/<n>-<m>.html

A deck built this way carries nothing that is not in its lesson: one slide per numbered
section (its table, its list or its key sentences), then the activity, the track
differences, the common mistakes and the quick review. The first paragraph of each
section becomes the speaker notes. The fragments are plain HTML and can be edited by
hand afterwards; once a fragment is hand-edited, do not regenerate it.
Then run tools/build_slides.py to build the decks.

slides/src/fit.json lists, per deck, the slides that overflowed the 1600x900 stage when
rendered, with a tightening level (fewer rows or items, shorter cells) for each.
"""
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FOLDERS = {"3": "03-courses/03-launch", "4": "03-courses/04-scale-and-govern"}
MAX_ITEM, MAX_CELL, MAX_ROWS, MAX_ITEMS, MAX_TABLE = 120, 95, 6, 6, 620
SHRINK = 0  # set per slide from slides/src/fit.json: slides that overflowed at 1600x900 get tighter limits


def plain(text):
    """Markdown inline -> text with bold markers kept as control characters."""
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"\(\[[ABCD]\d+\]\([^)]*\)(?:[،,] *\[[ABCD]\d+\]\([^)]*\))*\)", "", text)  # (source ids)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\*\*(.+?)\*\*", "\x01\\1\x02", text)
    text = text.replace("*", "").replace("<br>", " ")
    return re.sub(r"\s+", " ", text).strip()


def clip(text, limit):
    """Cut at a sentence or clause boundary; never mid-clause."""
    if len(text) <= limit:
        return text
    cut = text[:limit]
    for marks in (".؟!", "؛:", "،"):
        pos = max(cut.rfind(m) for m in marks)
        if pos > limit * 0.45:
            out = cut[:pos].rstrip()
            break
    else:
        out = cut[:cut.rfind(" ")].rstrip() + "…"
    if out.count("\x01") > out.count("\x02"):
        out += "\x02"
    if out.count("«") > out.count("»"):
        out += "»"
    if out.count("(") > out.count(")"):
        out = out[:out.rfind("(")].rstrip()
    return out


def mark(text):
    """Escape, isolate Latin terms and numeric runs, restore bold."""
    text = html.escape(text, quote=False)
    def latin(m):
        return "‹" + m.group(0) + "›"
    text = re.sub(r"[A-Za-z][A-Za-z0-9\-\.:/'’ ]*[A-Za-z0-9]|[A-Za-z]", latin, text)
    def num(m):
        return m.group(0) if m.group(0).isdigit() else "⟦" + m.group(0) + "⟧"
    parts = re.split(r"(‹[^›]*›)", text)
    for i in range(0, len(parts), 2):
        parts[i] = re.sub(r"\d[\d.,/%×:+\-–]*[\d%]|\d+%?", num, parts[i])
    text = "".join(parts)
    return text.replace("\x01", "<b>").replace("\x02", "</b>")


def blocks(body):
    """Split a section body into ('p'|'ul'|'ol'|'table', data) blocks."""
    out, lines, i = [], body.split("\n"), 0
    while i < len(lines):
        ln = lines[i].strip()
        if not ln or ln.startswith(("<div", "</div", "```", "<details", "</details", "<summary", "###", ">")):
            if ln.startswith("```"):
                i += 1
                while i < len(lines) and not lines[i].strip().startswith("```"):
                    i += 1
            i += 1
            continue
        if ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            out.append(("table", rows))
            continue
        m = re.match(r"(-|\d+\.) +(.*)", ln)
        if m:
            kind, items = ("ul" if m.group(1) == "-" else "ol"), []
            while i < len(lines):
                m2 = re.match(r"\s*(-|\d+\.) +(.*)", lines[i])
                if not m2:
                    if lines[i].strip() == "" and i + 1 < len(lines) and re.match(r"\s*(-|\d+\.) +", lines[i + 1]):
                        i += 1
                        continue
                    break
                items.append(m2.group(2))
                i += 1
            out.append((kind, items))
            continue
        out.append(("p", ln))
        i += 1
    return out


def table_html(rows):
    rows = [r for r in rows if any(r)]
    head, body = rows[0], rows[1:MAX_ROWS + 1 - SHRINK]
    if len(head) > 4 or not body:
        return None
    cells = [[clip(plain(c), MAX_CELL - 12 * SHRINK) for c in r] for r in [head] + body]
    if sum(len(c) for r in cells for c in r) > MAX_TABLE:
        return None
    th = "".join("<th>%s</th>" % mark(c) for c in cells[0])
    trs = "".join("        <tr data-step>%s</tr>\n" % "".join("<td>%s</td>" % mark(c) for c in r) for r in cells[1:])
    return '    <table class="tbl">\n      <thead><tr>%s</tr></thead>\n      <tbody>\n%s      </tbody>\n    </table>\n' % (th, trs)


def list_html(items, cls="checks", tag="ul", limit=MAX_ITEMS, size=MAX_ITEM):
    items = [clip(plain(x), size - 15 * SHRINK) for x in items][:max(3, limit - SHRINK)]
    items = [x for x in items if x]
    if not items:
        return None
    if cls == "checks" and len(items) > 4 and max(len(x) for x in items) <= 62:
        cls = "checks cols2"
    lis = "".join("      <li data-step>%s</li>\n" % mark(x) for x in items)
    return '    <%s class="%s">\n%s    </%s>\n' % (tag, cls, lis, tag)


def sentences(paragraphs, limit=3):
    out = []
    for p in paragraphs:
        for s in re.split(r"(?<=[.؟!]) +", plain(p)):
            if 25 <= len(s) <= 150 and len(out) < limit:
                out.append(s)
    return out


def notes_of(paragraphs, extra=""):
    text = " ".join(plain(p) for p in paragraphs[:2])
    text = clip(text, 420).replace("\x01", "").replace("\x02", "")
    text = (text + " " + extra).strip() or "راجع البند في الدرس قبل الجلسة."
    return "    <notes>%s</notes>\n" % html.escape(text, quote=False)


def slide(tag, kicker, title, content, notes, badge=False):
    b = '    <span class="badge illus">مثال المقرر · أرقام مختلقة</span>\n' if badge else ""
    return ('  <section class="slide">\n%s    <span class="modtag">%s</span>\n    <p class="kicker">%s</p>\n    <h2>%s</h2>\n%s%s  </section>\n'
            % (b, mark(tag), mark(kicker), mark(clip(plain(title), 95)), content, notes))


def build(course, path):
    text = path.read_text(encoding="utf-8")
    num = path.name[:3].replace("-", ".")
    h1 = re.findall(r"^# (.+)$", text, re.M)
    title = re.sub(r"^الوحدة [\d.]+: *", "", h1[0]).strip()
    head = re.search(r"\*\*المدة:\*\* (.+?) · \*\*ناتج التعلّم:\*\* (.+?) · \*\*المخرج:\*\* (.+)", text)
    dur, outc, deliv = (plain(x) for x in head.groups())
    main = text.split("**English summary.**")[0]
    secs = re.split(r"^## (.+)$", main, flags=re.M)
    sections = [(secs[i].strip(), secs[i + 1]) for i in range(1, len(secs) - 1, 2)]
    tag = "%s · %s" % (num, title)
    fit_file = path.parent.parent / "slides" / "src" / "fit.json"
    fit = json.loads(fit_file.read_text(encoding="utf-8")).get(path.name[:3], {}) if fit_file.exists() else {}

    class Deck(list):
        def append(self, item):
            global SHRINK
            list.append(self, item)
            SHRINK = fit.get(str(len(self) + 1), 0)
    out = Deck()
    idea = next((b for h, b in sections if h.startswith("الفكرة")), "")
    idea_ps = [d for k, d in blocks(idea) if k == "p"]
    lead = sentences(idea_ps, 2)
    if lead:
        lead = [lead[0], clip(plain(idea_ps[0]), 170)] if len(plain(idea_ps[0])) > len(lead[0]) + 20 else [lead[0]] + [clip(plain(p), 170) for p in idea_ps[1:2]]
    out.append('  <section class="slide dark" data-layout="title">\n    {{MOTIF}}\n    <p class="kicker">المقرر %s · الوحدة %s</p>\n    <h1>%s</h1>\n    <p class="sub">%s</p>\n    <div class="meta"><span><b>%s</b></span><span>ناتج التعلّم <b>%s</b></span><span>المخرج: %s</span></div>\n%s  </section>\n'
               % (course, mark(num), mark(title), mark(lead[0] if lead else title), mark(dur), mark(outc), mark(clip(deliv, 90)),
                  notes_of(idea_ps, "العرض مولَّد من الدرس: كل شريحة تحمل بنداً منه، والتفصيل في الدرس نفسه.")))
    if len(lead) > 1:
        out.append('  <section class="slide" data-layout="statement">\n    <span class="modtag">%s</span>\n    <p class="kicker">الفكرة</p>\n    <h2>%s</h2>\n%s  </section>\n'
                   % (mark(tag), mark(lead[1]), notes_of(idea_ps[1:] or idea_ps)))
    numbered = [(h, b) for h, b in sections if re.match(r"\d+\. ", h)]
    agenda = list_html([re.sub(r"^\d+\. ", "", h) for h, _ in numbered], limit=10, size=70)
    if agenda:
        out.append(slide(tag, "ما في هذه الوحدة", "%d بنود، ثم نشاط يُخرج %s" % (len(numbered), clip(deliv, 60)), agenda,
                         "    <notes>اعرض الخريطة في دقيقة. قل للمتعلمين أي بند سيأخذ أطول وقت، وأن المخرج يُبنى أثناء الجلسة لا بعدها.</notes>\n"))
    for h, b in numbered:
        n, name = h.split(". ", 1)
        bl = blocks(b)
        ps = [d for k, d in bl if k == "p"]
        badge = any(w in b for w in ("ريم", "مختلق", "مثال المقرر"))
        made = 0
        for k, d in bl:
            if k == "table" and made < 2:
                t = table_html(d)
                if t:
                    extra = "الجدول كاملاً في الدرس." if len(d) - 1 > MAX_ROWS else ""
                    out.append(slide(tag, "البند %s" % n, name, t, notes_of(ps, extra), badge))
                    made += 1
        if made == 0:
            for k, d in bl:
                if k == "table" and len(d) > 2 and len(d[0]) >= 2:
                    rows = ["**%s**: %s" % (plain(r[0]).replace("\x01", "").replace("\x02", ""), clip(plain(r[1]), 80)) for r in d[1:] if len(r) > 1 and r[0]]
                    t = list_html(rows, size=130)
                    if t:
                        out.append(slide(tag, "البند %s" % n, name, t, notes_of(ps, "الجدول كاملاً في الدرس."), badge))
                        made += 1
                        break
        if made == 0:
            lists = [d for k, d in bl if k in ("ul", "ol")]
            items = max(lists, key=len) if lists else []
            content = list_html(items) if len(items) >= 3 else None
            if not content:
                bolds = re.findall(r"\*\*(.+?)\*\*", " ".join(ps))
                content = list_html(["**%s**" % x for x in bolds if len(x) > 8]) if len(bolds) >= 3 else None
            if not content:
                content = list_html(sentences(ps, 3), size=150) or ""
            out.append(slide(tag, "البند %s" % n, name, content, notes_of(ps), badge))
    def sec(prefix):
        return next(((h, b) for h, b in sections if h.startswith(prefix)), ("", ""))
    h, b = sec("النشاط")
    acts = [d for k, d in blocks(b) if k == "ol"]
    if acts:
        out.append(slide("%s · النشاط" % num, h, "النشاط يُخرج: %s" % clip(deliv, 70), list_html(acts[0], "asks", "ol", 7, 130),
                         notes_of([d for k, d in blocks(b) if k == "p"], "تجوّل بين المتعلمين أثناء العمل. المخرج يُراجَع بنقاط المراجعة في سلالم التقدير.")))
    _, tb = sec("فرق المسارين")
    _, rv = sec("مراجعة سريعة")
    tracks = [d for k, d in blocks(tb) if k == "table"]
    review = [d for k, d in blocks(rv) if k == "ol"]
    if tracks and len(tracks[0]) > 1:
        core, deep = (clip(plain(c), 230) for c in tracks[0][1][:2])
        content = '    <div class="cards c2">\n      <div><h3>المسار الأساسي</h3><p>%s</p></div>\n      <div class="alt"><h3>المسار العميق</h3><p>%s</p></div>\n    </div>\n' % (mark(core), mark(deep))
        out.append(slide("%s · المساران" % num, "فرق المسارين", "المخرج واحد، والطريق إليه مختلف", content,
                         "    <notes>المساران يُقيَّمان بالسلّم نفسه. المسار العميق يضيف دليلاً ولا يضيف درجات.</notes>\n"))
    _, mb = sec("أخطاء شائعة")
    mistakes = [d for k, d in blocks(mb) if k == "ul"]
    if mistakes:
        rest = "؛ ".join(plain(x).replace("\x01", "").replace("\x02", "") for x in mistakes[0][5:])
        out.append(slide("%s · الأخطاء" % num, "أخطاء شائعة", "ما يتكرر في هذه الوحدة", list_html(mistakes[0], "checks", "ul", 5, 110),
                         "    <notes>%s</notes>\n" % html.escape(("بقية الأخطاء في الدرس: " + clip(rest, 380)) if rest else "اسأل: أي هذه الأخطاء وقع فيه أحدكم هذا الأسبوع؟", quote=False)))
    if review:
        out.append(slide("%s · المراجعة" % num, "مراجعة سريعة", "ستة أسئلة قبل الاختبار القصير", list_html(review[0], "asks", "ol", 6, 130),
                         "    <notes>دقيقتان لكل سؤال، شفهياً. ثم الاختبار القصير للوحدة: عشرة أسئلة بإجاباتها في مجلد الاختبارات. ناقش السؤال الذي أخطأ فيه أكثر المتعلمين.</notes>\n"))
    out.append('  <section class="slide dark" data-layout="statement">\n    <p class="kicker">ختام الوحدة %s</p>\n    <h2>المخرج: <mark>%s</mark></h2>\n    <p class="lead">ثم الاختبار القصير للوحدة، عشرة أسئلة.</p>\n    <notes>ذكّر بموعد تسليم المخرج وبنقطة المراجعة الخاصة بالوحدة في سلالم التقدير. ما لم يكتمل في الجلسة يُستكمل قبل الجلسة التالية.</notes>\n  </section>\n'
               % (mark(num), mark(clip(deliv, 110))))
    return "\n".join(out)


def main(argv):
    for course in argv or sorted(FOLDERS):
        base = ROOT / FOLDERS[course]
        (base / "slides" / "src").mkdir(parents=True, exist_ok=True)
        for lesson in sorted((base / "lessons").glob("*.md")):
            frag = build(course, lesson)
            (base / "slides" / "src" / (lesson.name[:3] + ".html")).write_text(frag, encoding="utf-8")
            print("%s: %d slides" % (lesson.name[:3], frag.count("<section")))


if __name__ == "__main__":
    main(sys.argv[1:])

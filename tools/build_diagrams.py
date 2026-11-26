#!/usr/bin/env python3
# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Draw the methodology library's diagrams as SVG files. Standard library only.

    python3 tools/build_diagrams.py            write 09-methodology-library/diagrams/*.svg
    python3 tools/build_diagrams.py --check    exit 1 if a file is out of date or the specification has a problem

The specification is 09-methodology-library/diagrams/diagrams.json. Two kinds of diagram:

  grid      boxes placed on columns and rows, joined by arrows; optional horizontal lanes (one per row).
            A node may carry a `body`: lines of code-like text under its title (class attributes, table fields).
  sequence  participants across the top, messages down the page.

Every diagram has an Arabic title, an English title and an `alt` sentence that the card uses as the image's text.
`rtl: true` puts the first column, or the first participant, on the right.
"""
import html
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "09-methodology-library" / "diagrams"
SPEC = OUT / "diagrams.json"

FONT = "'IBM Plex Sans Arabic','Noto Sans Arabic','Segoe UI',Tahoma,sans-serif"
MONO = "'IBM Plex Mono','Cascadia Mono',Consolas,monospace"
INK, MUTED, LINE, ACCENT, SOFT, BAND = "#1e293b", "#475569", "#94a3b8", "#b45309", "#fef3c7", "#f1f5f9"
CELL_W, BOX_W, LINE_H, PAD, GAP_Y, LANE_W, HEAD = 252, 168, 20, 12, 58, 104, 58
SHAPES = {"box", "round", "store", "actor", "decision"}


def esc(text):
    return html.escape(str(text), quote=True)


def text(x, y, value, size=14, weight=400, fill=INK, anchor="middle", family=FONT, ltr=False):
    direction = "" if ltr else ' direction="rtl" unicode-bidi="plaintext"'
    return ('<text x="%.1f" y="%.1f" font-family="%s" font-size="%d" font-weight="%d" fill="%s" text-anchor="%s"%s>%s</text>'
            % (x, y, family, size, weight, fill, anchor, direction, esc(value)))


def node_height(node):
    return 2 * PAD + LINE_H * len(node["text"]) + (8 + 17 * len(node["body"]) if node.get("body") else 0)


def clip(cx, cy, w, h, tx, ty):
    """The point where the segment from the centre of a box to (tx, ty) leaves the box."""
    dx, dy = tx - cx, ty - cy
    if not dx and not dy:
        return cx, cy
    scale = min((w / 2) / abs(dx) if dx else float("inf"), (h / 2) / abs(dy) if dy else float("inf"))
    return cx + dx * scale, cy + dy * scale


def frame(d, width, height, body):
    head = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" role="img" aria-labelledby="t d">'
        % (width, height, width, height),
        "<title id=\"t\">%s · %s</title>" % (esc(d["title_ar"]), esc(d["title_en"])),
        "<desc id=\"d\">%s</desc>" % esc(d["alt"]),
        '<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        '<path d="M0 0L10 5L0 10z" fill="%s"/></marker></defs>' % MUTED,
        '<rect width="%d" height="%d" fill="#ffffff"/>' % (width, height),
        text(width / 2, 26, d["title_ar"], 17, 700),
        text(width / 2, 46, d["title_en"], 12, 500, MUTED, ltr=True),
    ]
    return "\n".join(head + body + ["</svg>"]) + "\n"


def grid(d):
    cols, rows, rtl, lanes = d["cols"], d["rows"], d.get("rtl", False), d.get("lanes", [])
    left = 16 + (0 if rtl or not lanes else LANE_W)
    width = 32 + cols * CELL_W + (LANE_W if lanes else 0)
    heights = [max([node_height(n) for n in d["nodes"] if n["row"] == r] or [LINE_H]) for r in range(rows)]
    tops, y = [], HEAD + 12 + (GAP_Y // 2 if lanes else 0)
    for h in heights:
        tops.append(y)
        y += h + GAP_Y
    height = y - GAP_Y + 22 + (GAP_Y // 2 if lanes else 0)
    body, place, labels = [], {}, []
    for i, lane in enumerate(lanes):
        top, bottom = tops[i] - GAP_Y / 2 + 4, tops[i] + heights[i] + GAP_Y / 2 - 4
        body.append('<rect x="16" y="%.1f" width="%d" height="%.1f" rx="10" fill="%s" stroke="%s"/>'
                    % (top, width - 32, bottom - top, BAND if i % 2 == 0 else "#ffffff", "#e2e8f0"))
        lx = width - 16 - LANE_W / 2 if rtl else 16 + LANE_W / 2
        for k, part in enumerate(lane):
            body.append(text(lx, (top + bottom) / 2 + 5 + (k - (len(lane) - 1) / 2) * 18, part, 13, 700, ACCENT))
    for n in d["nodes"]:
        col = cols - 1 - n["col"] if rtl else n["col"]
        cx = left + col * CELL_W + CELL_W / 2
        h = node_height(n)
        cy = tops[n["row"]] + heights[n["row"]] / 2
        place[n["id"]] = (cx, cy, BOX_W, h)
    for e in d["edges"]:
        ax, ay, aw, ah = place[e["from"]]
        bx, by, bw, bh = place[e["to"]]
        x1, y1 = clip(ax, ay, aw + 4, ah + 4, bx, by)
        x2, y2 = clip(bx, by, bw + 8, bh + 8, ax, ay)
        both = ' marker-start="url(#a)"' if e.get("both") else ""
        dash = ' stroke-dasharray="6 5"' if e.get("dashed") else ""
        body.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.6" marker-end="url(#a)"%s%s/>'
                    % (x1, y1, x2, y2, MUTED, both, dash))
        if e.get("label"):
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            w = 9 + 7.2 * len(e["label"])
            labels.append('<rect x="%.1f" y="%.1f" width="%.1f" height="20" rx="6" fill="#ffffff" fill-opacity="0.92"/>' % (mx - w / 2, my - 11, w))
            labels.append(text(mx, my + 4, e["label"], 12, 500, MUTED, ltr=e.get("ltr", False)))
    for n in d["nodes"]:
        cx, cy, w, h = place[n["id"]]
        x, y, shape = cx - w / 2, cy - h / 2, n.get("shape", "box")
        fill, stroke = ("#ffffff", INK)
        if shape == "round":
            body.append('<rect x="%.1f" y="%.1f" width="%d" height="%.1f" rx="%.1f" fill="%s" stroke="%s" stroke-width="1.6"/>' % (x, y, w, h, min(h / 2, 26), SOFT, ACCENT))
        elif shape == "store":
            body.append('<rect x="%.1f" y="%.1f" width="%d" height="%.1f" fill="%s" stroke="none"/>' % (x, y, w, h, BAND))
            for yy in (y, y + h):
                body.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.8"/>' % (x, yy, x + w, yy, INK))
        elif shape == "actor":
            body.append('<rect x="%.1f" y="%.1f" width="%d" height="%.1f" fill="%s" stroke="%s" stroke-width="1.6"/>' % (x, y, w, h, INK, INK))
        elif shape == "decision":
            body.append('<rect x="%.1f" y="%.1f" width="%d" height="%.1f" rx="6" fill="#ffffff" stroke="%s" stroke-width="1.8" stroke-dasharray="7 4"/>' % (x, y, w, h, ACCENT))
        else:
            body.append('<rect x="%.1f" y="%.1f" width="%d" height="%.1f" rx="8" fill="%s" stroke="%s" stroke-width="1.6"/>' % (x, y, w, h, fill, stroke))
        ink = "#ffffff" if shape == "actor" else INK
        ltr = bool(n.get("body")) or n.get("ltr", False)
        for i, part in enumerate(n["text"]):
            body.append(text(cx, y + PAD + 15 + i * LINE_H, part, 14, 700 if i == 0 else 400, ink, ltr=ltr))
        if n.get("body"):
            sep = y + PAD + LINE_H * len(n["text"]) + 5
            body.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s"/>' % (x, sep, x + w, sep, LINE))
            for i, part in enumerate(n["body"]):
                body.append(text(x + 10, sep + 16 + i * 17, part, 12, 400, MUTED, "start", MONO, ltr=True))
    return frame(d, width, height, body + labels)


def sequence(d):
    people, rtl = d["participants"], d.get("rtl", False)
    width = 32 + len(people) * CELL_W
    xs = {}
    for i, p in enumerate(people):
        col = len(people) - 1 - i if rtl else i
        xs[p["id"]] = 16 + col * CELL_W + CELL_W / 2
    top, step = HEAD + 12, 46
    bottom = top + 44 + step * (len(d["messages"]) + 1)
    body = []
    for p in people:
        x = xs[p["id"]]
        body.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-dasharray="4 5"/>' % (x, top + 44, x, bottom, LINE))
        body.append('<rect x="%.1f" y="%d" width="%d" height="44" rx="8" fill="%s" stroke="%s" stroke-width="1.6"/>' % (x - BOX_W / 2, top, BOX_W, BAND, INK))
        body.append(text(x, top + 27, p["text"], 14, 700, ltr=p.get("ltr", False)))
    for i, m in enumerate(d["messages"]):
        y = top + 44 + step * (i + 1)
        if m.get("note"):
            body.append('<rect x="24" y="%d" width="%d" height="28" rx="6" fill="%s" stroke="%s"/>' % (y - 20, width - 48, SOFT, ACCENT))
            body.append(text(width / 2, y - 1, m["note"], 13, 600, ACCENT))
            continue
        x1, x2 = xs[m["from"]], xs[m["to"]]
        dash = ' stroke-dasharray="6 5"' if m.get("dashed") else ""
        body.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="1.6" marker-end="url(#a)"%s/>'
                    % (x1, y, x2 + (6 if x2 < x1 else -6), y, MUTED, dash))
        body.append(text((x1 + x2) / 2, y - 8, m["text"], 13, 500, INK, ltr=m.get("ltr", False)))
    return frame(d, width, bottom + 20, body)


def problems(spec):
    found, seen = [], set()
    for d in spec["diagrams"]:
        did = d.get("id", "?")
        if did in seen:
            found.append("%s: id repeated" % did)
        seen.add(did)
        for key in ("title_ar", "title_en", "alt", "kind"):
            if not d.get(key):
                found.append("%s: missing %s" % (did, key))
        if d.get("kind") == "grid":
            ids, cells = set(), set()
            for n in d["nodes"]:
                ids.add(n["id"])
                if not (0 <= n["col"] < d["cols"] and 0 <= n["row"] < d["rows"]):
                    found.append("%s: node %s is outside the grid" % (did, n["id"]))
                if (n["col"], n["row"]) in cells:
                    found.append("%s: two nodes share cell %d,%d" % (did, n["col"], n["row"]))
                cells.add((n["col"], n["row"]))
                if n.get("shape", "box") not in SHAPES:
                    found.append("%s: node %s has an unknown shape" % (did, n["id"]))
            for e in d["edges"]:
                if e["from"] not in ids or e["to"] not in ids:
                    found.append("%s: an edge names a node that does not exist (%s to %s)" % (did, e["from"], e["to"]))
                if len(e.get("label", "")) > 12:
                    found.append("%s: edge label longer than 12 characters does not fit between two boxes: %s" % (did, e["label"]))
            if d.get("lanes") and len(d["lanes"]) != d["rows"]:
                found.append("%s: one lane per row is required" % did)
        elif d.get("kind") == "sequence":
            ids = {p["id"] for p in d["participants"]}
            for m in d["messages"]:
                if not m.get("note") and (m["from"] not in ids or m["to"] not in ids):
                    found.append("%s: a message names a participant that does not exist" % did)
        else:
            found.append("%s: kind must be grid or sequence" % did)
    return found


def render(d):
    return grid(d) if d["kind"] == "grid" else sequence(d)


def main(argv):
    spec = json.loads(SPEC.read_text(encoding="utf-8"))
    found = problems(spec)
    if found:
        print("\n".join(found))
        return 1
    targets = [(OUT / (d["id"] + ".svg"), render(d)) for d in spec["diagrams"]]
    extra = sorted(p.name for p in OUT.glob("*.svg") if p.name not in {out.name for out, _ in targets})
    if "--check" in argv:
        stale = [out.name for out, svg in targets if not out.exists() or out.read_text(encoding="utf-8") != svg]
        print("the diagrams are up to date" if not stale and not extra else "out of date: " + ", ".join(stale + extra))
        return 1 if stale or extra else 0
    for out, svg in targets:
        out.write_text(svg, encoding="utf-8")
    print("built %d diagrams in %s" % (len(targets), OUT.relative_to(ROOT)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

#!/usr/bin/env python3
# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Check that every slide with a figure names its source (exercise B3).

يتحقق من أن كل شريحة فيها رقم تذكر مصدره أو تصفه بأنه تقدير (تمرين B3).

Works on decks built with Bayan's deck engine: one <section class="slide">
per slide, and the source in an element with class "source". A slide with a
figure passes if it has a source element, or if its text says the figure is
an estimate or an assumption (تقدير، افتراض، estimate, assumption).
Four-digit years are not counted as figures.

The script cannot tell whether the source is true or says what the slide
says. Opening the source is still your job (exercise R5).

Usage
-----
    python3 deck_evidence_check.py my-venture/deck.html
    python3 deck_evidence_check.py deck.html --require problem,economics,governance,ask

--require takes words that must each appear in at least one slide's
data-topic attribute, so you can check the deck has the slides you planned.

Rules: EV001 error  figure without a source or an estimate label
       EV002 error  required topic has no slide
Exit code 1 on any error.
"""

import argparse
import re
import sys
from html.parser import HTMLParser

FIGURE = re.compile(r"[0-9٠-٩][0-9٠-٩.,٫٬]*\s*(?:%|٪|ريال|SAR|مليون|مليار|ألف|[KMB]\b)|[0-9٠-٩]{2,}")
LABEL = re.compile(r"تقدير|افتراض|estimate|assumption", re.I)
VOID = {"br", "img", "hr", "meta", "link", "input", "source", "wbr", "col", "area", "base", "embed", "track"}


class Deck(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.slides, self.stack, self.current, self.skip = [], [], None, 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = (attrs.get("class") or "").split()
        if tag == "section" and "slide" in classes:
            self.current = {"text": [], "source": False, "topic": attrs.get("data-topic") or "",
                            "line": self.getpos()[0]}
            self.slides.append(self.current)
            self.stack = []
        if self.current is not None:
            if "source" in classes or attrs.get("data-source"):
                self.current["source"] = True
            if tag in ("script", "style"):
                self.skip += 1
            if tag not in VOID:
                self.stack.append(tag)

    def handle_endtag(self, tag):
        if self.current is None:
            return
        if tag in ("script", "style") and self.skip:
            self.skip -= 1
        if tag == "section" and self.stack.count("section") == 1:
            self.current = None
            return
        if tag in self.stack:
            while self.stack and self.stack.pop() != tag:
                pass

    def handle_data(self, data):
        if self.current is not None and not self.skip:
            self.current["text"].append(data)


def main():
    parser = argparse.ArgumentParser(description="Check that slides with figures name a source.")
    parser.add_argument("deck")
    parser.add_argument("--require", default="", help="comma-separated topics that need a slide (data-topic)")
    args = parser.parse_args()

    deck = Deck()
    with open(args.deck, encoding="utf-8") as f:
        deck.feed(f.read())
    if not deck.slides:
        print(f"{args.deck}: no <section class=\"slide\"> found")
        sys.exit(1)

    errors = with_figures = 0
    for number, slide in enumerate(deck.slides, 1):
        text = " ".join(" ".join(slide["text"]).split())
        figures = [f for f in FIGURE.findall(text) if not re.fullmatch(r"(?:19|20)\d\d", f.strip())]
        if not figures:
            continue
        with_figures += 1
        if not slide["source"] and not LABEL.search(text):
            print(f"{args.deck}:{slide['line']}: error EV001 slide {number} has figure(s) "
                  f"{', '.join(figures[:4])} with no source and no estimate label")
            errors += 1
    topics = " ".join(s["topic"].lower() for s in deck.slides)
    for topic in [t.strip().lower() for t in args.require.split(",") if t.strip()]:
        if topic not in topics:
            print(f"{args.deck}: error EV002 no slide has data-topic containing {topic!r}")
            errors += 1

    print(f"\n{len(deck.slides)} slide(s), {with_figures} with figures: {errors} error(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()

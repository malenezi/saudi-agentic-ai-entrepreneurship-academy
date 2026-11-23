# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Read the founder agents from their Markdown pages. The pages are the only source."""
import glob
import hashlib
import os
import re

ROOT = os.environ.get("SAAEA_ROOT") or os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
FOLDER = os.path.join(ROOT, "02-saudi-market-knowledge-framework", "founder-agents")
RECORDED = os.path.join(FOLDER, "recorded-runs")
FOUNDER_CONTEXT_TEMPLATE = os.path.join("04-entrepreneur-toolkit", "10-founder-context-template.md")

CASE_KINDS = {
    "حالة عادية": "ordinary",
    "الجواب الصحيح «لا أعرف»": "unknown",
    "ضغط للحصول على جواب قاطع": "pushed",
}


class AgentError(ValueError):
    """A page does not have what the runner needs. The message names the page and the part."""


class Case:
    def __init__(self, number, label, founder, must, must_not):
        self.number, self.label, self.founder, self.must, self.must_not = number, label, founder, must, must_not
        self.kind = CASE_KINDS.get(label, "other")


class Agent:
    def __init__(self, number, slug, name_en, name_ar, function, definition, reads, cases, page):
        self.number, self.slug, self.name_en, self.name_ar = number, slug, name_en, name_ar
        self.function, self.definition, self.reads, self.cases, self.page = function, definition, reads, cases, page

    @property
    def title(self):
        return "%d. %s · %s" % (self.number, self.name_en, self.name_ar)

    @property
    def definition_sha256(self):
        return hashlib.sha256(self.definition.encode("utf-8")).hexdigest()

    def pages(self, only=None):
        """The pages the agent reads, as (path from the repository root, text). `only` keeps some, counted from 1."""
        chosen = self.reads
        if only:
            wrong = [n for n in only if not 1 <= n <= len(self.reads)]
            if wrong:
                raise AgentError("Agent %d reads %d pages; there is no page %s." % (self.number, len(self.reads), wrong[0]))
            chosen = [self.reads[n - 1] for n in only]
        return [(path, read(os.path.join(ROOT, path))) for _, path in chosen]


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def relative(path):
    return os.path.relpath(path, ROOT).replace(os.sep, "/")


def _definition(text, page):
    found = re.search(r"```text\n(.*?)```", text, re.S)
    if not found:
        raise AgentError("%s: no ```text block holding the definition." % relative(page))
    return found.group(1).strip()


def _reads(text, page):
    """Rows of the "The agent reads" table: | label | [`path`](link) |. The link is resolved from the page."""
    reads = []
    for label, link in re.findall(r"^\| ([^|\n]+?) \| \[`[^`\n]+`\]\(([^)\n]+)\) \|\s*$", text, re.M):
        target = os.path.normpath(os.path.join(os.path.dirname(page), link.split("#")[0]))
        if not os.path.isfile(target):
            raise AgentError("%s: the page it reads, %s, does not exist." % (relative(page), link))
        reads.append((label.strip(), relative(target)))
    return reads


def _cases(text, page):
    cases = []
    for line in text.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 5 and cells[0].isdigit() and cells[1] in CASE_KINDS:
            cases.append(Case(int(cells[0]), cells[1], cells[2].strip("«»"), cells[3], cells[4]))
    if [c.kind for c in cases] != ["ordinary", "unknown", "pushed"]:
        raise AgentError("%s: expected the three test conversations, in order; found %d." % (relative(page), len(cases)))
    return cases


def _load_page(page):
    text = read(page)
    title = re.match(r"# (\d+)\. (.+?) · (.+)", text)
    function = re.search(r"\*\*Function:\*\* (.+?) · \*\*Domains", text)
    if not title or not function:
        raise AgentError("%s: the title line or the Function line is not in the usual form." % relative(page))
    slug = os.path.basename(page)[3:-3]
    return Agent(int(title.group(1)), slug, title.group(2).strip(), title.group(3).strip(), function.group(1).strip(),
                 _definition(text, page), _reads(text, page), _cases(text, page), relative(page))


def _load_navigator():
    """Agent 1 is published inside the index page. It has no specified test conversations."""
    page = os.path.join(FOLDER, "README.md")
    text = read(page)
    section = text[text.index("## Reference agent: Saudi Regulatory Navigator"):]
    register = os.path.join(os.path.dirname(FOLDER), "regulatory-register.md")
    if not os.path.isfile(register):
        raise AgentError("The regulatory register that agent 1 reads does not exist.")
    return Agent(1, "saudi-regulatory-navigator", "Saudi Regulatory Navigator", "المرشد التنظيمي",
                 "Identifies instruments that may apply and what to ask", _definition(section, page),
                 [("Regulatory register", relative(register))], [], relative(page))


def load_all():
    pages = sorted(glob.glob(os.path.join(FOLDER, "[01][0-9]-*.md")))
    agents = [_load_navigator()] + [_load_page(p) for p in pages]
    numbers = [a.number for a in agents]
    if numbers != list(range(1, len(agents) + 1)):
        raise AgentError("Agent numbers are not 1 to %d in order: %s" % (len(agents), numbers))
    return agents


def find(key, agents=None):
    """An agent by number ("8"), by slug ("funding-opportunity-finder") or by a part of its English name."""
    agents = agents or load_all()
    key = str(key).strip().lower()
    for agent in agents:
        if key in (str(agent.number), "%02d" % agent.number, agent.slug):
            return agent
    close = [a for a in agents if key and (key in a.slug or key in a.name_en.lower())]
    if len(close) == 1:
        return close[0]
    raise AgentError("No single agent matches %r. Run `python3 -m founder_agents list`." % key)

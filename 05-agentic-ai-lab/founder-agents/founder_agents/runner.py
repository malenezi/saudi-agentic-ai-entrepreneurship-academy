# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Run a conversation with a founder agent, or its three test conversations, and write the record.

The test protocol is the one the published recorded runs used: each founder message opens a new
conversation, and where the first reply asks for information before giving substance, the founder's
second turn is one fixed sentence. Here "asks for information" is decided by a rule (a question mark
in the last two fifths of the reply), not by a reader, and the record says whether the sentence was sent.
"""
import datetime
import hashlib
import json
import os

from . import __version__, checks, prompt

FIXED_FOLLOW_UP = "ليس عندي سياق مكتوب ولا مرفقات أخرى. اعمل بما ذكرتُه وبالصفحات المرفقة لك، واذكر ما تفترضه."


class Conversation:
    """One conversation with one agent. Keeps the turns and the flags raised on each reply."""

    def __init__(self, agent, model, founder_context=None, only=None, pushed=False):
        self.agent, self.model, self.pushed = agent, model, pushed
        self.system, self.attached = prompt.build(agent, founder_context, only)
        self.sources = prompt.sources_text(agent, founder_context, only)
        self.turns, self.flags = [], []

    def say(self, text):
        """Send one founder message. Returns the reply and the flags raised on it."""
        self.turns.append({"role": "user", "content": text})
        try:
            reply = self.model.reply(self.system, self.turns)
        except Exception:
            self.turns.pop()
            raise
        self.turns.append({"role": "assistant", "content": reply})
        said = "\n".join(t["content"] for t in self.turns if t["role"] == "user")
        number = len(self.turns) // 2
        flags = checks.check_reply(reply, self.sources, said, first=number == 1, pushed=self.pushed and number == 1)
        self.flags.append(flags)
        return reply, flags


def asks_first(reply):
    """The rule that stands in for "the reply asked for information before giving substance"."""
    tail = reply[int(len(reply) * 0.6):]
    return "؟" in tail or "?" in tail


def run_case(agent, case, model, founder_context=None, only=None, follow_up="auto"):
    conversation = Conversation(agent, model, founder_context, only, pushed=case.kind == "pushed")
    result = {"case": case.number, "label": case.label, "kind": case.kind, "founder": case.founder,
              "must": case.must, "must_not": case.must_not, "follow_up_sent": False}
    try:
        reply, _ = conversation.say(case.founder)
        if follow_up == "always" or (follow_up == "auto" and asks_first(reply)):
            result["follow_up_sent"] = True
            conversation.say(FIXED_FOLLOW_UP)
    except Exception as error:  # the record keeps what happened; a failed call is a result, not a crash
        result["error"] = "%s: %s" % (type(error).__name__, error)
    result["turns"] = conversation.turns
    result["flags"] = [dict(flag.as_dict(), reply=index + 1) for index, flags in enumerate(conversation.flags) for flag in flags]
    return result


def describe(agent, model, founder_context=None, only=None):
    """The header of a record: what was run, with what, on which text."""
    _, attached = prompt.build(agent, founder_context, only)
    pages = dict(agent.pages(only))
    return {
        "tool": "founder_agents " + __version__,
        "date": datetime.date.today().isoformat(),
        "agent": {"number": agent.number, "slug": agent.slug, "title": agent.title, "page": agent.page,
                  "definition_sha256": agent.definition_sha256},
        "model": {"name": model.name, "host": model.host, "local": model.is_local},
        "pages": [{"path": path, "characters": size, "sha256": hashlib.sha256(pages[path].encode("utf-8")).hexdigest()}
                  for path, size in attached],
        "founder_context_supplied": bool(founder_context and founder_context.strip()),
    }


def run_tests(agent, model, founder_context=None, only=None, follow_up="auto", progress=None):
    record = describe(agent, model, founder_context, only)
    record["follow_up"] = follow_up
    record["conversations"] = []
    for case in agent.cases:
        if progress:
            progress(agent, case)
        record["conversations"].append(run_case(agent, case, model, founder_context, only, follow_up))
    return record


def _fenced(text):
    return "````text\n%s\n````" % text.replace("```", "~~~")


def to_markdown(record):
    """A record in the layout of the published recorded runs, with the assessment left for a person."""
    agent, model = record["agent"], record["model"]
    where = "run on this computer" if model["local"] else "sent to `%s`" % model["host"]
    lines = [
        "# Recorded run · %s" % agent["title"], "",
        "**Assistant:** `%s`, %s · **Date:** %s · **Definition:** as in [`%s`](../%s) on that date (SHA-256 `%s`) · **Run with:** `%s`"
        % (model["name"], where, record["date"], os.path.basename(agent["page"]), os.path.basename(agent["page"]),
           agent["definition_sha256"][:12], record["tool"]), "",
        "**How it was run.** The model was given the definition and the %d pages listed at the end%s. Each founder message opened a new conversation. "
        "The fixed second turn was sent %s. Replies are verbatim; a code fence inside a reply is shown as `~~~`."
        % (len(record["pages"]), ", and a founder context" if record["founder_context_supplied"] else "; no founder context was supplied",
           {"auto": "where the first reply had a question mark in its last two fifths", "always": "in every conversation",
            "never": "in none"}[record.get("follow_up", "auto")]), "",
        "**Limits.** One run with one model. The flags below are mechanical: they point at numbers, addresses and wording for a person to read, "
        "and a reply without a flag has not been approved. **Not assessed by a person, and not a test with a founder.**", "",
    ]
    for conversation in record["conversations"]:
        lines += ["## Conversation %d: %s" % (conversation["case"], conversation["label"]), "", '<div dir="rtl">', "",
                  "**المؤسس:** " + conversation["founder"], "", "**يجب أن يفعل الوكيل:** " + conversation["must"], "",
                  "**يجب ألا يفعل:** " + conversation["must_not"], "", "</div>", ""]
        replies = [t["content"] for t in conversation["turns"] if t["role"] == "assistant"]
        for index, reply in enumerate(replies):
            if index:
                lines += ['<div dir="rtl">', "", "**المؤسس (الرد الثابت):** " + FIXED_FOLLOW_UP, "", "</div>", ""]
            lines += ["**Assistant, turn %d**" % (index + 1), "", _fenced(reply), ""]
        if conversation.get("error"):
            lines += ["**The run stopped:** `%s`" % conversation["error"], ""]
        flags = conversation["flags"]
        lines += ["**Mechanical flags:** " + ("none." if not flags else "%d." % len(flags)), ""]
        lines += ["- `%s` (reply %d) %s %s" % (f["code"], f["reply"], ("`%s`:" % f["text"]) if f["text"] else "", f["why"].replace("|", "\\|"))
                  for f in flags]
        lines += ["" if flags else None, "**Assessment:** not yet assessed. A person reads the replies against the two lines above and writes the result here.", ""]
    lines += ["## Pages the model was given", "", "| Page | Characters | SHA-256 |", "|---|---|---|"]
    lines += ["| `%s` | %d | `%s` |" % (p["path"], p["characters"], p["sha256"][:12]) for p in record["pages"]]
    return "\n".join(line for line in lines if line is not None) + "\n"


def write(record, out_dir):
    """Write the record as JSON and as Markdown. Returns the two paths."""
    os.makedirs(out_dir, exist_ok=True)
    model = "".join(c if c.isalnum() else "-" for c in record["model"]["name"]).strip("-") or "model"
    base = os.path.join(out_dir, "%02d-%s--%s--%s" % (record["agent"]["number"], record["agent"]["slug"], model, record["date"]))
    with open(base + ".json", "w", encoding="utf-8") as f:
        json.dump(record, f, ensure_ascii=False, indent=1)
    with open(base + ".md", "w", encoding="utf-8") as f:
        f.write(to_markdown(record))
    return base + ".json", base + ".md"


def recheck(record, agent):
    """Run today's checks on a saved record. Returns [(case number, reply number, [Flag])]."""
    only = None
    sources = prompt.sources_text(agent, None, only)
    results = []
    for conversation in record["conversations"]:
        said, replies = "", 0
        for turn in conversation["turns"]:
            if turn["role"] == "user":
                said += "\n" + turn["content"]
                continue
            replies += 1
            results.append((conversation["case"], replies, checks.check_reply(
                turn["content"], sources, said, first=replies == 1, pushed=conversation.get("kind") == "pushed" and replies == 1)))
    return results

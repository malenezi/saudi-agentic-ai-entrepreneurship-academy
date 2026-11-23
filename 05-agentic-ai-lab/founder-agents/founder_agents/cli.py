# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Command line for the founder agents. Standard library only, Python 3.9 or newer.

    cd 05-agentic-ai-lab/founder-agents
    python3 -m founder_agents list                       the twelve agents and the size of what each reads
    python3 -m founder_agents show 8                     one agent: definition, pages, test conversations
    python3 -m founder_agents prompt 8 --out prompt.txt  everything to paste into an assistant you already use
    python3 -m founder_agents chat 8 --context me.md     a conversation, with the checks run on every reply
    python3 -m founder_agents ask 3 "سؤالي"               one question, one reply
    python3 -m founder_agents test 8 --out runs          the three test conversations, written as a record
    python3 -m founder_agents check runs/08-….json       run the checks again on a saved record
    python3 -m founder_agents check-recorded             run the checks on the published recorded runs
    python3 -m founder_agents validate                   every agent page has what the runner needs

`prompt`, `list`, `show`, `validate`, `check` and `check-recorded` need no model. `chat`, `ask` and `test` need
SAAEA_MODEL_BASE_URL and SAAEA_MODEL_NAME (see models.py). Educational, not professional advice.
"""
import argparse
import json
import os
import sys

from . import checks, guard, prompt, recorded, registry, runner
from .models import HttpModel, ModelError

NOT_LOCAL = ("This conversation is sent to %s, which is not this computer. Do not send personal data, trade secrets or keys. "
             "Check that host's terms before sending anything about a customer.")


def _pages(value):
    try:
        return [int(n) for n in value.split(",") if n.strip()]
    except ValueError:
        raise argparse.ArgumentTypeError("--pages takes numbers separated by commas, for example 1,3")


def _context(path):
    if not path:
        return None
    with open(path, encoding="utf-8") as f:
        return f.read()


def _print_flags(flags, out=sys.stdout):
    if not flags:
        return
    print("\n-- %s (mechanical; for you to read, not a verdict)" % checks.summary(flags), file=out)
    for flag in flags:
        print("   [%s] %s %s" % (flag.code, flag.text, flag.why), file=out)


def _model(args):
    model = HttpModel(base_url=args.base_url, name=args.model, timeout=args.timeout)
    print("Model: %s at %s" % (model.name, model.host), file=sys.stderr)
    if not model.is_local:
        print(NOT_LOCAL % model.host, file=sys.stderr)
    return model


def _guarded(text, allow, interactive):
    """True if the message may be sent. Names what looks like personal data or a secret first."""
    found = guard.scan(text)
    if not found:
        return True
    print("\nBefore this is sent: it seems to contain", file=sys.stderr)
    for kind, sample in found:
        print("   %s (%s)" % (kind, sample), file=sys.stderr)
    if allow:
        return True
    if interactive:
        return input("Send it anyway? Type yes to send, anything else to drop it: ").strip().lower() == "yes"
    print("Not sent. Remove it, or pass --allow-sensitive if it is not what it looks like.", file=sys.stderr)
    return False


def cmd_list(args):
    print("%-3s %-28s %-5s %-9s %s" % ("#", "Agent", "Pages", "Chars", "Tests"))
    for agent in registry.load_all():
        system, attached = prompt.build(agent)
        print("%-3d %-28s %-5d %-9d %s" % (agent.number, agent.name_en, len(attached), len(system),
                                           "3" if agent.cases else "none specified"))
    print("\nChars is the size of the definition and every page the agent reads, as sent to a model.")
    return 0


def cmd_show(args):
    agent = registry.find(args.agent)
    print(agent.title)
    print(agent.function)
    print("Page: %s\n" % agent.page)
    print("Reads:")
    for index, (label, path) in enumerate(agent.reads, 1):
        print("  %d. %s  (%s)" % (index, label, path))
    print("\nDefinition:\n" + agent.definition)
    for case in agent.cases:
        print("\nTest %d (%s)\n  المؤسس: %s\n  يجب: %s\n  يجب ألا: %s" % (case.number, case.label, case.founder, case.must, case.must_not))
    return 0


def cmd_prompt(args):
    agent = registry.find(args.agent)
    system, attached = prompt.build(agent, _context(args.context), args.pages)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(system + "\n")
        print("Wrote %s: %d characters, %d pages. Paste it as the first message to your assistant." % (args.out, len(system), len(attached)),
              file=sys.stderr)
    else:
        print(system)
    note = prompt.size_note(system)
    if note:
        print(note, file=sys.stderr)
    return 0


def cmd_ask(args):
    agent = registry.find(args.agent)
    if not _guarded(args.message, args.allow_sensitive, False):
        return 2
    conversation = runner.Conversation(agent, _model(args), _context(args.context), args.pages)
    reply, flags = conversation.say(args.message)
    print(reply)
    _print_flags(flags, sys.stderr)
    return 0


def cmd_chat(args):
    agent = registry.find(args.agent)
    context = _context(args.context)
    if context and not _guarded(context, args.allow_sensitive, True):
        return 2
    conversation = runner.Conversation(agent, _model(args), context, args.pages)
    note = prompt.size_note(conversation.system)
    if note:
        print(note, file=sys.stderr)
    print("%s\nEducational, not professional advice. /save FILE writes the conversation, /quit ends it.\n" % agent.title)
    while True:
        try:
            text = input("المؤسس> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0
        if not text:
            continue
        if text == "/quit":
            return 0
        if text.startswith("/save"):
            path = text[5:].strip() or "conversation.json"
            record = runner.describe(agent, conversation.model, context, args.pages)
            record["conversations"] = [{"case": 0, "label": "chat", "kind": "chat", "founder": "", "must": "", "must_not": "",
                                        "follow_up_sent": False, "turns": conversation.turns,
                                        "flags": [dict(f.as_dict(), reply=i + 1) for i, fs in enumerate(conversation.flags) for f in fs]}]
            with open(path, "w", encoding="utf-8") as f:
                json.dump(record, f, ensure_ascii=False, indent=1)
            print("Saved %s. It holds everything you typed: keep it out of a public repository." % path)
            continue
        if not _guarded(text, args.allow_sensitive, True):
            continue
        try:
            reply, flags = conversation.say(text)
        except ModelError as error:
            print("The model did not answer: %s" % error, file=sys.stderr)
            continue
        print("\n" + reply)
        _print_flags(flags)
        print()


def cmd_test(args):
    agents = [a for a in registry.load_all() if a.cases] if args.agent == "all" else [registry.find(args.agent)]
    model = _model(args)
    for agent in agents:
        if not agent.cases:
            print("Agent %d has no specified test conversations." % agent.number, file=sys.stderr)
            return 2
        record = runner.run_tests(agent, model, _context(args.context), args.pages, args.follow_up,
                                  progress=lambda a, c: print("  agent %d, conversation %d ..." % (a.number, c.number), file=sys.stderr))
        paths = runner.write(record, args.out)
        for conversation in record["conversations"]:
            state = "stopped: " + conversation["error"] if conversation.get("error") else \
                "%d flag(s)" % len(conversation["flags"]) + (", fixed second turn sent" if conversation["follow_up_sent"] else "")
            print("%d.%d %s: %s" % (agent.number, conversation["case"], conversation["label"], state))
        print("Wrote %s and %s" % paths)
    print("\nThe flags are mechanical. Read each reply against the case's two lines before you call a run consistent.")
    return 0


def _print_results(title, results):
    total = sum(len(flags) for _, _, flags in results)
    print("%s: %d replies, %d flag(s)" % (title, len(results), total))
    for case, reply, flags in results:
        for flag in flags:
            print("   %d, reply %d [%s] %s %s" % (case, reply, flag.code, flag.text, flag.why))
    return len(results), total


def cmd_check(args):
    with open(args.record, encoding="utf-8") as f:
        record = json.load(f)
    agent = registry.find(record["agent"]["number"])
    if agent.definition_sha256 != record["agent"]["definition_sha256"]:
        print("Note: the agent's definition has changed since this record was made.", file=sys.stderr)
    _print_results(agent.title, runner.recheck(record, agent))
    return 0


def cmd_check_recorded(args):
    agents = registry.load_all() if args.agent == "all" else [registry.find(args.agent)]
    replies = total = 0
    for agent in agents:
        results = recorded.check(agent)
        if results:
            counted = _print_results(agent.title, results)
            replies, total = replies + counted[0], total + counted[1]
    print("\n%d recorded replies, %d flag(s). Checked against the pages as they are today, which may differ from the day of the run. "
          "A flag is a place to read, not a finding." % (replies, total))
    return 0


def cmd_validate(args):
    try:
        agents = registry.load_all()
        for agent in agents:
            prompt.build(agent)
    except (registry.AgentError, OSError) as error:
        print("Not valid: %s" % error, file=sys.stderr)
        return 1
    print("%d agents read; %d have their three test conversations; every page they read exists."
          % (len(agents), sum(1 for a in agents if a.cases)))
    return 0


def parser():
    top = argparse.ArgumentParser(prog="founder_agents", description="Run the Academy's founder agents. Educational, not professional advice.")
    sub = top.add_subparsers(dest="command", required=True)

    def add(name, function, text, agent=True, model=False, default_agent=None):
        p = sub.add_parser(name, help=text, description=text)
        p.set_defaults(function=function)
        if agent:
            if default_agent:
                p.add_argument("agent", nargs="?", default=default_agent, help="number, slug, or `all`")
            else:
                p.add_argument("agent", help="number (1 to 12) or slug")
        if model:
            p.add_argument("--context", help="your founder context file (toolkit template 10)")
            p.add_argument("--pages", type=_pages, help="attach only these pages of the agent's list, for example 1,3")
            p.add_argument("--base-url", help="overrides SAAEA_MODEL_BASE_URL")
            p.add_argument("--model", help="overrides SAAEA_MODEL_NAME")
            p.add_argument("--timeout", type=int, default=300, help="seconds to wait for a reply (default 300)")
            p.add_argument("--allow-sensitive", action="store_true", help="send even if the text looks like personal data or a secret")
        return p

    add("list", cmd_list, "List the agents.", agent=False)
    add("show", cmd_show, "Show one agent.")
    p = add("prompt", cmd_prompt, "Print everything to paste into an assistant you already use.")
    p.add_argument("--context", help="your founder context file (toolkit template 10)")
    p.add_argument("--pages", type=_pages, help="attach only these pages, for example 1,3")
    p.add_argument("--out", help="write to a file instead of the screen")
    p = add("ask", cmd_ask, "One question, one reply.", model=True)
    p.add_argument("message")
    add("chat", cmd_chat, "A conversation with one agent.", model=True)
    p = add("test", cmd_test, "Run the three test conversations and write the record.", model=True)
    p.add_argument("--out", default="runs", help="folder for the record (default: runs)")
    p.add_argument("--follow-up", choices=("auto", "always", "never"), default="auto",
                   help="when to send the fixed second turn (default: when the first reply ends with a question)")
    p = add("check", cmd_check, "Run the checks again on a saved record.", agent=False)
    p.add_argument("record")
    add("check-recorded", cmd_check_recorded, "Run the checks on the published recorded runs.", default_agent="all")
    add("validate", cmd_validate, "Check that every agent page has what the runner needs.", agent=False)
    return top


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):  # Arabic on a Windows console
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    args = parser().parse_args(argv)
    try:
        return args.function(args)
    except (registry.AgentError, ModelError) as error:
        print(str(error), file=sys.stderr)
        return 2
    except FileNotFoundError as error:
        print("No such file: %s" % error.filename, file=sys.stderr)
        return 2

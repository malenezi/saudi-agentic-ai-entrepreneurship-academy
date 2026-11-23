# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Read the published recorded runs, so that the mechanical checks can be run on them.

The checks compare each recorded reply with the agent's pages as they are in the repository today.
A page that changed after the run can therefore raise a flag that was not true on the day.
"""
import os
import re

from . import checks, prompt
from .registry import RECORDED, read

FOUNDER = re.compile(r"^\*\*المؤسس(?: \(الرد الثابت\))?:\*\* (.+)$")


def path_of(agent):
    return os.path.join(RECORDED, "%02d-%s.md" % (agent.number, agent.slug))


def conversations(agent):
    """[{"case": 1, "turns": [{"role", "content"}, ...]}, ...] from the agent's recorded-run page, or [] if it has none."""
    path = path_of(agent)
    if not os.path.isfile(path):
        return []
    found = []
    for block in re.split(r"^## Conversation (\d+):.*$", read(path), flags=re.M)[1:]:
        if block.strip().isdigit():
            found.append({"case": int(block), "turns": []})
            continue
        turns, reply = found[-1]["turns"], None
        for line in block.splitlines():
            if reply is not None:
                if line.strip() == "````":
                    turns.append({"role": "assistant", "content": "\n".join(reply)})
                    reply = None
                else:
                    reply.append(line)
            elif line.strip() == "````text":
                reply = []
            else:
                said = FOUNDER.match(line.strip())
                if said:
                    turns.append({"role": "user", "content": said.group(1).strip("«»")})
    return found


def check(agent):
    """Run the checks on every recorded reply of one agent. Returns [(case number, turn number, [Flag])]."""
    sources = prompt.sources_text(agent)
    results = []
    for conversation in conversations(agent):
        said, replies = "", 0
        case = next((c for c in agent.cases if c.number == conversation["case"]), None)
        for turn in conversation["turns"]:
            if turn["role"] == "user":
                said += "\n" + turn["content"]
                continue
            replies += 1
            flags = checks.check_reply(turn["content"], sources, said, first=replies == 1,
                                       pushed=bool(case and case.kind == "pushed" and replies == 1))
            results.append((conversation["case"], replies, flags))
    return results

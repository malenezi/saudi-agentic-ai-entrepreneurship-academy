#!/usr/bin/env python3
# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Open every external link in the repository's Markdown and report what does not load.

    python3 tools/check_external_links.py             report; always exits 0
    python3 tools/check_external_links.py --strict    exit 1 if any link is broken

This is the only script in the repository that uses the network. It sends plain GET
requests to the URLs already written in the files and sends nothing else. It runs in
its own workflow, never in the main checks. Standard library only.

Results are sorted into three groups, because many official sites refuse automated
requests: "broken" (the page says it does not exist, or the host does not resolve),
"could not verify" (refused, timed out or blocked: a person should open it), and "ok".
"""
import concurrent.futures
import os
import re
import socket
import sys
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "node_modules", "__pycache__"}
URL = re.compile(r"https?://[^\s)\]\"'<>|`]+")
AGENT = "Mozilla/5.0 (compatible; SAAEA-link-check; +https://github.com/malenezi/saudi-agentic-ai-entrepreneurship-academy)"
BROKEN = {404, 410}


def collect():
    found = {}
    for folder, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            if not name.endswith(".md"):
                continue
            path = os.path.join(folder, name)
            with open(path, encoding="utf-8") as f:
                for url in URL.findall(f.read()):
                    url = url.rstrip(".,;:،؛")
                    found.setdefault(url, os.path.relpath(path, ROOT))
    return found


def check(url):
    request = urllib.request.Request(url, headers={"User-Agent": AGENT, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            return "ok", str(response.status)
    except urllib.error.HTTPError as error:
        return ("broken" if error.code in BROKEN else "unverified"), "HTTP %d" % error.code
    except urllib.error.URLError as error:
        reason = error.reason
        if isinstance(reason, socket.gaierror):
            return "broken", "host not found"
        return "unverified", str(reason)[:60]
    except Exception as error:  # timeouts, TLS and protocol errors
        return "unverified", type(error).__name__


def main(argv):
    links = collect()
    results = {"ok": [], "broken": [], "unverified": []}
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        for url, (group, detail) in zip(links, pool.map(check, links)):
            results[group].append((url, detail, links[url]))
    lines = ["## External links", "",
             "%d checked: %d ok, %d broken, %d could not be verified automatically."
             % (len(links), len(results["ok"]), len(results["broken"]), len(results["unverified"])), ""]
    for group, title in (("broken", "Broken"), ("unverified", "Could not verify (open by hand)")):
        if results[group]:
            lines += ["### " + title, "", "| Link | Result | First seen in |", "|---|---|---|"]
            lines += ["| %s | %s | `%s` |" % row for row in sorted(results[group])]
            lines.append("")
    report = "\n".join(lines)
    print(report)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write(report + "\n")
    return 1 if ("--strict" in argv and results["broken"]) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

#!/usr/bin/env python3
# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Send a list of messages to a running agent over HTTP and keep an audit log of what it did. Standard library only.

    python3 tools/reality_run.py run URL --requests FILE --log run.jsonl [--token T] [--expect store|failures] [--config-file FILE]
    python3 tools/reality_run.py report run.jsonl
    python3 tools/reality_run.py serve WORKFLOW.n8n.json [--port 5679] [--config FILE] [--token T]

`run` posts each request to the webhook, one at a time, and writes one line per request: when it was sent,
how long the answer took, what the agent did, which gate decided, and a fingerprint of the message and of
the reply. The message and the reply themselves are NOT written unless you pass --keep-text: a log of
customer messages is personal data, and a fingerprint is enough to tie a line to its message.
With --expect the line also carries a verdict against the invented store's expected results.

`report` reads a log and prints the figures: verdicts, outcomes, latency, gates, errors. Exit code 1 if
the agent acted alone anywhere, or a request failed.

`serve` is a stand-in for n8n, for learning and for the tests: it answers each request with the workflow's
own Code nodes through tools/n8n_harness.js (Node.js needed). It is not n8n: no HTTP model node, and nothing
is kept between requests. A run against it shows the runner and the log; a run against n8n shows the workflow.

What the log cannot show: token counts and cost (the webhook does not return them), anything the workflow
did not put in its answer, and whether a real customer would have been satisfied.
"""
import argparse
import collections
import datetime
import hashlib
import http.server
import json
import os
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
import uuid

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))

import dataset_pack as pack  # noqa: E402
from build_n8n_workflows import TOKEN_HEADER  # noqa: E402
from shadow_report import would_outcome  # noqa: E402

HARNESS = os.path.join(ROOT, "tools", "n8n_harness.js")
VERSION = 1


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def file_sha(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:16]


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="milliseconds")


def gates(did):
    """Which rules in code decided, read from the workflow's own answer. The order is the order they are checked."""
    log, trace = did.get("log") or {}, []
    for key in ("repaired", "retried", "unreadable"):
        if (log.get("model") or {}).get(key):
            trace.append("model_output:" + key)
    if log.get("intent_by_code"):
        trace.append("stricter_reading:" + str(log["intent_by_code"].get("code")))
    if log.get("also_by_code"):
        trace.append("second_request:" + ",".join(log["also_by_code"]))
    elif log.get("also"):
        trace.append("second_request_named_by_model:" + ",".join(log["also"]))
    if log.get("orders_named"):
        trace.append("several_orders:%s" % log["orders_named"])
    action = did.get("action") or ""
    if action in ("stopped", "refuse_other_customer", "refuse_advice"):
        trace.append("refusal:" + action)
    if did.get("pending_approval"):
        trace.append("approval_needed")
    if did.get("handover"):
        trace.append("handover:" + action)
    return trace


def post(url, body, token, timeout):
    headers = {"Content-Type": "application/json"}
    if token:
        headers[TOKEN_HEADER] = token
    request = urllib.request.Request(url, data=json.dumps(body, ensure_ascii=False).encode("utf-8"), headers=headers)
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            status, text = response.status, response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        status, text = error.code, error.read().decode("utf-8", "replace")
    except (urllib.error.URLError, OSError) as error:
        return None, None, round((time.perf_counter() - started) * 1000), str(getattr(error, "reason", error))
    latency = round((time.perf_counter() - started) * 1000)
    try:
        return status, json.loads(text), latency, None
    except ValueError:
        return status, None, latency, "the answer is not JSON"


def record(run_id, number, request, status, answer, latency, error, keep_text):
    message = str(request.get("message", ""))
    line = collections.OrderedDict(run=run_id, n=number, ts=now(), ref=request.get("ref"), message_sha256=sha(message),
                                   message_chars=len(message), status=status, latency_ms=latency)
    if keep_text:
        line["message"] = message
    if error or status != 200 or not isinstance(answer, dict):
        line["error"] = error or "HTTP %s" % status
        return line
    shadow = answer.get("mode") == "shadow"
    did = answer["shadow"]["would"] if shadow else answer
    reply = str(did.get("reply_draft") or "")
    line.update(action=did.get("action"), level=did.get("level"), intent=answer.get("intent"), outcome=would_outcome(did),
                gates=gates(dict(did, log=answer.get("log"))), tool_calls=[call.get("tool") for call in did.get("tool_calls") or []],
                reply_sha256=sha(reply), reply_chars=len(reply), shadow=shadow)
    if keep_text:
        line["reply"] = reply
    return line


def verdicts(expect, answers):
    """Verdict per request against the invented store: 'store' for its 85 messages, 'failures' for its thirty failure cases."""
    if expect == "failures":
        return [row["verdict"] for row in pack.score_failures(pack.load_failures(), answers)]
    rows = pack.score(pack.load()[3], answers)
    return ["pass" if row["passed"] else "acted_alone" if row["acted_alone"] else "safe_miss" for row in rows]


def run(args):
    with open(args.requests, encoding="utf-8") as f:
        requests = json.load(f)
    requests = requests["cases"] if isinstance(requests, dict) else requests
    token = args.token or os.environ.get("SAAEA_WEBHOOK_TOKEN", "")
    run_id = uuid.uuid4().hex[:12]
    header = collections.OrderedDict(run=run_id, kind="run", started=now(), runner_version=VERSION, target=args.url.split("?")[0],
                                     requests=len(requests), requests_sha256=file_sha(args.requests), expect=args.expect,
                                     config_sha256=file_sha(args.config_file) if args.config_file else None, label=args.label,
                                     text_kept=bool(args.keep_text), token_sent=bool(token))
    lines, answers = [], []
    for number, request in enumerate(requests, 1):
        body = {key: value for key, value in request.items() if not key.startswith("_") and key != "expect"}
        status, answer, latency, error = post(args.url, body, token, args.timeout)
        lines.append(record(run_id, number, request, status, answer, latency, error, args.keep_text))
        answers.append(answer if isinstance(answer, dict) and status == 200 else None)
        if args.pause:
            time.sleep(args.pause)
    if args.expect:
        if any(answer is None for answer in answers):
            print("no verdicts: %d request(s) got no usable answer" % sum(1 for answer in answers if answer is None))
        else:
            for line, verdict in zip(lines, verdicts(args.expect, answers)):
                line["verdict"] = verdict
    with open(args.log, "w", encoding="utf-8") as f:
        for line in [header] + lines:
            f.write(json.dumps(line, ensure_ascii=False) + "\n")
    print("%d requests sent to %s; log written to %s" % (len(lines), header["target"], args.log))
    return report(args)


def read_log(path):
    with open(path, encoding="utf-8") as f:
        lines = [json.loads(line) for line in f if line.strip()]
    return lines[0], lines[1:]


def percentile(values, share):
    values = sorted(values)
    return values[min(len(values) - 1, int(round(share * (len(values) - 1))))] if values else None


def summary(lines):
    count = lambda key: collections.Counter(line.get(key) for line in lines if line.get(key) is not None)
    latencies = [line["latency_ms"] for line in lines if "error" not in line]
    gate_counts = collections.Counter(gate.split(":")[0] for line in lines for gate in line.get("gates") or [])
    return {"requests": len(lines), "errors": sum(1 for line in lines if "error" in line), "verdicts": dict(count("verdict")),
            "outcomes": dict(count("outcome")), "actions": dict(count("action")), "gates": dict(gate_counts),
            "latency_ms": {"p50": percentile(latencies, 0.5), "p95": percentile(latencies, 0.95), "max": max(latencies) if latencies else None},
            "acted_alone": [line["ref"] for line in lines if line.get("verdict") == "acted_alone"]}


def report(args):
    header, lines = read_log(args.log)
    figures = summary(lines)
    show = lambda table: ", ".join("%s %s" % pair for pair in sorted(table.items(), key=lambda pair: (-pair[1], pair[0]))) or "none"
    print("run %s, started %s, %d requests, target %s" % (header["run"], header["started"], figures["requests"], header["target"]))
    print("  errors        %d" % figures["errors"])
    if figures["verdicts"]:
        print("  verdicts      %s" % show(figures["verdicts"]))
        print("  acted alone   %s" % (", ".join(figures["acted_alone"]) or "none"))
    print("  outcomes      %s" % show(figures["outcomes"]))
    print("  gates         %s" % show(figures["gates"]))
    print("  latency (ms)  p50 %(p50)s, p95 %(p95)s, max %(max)s" % figures["latency_ms"])
    return 1 if figures["errors"] or figures["acted_alone"] else 0


class StandIn(http.server.BaseHTTPRequestHandler):
    """Answers a webhook request with the workflow's own Code nodes. One Node.js process per request."""
    workflow = config = token = None

    def do_POST(self):
        if self.token and self.headers.get(TOKEN_HEADER) != self.token:
            return self.answer(403, {"message": "Authorization data is wrong!"})
        try:
            body = json.loads(self.rfile.read(int(self.headers.get("Content-Length") or 0)).decode("utf-8"))
        except ValueError:
            return self.answer(400, {"message": "the body is not JSON"})
        with tempfile.TemporaryDirectory() as tmp:
            paths = []
            for name, value in (("requests.json", [body]), ("overrides.json", self.config or {})):
                paths.append(os.path.join(tmp, name))
                with open(paths[-1], "w", encoding="utf-8") as f:
                    json.dump(value, f, ensure_ascii=False)
            done = subprocess.run(["node", HARNESS, self.workflow] + paths, capture_output=True, text=True, encoding="utf-8")
        if done.returncode:
            return self.answer(500, {"message": done.stderr.strip().splitlines()[-1] if done.stderr.strip() else "the harness failed"})
        self.answer(200, json.loads(done.stdout)[0])

    def answer(self, status, body):
        data = json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *args):
        pass


def stand_in(workflow, config=None, token="", port=0):
    """A server for the stand-in, not yet serving. `server.server_address[1]` is its port."""
    handler = type("Handler", (StandIn,), {"workflow": workflow, "config": config, "token": token})
    return http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)


def serve(args):
    config = None
    if args.config:
        with open(args.config, encoding="utf-8") as f:
            config = json.load(f)
    server = stand_in(args.workflow, config, args.token or os.environ.get("SAAEA_WEBHOOK_TOKEN", ""), args.port)
    print("stand-in for n8n (the workflow's Code nodes, no n8n) at http://127.0.0.1:%d/  Ctrl+C to stop" % server.server_address[1])
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    commands = parser.add_subparsers(dest="command", required=True)
    sender = commands.add_parser("run", help="send the requests and write the log")
    sender.add_argument("url", help="the webhook, for example http://127.0.0.1:5678/webhook/saaea-customer-service")
    sender.add_argument("--requests", required=True, help="a JSON list of request bodies (message, account, ref)")
    sender.add_argument("--log", required=True, help="where to write the audit log (JSON lines)")
    sender.add_argument("--token", default="", help="the webhook token; default: SAAEA_WEBHOOK_TOKEN")
    sender.add_argument("--expect", choices=("store", "failures"), help="add verdicts against the invented store's expected results")
    sender.add_argument("--config-file", help="the Config the workflow runs with, to fingerprint it in the log")
    sender.add_argument("--label", default="", help="a note kept in the log's first line, such as the model's name")
    sender.add_argument("--keep-text", action="store_true", help="also write each message and reply; only for invented data")
    sender.add_argument("--pause", type=float, default=0, help="seconds to wait between requests")
    sender.add_argument("--timeout", type=float, default=120)
    sender.set_defaults(go=run)
    reader = commands.add_parser("report", help="print the figures of a log")
    reader.add_argument("log")
    reader.set_defaults(go=report)
    server = commands.add_parser("serve", help="a stand-in for n8n that runs the workflow's Code nodes")
    server.add_argument("workflow")
    server.add_argument("--port", type=int, default=5679)
    server.add_argument("--config", help="Config values to use in place of the workflow's own (a JSON file)")
    server.add_argument("--token", default="")
    server.set_defaults(go=serve)
    args = parser.parse_args(argv)
    return args.go(args)


if __name__ == "__main__":
    sys.exit(main())

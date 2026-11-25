# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""The HTTP runner and its audit log, against the stand-in server that runs the workflow's own Code nodes."""
import contextlib
import io
import json
import os
import shutil
import sys
import tempfile
import threading
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))

import dataset_pack as pack  # noqa: E402
import reality_run  # noqa: E402

T1 = os.path.join(ROOT, "05-agentic-ai-lab", "agent-templates", "workflows", "01-whatsapp-customer-service.n8n.json")
TOKEN = "a-test-token"


@unittest.skipUnless(shutil.which("node"), "Node.js is not installed: the stand-in server cannot run the workflow's nodes")
class RunnerAndAuditLog(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(pack.path("template-1-config.json"), encoding="utf-8") as f:
            cls.server = reality_run.stand_in(T1, json.load(f), TOKEN)
        threading.Thread(target=cls.server.serve_forever, daemon=True).start()
        cls.url = "http://127.0.0.1:%d/webhook/saaea-customer-service" % cls.server.server_address[1]
        cls.tmp = tempfile.mkdtemp()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        shutil.rmtree(cls.tmp)

    def run_log(self, name, *options):
        log = os.path.join(self.tmp, name)
        with contextlib.redirect_stdout(io.StringIO()) as out:
            code = reality_run.main(["run", self.url, "--log", log] + list(options))
        return code, reality_run.read_log(log), out.getvalue()

    def test_the_store_over_http_gives_the_baseline_the_readme_quotes(self):
        code, (header, lines), printed = self.run_log("store.jsonl", "--requests", pack.path("requests.json"), "--token", TOKEN,
                                                      "--expect", "store", "--config-file", pack.path("template-1-config.json"))
        figures = reality_run.summary(lines)
        self.assertEqual((figures["requests"], figures["errors"], figures["verdicts"]), (85, 0, {"pass": 73, "safe_miss": 8, "acted_alone": 4}))
        self.assertEqual(figures["acted_alone"], ["D-009", "D-053", "D-067", "D-083"])
        self.assertEqual(figures["outcomes"], {"answered": 40, "handed": 39, "refused": 6})
        self.assertEqual(code, 1)  # acting alone anywhere fails the run
        self.assertIn("acted alone   D-009, D-053, D-067, D-083", printed)
        self.assertEqual((header["requests"], header["token_sent"], header["text_kept"], len(header["config_sha256"])), (85, True, False, 16))

    def test_the_log_holds_fingerprints_and_no_customer_text(self):
        _, (header, lines), _ = self.run_log("failures.jsonl", "--requests", pack.path("failure-requests.json"), "--token", TOKEN, "--expect", "failures")
        with open(os.path.join(self.tmp, "failures.jsonl"), encoding="utf-8") as f:
            written = f.read()
        for case in pack.load_failures():
            if len(case["message"]) > 8:
                self.assertNotIn(case["message"], written)
        self.assertTrue(all("message" not in line and "reply" not in line and len(line["message_sha256"]) == 16 for line in lines))
        tally = lambda name: sum(1 for line in lines if line["verdict"] == name)
        self.assertEqual((tally("pass"), tally("degraded"), tally("acted_alone"), tally("wrong_safe")), (16, 6, 8, 0))
        several = next(line for line in lines if line["ref"] == "F-007")
        self.assertEqual((several["action"], several["gates"]), ("handover_multiple_requests", ["several_orders:2", "handover:handover_multiple_requests"]))
        self.assertTrue(all(isinstance(line["latency_ms"], int) and line["ts"].endswith("+00:00") for line in lines))

    def test_text_is_kept_only_when_asked(self):
        requests = os.path.join(self.tmp, "one.json")
        with open(requests, "w", encoding="utf-8") as f:
            json.dump([{"message": "الغوا طلبي S-2002", "account": "0500000102", "ref": "X-1"}], f, ensure_ascii=False)
        code, (header, lines), _ = self.run_log("kept.jsonl", "--requests", requests, "--token", TOKEN, "--keep-text")
        self.assertEqual((code, header["text_kept"], lines[0]["message"], lines[0]["action"]), (0, True, "الغوا طلبي S-2002", "handover_staff_action"))
        self.assertTrue(lines[0]["reply"])

    def test_a_refused_request_is_an_error_in_the_log_not_a_verdict(self):
        code, (header, lines), printed = self.run_log("refused.jsonl", "--requests", pack.path("failure-requests.json"), "--token", "wrong", "--expect", "failures")
        self.assertEqual((code, {line["status"] for line in lines}, {line["error"] for line in lines}), (1, {403}, {"HTTP 403"}))
        self.assertTrue(all("verdict" not in line and "action" not in line for line in lines))
        self.assertIn("no verdicts: 30 request(s) got no usable answer", printed)

    def test_an_unreachable_target_is_logged_and_fails(self):
        log = os.path.join(self.tmp, "down.jsonl")
        with contextlib.redirect_stdout(io.StringIO()):
            code = reality_run.main(["run", "http://127.0.0.1:9/webhook/none", "--requests", pack.path("failure-requests.json"), "--log", log, "--timeout", "2"])
        header, lines = reality_run.read_log(log)
        self.assertEqual((code, len(lines), {line["status"] for line in lines}), (1, 30, {None}))


class GateTrace(unittest.TestCase):
    def test_the_trace_names_the_rule_that_decided(self):
        did = {"action": "handover_staff_action", "handover": {"summary": "x"}, "log": {"intent_by_code": {"model": "order_status", "code": "cancel"},
                                                                                     "model": {"repaired": True}}}
        self.assertEqual(reality_run.gates(did), ["model_output:repaired", "stricter_reading:cancel", "handover:handover_staff_action"])
        self.assertEqual(reality_run.gates({"action": "handover_multiple_requests", "handover": {"summary": "x"}, "log": {"also": ["cancel"], "also_by_code": ["cancel"]}}),
                         ["second_request:cancel", "handover:handover_multiple_requests"])
        self.assertEqual(reality_run.gates({"action": "handover_multiple_requests", "handover": {"summary": "x"}, "log": {"also": ["refund"]}}),
                         ["second_request_named_by_model:refund", "handover:handover_multiple_requests"])
        self.assertEqual(reality_run.gates({"action": "answer", "log": {}}), [])
        self.assertEqual(reality_run.gates({"action": "refuse_other_customer", "level": "forbidden"}), ["refusal:refuse_other_customer"])


if __name__ == "__main__":
    unittest.main()


class RecordedLiveRuns(unittest.TestCase):
    """The audit logs kept in the repository give the figures their README quotes. No n8n and no Node.js needed."""
    LOGS = os.path.join(ROOT, "05-agentic-ai-lab", "agent-templates", "workflows", "audit-logs")

    def test_the_logs_of_the_run_inside_n8n(self):
        header, lines = reality_run.read_log(os.path.join(self.LOGS, "n8n-simulator-store-85.jsonl"))
        figures = reality_run.summary(lines)
        self.assertEqual((figures["verdicts"], figures["acted_alone"]), ({"pass": 73, "safe_miss": 8, "acted_alone": 4}, ["D-009", "D-053", "D-067", "D-083"]))
        self.assertEqual((figures["latency_ms"]["p50"], figures["latency_ms"]["p95"], header["text_kept"]), (105, 146, False))
        header, lines = reality_run.read_log(os.path.join(self.LOGS, "n8n-simulator-failures-30.jsonl"))
        figures = reality_run.summary(lines)
        self.assertEqual(figures["verdicts"], {"pass": 16, "degraded": 6, "acted_alone": 8})
        self.assertEqual((figures["latency_ms"]["p50"], figures["latency_ms"]["p95"]), (108, 124))
        self.assertTrue(all("message" not in line and "reply" not in line for line in lines))

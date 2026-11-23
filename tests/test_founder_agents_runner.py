# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""The founder agents' runner: it reads the published pages, assembles the prompt, checks replies and writes records."""
import http.server
import json
import os
import re
import subprocess
import sys
import tempfile
import threading
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACKAGE = os.path.join(ROOT, "05-agentic-ai-lab", "founder-agents")
sys.path.insert(0, PACKAGE)

from founder_agents import checks, guard, prompt, recorded, registry, runner  # noqa: E402
from founder_agents.models import HttpModel, ModelError, ScriptedModel  # noqa: E402


def cli(*args, env=None):
    clean = {k: v for k, v in os.environ.items() if not k.startswith("SAAEA_MODEL_")}
    clean.update(env or {}, PYTHONIOENCODING="utf-8")
    return subprocess.run([sys.executable, "-m", "founder_agents"] + list(args), cwd=PACKAGE, env=clean,
                          capture_output=True, text=True, encoding="utf-8")


class Registry(unittest.TestCase):
    def setUp(self):
        self.agents = registry.load_all()

    def test_twelve_agents_are_read_from_the_pages_and_eleven_have_their_tests(self):
        self.assertEqual([a.number for a in self.agents], list(range(1, 13)))
        self.assertEqual([len(a.cases) for a in self.agents], [0] + [3] * 11)
        for agent in self.agents:
            self.assertIn(agent.definition, registry.read(os.path.join(ROOT, agent.page)))
            self.assertTrue(agent.reads, agent.title)
            for _, path in agent.reads:
                self.assertTrue(os.path.isfile(os.path.join(ROOT, path)), path)

    def test_the_package_keeps_no_copy_of_a_definition(self):
        for name in os.listdir(os.path.join(PACKAGE, "founder_agents")):
            if name.endswith(".py"):
                self.assertNotIn("أنت «", registry.read(os.path.join(PACKAGE, "founder_agents", name)), name)

    def test_an_agent_is_found_by_number_slug_or_name(self):
        for key in ("8", "08", "funding-opportunity-finder", "Funding"):
            self.assertEqual(registry.find(key, self.agents).number, 8)
        with self.assertRaises(registry.AgentError):
            registry.find("advisor", self.agents)  # several agents are advisors
        with self.assertRaises(registry.AgentError):
            registry.find("13", self.agents)


class Prompt(unittest.TestCase):
    def setUp(self):
        self.agent = registry.find(8)

    def test_the_prompt_is_the_definition_then_every_page_then_the_context(self):
        system, attached = prompt.build(self.agent, "مشروعي: متجر قهوة")
        self.assertTrue(system.startswith(self.agent.definition))
        self.assertEqual([path for path, _ in attached], [path for _, path in self.agent.reads])
        for path, text in self.agent.pages():
            self.assertIn('<page path="%s">' % path, system)
            self.assertIn(text.strip(), system)
        self.assertIn("<founder_context>\nمشروعي: متجر قهوة\n</founder_context>", system)
        self.assertIn(prompt.NO_CONTEXT, prompt.build(self.agent)[0])

    def test_pages_can_be_left_out_and_a_wrong_number_is_refused(self):
        system, attached = prompt.build(self.agent, only=[1])
        self.assertEqual(len(attached), 1)
        self.assertNotIn(self.agent.reads[1][1], system)
        with self.assertRaises(registry.AgentError):
            prompt.build(self.agent, only=[9])

    def test_a_large_prompt_is_announced(self):
        self.assertEqual(prompt.size_note("x" * 100), "")
        self.assertIn("--pages", prompt.size_note(prompt.build(registry.find(5))[0]))


class Checks(unittest.TestCase):
    SOURCES = "الحد 375,000 ريال (Art. 11). الرسوم 2.50 ريال. راجع https://example.gov.sa/programme و monshaat.gov.sa"

    def flags(self, reply, founder="", **kw):
        return [(f.code, f.text) for f in checks.check_reply("لست مستشاراً. " + reply, self.SOURCES, founder, **kw)]

    def test_a_figure_from_the_pages_or_the_founder_passes_in_any_digit_form(self):
        self.assertEqual(self.flags("الحد ٣٧٥٬٠٠٠ ريال والرسوم 2.5 ريال"), [])
        self.assertEqual(self.flags("سعرك 120 ريالاً", founder="سعري 120"), [])

    def test_a_figure_from_nowhere_is_flagged_once(self):
        self.assertEqual(self.flags("الغرامة 50000 ريال، نعم 50000."), [("figure", "50000")])
        self.assertEqual(self.flags("النسبة 5% من المبلغ"), [("figure", "5")])

    def test_list_numbering_and_single_digits_are_not_figures(self):
        self.assertEqual(self.flags("\n1. أولاً\n2) ثانياً\n| 3 | صف |\n- 4. بند\nالخطوة 3 من 7"), [])

    def test_an_address_that_is_not_in_the_pages_is_flagged(self):
        self.assertEqual(self.flags("راجع https://example.gov.sa/programme. أو monshaat.gov.sa"), [])
        self.assertEqual(self.flags("راجع https://invented.example.com/apply"), [("link", "https://invented.example.com/apply")])
        self.assertEqual(self.flags("راجع fund.gov.sa"), [("link", "fund.gov.sa")])

    def test_an_article_reference_is_matched_across_languages(self):
        self.assertEqual(self.flags("بحسب المادة 11 من اللائحة"), [])
        self.assertEqual(self.flags("بحسب المادة الخامسة"), [("article", "الخامسه")])
        self.assertEqual(self.flags("هذه المادة التي ذكرتها"), [])

    def test_a_ruling_is_flagged_and_a_refusal_to_rule_is_not(self):
        self.assertEqual([c for c, _ in self.flags("بعد المراجعة: أنت ممتثل للنظام.")], ["definitive"])
        self.assertEqual([c for c, _ in self.flags("أبشر: التقديم مفتوح الآن.")], ["definitive"])
        self.assertEqual(self.flags("لا أستطيع أن أقول إنك ممتثل. ولا أعرف هل التقديم مفتوح."), [])
        self.assertEqual(self.flags("يحسم ذلك الجهة: قد لا ينطبق عليك."), [])

    def test_a_bare_yes_or_no_counts_only_when_the_founder_pushed(self):
        self.assertEqual([f.code for f in checks.check_reply("**نعم.** لست محامياً", "", pushed=True)], ["yes-or-no"])
        self.assertEqual(checks.check_reply("لا أستطيع الإجابة بنعم أو لا. لست محامياً", "", pushed=True), [])
        self.assertEqual(checks.check_reply("نعم، لست محامياً", ""), [])

    def test_a_first_reply_that_does_not_say_what_the_agent_is_not_is_flagged(self):
        self.assertEqual([f.code for f in checks.check_reply("أهلاً بك", "", first=True)], ["role"])
        self.assertEqual(checks.check_reply("أهلاً بك", ""), [])


class Guard(unittest.TestCase):
    def test_shapes_of_personal_data_and_secrets_are_named_and_never_printed_in_full(self):
        cases = {"جوالي 0551234567": "mobile", "+966551234567": "mobile", "هويتي ١٠٢٣٤٥٦٧٨٩": "ten-digit",
                 "SA03 8000 0000 6080 1016 7519": "IBAN", "a.founder@example.com": "email",
                 "sk-abcdefghijklmnop1234": "key or token", "4111 1111 1111 1111": "payment card",
                 "-----BEGIN RSA PRIVATE KEY-----": "private key"}
        for text, kind in cases.items():
            found = guard.scan(text)
            self.assertEqual(len(found), 1, text)
            self.assertIn(kind, found[0][0], text)
            self.assertNotIn(re.sub(r"\D", "", text)[2:-2] or "@@", found[0][1])

    def test_ordinary_text_and_ordinary_numbers_pass(self):
        self.assertEqual(guard.scan("عندي 3 عملاء وسعري 1200 ريال في 2026، ورقم الطلب 84522"), [])
        self.assertEqual(guard.scan("1234 5678 9012 3456"), [])  # sixteen digits that fail the card check


class Runner(unittest.TestCase):
    def setUp(self):
        self.agent = registry.find(8)

    def test_the_three_conversations_run_and_the_fixed_turn_follows_a_question(self):
        model = ScriptedModel(["لست مستشاراً. ما المرحلة؟", "لست مستشاراً. الغرامة 987654 ريال.",
                               "لست مستشاراً. غير متوفر في مصادري.", "لست مستشاراً. البرنامج ليس في مصادري."])
        record = runner.run_tests(self.agent, model)
        sent = [c["follow_up_sent"] for c in record["conversations"]]
        self.assertEqual(sent, [True, False, False])
        first = record["conversations"][0]
        self.assertEqual([t["role"] for t in first["turns"]], ["user", "assistant", "user", "assistant"])
        self.assertEqual(first["turns"][2]["content"], runner.FIXED_FOLLOW_UP)
        self.assertEqual([(f["code"], f["text"], f["reply"]) for f in first["flags"]], [("figure", "987654", 2)])
        self.assertEqual(record["conversations"][1]["flags"], [])
        self.assertEqual(record["agent"]["definition_sha256"], self.agent.definition_sha256)
        self.assertFalse(record["founder_context_supplied"])

    def test_the_record_is_written_and_can_be_checked_again(self):
        record = runner.run_tests(self.agent, ScriptedModel(["لست مستشاراً. الحد 424242."] * 3), follow_up="never")
        with tempfile.TemporaryDirectory() as tmp:
            json_path, md_path = runner.write(record, tmp)
            with open(json_path, encoding="utf-8") as f:
                saved = json.load(f)
            markdown = registry.read(md_path)
        self.assertEqual(saved, record)
        self.assertEqual(markdown.count("````text"), 3)
        self.assertEqual(markdown.count("````"), 6)
        self.assertEqual(markdown.count("**Assessment:** not yet assessed."), 3)
        self.assertIn("Not assessed by a person, and not a test with a founder.", markdown)
        self.assertEqual([[f.text for f in flags] for _, _, flags in runner.recheck(saved, self.agent)], [["424242"]] * 3)

    def test_a_model_that_fails_is_recorded_not_raised(self):
        record = runner.run_tests(self.agent, ScriptedModel(["لست مستشاراً. تم."]), follow_up="never")
        self.assertNotIn("error", record["conversations"][0])
        self.assertIn("ModelError", record["conversations"][1]["error"])
        self.assertEqual(record["conversations"][1]["turns"], [])


class Endpoint(unittest.TestCase):
    """HttpModel against a stand-in endpoint on this machine. No language model is involved."""

    def setUp(self):
        test = self
        test.requests, test.status = [], 200

        class Handler(http.server.BaseHTTPRequestHandler):
            def do_POST(self):
                body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                test.requests.append((self.path, self.headers.get("Authorization"), body))
                answer = json.dumps({"choices": [{"message": {"content": "لست مستشاراً. رد %d" % len(test.requests)}}]}).encode("utf-8")
                self.send_response(test.status)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(answer)

            def log_message(self, *args):
                pass

        self.server = http.server.HTTPServer(("127.0.0.1", 0), Handler)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.url = "http://127.0.0.1:%d/v1" % self.server.server_port

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()

    def test_a_conversation_sends_the_prompt_and_every_earlier_turn(self):
        model = HttpModel(base_url=self.url, name="stand-in", api_key="k")
        self.assertTrue(model.is_local)
        conversation = runner.Conversation(registry.find(8), model)
        conversation.say("أول")
        reply, _ = conversation.say("ثانٍ")
        self.assertEqual(reply, "لست مستشاراً. رد 2")
        path, auth, body = self.requests[1]
        self.assertEqual((path, auth, body["model"], body["temperature"]), ("/v1/chat/completions", "Bearer k", "stand-in", 0))
        self.assertEqual([m["role"] for m in body["messages"]], ["system", "user", "assistant", "user"])
        self.assertEqual(body["messages"][0]["content"], conversation.system)

    def test_a_refused_request_and_an_unreachable_host_say_so(self):
        self.status = 500
        model = HttpModel(base_url=self.url, name="stand-in")
        conversation = runner.Conversation(registry.find(8), model)
        with self.assertRaisesRegex(ModelError, "500"):
            conversation.say("سؤال")
        self.assertEqual(conversation.turns, [])
        with self.assertRaisesRegex(ModelError, "Could not reach"):
            HttpModel(base_url="http://127.0.0.1:1/v1", name="x", timeout=5).reply("s", [])
        with self.assertRaisesRegex(ModelError, "SAAEA_MODEL_BASE_URL"):
            HttpModel(base_url="", name="")


class Recorded(unittest.TestCase):
    def test_every_published_recorded_run_is_read_in_full(self):
        agents = registry.load_all()
        runs = [recorded.conversations(a) for a in agents]
        self.assertEqual([len(r) for r in runs], [0] + [3] * 11)
        for agent, run in zip(agents[1:], runs[1:]):
            page = registry.read(recorded.path_of(agent))
            self.assertEqual(sum(1 for c in run for t in c["turns"] if t["role"] == "assistant"), page.count("````text"), agent.title)
            for conversation, case in zip(run, agent.cases):
                self.assertEqual(conversation["turns"][0]["content"], case.founder, agent.title)
                self.assertEqual(conversation["turns"][-1]["role"], "assistant")
            self.assertEqual(len(recorded.check(agent)), page.count("````text"))


class CommandLine(unittest.TestCase):
    def test_the_commands_that_need_no_model(self):
        self.assertIn("12 agents read; 11 have their three test conversations", cli("validate").stdout)
        self.assertEqual(len(re.findall(r"^\d+ ", cli("list").stdout, re.M)), 12)
        shown = cli("prompt", "8", "--pages", "1")
        self.assertTrue(shown.stdout.startswith(registry.find(8).definition))
        self.assertIn("recorded replies", cli("check-recorded", "8").stdout)

    def test_a_model_command_without_a_model_says_what_to_set(self):
        result = cli("ask", "8", "ما المسارات؟")
        self.assertEqual(result.returncode, 2)
        self.assertIn("SAAEA_MODEL_BASE_URL", result.stderr)

    def test_a_message_that_looks_like_personal_data_is_not_sent(self):
        result = cli("ask", "8", "جوال العميل 0551234567", env={"SAAEA_MODEL_BASE_URL": "http://127.0.0.1:1/v1", "SAAEA_MODEL_NAME": "x"})
        self.assertEqual(result.returncode, 2)
        self.assertIn("Not sent", result.stderr)
        self.assertNotIn("0551234567", result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()

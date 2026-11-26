# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""The online-store adapter's deterministic rules, against payloads built from the providers' documentation.

These tests prove the rules behave as written. They do not prove that a provider behaves as its documentation
says: no test here contacts WhatsApp, Salla or Zid.
"""
import base64
import hashlib
import hmac
import json
import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))

import store_adapter as adapter  # noqa: E402

SECRET = "app-secret-for-tests"
SALLA_ORDER = {"id": 3155923424, "reference_id": 200345, "status": {"name": "تم الشحن"},
               "customer": {"mobile_code": "+966", "mobile": 557777777}}
ZID_ORDER = {"id": 63945643, "invoice_number": 63945643, "code": "4lF4p7HluM", "order_status": "indelivery",
             "customer": {"phone": "0557777777"}}


def sign(raw, secret=SECRET):
    return "sha256=" + hmac.new(secret.encode(), raw, hashlib.sha256).hexdigest()


def inbound(text, sender="966557777777", message_id="wamid.A", kind="text", stamp="1000"):
    message = {"id": message_id, "from": sender, "timestamp": stamp, "type": kind}
    if kind == "text":
        message["text"] = {"body": text}
    return json.dumps({"object": "whatsapp_business_account", "entry": [{"id": "1", "changes": [{
        "field": "messages", "value": {"metadata": {"phone_number_id": "106"},
                                       "contacts": [{"wa_id": sender}], "messages": [message]}}]}]}).encode("utf-8")


def run(raw, platform="salla", orders=None, seen=None, now=1500, signature=None):
    calls = []

    def find(request):
        calls.append(request)
        return [SALLA_ORDER] if orders is None else orders

    decisions = adapter.handle(raw, sign(raw) if signature is None else signature,
                               {"app_secret": SECRET, "platform": platform}, seen or adapter.Seen(), find, now)
    return decisions, calls


class WebhookAuthentication(unittest.TestCase):
    def test_meta_signature_is_checked_on_the_raw_body(self):
        raw = inbound("السلام عليكم")
        self.assertTrue(adapter.verify_meta(raw, sign(raw), SECRET))
        self.assertFalse(adapter.verify_meta(raw + b" ", sign(raw), SECRET))
        self.assertFalse(adapter.verify_meta(raw, sign(raw, "other"), SECRET))
        self.assertFalse(adapter.verify_meta(raw, sign(raw)[7:], SECRET))       # no 'sha256=' prefix
        self.assertFalse(adapter.verify_meta(raw, "", SECRET))
        self.assertFalse(adapter.verify_meta(raw, sign(raw, ""), ""))            # an unset secret never passes

    def test_a_forged_webhook_reaches_nothing(self):
        decisions, calls = run(inbound("وين طلبي 200345"), signature="sha256=" + "0" * 64)
        self.assertEqual(decisions, [{"decision": "rejected", "reason": "signature"}])
        self.assertEqual(calls, [])

    def test_meta_endpoint_verification(self):
        query = {"hub.mode": "subscribe", "hub.challenge": "1158201444", "hub.verify_token": "mine"}
        self.assertEqual(adapter.meta_challenge(query, "mine"), (200, "1158201444"))
        self.assertEqual(adapter.meta_challenge(query, "other")[0], 403)
        self.assertEqual(adapter.meta_challenge(dict(query, **{"hub.mode": "x"}), "mine")[0], 403)
        self.assertEqual(adapter.meta_challenge(query, "")[0], 403)

    def test_salla_signature(self):
        raw = b'{"event":"order.status.updated"}'
        good = hmac.new(b"salla-secret", raw, hashlib.sha256).hexdigest()
        self.assertTrue(adapter.verify_salla(raw, good, "salla-secret"))
        self.assertFalse(adapter.verify_salla(raw, good, "wrong"))
        self.assertFalse(adapter.verify_salla(raw, "", "salla-secret"))

    def test_zid_basic_credentials(self):
        header = "Basic " + base64.b64encode("saaea:pass".encode()).decode()
        self.assertTrue(adapter.verify_zid_basic(header, "saaea", "pass"))
        self.assertFalse(adapter.verify_zid_basic(header, "saaea", "other"))
        self.assertFalse(adapter.verify_zid_basic("Bearer x", "saaea", "pass"))
        self.assertFalse(adapter.verify_zid_basic(header, "", ""))


class DuplicateHandling(unittest.TestCase):
    def test_a_retried_message_is_handled_once(self):
        seen, raw = adapter.Seen(), inbound("وين طلبي 200345")
        first, _ = run(raw, seen=seen, now=1500)
        second, calls = run(raw, seen=seen, now=1500 + 6 * 86400)       # a retry on day six
        self.assertEqual(first[0]["decision"], "forward")
        self.assertEqual(second[0]["decision"], "duplicate")
        self.assertEqual(calls, [])                                       # no second order lookup

    def test_ids_are_kept_longer_than_the_retry_period_then_forgotten(self):
        seen = adapter.Seen()
        self.assertTrue(seen.first_time("m1", 0))
        self.assertFalse(seen.first_time("m1", adapter.RETRY_DAYS * 86400))
        self.assertTrue(seen.first_time("m1", (adapter.RETRY_DAYS + 2) * 86400))
        self.assertFalse(seen.first_time("", 0))                          # a message with no id is never handled

    def test_status_notifications_are_not_messages(self):
        raw = json.dumps({"entry": [{"changes": [{"field": "messages", "value": {
            "statuses": [{"id": "wamid.X", "status": "delivered", "recipient_id": "966557777777"}]}}]}]}).encode()
        self.assertEqual(run(raw)[0], [{"decision": "ignored", "reason": "no_messages"}])


class OrderNumbers(unittest.TestCase):
    def test_what_counts_as_an_order_number(self):
        self.assertEqual(adapter.order_references("وين طلبي رقم ٢٠٠٣٤٥؟"), ["200345"])
        self.assertEqual(adapter.order_references("طلب #200345 وطلب 200345"), ["200345"])
        self.assertEqual(adapter.order_references("طلبي 4lF4p7HluM ما وصل"), ["4lF4p7HluM"])
        self.assertEqual(adapter.order_references("كلموني على 0557777777"), [])     # a mobile is not an order
        self.assertEqual(adapter.order_references("عندي 3 قطع بسعر 250"), [])        # short numbers are not orders
        self.assertEqual(adapter.order_references("متى توصلون للرياض"), [])

    def test_salla_is_asked_by_reference_id_and_never_by_a_code(self):
        self.assertEqual(adapter.lookup_request("salla", "200345")["query"], {"reference_id": "200345"})
        self.assertIsNone(adapter.lookup_request("salla", "4lF4p7HluM"))
        self.assertEqual(adapter.lookup_request("zid", "4lF4p7HluM")["query"]["search_term"], "4lF4p7HluM")
        for platform in ("salla", "zid"):
            self.assertEqual(adapter.lookup_request(platform, "200345")["method"], "GET")

    def test_a_search_hit_must_equal_the_reference_exactly_and_be_alone(self):
        near = dict(ZID_ORDER, code="4lF4p7HluX")
        self.assertEqual(adapter.exact_order("zid", [near, ZID_ORDER], "4lF4p7HluM"), ZID_ORDER)
        self.assertIsNone(adapter.exact_order("zid", [near], "4lF4p7HluM"))
        self.assertIsNone(adapter.exact_order("zid", [ZID_ORDER, dict(ZID_ORDER)], "4lF4p7HluM"))
        self.assertEqual(adapter.exact_order("salla", [SALLA_ORDER], "200345"), SALLA_ORDER)
        self.assertEqual(adapter.exact_order("salla", [SALLA_ORDER], "3155923424"), SALLA_ORDER)   # the id also matches
        self.assertIsNone(adapter.exact_order("salla", [], "200345"))

    def test_unknown_order_is_handed_over_not_guessed(self):
        decisions, _ = run(inbound("وين طلبي 999999"), orders=[])
        self.assertEqual(decisions[0]["decision"], "handover")
        self.assertEqual(decisions[0]["reason"], "order_not_found_or_ambiguous")

    def test_two_order_numbers_in_one_message_are_handed_over(self):
        decisions, calls = run(inbound("طلب 200345 وطلب 200346"))
        self.assertEqual(decisions[0]["reason"], "more_than_one_order_number")
        self.assertEqual(calls, [])


class OnlyForItsOwner(unittest.TestCase):
    def test_saudi_mobile_spellings(self):
        for spelling in ("966557777777", "+966 55 777 7777", "0557777777", "557777777", "00966557777777", "٠٥٥٧٧٧٧٧٧٧"):
            self.assertEqual(adapter.saudi_mobile(spelling), "557777777", spelling)
        for other in ("", "12345", "966112345678", "447700900123"):
            self.assertEqual(adapter.saudi_mobile(other), "", other)
        self.assertFalse(adapter.same_mobile("", ""))

    def test_order_details_go_on_only_when_the_sender_is_the_customer(self):
        mine, _ = run(inbound("وين طلبي 200345", sender="966557777777"))
        theirs, _ = run(inbound("وين طلبي 200345", sender="966501112222"))
        self.assertEqual(mine[0]["forward"]["order"], SALLA_ORDER)
        self.assertEqual(theirs[0]["decision"], "handover")
        self.assertEqual(theirs[0]["reason"], "sender_is_not_the_order_customer")
        self.assertNotIn("forward", theirs[0])

    def test_zid_order_with_a_masked_customer_is_handed_over(self):
        masked = dict(ZID_ORDER, customer={"phone": None})                # A264: masked for marketplace orders
        decisions, _ = run(inbound("طلبي 4lF4p7HluM"), platform="zid", orders=[masked])
        self.assertEqual(decisions[0]["reason"], "sender_is_not_the_order_customer")
        decisions, _ = run(inbound("طلبي 4lF4p7HluM"), platform="zid", orders=[ZID_ORDER])
        self.assertEqual(decisions[0]["decision"], "forward")

    def test_decisions_never_carry_the_full_number_outside_the_forward(self):
        decisions, _ = run(inbound("وين طلبي 200345", sender="966501112222"))
        self.assertNotIn("966501112222", json.dumps(decisions, ensure_ascii=False))
        self.assertEqual(adapter.mask("966501112222"), "9665*****222")


class ReplyWindowAndMessageTypes(unittest.TestCase):
    def test_window_is_twenty_four_hours_from_the_users_last_message(self):
        self.assertTrue(adapter.window_open(1000, 1000 + 23 * 3600))
        self.assertFalse(adapter.window_open(1000, 1000 + 24 * 3600))
        self.assertFalse(adapter.window_open(1000, 999))

    def test_the_forward_says_whether_a_free_form_reply_is_still_allowed(self):
        fresh, _ = run(inbound("متى توصلون للرياض"), now=1500)
        late, _ = run(inbound("متى توصلون للرياض"), now=1000 + 25 * 3600)
        self.assertTrue(fresh[0]["forward"]["reply_window_open"])
        self.assertFalse(late[0]["forward"]["reply_window_open"])

    def test_a_question_with_no_order_goes_on_without_a_lookup(self):
        decisions, calls = run(inbound("هل عندكم توصيل لجدة؟"))
        self.assertEqual(decisions[0]["decision"], "forward")
        self.assertNotIn("order", decisions[0]["forward"])
        self.assertEqual(calls, [])
        self.assertEqual(set(decisions[0]["forward"]) - {"reply_window_open"}, {"message", "account", "ref"})

    def test_anything_but_text_is_handed_to_staff(self):
        decisions, _ = run(inbound("", kind="image"))
        self.assertEqual(decisions[0]["reason"], "not_a_text_message")

    def test_self_check_passes(self):
        import contextlib
        import io
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(adapter.self_check(), 0)


if __name__ == "__main__":
    unittest.main()

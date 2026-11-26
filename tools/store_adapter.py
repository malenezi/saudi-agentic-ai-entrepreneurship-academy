# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""The deterministic front of the online-store recipe: everything that must be decided before a model sees a message.

It checks who sent a webhook, drops a message it has already seen, reads the customer's message out of the
channel's payload, finds the order number the customer typed, and refuses to pass an order's details on unless
the sender's mobile number is the one on the order. It sends nothing and writes nothing to a store.

    python3 tools/store_adapter.py --self-check

STATUS, stated plainly: written from the providers' documentation (SOURCES.md, A254 to A265) and tested against
payloads built from that documentation. It has NOT been run against WhatsApp, Salla or Zid, and it is not wired
into the n8n template. Standard library only.
"""
import argparse
import base64
import hashlib
import hmac
import json
import re
import sys

WINDOW_HOURS = 24            # A256: the customer service window
RETRY_DAYS = 7               # A254: Meta retries a failed delivery for up to seven days
ARABIC_DIGITS = str.maketrans("٠١٢٣٤٥٦٧٨٩۰۱۲۳۴۵۶۷۸۹", "01234567890123456789")


# ---------- who sent this webhook ----------

def _hmac_hex(secret, raw):
    return hmac.new(secret.encode("utf-8"), raw, hashlib.sha256).hexdigest()


def verify_meta(raw, header, app_secret):
    """A255: X-Hub-Signature-256 is 'sha256=' + HMAC-SHA256 of the raw body, keyed with the app secret."""
    if not (app_secret and header and header.startswith("sha256=")):
        return False
    return hmac.compare_digest(header[7:].strip().lower(), _hmac_hex(app_secret, raw))


def meta_challenge(query, verify_token):
    """A255: answer the verification GET with 200 and hub.challenge, or 403."""
    if verify_token and query.get("hub.mode") == "subscribe" and hmac.compare_digest(
            str(query.get("hub.verify_token", "")), verify_token):
        return 200, str(query.get("hub.challenge", ""))
    return 403, ""


def verify_salla(raw, signature, secret):
    """A259: X-Salla-Signature under the Signature strategy; the page's examples compute a hex HMAC-SHA256."""
    if not (secret and signature):
        return False
    return hmac.compare_digest(signature.strip().lower(), _hmac_hex(secret, raw))


def verify_zid_basic(authorization, username, password):
    """A261: Zid sends 'Authorization: Basic base64(username:password)' when both were given at creation."""
    if not (username and password and authorization and authorization.startswith("Basic ")):
        return False
    expected = base64.b64encode(("%s:%s" % (username, password)).encode("utf-8")).decode("ascii")
    return hmac.compare_digest(authorization[6:].strip(), expected)


# ---------- a message seen twice is handled once ----------

class Seen:
    """Message ids already handled. Kept longer than the channel retries, then forgotten."""

    def __init__(self, keep_seconds=(RETRY_DAYS + 1) * 86400, ids=None):
        self.keep, self.ids = keep_seconds, dict(ids or {})

    def first_time(self, message_id, now):
        for old in [key for key, at in self.ids.items() if now - at > self.keep]:
            del self.ids[old]
        if not message_id or message_id in self.ids:
            return False
        self.ids[message_id] = now
        return True


# ---------- reading the channel's payload ----------

def whatsapp_messages(payload):
    """A265: entry[].changes[].value.messages[]. Status notifications carry statuses[] and yield nothing."""
    found = []
    for entry in payload.get("entry") or []:
        for change in entry.get("changes") or []:
            value = change.get("value") or {}
            if change.get("field") != "messages":
                continue
            for message in value.get("messages") or []:
                stamp = str(message.get("timestamp", ""))
                found.append({
                    "id": message.get("id", ""), "sender": str(message.get("from", "")),
                    "timestamp": int(stamp) if stamp.isdigit() else 0, "type": message.get("type", ""),
                    "text": ((message.get("text") or {}).get("body") or "") if message.get("type") == "text" else "",
                    "phone_number_id": (value.get("metadata") or {}).get("phone_number_id", ""),
                })
    return found


# ---------- the number the customer typed ----------

def digits(text):
    return re.sub(r"\D", "", str(text).translate(ARABIC_DIGITS))


def saudi_mobile(number):
    """The nine digits of a Saudi mobile ('5XXXXXXXX') from any common spelling, or '' if it is not one."""
    found = digits(number)
    for prefix in ("00966", "966", "0"):
        if found.startswith(prefix) and len(found) - len(prefix) == 9:
            found = found[len(prefix):]
            break
    return found if len(found) == 9 and found.startswith("5") else ""


def same_mobile(one, other):
    first, second = saudi_mobile(one), saudi_mobile(other)
    return bool(first) and first == second


def mask(number):
    found = digits(number)
    return found[:4] + "*" * max(len(found) - 7, 0) + found[-3:] if len(found) > 7 else "*" * len(found)


def order_references(text):
    """Candidates for an order number in a message, in order, without repeats.

    Numbers of 4 to 12 digits that are not a mobile number (Arabic-Indic digits accepted), and codes of 8 to 12
    letters and digits that hold both (Zid's public order code looks like '4lF4p7HluM', A264). Which of the
    platform's identifiers the customer actually types is NOT settled by the documentation: see the recipe.
    """
    text = str(text).translate(ARABIC_DIGITS)
    found = []
    for token in re.findall(r"[A-Za-z0-9]+", text):
        numeric = token.isdigit() and 4 <= len(token) <= 12 and not saudi_mobile(token)
        code = (8 <= len(token) <= 12 and re.search(r"[A-Za-z]", token) and re.search(r"\d", token))
        if (numeric or code) and token not in found:
            found.append(token)
    return found


def lookup_request(platform, reference):
    """The read-only request that looks one order up by what the customer typed. Described, not sent."""
    if platform == "salla":      # A263: GET /orders accepts reference_id (integer)
        if not reference.isdigit():
            return None
        return {"method": "GET", "path": "/orders", "query": {"reference_id": reference}, "scope": "orders.read"}
    if platform == "zid":        # A264: search_term covers the order code; there is no exact-match code filter
        return {"method": "GET", "path": "/v1/managers/store/orders",
                "query": {"search_term": reference, "page": "1", "per_page": "10"}, "scope": "orders.read"}
    raise ValueError("unknown platform: %s" % platform)


def exact_order(platform, orders, reference):
    """Exactly one order whose own identifier equals the reference, or None. A search is never trusted alone."""
    keys = ("reference_id", "id") if platform == "salla" else ("code", "id", "invoice_number")
    hits = [order for order in orders or [] if any(str(order.get(key, "")) == reference for key in keys)]
    return hits[0] if len(hits) == 1 else None


def customer_mobile(platform, order):
    customer = order.get("customer") or {}
    if platform == "salla":      # A263: customer.mobile_code '+966' and customer.mobile 557777777
        return "%s%s" % (customer.get("mobile_code", ""), customer.get("mobile", ""))
    return str(customer.get("mobile") or customer.get("phone") or "")   # A264 names customer.phone only


# ---------- the reply window ----------

def window_open(last_user_message_at, now, hours=WINDOW_HOURS):
    """A256: free-form replies only within 24 hours of the user's last message; after that, a template."""
    return 0 <= now - last_user_message_at < hours * 3600


# ---------- one inbound webhook, start to finish ----------

def handle(raw, signature, config, seen, find_orders, now):
    """Decide, for each message in one WhatsApp webhook, what may go on to template 1.

    find_orders(request) performs lookup_request's request and returns the platform's list of orders.
    Returns a list of decisions: rejected | ignored | duplicate | handover | forward. Nothing is sent.
    """
    if not verify_meta(raw, signature, config.get("app_secret", "")):
        return [{"decision": "rejected", "reason": "signature"}]
    try:
        payload = json.loads(raw.decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        return [{"decision": "rejected", "reason": "not_json"}]
    platform, decisions = config["platform"], []
    for message in whatsapp_messages(payload):
        base = {"ref": message["id"], "account": mask(message["sender"])}
        if not seen.first_time(message["id"], now):
            decisions.append(dict(base, decision="duplicate", reason="message_id_seen"))
            continue
        if message["type"] != "text" or not message["text"].strip():
            decisions.append(dict(base, decision="handover", reason="not_a_text_message"))
            continue
        forward = {"message": message["text"], "account": message["sender"], "ref": message["id"],
                   "reply_window_open": window_open(message["timestamp"], now)}
        references = order_references(message["text"])
        if len(references) > 1:
            decisions.append(dict(base, decision="handover", reason="more_than_one_order_number"))
            continue
        if references:
            request = lookup_request(platform, references[0])
            order = exact_order(platform, find_orders(request) if request else [], references[0])
            if order is None:
                decisions.append(dict(base, decision="handover", reason="order_not_found_or_ambiguous"))
                continue
            if not same_mobile(message["sender"], customer_mobile(platform, order)):
                decisions.append(dict(base, decision="handover", reason="sender_is_not_the_order_customer"))
                continue
            forward["order"] = order
        decisions.append(dict(base, decision="forward", forward=forward))
    return decisions or [{"decision": "ignored", "reason": "no_messages"}]


def self_check():
    raw = json.dumps({"entry": [{"changes": [{"field": "messages", "value": {
        "metadata": {"phone_number_id": "1"}, "messages": [
            {"id": "wamid.1", "from": "966557777777", "timestamp": "1000", "type": "text",
             "text": {"body": "وين طلبي ٢٠٠٣٤٥"}}]}}]}]}).encode("utf-8")
    config = {"app_secret": "s", "platform": "salla"}
    orders = [{"id": 9, "reference_id": 200345, "customer": {"mobile_code": "+966", "mobile": 557777777}}]
    seen = Seen()
    first = handle(raw, "sha256=" + _hmac_hex("s", raw), config, seen, lambda request: orders, 1500)
    again = handle(raw, "sha256=" + _hmac_hex("s", raw), config, seen, lambda request: orders, 1600)
    forged = handle(raw, "sha256=" + "0" * 64, config, Seen(), lambda request: orders, 1500)
    ok = (first[0]["decision"] == "forward" and again[0]["decision"] == "duplicate"
          and forged[0]["decision"] == "rejected")
    print("self-check: %s (local payloads built from the documentation; no provider was contacted)"
          % ("passed" if ok else "FAILED"))
    return 0 if ok else 1


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--self-check", action="store_true", help="run three local cases and exit")
    args = parser.parse_args(argv)
    if args.self_check:
        return self_check()
    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())

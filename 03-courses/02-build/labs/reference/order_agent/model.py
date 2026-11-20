# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""The model step: read one customer message, return a structured understanding.

Two interchangeable models:

SimModel   A deterministic stand-in. It is NOT a language model. It matches keywords, and
           it knows Saudi dialect terms only when a glossary is placed in its context,
           which imitates a real weakness you will measure in Module 2.5. It lets the
           labs run offline, with identical results for every learner.
HttpModel  Any chat endpoint that follows the OpenAI chat-completions format, local or
           hosted. Results will differ from the simulator; that is the point of testing.

Both return the same dictionary, and the application validates it before acting on it:
    {"intent": str, "order_id": str or None, "city": str or None,
     "urgent": bool, "conditional": bool}
"""
import json
import os
import urllib.request

from .text import find_order_id, normalise

INTENTS = ("order_status", "shipping_question", "cancel", "refund", "address_change", "complaint", "unknown")

# What the simulator "knows" without help: Modern Standard Arabic and common loanwords.
BASE_LEXICON = [
    ("refund", ["استرداد", "استرجاع", "فلوس", "المبلغ", "refund"]),
    ("cancel", ["الغاء", "الغي", "كنسل", "cancel"]),
    ("address_change", ["العنوان", "عنوان", "address"]),
    ("complaint", ["شكوي", "complaint"]),
    ("shipping_question", ["الشحن", "تشحن", "shipping"]),
    ("order_status", ["حاله", "حالة", "اين", "وين طلبي", "تاخر", "تتبع", "status", "update", "order", "track"]),
]
CITIES = {"رياض": "الرياض", "جدة": "جدة", "دمام": "الدمام"}  # matched without the article, so "للرياض" is found
CONDITION_WORDS = ["اذا", "لو ما", "ان لم"]
URGENT_WORDS = ["اليوم", "بكره", "مناسبه", "مناسبة", "عاجل", "ضروري"]


class SimModel:
    """Keyword simulator. `glossary` maps a dialect term to an intent; `rules` is a set of rule names."""

    name = "sim-a"
    calls = 0

    def __init__(self, glossary=None, rules=()):
        self.glossary = {normalise(k): v for k, v in (glossary or {}).items()}
        self.rules = set(rules)

    def extract_order_id(self, text):
        return find_order_id(text)

    def understand(self, message):
        self.calls += 1
        text = normalise(message)
        order_id = self.extract_order_id(text)
        intent = "unknown"
        for name, words in BASE_LEXICON:
            if any(normalise(w) in text for w in words):
                intent = name
                break
        if intent == "unknown":
            for term, name in self.glossary.items():
                if term in text:
                    intent = name
                    break
        if intent in ("unknown", "shipping_question") and order_id:
            intent = "order_status"
        conditional = False
        if intent == "cancel" and "conditional_cancel" in self.rules:
            conditional = any(normalise(w) in text for w in CONDITION_WORDS)
        urgent = conditional and any(normalise(w) in text for w in URGENT_WORDS)
        city = next((v for k, v in CITIES.items() if normalise(k) in text), None)
        return {"intent": intent, "order_id": order_id, "city": city, "urgent": urgent, "conditional": conditional}


class SimModelB(SimModel):
    """A weaker stand-in for the comparison in Module 2.4: it copies the word before the number into the tool input."""

    name = "sim-b"

    def extract_order_id(self, text):
        order_id = find_order_id(text)
        if order_id and ("رقم " + order_id) in text:
            return "رقم " + order_id
        return order_id


class HttpModel:
    """A chat-completions endpoint. Configure with environment variables; never put a key in a file.

        SAAEA_MODEL_BASE_URL   for example http://localhost:11434/v1 for a local Ollama server
        SAAEA_MODEL_NAME       the model name the endpoint expects
        SAAEA_MODEL_API_KEY    optional for local runtimes
    """

    calls = 0

    def __init__(self, instructions, glossary=None, base_url=None, name=None, api_key=None, timeout=60):
        self.base_url = (base_url or os.environ.get("SAAEA_MODEL_BASE_URL", "")).rstrip("/")
        self.name = name or os.environ.get("SAAEA_MODEL_NAME", "")
        self.api_key = api_key or os.environ.get("SAAEA_MODEL_API_KEY", "")
        self.timeout = timeout
        self.system = instructions
        if glossary:
            self.system += "\n\nمصطلحات العملاء:\n" + "\n".join("- %s: %s" % kv for kv in glossary.items())
        if not self.base_url or not self.name:
            raise ValueError("Set SAAEA_MODEL_BASE_URL and SAAEA_MODEL_NAME, or use the simulator.")

    def understand(self, message):
        self.calls += 1
        body = json.dumps({"model": self.name, "temperature": 0, "messages": [
            {"role": "system", "content": self.system},
            {"role": "user", "content": "<customer_message>\n%s\n</customer_message>" % message}]}).encode("utf-8")
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = "Bearer " + self.api_key
        request = urllib.request.Request(self.base_url + "/chat/completions", data=body, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                content = json.load(response)["choices"][0]["message"]["content"]
            start, end = content.find("{"), content.rfind("}")
            return json.loads(content[start:end + 1])
        except Exception as error:  # a model failure must never crash the agent or act on its own
            return {"intent": "unknown", "error": type(error).__name__}

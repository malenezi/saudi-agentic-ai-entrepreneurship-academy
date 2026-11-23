# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Point 9 of the operating standard, applied before a message leaves the computer.

Every agent asks the founder not to paste personal data or secrets. This module looks at what the
founder is about to send and names what looks like one, so that the founder decides before it is
sent. It matches shapes, so it misses what has no fixed shape (a name, an address, a customer's
complaint) and it sometimes points at something harmless. The value it found is never printed in full.
"""
import re

from .checks import digits

PATTERNS = [
    ("a private key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("an access key or token", re.compile(r"\b(?:sk|pk|rk|ghp|gho|ghs|glpat|xox[abpr])[-_][A-Za-z0-9_\-]{16,}|\bAKIA[0-9A-Z]{16}\b")),
    ("a Saudi IBAN", re.compile(r"\bSA\d{2}(?:[ -]?[0-9A-Z]{4}){5}\b", re.I)),
    ("an email address", re.compile(r"\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b")),
    ("a Saudi mobile number", re.compile(r"(?<!\d)(?:\+966|00966|966|0)5\d{8}(?!\d)")),
    ("a ten-digit number starting with 1 or 2 (a national ID or residence number has this shape; so does a commercial registration number)",
     re.compile(r"(?<!\d)[12]\d{9}(?!\d)")),
]
CARD = re.compile(r"(?<!\d)(?:\d[ -]?){13,19}(?!\d)")
LONG_TOKEN = re.compile(r"\b(?=[A-Za-z0-9_\-]*\d)(?=[A-Za-z0-9_\-]*[A-Za-z])[A-Za-z0-9_\-]{40,}\b")


def _luhn(number):
    total = 0
    for index, digit in enumerate(reversed(number)):
        value = int(digit) * (2 if index % 2 else 1)
        total += value - 9 if value > 9 else value
    return total % 10 == 0


def mask(value):
    value = value.strip()
    return value[:2] + "…" + value[-2:] if len(value) > 6 else "…"


def scan(text):
    """What looks like personal data or a secret: a list of (what it looks like, masked sample), without repeats."""
    text, found, taken = digits(text), [], []

    def add(kind, match):
        if not any(a < match.end() and match.start() < b for a, b in taken):
            taken.append((match.start(), match.end()))
            found.append((kind, mask(match.group(0))))

    for kind, pattern in PATTERNS:
        for match in pattern.finditer(text):
            add(kind, match)
    for match in CARD.finditer(text):
        number = re.sub(r"[ -]", "", match.group(0))
        if 13 <= len(number) <= 19 and _luhn(number):
            add("a payment card number", match)
    for match in LONG_TOKEN.finditer(text):
        add("a long random string (a key or token has this shape)", match)
    return found

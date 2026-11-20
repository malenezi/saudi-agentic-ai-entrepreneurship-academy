# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Arabic text helpers used before any matching or tool call."""
import re

_TASHKEEL = re.compile("[ً-ْـ]")
_ALEF = str.maketrans("أإآى", "اااي")
_ARABIC_DIGITS = str.maketrans("٠١٢٣٤٥٦٧٨٩۰۱۲۳۴۵۶۷۸۹", "01234567890123456789")
ORDER_ID = re.compile(r"(?<!\d)\d{5}(?!\d)")


def normalise(text):
    """Lower-case Latin, drop diacritics and tatweel, unify alef and final ya."""
    return _TASHKEEL.sub("", text).translate(_ALEF).lower()


def western_digits(text):
    """Arabic-Indic and Persian digits to 0-9. Done in code, never left to the model."""
    return text.translate(_ARABIC_DIGITS)


def find_order_id(text):
    """The first standalone five-digit run, or None."""
    match = ORDER_ID.search(text)
    return match.group(0) if match else None


def mask_phone(phone):
    """Keep the last two digits only, for logs."""
    return "*" * max(len(phone) - 2, 0) + phone[-2:]

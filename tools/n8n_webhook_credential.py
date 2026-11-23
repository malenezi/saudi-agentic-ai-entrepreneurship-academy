#!/usr/bin/env python3
# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Make the Header Auth credential the workflows' Webhook nodes ask for.

    python3 tools/n8n_webhook_credential.py                     # writes saaea-webhook-credential.json
    python3 tools/n8n_webhook_credential.py --out /tmp/c.json
    npx n8n import:credentials --input=saaea-webhook-credential.json
    rm saaea-webhook-credential.json

The file holds a new random token in plain text: import it, then delete it. n8n keeps the
credential encrypted. The token is printed once; send it in the X-SAAEA-Token header.
Running this again makes a different token, and importing it replaces the old one.
You can also create the credential in the editor (Webhook node, Credential for Header Auth).
Standard library only.
"""
import argparse
import json
import os
import secrets
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_n8n_workflows import CREDENTIAL, TOKEN_HEADER  # noqa: E402

DEFAULT = "saaea-webhook-credential.json"


def credential(token):
    reference = CREDENTIAL["httpHeaderAuth"]
    return [{"id": reference["id"], "name": reference["name"], "type": "httpHeaderAuth",
             "data": {"name": TOKEN_HEADER, "value": token}}]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--out", default=DEFAULT)
    out = parser.parse_args(argv).out
    if os.path.exists(out):
        print("error: %s exists. Delete it or choose another --out." % out)
        return 1
    token = secrets.token_urlsafe(32)
    with os.fdopen(os.open(out, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600), "w", encoding="utf-8") as f:
        json.dump(credential(token), f)
    print("Wrote %s (plain text: import it, then delete it)." % out)
    print("  npx n8n import:credentials --input=%s" % out)
    print("Send this header with every request:")
    print("  %s: %s" % (TOKEN_HEADER, token))
    return 0


if __name__ == "__main__":
    sys.exit(main())

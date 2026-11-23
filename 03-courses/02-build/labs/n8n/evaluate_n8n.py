#!/usr/bin/env python3
# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Score the n8n order-enquiry agent on the lab's test set, with the same rules as Module 2.5.

    python3 03-courses/02-build/labs/n8n/evaluate_n8n.py
    python3 03-courses/02-build/labs/n8n/evaluate_n8n.py --cases data/heldout.json
    python3 03-courses/02-build/labs/n8n/evaluate_n8n.py --base http://localhost:5678 --failures failures.csv

It posts every case to the workflow's production webhook and checks the answer with the
reference evaluator (labs/reference/order_agent/evaluate.py), so the numbers mean the same
thing in both tracks. The workflow must be imported, published and running, and its webhook
asks for a token: pass it with --token, or set SAAEA_WEBHOOK_TOKEN once in the terminal.
Standard library only.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
REFERENCE = os.path.join(os.path.dirname(HERE), "reference")
sys.path.insert(0, REFERENCE)

from order_agent.evaluate import first_wrong_step, load, report, write_failures  # noqa: E402
from order_agent.tools import Store  # noqa: E402


def main(argv=None):
    parser = argparse.ArgumentParser(description="Evaluate the n8n order-enquiry agent on a test set")
    parser.add_argument("--base", default="http://localhost:5678", help="where n8n is running")
    parser.add_argument("--cases", default="data/cases.json", help="relative to labs/reference")
    parser.add_argument("--name", default="n8n workflow, as configured")
    parser.add_argument("--failures", help="write failed cases to this CSV file")
    parser.add_argument("--token", default=os.environ.get("SAAEA_WEBHOOK_TOKEN", ""),
                        help="the webhook token; default: the SAAEA_WEBHOOK_TOKEN environment variable")
    args = parser.parse_args(argv)
    if not args.token:
        print("The webhook asks for a token. Pass --token, or set SAAEA_WEBHOOK_TOKEN (see the lab, step 1).")
        return 2
    url = args.base.rstrip("/") + "/webhook/saaea-order-agent"
    store = Store(os.path.join(REFERENCE, "data", "orders.json"), os.path.join(REFERENCE, "data", "policy-v2-approved-only.json"))
    rows = []
    for case in load(args.cases)["cases"]:
        body = json.dumps({"message": case["message"], "account": case["account"]}).encode("utf-8")
        request = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json", "X-SAAEA-Token": args.token})
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                result = json.load(response)
        except urllib.error.HTTPError as error:
            if error.code not in (403, 500):
                raise
            print("The workflow refused the request (HTTP %d). %s" % (error.code, "The token is not the one in n8n's credential."
                  if error.code == 403 else "Has the Header Auth credential been created in n8n? (see the lab, step 1)"))
            return 2
        except (urllib.error.URLError, ValueError) as error:
            print("Could not reach the workflow at %s (%s).\nIs n8n running, and is the workflow published?" % (url, error))
            return 2
        rows.append((case, result, first_wrong_step(case, result, store)))
    report(rows, {"name": args.name, "launch_rule": {"overall_percent": 85}})
    if args.failures:
        write_failures(rows, args.failures)
        print("failure log written to", args.failures)
    return 0


if __name__ == "__main__":
    sys.exit(main())

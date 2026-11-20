# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Send one message to the agent and print the full trace.

    python3 -m order_agent.cli "ما حالة طلبي رقم 84522؟"
    python3 -m order_agent.cli "وين طلبي 84530" --account 0500000001 --config config/stage-0-baseline.json
"""
import argparse
import json

from .evaluate import build_agent, load


def main(argv=None):
    parser = argparse.ArgumentParser(description="One message through the order-enquiry agent")
    parser.add_argument("message")
    parser.add_argument("--account", default="0500000001", help="the verified phone number of the sender (test data)")
    parser.add_argument("--notes", default="", help="untrusted free text, such as an order-notes field")
    parser.add_argument("--config", default="config/stage-3-cycle-2.json")
    parser.add_argument("--approve", help="name of the person approving any pending level B action")
    args = parser.parse_args(argv)
    agent = build_agent(load(args.config))
    result = agent.handle(args.message, args.account, args.notes)
    if args.approve:
        result["approved"] = [agent.approve(p, args.approve) for p in result["pending_approval"]]
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

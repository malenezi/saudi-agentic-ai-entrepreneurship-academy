# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""The four tools of the worked example. There is no tool to cancel, refund or change an address."""
import json
import re

VALID_ORDER_ID = re.compile(r"^\d{5}$")


class ToolInputError(ValueError):
    """The model asked for a tool with input the contract does not allow."""


class Store:
    """Test data standing in for the shop's systems. Never connect a lab to a production system."""

    def __init__(self, orders_path, policy_path):
        with open(orders_path, encoding="utf-8") as f:
            self.orders = json.load(f)["orders"]
        with open(policy_path, encoding="utf-8") as f:
            self.policy = json.load(f)
        self.tickets = {}

    # Level A: read only.
    def get_order_status(self, order_id):
        if not isinstance(order_id, str) or not VALID_ORDER_ID.match(order_id):
            raise ToolInputError("order_id must be five digits, got %r" % (order_id,))
        order = self.orders.get(order_id)
        if order is None:
            return None
        return {"order_id": order_id, "status": order["status"], "days_since_update": order["days_since_update"]}

    def owner_of(self, order_id):
        order = self.orders.get(order_id)
        return order["account"] if order else None

    # Level A: read the policy. Returns the FIRST entry for the city, in file order.
    def get_shipping_policy(self, city):
        for version in self.policy["versions"]:
            if city in version["delivery"]:
                return {"city": city, "duration": version["delivery"][city], "approved_on": version.get("approved_on")}
        return None

    def followup_after_days(self):
        return self.policy["followup_after_days"]

    # Level B: writes. Called only after a person approves. One ticket per order.
    def create_followup_ticket(self, order_id, approved_by):
        if not approved_by:
            raise PermissionError("create_followup_ticket needs a named approver")
        if order_id in self.tickets:
            return self.tickets[order_id]
        self.tickets[order_id] = {"ticket": "T-%s" % order_id, "approved_by": approved_by}
        return self.tickets[order_id]

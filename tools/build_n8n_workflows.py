#!/usr/bin/env python3
# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Build the importable n8n workflows from their sources.

    python3 tools/build_n8n_workflows.py            # write every workflow
    python3 tools/build_n8n_workflows.py --check    # exit 1 if a built file is out of date

Each workflow has a source folder with `spec.json` (name, webhook path, the Config node's
values) and the JavaScript of its Code nodes. The JavaScript is kept in files so it can be
read, reviewed and tested without n8n (`node tools/n8n_harness.js`). Every workflow has
the same shape:

    Webhook -> Config -> Prepare -> Real model? -> Simulated model ------------------------------------------> Decide -> Respond
                                                -> Model (HTTP) -> Check model output -> Retry model? -> Decide
                                                                                                      -> Model retry (HTTP) -> Decide

An answer from the HTTP model that cannot be read as one JSON object is repaired where that changes no meaning, and
otherwise asked for once more. Decide reads whatever comes back and decides; an unreadable answer never acts.

The model proposes and the Decide node decides: every limit is enforced there, in code.
Every Webhook node asks for a header token (n8n's Header Auth). The built file names the credential
and holds no secret: until a credential with that id exists in n8n, the webhook answers nothing.
`tools/n8n_webhook_credential.py` makes one.
Standard library only. Node and n8n are not needed to build.
"""
import json
import os
import re
import sys
import uuid

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMMON = os.path.join(ROOT, "05-agentic-ai-lab", "agent-templates", "workflows", "src", "common")
TEMPLATES = os.path.join(ROOT, "05-agentic-ai-lab", "agent-templates", "workflows")
SOURCES = [os.path.join(ROOT, "03-courses", "02-build", "labs", "n8n", "src")] + sorted(
    os.path.join(TEMPLATES, "src", d) for d in os.listdir(os.path.join(TEMPLATES, "src"))
    if d != "common" and os.path.isfile(os.path.join(TEMPLATES, "src", d, "spec.json")))
NAMESPACE = uuid.UUID("5aaea000-0000-4000-8000-000000000009")
# The Header Auth credential every Webhook node refers to. A reference, not a secret.
CREDENTIAL = {"httpHeaderAuth": {"id": "saaeaWebhookTok1", "name": "SAAEA webhook token"}}
TOKEN_HEADER = "X-SAAEA-Token"
AUTH_NOTE = ("\n\n**The webhook needs a token.** It answers nothing until a Header Auth credential exists: open the Webhook node and create one "
             "(Name `%s`, Value a long random string), or run `python3 tools/n8n_webhook_credential.py`. Send the token in that header." % TOKEN_HEADER)
LICENCE = "// Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors. Apache-2.0.\n"


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def code(folder, name):
    """A Code node's JavaScript, with `//#include x` replaced by common/x.js."""
    path = os.path.join(folder, name)
    if not os.path.exists(path):
        path = os.path.join(COMMON, name)
    text = read(path)
    return LICENCE + re.sub(r"^//#include (\w+)$", lambda m: read(os.path.join(COMMON, m.group(1) + ".js")).rstrip(), text, flags=re.M)


def config_of(folder, spec):
    config = dict(spec["config"])
    for key, source in spec.get("config_files", {}).items():
        text = read(os.path.normpath(os.path.join(folder, source["path"])))
        value = json.loads(text) if source["path"].endswith(".json") else text.strip()
        config[key] = value[source["key"]] if source.get("key") else value
    return config


def build(folder):
    spec = json.loads(read(os.path.join(folder, "spec.json")))
    key = spec["webhook_path"]
    uid = lambda name: str(uuid.uuid5(NAMESPACE, key + "/" + name))
    nodes, connections = [], {}

    def node(name, kind, version, position, parameters, **extra):
        nodes.append(dict({"parameters": parameters, "id": uid(name), "name": name, "type": kind,
                           "typeVersion": version, "position": position}, **extra))

    def connect(source, target, output=0):
        outputs = connections.setdefault(source, {"main": []})["main"]
        while len(outputs) <= output:
            outputs.append([])
        outputs[output].append({"node": target, "type": "main", "index": 0})

    js = lambda name, file, pos: node(name, "n8n-nodes-base.code", 2, pos, {"jsCode": code(folder, file)})
    node("Read me first", "n8n-nodes-base.stickyNote", 1, [-80, -320],
         {"content": spec["note"] + AUTH_NOTE, "height": 280, "width": 1180})
    node("Webhook", "n8n-nodes-base.webhook", 2, [0, 0],
         {"httpMethod": "POST", "path": key, "authentication": "headerAuth", "responseMode": "responseNode", "options": {}},
         webhookId=uid("webhook-id"), credentials=CREDENTIAL)
    node("Config", "n8n-nodes-base.set", 3.4, [220, 0],
         {"mode": "raw", "jsonOutput": json.dumps(config_of(folder, spec), ensure_ascii=False, indent=2), "options": {}})
    js("Prepare", "prepare.js", [440, 0])
    node("Real model?", "n8n-nodes-base.if", 2.2, [660, 0], {
        "conditions": {"options": {"caseSensitive": True, "leftValue": "", "typeValidation": "strict", "version": 2},
                       "conditions": [{"id": uid("condition"), "leftValue": "={{ $json.route }}", "rightValue": "http",
                                       "operator": {"type": "string", "operation": "equals"}}],
                       "combinator": "and"},
        "options": {}})
    node("Model (HTTP)", "n8n-nodes-base.httpRequest", 4.2, [880, -100],
         {"method": "POST", "url": "={{ $json.model_url }}", "sendBody": True, "specifyBody": "json",
          "jsonBody": "={{ JSON.stringify($json.request_body) }}", "options": {"timeout": 60000}},
         onError="continueRegularOutput")
    js("Simulated model", "sim.js", [880, 140])
    js("Check model output", "check_model.js", [1100, -100])
    node("Retry model?", "n8n-nodes-base.if", 2.2, [1320, -100], {
        "conditions": {"options": {"caseSensitive": True, "leftValue": "", "typeValidation": "strict", "version": 2},
                       "conditions": [{"id": uid("retry-condition"), "leftValue": "={{ $json.retry }}", "rightValue": "",
                                       "operator": {"type": "boolean", "operation": "true", "singleValue": True}}],
                       "combinator": "and"},
        "options": {}})
    node("Model retry (HTTP)", "n8n-nodes-base.httpRequest", 4.2, [1540, -200],
         {"method": "POST", "url": "={{ $json.model_url }}", "sendBody": True, "specifyBody": "json",
          "jsonBody": "={{ JSON.stringify($json.request_body) }}", "options": {"timeout": 60000}},
         onError="continueRegularOutput")
    js("Decide", "decide.js", [1760, 0])
    node("Respond", "n8n-nodes-base.respondToWebhook", 1.1, [1980, 0], {"respondWith": "firstIncomingItem", "options": {}})
    for source, target in [("Webhook", "Config"), ("Config", "Prepare"), ("Prepare", "Real model?"),
                           ("Model (HTTP)", "Check model output"), ("Check model output", "Retry model?"),
                           ("Model retry (HTTP)", "Decide"), ("Simulated model", "Decide"), ("Decide", "Respond")]:
        connect(source, target)
    connect("Real model?", "Model (HTTP)", 0)
    connect("Real model?", "Simulated model", 1)
    connect("Retry model?", "Model retry (HTTP)", 0)
    connect("Retry model?", "Decide", 1)
    if os.path.exists(os.path.join(folder, "approve.js")):
        node("Approval webhook", "n8n-nodes-base.webhook", 2, [0, 320],
             {"httpMethod": "POST", "path": key + "-approve", "authentication": "headerAuth", "responseMode": "responseNode", "options": {}},
             webhookId=uid("approve-webhook-id"), credentials=CREDENTIAL)
        js("Approve", "approve.js", [440, 320])
        node("Respond to approver", "n8n-nodes-base.respondToWebhook", 1.1, [660, 320],
             {"respondWith": "firstIncomingItem", "options": {}})
        connect("Approval webhook", "Approve")
        connect("Approve", "Respond to approver")
    # A stable id lets `n8n import:workflow` work from the command line; importing again replaces the same workflow.
    workflow = {"id": uuid.uuid5(NAMESPACE, key).hex[:16], "name": spec["name"], "nodes": nodes, "connections": connections, "active": False,
                "settings": {"executionOrder": "v1"}, "pinData": {}, "meta": {"templateCredsSetupCompleted": True}}
    out = os.path.normpath(os.path.join(folder, spec["output"]))
    return out, json.dumps(workflow, ensure_ascii=False, indent=2) + "\n"


def main(argv):
    stale = []
    for folder in SOURCES:
        out, text = build(folder)
        if "--check" in argv:
            if not os.path.exists(out) or read(out) != text:
                stale.append(os.path.relpath(out, ROOT))
        else:
            with open(out, "w", encoding="utf-8") as f:
                f.write(text)
            print("built", os.path.relpath(out, ROOT))
    if stale:
        print("out of date, run tools/build_n8n_workflows.py:", ", ".join(stale))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

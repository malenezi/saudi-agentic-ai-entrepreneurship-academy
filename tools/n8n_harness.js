#!/usr/bin/env node
// Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
// Licensed under the Apache License, Version 2.0
//
// Run a built workflow's Code nodes without n8n, for tests and for reading along.
//
//   node tools/n8n_harness.js <workflow.n8n.json> <requests.json> [config-overrides.json]
//
// requests.json: a list of request bodies, or an object with a "cases" list. A body may
// carry "_model_response" to stand in for what the HTTP model node would return, "_model_retry_response" for its second answer when the first cannot be read, "_config" to
// change Config values for that request, and "_approve" to call the approval flow instead. Prints one result per request as JSON.
// This follows the workflow's fixed shape (see tools/build_n8n_workflows.py). It is not n8n:
// it proves the logic of the nodes, and the import itself is tested in n8n separately.
const fs = require('fs');
const [workflowPath, requestsPath, overridesPath] = process.argv.slice(2);
const workflow = JSON.parse(fs.readFileSync(workflowPath, 'utf8'));
const loaded = JSON.parse(fs.readFileSync(requestsPath, 'utf8'));
const requests = Array.isArray(loaded) ? loaded : loaded.cases;
const node = (name) => workflow.nodes.find((n) => n.name === name);
const config = Object.assign(JSON.parse(node('Config').parameters.jsonOutput),
  overridesPath ? JSON.parse(fs.readFileSync(overridesPath, 'utf8')) : {});
const staticData = {};

function run(name, input, outputs) {
  const $ = (other) => {
    if (!(other in outputs)) throw new Error(`${name} reads "${other}", which has not run in this flow`);
    return { first: () => ({ json: outputs[other] }) };
  };
  const body = new Function('$input', '$', '$getWorkflowStaticData', node(name).parameters.jsCode);
  const items = body({ first: () => ({ json: input }), all: () => [{ json: input }] }, $, () => staticData);
  return JSON.parse(JSON.stringify(items[0].json));
}

const results = requests.map((request) => {
  const { _model_response: modelResponse, _model_retry_response: retryResponse, _approve: approve, _config: caseConfig, expect, ...body } = request;
  const outputs = { Webhook: { body }, Config: Object.assign({}, config, caseConfig || {}) };
  if (approve) return run('Approve', { body: approve }, {}); // its own flow: no other node has run
  outputs.Prepare = run('Prepare', outputs.Config, outputs);
  const model = outputs.Prepare.route === 'http'
    ? (modelResponse === undefined ? { error: { message: 'no endpoint in the harness' } } : modelResponse)
    : run('Simulated model', outputs.Prepare, outputs);
  if (outputs.Prepare.route !== 'http') return run('Decide', model, outputs);
  outputs['Check model output'] = run('Check model output', model, outputs);
  if (!outputs['Check model output'].retry) return run('Decide', outputs['Check model output'], outputs);
  return run('Decide', retryResponse === undefined ? { error: { message: 'no endpoint in the harness' } } : retryResponse, outputs);
});
process.stdout.write(JSON.stringify(results, null, 1) + '\n');

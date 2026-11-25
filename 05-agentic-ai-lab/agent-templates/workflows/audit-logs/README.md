# Audit logs of live runs

Logs written by [`tools/reality_run.py`](../README.md) against a workflow running inside n8n. One line per request; the first line describes the run. No message and no reply is in these files, only their fingerprints.

| File | What ran | Result |
|---|---|---|
| [`n8n-simulator-store-85.jsonl`](n8n-simulator-store-85.jsonl) | Template 1 with the invented store's Config, inside n8n 2.35.7 on 25 November 2026, keyword simulator, the store's 85 messages | 73 pass, 8 safe misses, 4 acted alone (D-009, D-053, D-067, D-083); latency p50 105 ms, p95 146 ms |
| [`n8n-simulator-failures-30.jsonl`](n8n-simulator-failures-30.jsonl) | The same workflow, the thirty failure cases | 16 pass, 6 degraded, 8 acted alone; latency p50 108 ms, p95 124 ms |

```bash
python3 tools/reality_run.py report 05-agentic-ai-lab/agent-templates/workflows/audit-logs/n8n-simulator-store-85.jsonl
```

**What these show.** The figures over HTTP inside n8n are the figures the Code nodes give outside it: the import, the webhook token and the response node add nothing and lose nothing. **What they do not show.** A language model: the model step is the keyword simulator. The latency is that of a workflow with no model call, on one machine with n8n and the runner side by side; it says nothing about a model's or a channel's delay. The store, its orders and every message are invented.

# دليل حوكمة الوكلاء الأذكياء في المملكة
# Saudi Agentic AI Governance Playbook

Version 0.1 · Last reviewed 16 November 2026 · Academy practice, not a legal requirement

<div dir="rtl">

## لماذا دليل خاص بالوكلاء؟

الوكيل الذي **يقترح** إجراء يختلف في مخاطره عن الوكيل الذي **ينفّذ**: يصدر دفعة، أو يعدّل سجلاً، أو يراسل عميلاً. هذا الدليل يحدد تسعة ضوابط تجعل الوكيل قابلاً للثقة والبيع، وكلها تُفرض خارج النموذج.

**المبدأ:** الاستدلال احتمالي، والصلاحية حتمية.

</div>

An agent that recommends has a different risk profile from one that acts: issues a payment, changes a record or messages a customer. This playbook sets nine controls. All are enforced outside the model.

## Step 0: classify the agent

| Level | The agent... | Examples | Minimum governance |
|---|---|---|---|
| **1 Informs** | Answers from approved content | FAQ assistant | Disclosure, approved sources, human fallback |
| **2 Recommends** | Proposes an action a person takes | Lead scoring, tender fit | Level 1 plus logged reasoning and a named reviewer |
| **3 Acts, reversible** | Takes actions that can be undone | Booking, drafting, record updates | Level 2 plus allow-lists, limits, action log, kill switch |
| **4 Acts, consequential** | Moves money, changes rights, sends binding communications | Refunds, payments, approvals | Level 3 plus human approval, impact assessment, incident plan |
| **Not for agents alone** | Decisions reserved to licensed professionals or with serious effects on individuals | Diagnosis, legal advice, credit denial | A qualified person decides; the agent assists at most |

Record the level and the reason for every agent. Raise the level if the agent handles sensitive data or serves a regulated sector.

## The nine controls

### 1. Agent identity and authorization
- Every agent has its own identity and credentials. No shared service accounts.
- Credentials are scoped to the task, rotated, and revocable in one step.
- Each agent has a named human owner.

### 2. Tool and API permissions
- An allow-list of tools per agent, with allowed parameters.
- Read-only by default; write access granted per action.
- Tool calls are validated before execution: format, value ranges, recipient.

### 3. Financial transaction restrictions
- Agents hold no payment credentials unless the product requires it.
- Any movement of money needs human approval at levels 3 and 4, with value thresholds.
- Daily and per-transaction caps enforced by the payment layer.

### 4. Human approval thresholds
- Written in the [human oversight matrix](../compliance-toolkit/human-oversight-matrix.md): autonomous, notify, approve, forbidden.
- Approvals identify who approved and when; timeouts default to "do nothing".

### 5. Memory and data retention
- State what the agent remembers, about whom, and for how long.
- Deletion reaches conversation logs, long-term memory, vector stores and backups.
- No personal data in long-term memory without a purpose recorded in the [PDPL self-assessment](../compliance-toolkit/pdpl-self-assessment.md).

### 6. Prompt injection and tool poisoning
- Everything the agent reads (messages, documents, web pages, tool outputs) is data, never instruction.
- Authority does not depend on the model resisting persuasion.
- Third-party tools and connectors come from trusted sources with pinned versions; review what each can access.
- Keep an injection test set in Arabic and English and run it on every change.

### 7. Audit trails and accountability
- Log every tool call: what, when, inputs, result, and the approval if one was needed.
- Keep a change log for model, instructions and tools, each with the evaluation result after the change.
- Logs avoid unnecessary personal data and have restricted access.

### 8. Safe execution and rollback
- Prefer reversible actions; confirm before irreversible ones.
- Caps on steps, spend and action rate per task.
- A tested kill switch that routes work to a person.
- A documented way to undo each reversible action.

### 9. Third-party and multi-agent dependencies
- Assess each provider with the [provider assessment](../compliance-toolkit/third-party-provider-assessment.md).
- When agents hand work to each other, the receiving agent treats the handoff as untrusted input and keeps its own limits.
- Pin model versions; re-run the evaluation set before upgrading.
- Have a fallback for the main provider.

## Graduated autonomy

Start an agent one level below where you intend it to operate. Promote it only when all three hold:

1. Success rate on the evaluation set has been stable over several weeks.
2. Safety and authority test cases pass at 100%.
3. Sampled production reviews show no unhandled error class.

Demote immediately after any incident and promote again only when the cause is fixed and added to the test set.

## One-page governance record

| Field | Entry |
|---|---|
| Agent name and purpose | |
| Level (1 to 4) and reason | |
| Named owner | |
| Tools and permissions | |
| Approval thresholds | |
| Data handled and retention | |
| Model, version and processing location | |
| Evaluation result and date | |
| Kill switch and rollback | |
| Last review | |

## How this relates to Saudi instruments

| Control | Related instrument | Status |
|---|---|---|
| Disclosure, accountability, fairness | SDAIA AI Ethics Principles | Official guidance |
| Risk classification and register | National AI Risk Management Framework | Official guidance |
| Memory, retention, transfers | PDPL and regulations | Binding |
| Identity, logging, third parties | NCA controls applicable to your entity | Binding for those in scope |
| Agent-specific security | NCA AI Cybersecurity Guidelines | **Draft**, non-binding |

This playbook is the academy's recommended practice. It is consistent with the direction of those instruments but is not a statement of what any of them requires. Check each at source.

<div dir="rtl">

## الخلاصة العملية

1. صنّف كل وكيل من 1 إلى 4 واكتب السبب.
2. أعطِ كل وكيل هوية خاصة وأقل صلاحية تكفيه ومالكاً مسمّى.
3. لا مال يتحرك ولا إجراء غير قابل للتراجع دون موافقة بشرية.
4. سجّل كل استدعاء أداة.
5. ابدأ بمستوى استقلالية أدنى، وارفعه بالدليل.

</div>

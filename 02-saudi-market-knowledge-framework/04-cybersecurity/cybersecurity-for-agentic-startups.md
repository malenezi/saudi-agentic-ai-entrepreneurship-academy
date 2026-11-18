# الأمن السيبراني للمشاريع الوكيلية
# Cybersecurity for agentic startups

Last reviewed: 16 November 2026 · Educational, not legal advice

النسخة العربية: [cybersecurity-for-agentic-startups.ar.md](cybersecurity-for-agentic-startups.ar.md)

<div dir="rtl">

## الخلاصة

الهيئة الوطنية للأمن السيبراني تضع الضوابط والإرشادات في المملكة. ضوابطها الأساسية ملزمة للجهات الداخلة في نطاقها، وهذه الجهات تنقل متطلباتها إلى مورّديها بالعقود. فإذا أردت أن تبيع لجهة حكومية أو شبه حكومية أو لقطاع حساس، فستُسأل عن أمنك السيبراني قبل أن تُسأل عن منتجك.

وللوكلاء مخاطر خاصة: حقن التعليمات، تسرب البيانات عبر الأدوات، والصلاحيات الواسعة.

</div>

---

## 1. What exists

| Instrument | Issuer | Relevance |
|---|---|---|
| Essential Cybersecurity Controls (ECC) | NCA | Baseline controls for government and critical-infrastructure entities; expected of their vendors through contracts |
| Data Cybersecurity Controls | NCA | Protection of data through its lifecycle |
| Cloud Cybersecurity Controls | NCA | For cloud providers and tenants within scope |
| AI Cybersecurity Guidelines (AICG-1:2026) | NCA | **Draft** published for consultation, 5 July to 5 August 2026, described as non-binding guidelines. Four domains: governance, defence, resilience, third-party. Confirm final status before relying on it |

Get current versions from nca.gov.sa. Version numbers change; cite the one in force when you answer a buyer.

## 2. Threats specific to agents

| Threat | How it happens | First control |
|---|---|---|
| Prompt injection | Text in a message, document or web page instructs the agent to ignore its rules | Treat all external content as data; enforce permissions outside the model; test with an injection set |
| Data leakage through tools | The agent sends personal or confidential data to a tool or recipient that should not have it | Allow-lists for tools and recipients; redaction; output checks |
| Excessive permissions | The agent's credentials can do far more than the task needs | Least privilege; scoped API keys; read-only by default |
| Unsafe actions | The agent pays, deletes or sends without a check | Approval gates; value limits; confirmation steps |
| Compromised integration | A connected tool or third-party server behaves maliciously | Use trusted sources; pin versions; review what each integration can access |
| Secrets exposure | API keys in prompts, workflows, logs or repositories | Secrets manager; never in prompts; rotate keys |
| Memory poisoning | False information stored in long-term memory influences later actions | Validate what is written to memory; allow review and deletion |
| Cost exhaustion | Loops or abuse drive up usage bills | Budgets, rate limits, loop caps, alerts |

## 3. Baseline for a startup

**Access**
- [ ] Multi-factor authentication on every admin account
- [ ] Separate credentials for development and production
- [ ] Scoped, rotated API keys kept in a secrets manager

**Agent**
- [ ] Tool and recipient allow-lists enforced outside the model
- [ ] Approval gates for financial, irreversible and external-communication actions
- [ ] Maximum steps, spend and actions per task
- [ ] Kill switch tested

**Data**
- [ ] Encryption in transit and at rest
- [ ] Logs without unnecessary personal data; restricted access
- [ ] Backups and a tested restore

**Operations**
- [ ] Action log: who or what did what, when and why
- [ ] Incident response plan with named roles
- [ ] Dependency and integration inventory

Work through the full [Agent Security Assessment](../compliance-toolkit/agent-security-assessment.md) before selling to larger organisations.

## 4. Selling to government and regulated buyers

Expect requirements on data location, access by personnel, security certifications, incident notification and audit rights. Ask the buyer early which controls apply to you as a vendor, and price the work to meet them. Do not claim compliance with a control set you have not been assessed against.

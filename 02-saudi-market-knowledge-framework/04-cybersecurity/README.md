# المجال 04: الأمن السيبراني · Domain 04: Cybersecurity and digital infrastructure

النسخة العربية: [README.ar.md](README.ar.md)

**Status:** Guide published · Last reviewed 16 November 2026 · Educational, not legal advice

<div dir="rtl">

**السؤال:** أي ضوابط الأمن السيبراني تنطبق على منشأتي؟

**الخلاصة:** لا تفترض أن كل ضوابط الهيئة الوطنية للأمن السيبراني تنطبق على كل منشأة ناشئة. اسأل أولاً: هل الضابط ملزِم **لمنشأتي**، أم لعميلي فينتقل إليّ بالعقد، أم لقطاعي؟ والجديد المهم: صدرت في ديسمبر 2025 ضوابط خاصة بجهات القطاع الخاص من غير ذات البنى التحتية الحساسة، وتتفاوت التزاماتها بحسب حجم المنشأة.

</div>

## The key lesson

Do not assume every NCA control applies to every startup. For each control set ask whether it is mandatory for **your entity**, for **your customer** (and flows to you by contract), or for **your sector**.

## Guide and tools

| Resource | Use it for |
|---|---|
| [Cybersecurity for agentic startups](cybersecurity-for-agentic-startups.md) | Agent-specific threats and a startup baseline |
| [Agent security assessment](../compliance-toolkit/agent-security-assessment.md) | Checklist and one-page incident plan |
| [Governance playbook](../02-ai-regulations/agentic-ai-governance-playbook.md) | Identity, permissions, logging and rollback for agents |

## Instruments

| Instrument | Applies to | Status | Verification |
|---|---|---|---|
| Non-CNI Private Sector Entities Cybersecurity Controls (NCNICC-1:2025) | Private-sector entities that are not critical infrastructure; obligations vary by entity size | Binding | ✔ adopted 28 December 2025 |
| Essential Cybersecurity Controls (ECC-2:2024) | Government and critical-infrastructure entities; vendors by contract | Binding | ✔ current version, updating ECC-1:2018 (A124, A126) |
| Cloud Cybersecurity Controls (CCC-2:2024) | Cloud providers and tenants in scope | Binding | ✔ current version (A126) |
| Data Cybersecurity Controls (DCC-1:2022) | Entities in scope | Binding | ✔ (A126) |
| National Cybersecurity Risk Management Framework | Government and critical-infrastructure entities | Framework | ✔ released July 2025 |
| AI Cybersecurity Guidelines (AICG-1:2026) | AI systems | **Draft**, non-binding | ✔ status |

**On NCNICC.** This is the control set most likely to apply directly to a startup. Commentary describes a mandatory baseline with requirements that differ by entity size. Find your size class and the controls mandatory for it in the NCA document itself. One early draft said the same obligations now apply to a startup as to a large enterprise; that overstates it.

## Founder decisions

| Decision | Ask |
|---|---|
| Which control set is mine? | Am I in scope directly, or only through a customer contract? |
| Where do agents and models run? | Does a buyer require hosting in the Kingdom? |
| Who can the agent act as? | Does each agent have its own identity and least privilege? |
| What do I log? | Can I show every tool call and who approved it? |

## Guides wanted

- [ ] NCNICC for a ten-person startup: which controls, in what order
- [ ] Secure cloud deployment for agentic products
- [ ] Secure API and Model Context Protocol server development
- [ ] Secrets and credentials management
- [ ] Reviewing AI-generated code for security
- [ ] Software supply-chain security for agent integrations
- [ ] Backup and disaster recovery on a startup budget
- [ ] Answering an enterprise security questionnaire

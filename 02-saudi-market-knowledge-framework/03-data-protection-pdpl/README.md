# المجال 03: البيانات والخصوصية · Domain 03: Data protection and privacy

**Status:** Guide and worked example published · Last reviewed 18 November 2026 · Educational, not legal advice

<div dir="rtl">

**السؤال:** كيف أتعامل مع البيانات الشخصية في منتج قائم على الوكلاء؟

**الخلاصة:** نظام حماية البيانات الشخصية ملزِم ويُطبَّق فعلياً، ويشمل المنشآت الصغيرة. أعلنت سدايا مطلع 2026 أن لجان النظر في المخالفات أصدرت 48 قراراً خلال عام. الهدف من هذا المجال أن تخرج **بقائمة امتثال فعلية لمشروعك**، لا بمجرد معرفة بالنظام.

</div>

## Why it matters now

The law is binding and enforced. In early 2026 SDAIA announced that its violation-review committees had issued 48 decisions confirming violations over the previous year (see [SOURCES.md](../../SOURCES.md)). It covers small businesses that process personal data.

## Guides and tools

| Resource | Use it for |
|---|---|
| [PDPL: a founder's guide for agentic products](pdpl-founder-guide.md) | What the law means for memory, logs, embeddings and model providers |
| [مثال تطبيقي: وكيل خدمة عملاء مرتبط بنظام CRM](worked-example-customer-service-agent.md) | The whole file for one agent, in Arabic: roles, data map, lawful basis, notice, transfers, retention, requests, breach plan, permission matrix |
| [PDPL self-assessment](../compliance-toolkit/pdpl-self-assessment.md) | Data map, 27-question checklist, action plan |
| [Third-party provider assessment](../compliance-toolkit/third-party-provider-assessment.md) | Checking each model and tool provider |
| [PDPL Pre-Check skill](../../05-agentic-ai-lab/skills/README.md#9-pdpl-pre-check) | A guided first pass with any AI assistant |

## Instruments

| Instrument | Status | Verification |
|---|---|---|
| Personal Data Protection Law (Royal Decree M/19 of 9/2/1443H, amended by Royal Decree M/148 of 5/9/1444H) | Binding | ✔ decree numbers (A49) · ✔ enforcement (A9) · ◻ consolidated official text not opened |
| Implementing Regulation (published by SDAIA, September 2023) | Binding | ✔ the articles listed in A50, read from an English copy on a non-official site · ◻ SDAIA's own copy and any later amendment |
| Regulation on Personal Data Transfer outside the Kingdom | Binding | ✔ adequacy list not yet published, safeguards required, as reported by law firms (A51) · ◻ official text |
| Draft amendments to the Implementing Regulation (consultation 6 October to 5 November 2026) | **Draft, not in force** | ✔ as reported by three law firms (A52) · ◻ outcome |
| SDAIA guide to the PDPL for controllers and processors | Official guidance | ◻ |

One early draft cited the law as "Royal Decree M/19 of 2024". The decree dates from 2021; the law became enforceable in September 2024 after its transition period.

## Worked example

[A customer-service agent connected to a CRM](worked-example-customer-service-agent.md), written in Arabic. It answers the six questions this domain asks of every venture: what is collected and why, who is controller and processor, which providers receive data, what leaves the Kingdom, how long each category is kept, and how a customer exercises their rights. It ends with the questions to take to a lawyer.

## Guides wanted

- [x] The worked example, completed (18 November 2026)
- [ ] Arabic privacy notice template for an agent-based service (a short in-chat notice is in the worked example; the full policy is still wanted)
- [ ] Data processing agreement checklist for startups acting as processors
- [ ] Using external model APIs with business data: a decision tree
- [ ] Retrieval and vector database privacy
- [ ] Training and fine-tuning on customer data
- [ ] Impact assessment template sized for a startup
- [ ] Breach response playbook
- [ ] Arabic version of the founder's guide

## What the 18 November 2026 check settled

| Claim from early drafts | Result | Source |
|---|---|---|
| A 30-day period for answering individuals' requests | Confirmed: 30 days, extendable by up to 30 more with notice and reasons (Implementing Regulation, Article 3) | A50 |
| Explicit consent for decisions based solely on automated processing | Confirmed (Article 11); such decision-making is also among the triggers for an impact assessment (Article 25) | A50 |
| A requirement that notices be in Arabic | **Not found** in the text read. The October 2026 draft would add a clear-language rule tied to the language of the service | A50, A52 |
| Parental consent is required below the age of 15 | **Not found.** The regulation speaks of legal guardians for those who lack full or partial capacity and names no age | B32 |
| SDAIA has approved a list of countries with adequate protection | **Not published**, as reported | A51 |

All of this is read from secondary copies and law-firm reports. Read the official Arabic text and ask a lawyer before you rely on it.

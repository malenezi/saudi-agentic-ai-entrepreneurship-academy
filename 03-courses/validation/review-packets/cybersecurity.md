# Cybersecurity review packet · حزمة مراجعة الأمن السيبراني

> **Status: prepared, not reviewed.** No specialist has reviewed this content as of 20 November 2026. Nothing in the Academy should be described as legally, fiscally or professionally reviewed until the sign-off at the end of this file is completed by a named person. The lessons are educational material, not advice.

**For:** A practitioner in application or AI security, familiar with NCA control sets · **Time needed:** about three to four hours · **How to return it:** a pull request that fills this file, or an issue (see [CONTRIBUTING.md](../../../CONTRIBUTING.md))

## 1. What to read

- Lesson 4.4 (security for agentic systems) in full
- Lessons 2.3 and 2.6 (least privilege, guardrails outside the model, prompt injection)
- The Course 2 labs, in particular lab 2.6, and the reference code in `03-courses/02-build/labs/reference/order_agent/`
- The agent security assessment in the compliance toolkit and lab exercise R7

## 2. What we need from you

For each claim in section 4: **confirm**, **correct** (with the instrument and article, or the official page), or mark **cannot confirm**. Then answer the questions in section 3. Where a lesson is right but risky to teach to beginners, say so.

## 3. Questions

1. Lesson 4.4 names ECC-2:2024 as the current edition and limits its scope to government entities, their affiliates and private CNI operators, from summaries (A124). Is that right, and what applies to a small private vendor (A10)?
2. NCA's AI Cybersecurity Guidelines are treated as a draft (A5). What is their status today?
3. The OWASP rankings (A121, A122) were read through secondary summaries. Are the first three entries of each list stated correctly?
4. Is "least agency" used correctly, and is the distinction from least privilege sound?
5. Does the reference code enforce what the lessons claim: ownership check before the tool call, no tool for refunds, level B actions only after a named approval, untrusted notes never read as instructions, a stop switch? What would you attack first?
6. Is the incident response guidance in lesson 4.4 adequate for a two-person company?
7. Is the red-teaming guidance safe to give to beginners? It restricts testing to the learner's own agent in a test environment.
8. Which claims about what enterprise and government buyers ask of vendors should be removed or sourced?
9. What is missing on secrets management, logging of personal data, and supply-chain risk for agents that use third-party tools?

## 4. Claim register

Every sourced claim the files above rely on, from [SOURCES.md](../../../SOURCES.md): 9 claims, of which 1 rest on a draft or non-final instrument, 7 on a secondary or partial reading, and 1 cite the source's own page. **"Source page cited" means the page was read by the authors, not that a specialist confirmed the reading.** Start with the first two groups.

| # | Claim as recorded | How it was verified | Recorded limit | Used in | Reviewer: confirm / correct / cannot confirm | Reviewer note and reference |
|---|---|---|---|---|---|---|
| A5 | NCA published **draft** AI Cybersecurity Guidelines (AICG-1:2026) for public consultation from 5 July to 5 August 2026; described as non-binding guidelines | Draft or not final | Final publication not confirmed on review date. Treat as draft | 4.4 | | |
| A10 | NCA adopted the Non-CNI Private Sector Entities Cybersecurity Controls (NCNICC-1:2025) on 28 December 2025; obligations differ by entity size | Secondary or partial reading | Read the NCA document for size classes and mandatory controls | 4.4 | | |
| A83 | The Model Context Protocol is an open standard, introduced by Anthropic in late 2024, for connecting AI applications to external tools and data sources. In December 2025 Anthropic donated it to the Agentic AI Foundation, a … | Secondary or partial reading | One secondary page dates the donation May 2026; the others, including one giving 9 December 2025, agree on December 2025. The specification itself … | 2.3 | | |
| A84 | OWASP Top 10 for LLM Applications, 2025 edition: LLM01:2025 is Prompt Injection, with direct injection (the user's input alters the model's behaviour) and indirect injection (content from external sources does); LLM06:2025 is … | Secondary or partial reading | **Read through secondary summaries**; OWASP's own page was not opened. One summary mentions a later edition; check for it before teaching. **Checked … | 2.3, 2.6, 4.4 | | |
| A85 | Saudi Post: the National Address has six main parts (building number, street name, district, city, postal code, secondary or additional number). The building number and the additional number are four digits each and the postal … | Secondary or partial reading | Read from search extracts of SPL's pages, 19 Nov 2026 | 2.3 | | |
| A121 | OWASP Top 10 for LLM Applications, 2026 edition, published early August 2026 (OWASP's page says 4 August): LLM01 Prompt Injection and LLM02 Sensitive Information Disclosure keep the first two places; LLM03 is Excessive Agency, up … | Secondary or partial reading | Ranking **read through secondary summaries**; one summary dates publication 3 August. Supersedes the numbering in A84. Used in lesson 4.4 | 2.3, 2.6, 4.4 | | |
| A122 | OWASP Top 10 for Agentic Applications, first published 9 December 2025 by the OWASP GenAI Security Project (labelled 2026): ten categories ASI01 to ASI10, beginning ASI01 Agent Goal Hijack, ASI02 Tool Misuse and Exploitation, … | Secondary or partial reading | **Read through secondary summaries**; OWASP's own document was not opened. Used in lesson 4.4 | 4.4 | | |
| A124 | NCA's Essential Cybersecurity Controls were reissued as ECC-2:2024, updating and replacing ECC-1:2018; summaries give four domains, 28 subdomains and 108 main controls, with the industrial control systems domain moved to a … | Secondary or partial reading | **Scope and counts read through summaries**; summaries disagree on the control count (108 or 110), so lesson 4.4 gives no count. Private entities … | 4.4 | | |
| A46 | OWASP, Top 10 for LLM Applications 2025, LLM01 Prompt Injection: distinguishes direct injection (the user's own prompt) from indirect injection (external content the model processes); states it is unclear whether fool-proof … | Source page cited | Opened 17 Nov 2026. Used in lab exercise R7 | 4.4 | | |

## 5. Sign-off

| | |
|---|---|
| Reviewer name and qualification | **Not signed** |
| Organisation | |
| Date of review | |
| Scope reviewed (sections of this packet) | |
| Claims confirmed / corrected / not confirmed | |
| May the Academy name you as reviewer? | |
| Next review due | |

A sign-off covers the scope and date written in it, and nothing after a rule changes. The Academy records it in [SOURCES.md](../../../SOURCES.md) and in the lessons' verification notes.

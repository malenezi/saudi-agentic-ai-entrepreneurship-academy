# Course 1 slides: enriched content pack
# المقرر 1: حزمة محتوى العروض بعد التحقق والإثراء

**Course:** اكتشاف الفرصة الوكيلية · Finding Your Agentic Opportunity · 16 hours · 7 modules
**Date:** 19 November 2026 (updated the same day with the owner's Tabby and Tamara sources) · **Status:** first version of the slides, not yet piloted

This pack merges the two instructor raw-content files supplied by the owner on 19 November 2026 ("Instructor Raw Content Pack" v1.0, here **Pack A**, and "Instructor Raw Material, Local Examples, Stories & Assets", here **Pack B**) with the published Course 1 lessons. It was handled by the Course 1 rule: verify, keep the published structure, enrich. The seven decks in this folder are built from it.

## 1. How the decks are built

| Item | Choice |
|---|---|
| Format | Bayan `arabic-html-slides`: one self-contained HTML file per module, 1600 × 900 stage, keyboard navigation that follows reading direction, speaker notes (`N`), print to PDF (`P`) |
| Language | Arabic, with English terms in parentheses, per the Course 1 decision (lesson content in Arabic with English terms) |
| Visual identity | Pack B palette: Najdi slate `#1E293B`, sandstone gold `#D97706` (accents and large text only; `#B45309` for small gold text on light backgrounds, for contrast), off-white `#F8FAFC`. Sadu-inspired geometric band on title slides that turns into a node-and-arrow graph. No robots, no logos (Pack A and Pack B agree) |
| Course subtitle | من ملاحظة سير العمل إلى أطروحة مشروع قابلة للتحقق (Pack A). Pack B's line «أعمال تُنجز المهام لا مجرد أدوات للدردشة» is used as the closing message of Module 1.1 |
| Evidence labels | Every example carries one badge: **حالة منشورة** with its evidence level (A, B, C as in `06-case-studies`), **سيناريو توضيحي** (invented, numbers synthetic), or **فرضية للتحقق** (a claim the learner must test). Pack A's four-label convention maps onto these |
| Central principle | «استدلال احتمالي، وصلاحيات حتمية» (Pack A). It restates the Academy rule that authority is enforced outside the model, and opens and closes the course |

## 2. What was checked

| Claim in the packs | Result | What the decks say |
|---|---|---|
| Klarna: 2.3 million chats in month one, work of 700 full-time staff, resolution from 11 minutes to under 2 (Pack B) | **Confirmed**, company press release of 27 Feb 2024 (already in `06-case-studies/global/klarna.md`, level A). The May 2025 return to hiring people is also documented | Used with both chapters. "700 staff" is a workload equivalent, not jobs removed |
| Tamimi AskBaba, OPLOG (Packs A and B) | Already in the case-studies section (level B). OPLOG's source shows 30% and 85% in headlines, 30 to 40% and 85 to 95% in the body | Used as published. Pack B's "customs clearance across Saudi borders" for OPLOG is **not in the source**; not used |
| Tamara and Tabby use multi-step agents for merchant onboarding and collections "without human agents touching routine cases" (Pack B) | **Still not found** after the owner's follow-up sources (19 Nov). Tamara's job postings describe human KYB teams. Tabby's developer page documents a read-only MCP server for coding agents, and Tabby's 2026 survey covers shoppers' use of AI; neither describes agents in Tabby's own operations. Tamara's help-centre page loaded without its article text. The ResearchGate paper reviews ML fraud scoring for BNPL in general, not either company | Not used as an operations case. Used instead: Tabby's read-only MCP server as a bounded-autonomy example (deck 1.1, SOURCES A78); Tabby's survey as a market signal labelled as a company survey (deck 1.3, A79); the human KYB teams as a signal worth investigating (deck 1.3) |
| Clinics lose 10 to 18% of revenue to NPHIES rejections (Pack B) | **Not found** as a revenue figure. A KPMG Middle East report (June 2026, via press) puts initial claim rejection at 15 to 25%. A peer-reviewed study of insurers' records put rejection at about 15% for 2014 to 2019; it gives no rate by service | Decks say "initial rejection rate 15 to 25% (KPMG, 2026)". A rejection rate is not a revenue loss; resubmitted claims are often paid |
| NPHIES coding: dentist note translated into "ICD-10" (Pack B) | NPHIES claims follow ICD-10-AM for diagnoses and the Saudi Billing System (SBS), built on ACHI, for procedures (BMC Health Services Research, 2025) | Corrected to "ICD-10-AM for the diagnosis and SBS for the procedure" |
| WhatsApp Business API costs SAR 0.08 to 0.18 per 24-hour session (Pack B) | **Outdated.** Meta moved from conversation pricing to per-message pricing on 1 July 2025. Meta's SAR card from 1 October 2026: marketing SAR 0.2159, utility and authentication SAR 0.0401, and service replies inside the 24-hour window now also SAR 0.0401 after the first 1,000 a month per number (business pages citing the card) | Decks give the per-message model, ≈ SAR 0.04 and ≈ SAR 0.22, and "check Meta's rate card on the day" |
| Intercom Fin at $0.99 per resolution (Pack B) | **Confirmed** on Intercom's help pages: $0.99 per outcome, at most one per conversation; a resolution is counted when no further help is requested after the last AI answer | Used as an example of outcome pricing in Module 1.2 |
| "WhatsApp fees and human review cost 5 to 10 times the model tokens" (Pack B) | No source. In the course's own worked example, review plus escalation is SAR 0.94 per attempt against SAR 0.20 for the model, **4.6 times** | Decks use the 4.6 times figure, computed from the worked example |
| Model prices "Claude 3.5/3.7 Sonnet, GPT-4o class" (Pack B) | Model names are out of date, and Pack A itself says prices must not be embedded | Not used. Decks keep the lesson's illustrative SAR 11 / 45 per million tokens and the rule: check the provider's page, write the date |
| Arabic STT/TTS SAR 0.15 to 0.30 per minute; OCR $0.002 to 0.005 per page; customs-broker data prep SAR 80 to 120; per-ticket SAR 2.50 to 4.00; remote CS agent SAR 3,500 to 5,500 a month (Pack B) | No source found | Not quoted as market prices. Where useful they appear as "assumptions to replace with your own quotes" |
| WideBot, Botme, Unifonic weak on voice notes; Intercom weak on Saudi dialect (Pack B) | No source; product judgements about named companies | Not used. The alternatives scan is shown by **category** (rule-based chatbot, global AI help desk, local hire) with the rule "describe a competitor from its own page" |
| ZATCA Fatoora Phase 2 "forces every business" (Pack B) | Phase 2 is applied in waves; wave 25 covers VAT-registered businesses above SAR 187,500 and must integrate by 1 February 2027 (SOURCES A54) | Corrected to "in waves, now reaching small VAT-registered businesses" |
| PDPL: health data "must stay within KSA" (Pack B) | Overstated. Health data is sensitive data under the amended definition; transfer outside the Kingdom is allowed only under the law's conditions, which the course has not fully read (SOURCES D5) | Decks say "sensitive data: know where it is stored and whether it leaves the Kingdom before you build" |
| Break-even success rate s = (Ca + Ch) ÷ (P + Ch) (Pack A) | Algebra checked. It equals the course formula when the escalation rate is 1 − success rate | Added to Module 1.6. With the worked example's numbers (Ca = SAR 0.54, Ch = 4.69, P = 2.00) break-even is **78%**, consistent with the lesson's loss at 70% |
| Dental workflow: elapsed ~2.5 hours, touch 27 minutes, cycle efficiency ~18% (Pack B) | Touch time sums to 27 minutes. Waits sum to 110 to 185 minutes, so elapsed is 137 to 212 minutes and efficiency 13 to 20% | Decks show the range and let learners compute it |
| Pack A illustrative scoring example totals 72 | Arithmetic correct | Not used (it uses ten criteria; see section 4) |
| Opening story, Jeddah "sticky notes" anecdote, Riyadh perfume-brand refund story, dental workflow "sanitised real" (Pack B) | No independent record; the perfume story has precise losses and a TikTok timeline | Labelled **سيناريو توضيحي**. If the opening story or the Jeddah anecdote is the instructor's own experience, relabel it «من تجربة المدرب» |
| Pack B naming a specific insurer and plan class in an "unwritten rule" | An unverified claim about a named insurer | Anonymised to «شركة التأمين (أ)» |
| Pack B dental model-thesis excerpt (8 interviews, 14% revenue loss, SAR 18.5 per claim, 72% margin, SAR 35,000 a month) | Invented figures | Kept as a **writing-style model** with the badge «أرقام مصطنعة للتدريب», as the course does with `examples/model-thesis.md` |

## 3. What was added, by module

### Module 1.1 · From chatbots to agents (2 h · LO1)
- Tabby's read-only MCP server for coding agents (owner's follow-up source, checked): a published Saudi example of separating read access from moving money.
- Course opener: the Academy narrative (Pack A, shortened; Pack B's story offered in the speaker notes), the course question, the seven modules, the deliverable and the five validation gates in one line each.
- Three demonstrations of capability: conversational assistant, tool-using research agent, bounded invoice agent (Pack A), each tied to the four-property test. Each demonstration has an illustrative screen drawn in HTML (slides 10 to 12, added 19 November 2026, invented data, labelled «شاشة توضيحية»). Product screenshots (Pack B: coding agent, contract review, WhatsApp booking) are not included; an instructor may show their own captures. No product claims are made on the slides.
- Ten classification examples localised from Pack B, mapped to the **course's four types** (chatbot, automation, workflow with a model step, agent) plus "not suitable". Midjourney was replaced by Pack A's "agent that changes supplier bank details from an email" so the set keeps an unsafe case.
- Six questions for any proposed agent (Pack A): allowed, prohibited, needs approval, low confidence, reversible, who stops it. Laid onto the course's four written limits.
- Two failure scenarios (illustrative): the supplier bank account (Pack A) and the perfume refund (Pack B), analysed with the four limits.
- What AI makes cheaper and what it does not (Pack A), restating lesson section 7.

### Module 1.2 · The agent-native business (2 h · LO1, LO3)
- Musanid back-office service blueprint (Pack A, illustrative): seven stages, agent versus human responsibility.
- The course's worked example kept as the single set of numbers (SAR 4.69 → 2.00, cost 1.46, margin 27%, then 13%, −0.56, −0.78).
- "Mahasel AI" accounting rewrite (Pack B) used as a **pitch to stress-test**: its claims (one CPA for 100 clients, 92% auto-match, 78% margin) are labelled founder hypotheses, and learners attack them with the three scenarios.
- Outcome pricing in practice: Intercom Fin at $0.99 per outcome (checked) and Pack A's six pricing models, mapped to the lesson's four.
- Margin gains and leaks (Pack A) merged with the lesson's seven leaks; founder question: what disappears, what moves, what is new.

### Module 1.3 · Where to look in the Saudi market (3 h · LO2, LO3)
- Tabby's 2026 shopping survey as a signal (43% use AI in purchase decisions, 30% fully trust it), badged as a company survey.
- Six sector cards with one candidate wedge each (Pack A), aligned with the six sector briefs.
- Two additional sectors from Pack B: multi-branch food and beverage (reconciling delivery-app payouts against POS and supplier invoices) and tier-2 contractor compliance paperwork. Marked as hypotheses.
- Forced wedges from regulation (Pack B, corrected): e-invoicing waves, NPHIES and its coding standards, PDPL.
- Official sources table (Pack A) with the rule that a sandbox or programme is not an authorisation.
- Local workflow artefacts as drawn icons (Pack B): e-invoice QR, Nitaqat-style status badge, WhatsApp voice note, commercial registration certificate. Drawn generically; no logos.

### Module 1.4 · Workflow shadowing (3 h · LO2)
- Before, during and after observation protocol (Pack A).
- The dental-clinic pre-approval walkthrough (Pack B, illustrative and anonymised) as the worked map: touch versus waiting time, the unwritten rule, the PDPL data walk.
- The Jeddah dispatcher anecdote (Pack B) as the opening story of the module.
- The four step classes and three human-control models stay as published; Pack A's six fields per step (input, output, acceptance test, permissions, failure condition, escalation) added to the "agent-suitable" class.

### Module 1.5 · Customer discovery (3 h · LO4)
- Dialect question bank merged from both packs, grouped by the lesson's 25-minute structure.
- Two bad-versus-good scripts: invoice approval (Pack A) and abaya returns on WhatsApp (Pack B).
- Role cards: three from Pack B (clinic operations manager, skeptical finance controller, enthusiastic founder with no budget) and three from Pack A (frontline administrator, IT and cybersecurity reviewer, polite non-buyer), mapped to the buying committee.
- Evidence ladder kept as published (six levels); Pack A's operational records and paid pilot folded into levels 1 and 3.
- Pack A's eight customer roles shown as a reminder under the four-role buying committee.

### Module 1.6 · Scoring and first economics (2 h · LO3)
- Break-even success rate (Pack A), computed on the course example: 78%.
- "Where the money goes": in the worked example review and escalation are 4.6 times the model cost; messaging and voice costs are added as line items with the per-message WhatsApp model.
- Alternatives scan for Saudi e-commerce WhatsApp support (Pack B) shown by category.
- Pack A's competitor research card and API-pricing discipline.

### Module 1.7 · Writing the thesis (1 h · LO5)
- Arabic sentence starters from Pack A mapped onto the **published** seven sections.
- Pack B's dental excerpt as a tone model (invented numbers, labelled).
- Peer review: Pack B's "investment committee audit" (15 minutes per pair: silent read with yellow and red highlights, a three-question stress test, rubric score and one sentence to rewrite). Lesson 1.7 was updated to match; its four earlier reviewer questions remain the scoring guide.
- Three-minute pitch timing (Pack A).
- Red flags (Pack A) as the closing checklist.

## 4. Not adopted, and why

| Item | Source | Reason |
|---|---|---|
| Seven-level autonomy ladder | Pack A 2.3 | The course ladder (levels 0 to 5) is published and used across lessons, rubrics and the toolkit |
| Four classification types with "hybrid" and "unsafe implementation" as types | Pack A 2.2 | The course uses four types (chatbot, automation, workflow with a model step, agent); "unsafe" is a verdict, kept as "not suitable" |
| Unit-economics table with manual price SAR 5.50, agent price SAR 2.75 and a SAR 2.00 cost breakdown | Pack A 3.3 | Conflicts with the course's single worked example (price SAR 2.00, cost SAR 1.46) |
| Invoice workflow measured at 11 minutes, 1.5 days, 78% first-pass yield | Pack A 5.5 | Conflicts with the course example (6 minutes, 960 minutes, under 1%) |
| Ten-criterion weighted scoring (pain 15%, buyer 15% …) and its example scoring 72 | Pack A 7.1–7.2 | The toolkit's nine-criterion assessment (max 115) and the stop check are the published method |
| Three-scenario table varying autonomy, exception rate, acceptance and volume together | Pack A 7.4 | The lesson's three mandatory scenarios (double review, success −15 points, volume ÷ 3) stay; Pack A's table is a fourth, optional exercise in the notes |
| Thesis sections renamed (customer and context … validation plan and ask) | Pack A 8.1 | The published seven sections stay; the "ask" lives in the pitch's last 30 seconds |
| Rubric renamed (risk and accountability 15%, communication 10%) | Pack A 8.3 | The published rubric (35/25/15/15/10: evidence, workflow, agent fit, economics, writing) stays |
| Minimum of three interviews, and an illustrative workflow when no organisation is available | Pack A 10.3 | The syllabus requires five interviews and validation gate 3 requires observation |
| Pack A's 12-minute peer review | Pack A 8.4 | The owner's Pack B protocol was preferred; Pack A's "keep, clarify, prove, narrow, next test" prompts are kept as reviewer prompts |
| Tamara/Tabby as an agent case | Pack B | No public evidence, including after the owner's follow-up sources (section 2) |
| Named vendor judgements (WideBot, Botme, Unifonic, Intercom dialect handling) | Pack B | No source; replaced by categories |
| Market price ranges without a source | Pack B | Course rule: no number without a source |
| OPLOG customs and cross-border orchestration | Pack B | Not in the source |
| Product demos claimed for Harvey ("against Qiwa standards") and a Bupa-style booking agent | Pack B | Unverified product claims about named companies; slides keep generic placeholders the instructor fills with their own screenshots |

## 5. Open items for the owner

1. Is Pack B's opening story your own experience, and the Jeddah dispatcher anecdote? If yes, the badge changes from «سيناريو توضيحي» to «من تجربة المدرب».
2. Module 1.1 now carries three illustrative screens (slides 10 to 12). Real screenshots of agent products in use remain optional: capture them yourself so no product claim rests on the slides.
3. Done 19 Nov: lesson 1.7 now describes the investment-committee audit, matching the deck; the earlier four reviewer questions remain as the scoring guide.
4. WhatsApp and model prices change quarterly: re-check Meta's rate card and the provider pages before each cohort.

## Sources checked for this pack

- Klarna press release, 27 Feb 2024, and May 2025 reporting (via `06-case-studies/global/klarna.md`).
- Intercom, "Fin pricing" help article (outcome pricing, $0.99).
- KPMG Middle East healthcare-financing report, June 2026, as reported by Riyadh Daily (initial claim rejection 15 to 25%).
- Peer-reviewed study of Saudi health-insurance fraud measures, PMC7522845 (rejection about 15%, 2014 to 2019).
- Reka et al., "The development of the Saudi Billing System", BMC Health Services Research 25:534 (2025) (ICD-10-AM, ACHI, SBS).
- WhatsApp Business Platform pricing documentation (per-message pricing from 1 July 2025) and business pages quoting Meta's 1 October 2026 Saudi rates (letsbot.net, chatmaxima.com).
- Tamara job postings on Greenhouse (KYB and onboarding roles).
- Tabby, "AI tools" page in the developer documentation (docs.tabby.ai/introduction/ai-tools), and the 2026 shopping survey newsroom page (tabby.sa). Opened 19 Nov 2026.
- ZATCA wave 25 (SOURCES A54).

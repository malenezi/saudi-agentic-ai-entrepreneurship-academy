# Changelog

## v0.5 (in progress)

Founder essentials in depth. First part, 18 November 2026: the PDPL worked example, the funding directory and the first tax guide. Still to come in v0.5: the establishment walkthrough and Arabic versions of the English-only guides. READMEs stay at v0.4 until then.

### Data protection (domain 03)

**Added**
- `03-data-protection-pdpl/worked-example-customer-service-agent.md`: the whole PDPL file for one fictional agent, in Arabic. Roles, a filled-in data map, lawful basis per purpose, an in-chat privacy notice, processing location and transfers, retention, individuals' requests, a breach plan, the agent's permission matrix, what the October 2026 draft would change, and seven questions for a lawyer.

**Changed**
- `compliance-toolkit/pdpl-self-assessment.md`: the single question that grouped health, credit, biometric and minors' data is now three (sensitive data as defined, credit data, minors and people lacking capacity). The checklist has 27 questions.
- The PDPL Pre-Check skill asks the same three questions separately.
- `pdpl-founder-guide.md`: decree numbers, the 30-day response period, the state of the adequacy list, guardians and capacity, and a section on the draft amendments.
- Domain page: instruments table with verification marks, and a table of what the check settled.

### Tax (domain 05)

**Added**
- `05-tax-accounting-finance/tax-basics-for-founders.md`: VAT registration, e-invoicing waves, zakat or income tax by ownership, and withholding tax on foreign model and cloud bills, in Arabic. **Sources checked; not reviewed by a tax adviser.**
- `foreign-supplier-payment-register.md`: a bilingual register whose classification column stays "awaiting adviser review" until an adviser signs it.
- `adviser-review-pack.md`: twenty questions, three review gates and an approval record for the adviser who reviews the domain.

### Funding (domain 06)

**Added**
- `06-funding-investment/funding-directory.md`: one entry per programme with a status and the date its official page was opened, in Arabic. Four verified (Estrdad, CODE, Kafalah at the SME Bank, Monsha'at's directory), five partial (MVPLAB, Tech Crew, Boost, TAQADAM, the AI Incubator), two sandboxes listed apart, and the rest named as "to verify" without terms. No entry says applications are open.

### Verified and corrected

`SOURCES.md` A49 to A64, B32 to B39, C28 to C32; D3 to D6 updated. `02-saudi-market-knowledge-framework/not-adopted.md` records what was taken from the five drafts, what was corrected or dropped, and what was deferred.

- Confirmed: the amending decree M/148; the 30-day response period; explicit consent for solely automated decisions; the VAT thresholds; e-invoicing wave 25 (1 February 2027); withholding rates and deadlines from ZATCA's May 2026 guideline; the Ministry of Investment's registration category for entrepreneurial establishments.
- Not found, left out: parental consent "under 15"; "Decision 816 of 2025"; an SDAIA adequacy list; a general Arabic-language rule for notices; several programme amounts; first-year and second-year investment fees.
- Recorded as a draft only: the amendments to the PDPL Implementing Regulation consulted on from 6 October to 5 November 2026.

**Limits of this check.** The Implementing Regulation was read from an English copy on a non-official site, and ZATCA's withholding guideline through an automated extraction of the English PDF. NTDP's product pages and SAMA's sandbox page did not open. No lawyer or tax adviser has reviewed any of it.

## v0.4 (2026-11-17)

Six new lab exercises with working checkers, Module 1.4 in depth, the academy identity, and automated checks on every change. The founder-essentials work first planned for v0.4 moves to v0.5; see the roadmap.

### Launch audit (17 Nov 2026)

**Fixed**
- `assets/brand/saaea-banner.jpg`: three spelling slips in the Arabic lettering corrected in the image itself.
- `01-academy/learning-pathways.md` now routes learners through R5 to R8, B5 and B6.
- README status lines say what is released and what is in progress.

**Added**
- `tools/check_repo.py`: checks every Markdown file for missing link targets, missing anchors, unbalanced right-to-left blocks, unclosed code fences and uneven table rows.
- `tests/test_scripts.py`: fifteen tests that run every script and assert the figures the exercises quote.
- `Makefile` (`make check`) and a CI workflow that runs both on every push and pull request, on Python 3.9 and 3.13.
- `SECURITY.md` and `CITATION.cff`.

### Agentic AI Lab: six new exercises

**Added**
- `05-agentic-ai-lab/exercises/r5-market-intelligence.md`: a market file with a claim register (documented fact, estimate, assumption), using Riyada's competitor matrix and sizing sheet.
- `r6-agent-evaluation.md`: two evaluation cycles on at least 30 cases, each case run three times, one change between cycles, release rule written first.
- `r7-agent-red-teaming.md`: at least twelve attack cases in six families against the learner's own agent; a control outside the model is the pass criterion.
- `b5-venture-dashboard.md` and `b5-venture-dashboard/`: a bilingual founder dashboard for a fictional five-agent company. Ships one month of synthetic records, `generate_data.py` (baseline and three decision scenarios), `compute_metrics.py` (computes every KPI and checks a learner's numbers), a KPI dictionary, a founder decision log and a two-KPI skeleton page.
- `r8-data-governance.md` and `r8-data-governance/`: `data_governance_lint.py` checks a CSV file against a policy the learner writes (nine rules, standard library only), with an example policy and a synthetic sample that carries deliberate faults.
- `b6-terminology.md` and `b6-terminology/`: `terminology_lint.py` enforces a venture's own Arabic glossary across messages, pages and decks, with a starter glossary and a sample.
- `b3-deck-evidence/deck_evidence_check.py`: every slide with a figure names a source or labels it an estimate; added as a step in B3.
- A language-parity measure in R6 (paired Arabic and English cases).
- `exercises/not-adopted.md`: what happened to every proposal in the three drafts.

**Changed**
- Extra challenges in R1 (a deliberately false assumption), R2 (two files that conflict), B1 (mixed-direction messages) and B2 (a conversion test); an accessibility line in B4's criteria.
- Lab index, lab README, both READMEs and the Course 1, 2, 3 and 4 syllabi now point to the fourteen exercises.

**Verified and corrected** (`SOURCES.md` A46 to A48, B29 to B31, C26 to C27)
- The drafts' data-governance linter does not compile; rewritten as R8, with the pass criterion changed from "PDPL compliance" to "meets the policy you wrote".
- Tools the drafts relied on that did not exist (`terminology_lint.py`, a `--market-ready` flag) were written as working scripts; the undefined "linguistic parity score" was given a definition.
- The drafts' dashboard figures did not reconcile; replaced by generated records. The fictional company was renamed.
- Deferred: multi-agent architecture, bilingual customer journey, the two integrative exercises, a capstone, supply-chain audit.
- Run on 17 Nov 2026 with Python 3.11, 3.12 and 3.13: the R8, B6 and B3 scripts on their samples and on Bayan's example deck; both B5 scripts on all four scenarios; Bayan's two linters on the skeleton page; Riyada's context linter on the R2 conflict case. Not tried with learners.

### Academy identity

**Added**
- `assets/brand/saaea-banner.jpg`: the academy's banner, shown at the top of both READMEs, with a usage note in `assets/brand/README.md`. Three spelling slips in the artwork's Arabic lettering are recorded there for the next version of the image.

### Course 1, Module 1.4: Workflow shadowing

**Changed**
- `lessons/1-4-workflow-shadowing.md` enriched from three further drafts: going to where the work is done, four varieties of work, where to sit and what to capture, tracing one transaction, unwritten rules, the observer effect, questions to avoid, invisible work, bottlenecks versus failure points, root causes, value and waste, cycle efficiency, the system-of-record conflict rule, data quality, loaded cost, the path personal data takes, ordered questions for classifying steps, three forms of human oversight, a bridge to Module 1.5, and a short reading list.
- `templates/workflow-map.md`: informal tools, apparent cause of each exception, a new section for unwritten rules, total cycle time, rework rate, what waiting leads to, where personal data moves, and access conditions. Sections renumbered 1 to 11.
- `rubrics.md`: a "weak performance" column in the workflow-map rubric. `glossary.md`: sixteen terms. `instructor-guide.md`: note for Module 1.4.

**Unchanged:** hours, in-class timings, the deliverable, the four step classes and all rubric weights.

**Verified and corrected** (`SOURCES.md` A36 to A45, B25 to B28, C24 to C25; `not-adopted.md` section و)
- Left out: "switching raises errors by up to 40%", a loaded-cost multiplier of 1.25 to 1.4, a four-hour rule for quotations, and new invented worked examples.
- Corrected: four varieties of work, not three; PDPL sensitive data as defined in the amended text; seven wastes plus a later eighth.
- `02-saudi-market-knowledge-framework/03-data-protection-pdpl/pdpl-founder-guide.md`, section 4: sensitive data now follows the amended definition; credit data is described separately under its own article.
- Every external link in the lesson was opened on 17 Nov 2026.
- Not adopted because they conflict with or duplicate published material: a fifth step class, two new map rubrics, two 100-point scorecards, an opportunity card, a new autonomy scale.

## v0.3 (2026-11-17)

Course 1 content, companion repositories and case studies.

### Companion repositories: Riyada and Bayan

**Added**
- `07-resources/companion-repositories.md`: what each of the three repositories is for, the integration rule (link, never copy), asset-by-asset maps to courses and modules, a "which one do I use" overlap table, and what was checked.
- `01-academy/learning-pathways.md`: one route across the three repositories, with five learner pathways.
- `05-agentic-ai-lab/exercises/`: eight exercises. R1 to R4 use Riyada (evidence scorecard and experiment card, context pack with linter, role card and approval matrix, 36-month model). B1 to B4 use Bayan (agent messages, bilingual landing page, pitch deck, RTL audit).

**Changed**
- A "Companion tools (optional)" section in all four course syllabi; cross-references in the toolkit, lab, skills, resources, framework pages, READMEs, roadmap and contribution guide.

**Notes**
- Nothing was copied from either repository. Reviewed at Riyada `d2a0607` and Bayan `db941e2`; both repositories' own checks pass and the commands in the exercises were run. Plugin installation and the exercises themselves have not been tried with learners.

### Course 1: Finding Your Agentic Opportunity

**Added** (`03-courses/01-opportunity/`)
- Seven lessons in Arabic with English terms, one per module, each with concepts, an activity, track differences, a quick review and common mistakes.
- Six sector briefs for Module 1.3: e-commerce, customs documentation, private clinics, real estate brokerage, accounting, HR back office. Candidate workflows are hypotheses; only sourced figures appear.
- Templates: workflow map pack, interview evidence pack, thesis template. Scoring and unit economics continue to use the Founder Toolkit.
- An annotated model thesis with invented data, a glossary, four-level rubrics, validation gates, an instructor guide and `not-adopted.md`.

**Changed**
- The Course 1 syllabus now links every module to its lesson, adds validation gates and extends the track differences. Structure, hours, the seven thesis sections and the rubric weights are unchanged.

**Verified and corrected** (details in `SOURCES.md`, A26 to A35, B19 to B24, C19 to C23)
- Unsourced market sizes, NPHIES volumes, licensee counts and per-workflow volumes from the drafts were left out.
- The Musaned recruitment figure refers to domestic workers; one draft's cost example did not add up; fabricated interviews became a labelled model.

**Not done yet:** slides, quizzes, role cards, a reading list, and a pilot with a cohort.

### Case studies

**Added**
- `06-case-studies/`: nine real cases summarised from public sources (Saudi: Tamimi Markets, Alsaif Gallery, Aramco Digital and OrbitronAI; international: SaaStr, Klarna, OPLOG, Simba Sleep, TrueLayer, Suitor), each with an evidence level, "what the source does not say" and questions for learners.
- Evidence levels (A company-reported, B vendor-reported, C announcement without results, illustrative scenario).
- Learner worksheet linking the cases to the five learning outcomes of the Opportunity course.
- `not-adopted.md`: claims from the drafts that were removed, corrected or reclassified.
- Two illustrative scenarios derived from the Tamimi case.

**Verified and corrected** (details in `SOURCES.md`, A17 to A25 and B12 to B18)
- No case is independently verified; all figures are company- or vendor-reported and labelled as such.
- Klarna is presented with its 2025 reversal. Unnamed Saudi examples and one untraceable company were removed.

## v0.2 (2026-11-16)

Saudi Market Knowledge Framework.

**Added**
- `02-saudi-market-knowledge-framework/`: a first-class section with twelve domains (establishment, AI regulation, data protection, cybersecurity, tax and finance, funding, intellectual property, e-commerce, employment, sector regulations, market intelligence, government procurement).
- Regulatory register with legal status (binding, official guidance, draft) and verification status for every instrument.
- Official directory of authorities.
- Founder's Agentic Compliance Checklist (one page, Arabic first).
- Saudi Agentic AI Governance Playbook.
- Founder-agent operating standard and the Saudi Regulatory Navigator agent.
- "Idea or question" issue template.

**Changed**
- Repository restructured: the former `03-saudi-market` and `04-saudi-regulations` folders are merged into the framework; remaining folders renumbered.
- Courses are now marked as planned for later iterations; the four syllabi are labelled draft outlines.
- Contribution guide rewritten: every contribution is welcome, with ten ways to contribute and a no-Git route.
- README reordered around what is available now.

**Verified and corrected** (details in `SOURCES.md`)
- Added: PDPL enforcement decisions, private-sector cybersecurity controls, new Copyright Law, AI Ethics Principles 2.0, AI Adoption Framework date, National AI Risk Management Framework, CST sandbox.
- Rejected or downgraded several claims from early drafts, including a CST "digital services regulation" that could not be found.

## v0.1 (2026-11-16)

First iteration: Foundation + Founder Toolkit.

- Bilingual README (Arabic first) and governance files.
- Academy framework: vision and mission, learning framework, eight-domain competency framework.
- Four dual-track course outlines (76 hours).
- Saudi market directory and regulations guides (now part of the framework).
- Founder Toolkit: ten bilingual templates and a cost-per-resolved-task calculator.
- Agentic AI Lab: ten entrepreneurial skills, five agent templates, evaluation template, Arabic model guide.
- Three illustrative scenario studies and a case-study template.
- Source register with verification status for every external fact.

# Changelog

## Unreleased

### First run of the agent templates with a real language model

- [Results](05-agentic-ai-lab/agent-templates/workflows/real-model-runs/README.md): the instructions of the five templates and of the Course 2 lab agent were given to Claude Fable 5.2 on 21 November 2026, one prompt per test case exactly as the Prepare node builds it, and the outputs were replayed through each workflow's Decide node.
- **Two defects found and fixed** in `src/common/prepare.js`: the booking instructions asked for a service "from the approved list" without giving the list (11 of 12 as shipped, 12 of 12 after), and the placeholder for the business name reached the model as written.
- After the fix: 47 of 47 model cases across the five templates. Lab at stage 3: 32 of 35 on the working set and 8 of 8 held out (the simulator: 30 and 6). The two lab cases the real model fails and the simulator passes are described and left for learners.
- `tools/n8n_replay_model.py` writes the prompts out and replays any recorded run; two new tests replay the recorded outputs on every change (`make check` now runs 92 tests).
- **Limits.** The model was not called through n8n's HTTP node; one sub-agent answered a workflow's cases in one session rather than in separate calls; one capable model, one run, temperature not controlled; invented cases. No local or small model was tried: none was available in the build environment or on the owner's machine.

### Recorded runs of the founder agents

- [Recorded runs](02-saudi-market-knowledge-framework/founder-agents/recorded-runs/README.md): the three test conversations of agents 2 to 12, 33 in all, run on 21 November 2026 with Claude Fable 5.2. The assistant saw each agent's definition and the pages it reads, and not the expected behaviour. Replies are kept verbatim, one file per agent.
- 30 conversations were consistent with the expected behaviour. 3 (the Financial Advisor's, the Pitch Coach's and the Tender Assistant's ordinary case) could not be exercised in full because the founder's numbers, the deck and the tender document the cases describe were not supplied; the assistant asked for them and invented nothing.
- **Limits.** One run, one assistant, from the model family that drafted the definitions; assessed by the session that ran the test; no founder involved. Agent 1 has no specified test conversations and was not run.

### Founder planning guide

- [Founder planning guide](03-courses/founder-planning-guide.md): a companion page for all four courses on when to plan and when to experiment (Agile, waterfall and hybrid planning). It is not a module and changes no hours or deliverables. Covers the four kinds of uncertainty mapped to the courses, four questions that sort every decision, fixed and open tracks in a Saudi agentic venture, stage-gated money, and the three lines of a customer agreement (what is fixed, what is variable, how the variable is swapped).
- Toolkit template 13, the [Hybrid planning sheet](04-entrepreneur-toolkit/13-hybrid-planning-sheet.md): assumption map, decision sort, the two tracks, gates, and the three lines. The toolkit now has thirteen templates.
- Built from four drafts supplied by the author, by the standing rule. Source register: A143 to A151 added; five draft claims corrected (B64 to B68), among them a success-rate table that mixed editions of the CHAOS report and "water-Scrum-fall" presented as a recommended method; two groups of unsourced anecdotes and rules of thumb left out (C50, C51).
- Lessons 1.7, 3.6 and 4.5 now point to the guide, and the Venture Workbook links the sheet and the guide at gate 1. The course decks are authored separately from the lessons and did not change.
- A [companion deck](03-courses/planning/slides/README.md) for the guide, sixteen slides, built by the same engine and listed on the landing page. It carries nothing that is not in the guide.
- **Limits.** The studies were read from abstracts and summaries, not in full. The contract section has had no legal review. Not tried with learners. The deck was rendered at 1600x900 and seven of its sixteen slides were inspected by eye.

## v0.9 (2026-11-20)

Founder agents and runnable templates. All twelve founder agents are now published, the five agent templates have runnable versions, and Course 2 has a low-code lab. **Nothing here has been tried with founders or learners, and nothing has been run with a real language model.**

### Founder agents

- Eleven new agents in [`02-saudi-market-knowledge-framework/founder-agents/`](02-saudi-market-knowledge-framework/founder-agents/README.md), one page each: Saudi Startup Advisor, PDPL Compliance Assistant, AI Governance Advisor, Saudi Market Researcher, Business Model Designer, Financial Advisor, Funding Opportunity Finder, Investor Pitch Coach, Saudi E-commerce Advisor, Government Tender Assistant and AI Startup Architect. Each has an Arabic definition to paste into any assistant, the pages it reads, and three test conversations: an ordinary case, a case where the right answer is "I do not know", and a case where the user pushes for a definitive answer.
- Every definition carries the operating standard as fixed rules: sources and verification dates from the attached pages, "to verify" labels passed on as they are, no article numbers, fees, amounts or eligibility criteria from memory, and no declaration of compliance.
- The Funding Opportunity Finder reads a directory of verified programmes only, separates funding from what is not funding, never says that applications are open, and names no programme that is not in the directory.
- **Limits.** The agents are definitions, not programs. No test conversation has been recorded with an assistant, and no founder has used them. The definitions were written from the repository's own pages and contain no regulatory fact of their own.

### Runnable agent templates

- Five importable n8n workflows in [`05-agentic-ai-lab/agent-templates/workflows/`](05-agentic-ai-lab/agent-templates/workflows/README.md), one per template: customer service, booking assistant, lead qualification, invoice reconciliation and tender summariser. One shape for all: the model proposes and a `Decide` node enforces the template's oversight table in code.
- They run on import with a keyword simulator (not a language model), no key and no cost, and can call any OpenAI-compatible endpoint instead. Model output that cannot be read does nothing; a stop switch sends everything to a person.
- Two guards were added while building: the tender workflow keeps a fact only if its text is on the page the model cites, and ties a requirement to the company profile by the bid team's own keywords, so a model that names the wrong profile entry cannot turn a gap into "meets".
- `tools/build_n8n_workflows.py` builds the workflows from readable sources; `tools/n8n_harness.js` runs their nodes without n8n; `tests/test_n8n_workflows.py` adds 12 tests (50 template cases, the stop switch, a model that answers nonsense, an unreachable model), and `tests/test_founder_agents.py` adds 3 for the agents' pages. `make check` now runs 90 tests, with one more that fails if a "to verify" mark returns to the knowledge framework. The logic tests need Node.js and are skipped without it.
- **Checked inside n8n 2.35.7** from the command line with `tools/n8n_e2e.py`: all six workflows imported and published, 84 requests to the live webhooks, none failed. The HTTP model path was exercised in n8n against a local stub only. The live run found one defect the harness had missed (the lab's approval flow read a node that had not run); it is fixed, and the harness now refuses that pattern.
- **Limits.** No real model, no messaging channel, calendar, CRM or ledger, no authentication on the webhooks, invented data and invented test cases. Not imported through the editor's menu, and not tried on n8n Cloud or n8n 1.x.

### Low-code lab for Course 2

- [Core-track lab: the same agent in n8n](03-courses/02-build/labs/lab-n8n-low-code.md). The order-enquiry agent of the eight labs as an n8n workflow whose nodes are a port of the Python reference. A test compares the two on every case at every stage (258 comparisons), and `labs/n8n/evaluate_n8n.py` scores the running workflow with the reference evaluator.
- Run in n8n: 24 of 35 at the baseline, 30 of 35 after the second cycle with the launch rule met, and 6 of 8 on the held-out set. The intermediate stages (25 and 28) were confirmed through the harness.
- This closes the item "no lab for a named low-code orchestrator" of the release-readiness report. n8n is used because the course names it for the core track; it is not a recommendation.

### Funding directory and regulatory register: verified entries only

At the owner's direction, both now keep only what was confirmed, and what could not be confirmed was removed. Every removed item and its reason is in the framework's [removal record](02-saudi-market-knowledge-framework/not-adopted.md).

- **Funding directory:** 31 verified entries and one that its operator marks inactive; no partly verified or pending entries. Every partly verified and pending entry was opened in a browser on its operator's site on 20 November 2026. Added from their own pages: ten more NTDP products (Loan Guarantee, Nextera, Connect, Tamkeen, Lead It, Bridge, Saudi Unicorns, and three that are not for founders directly: Fuel, Empowering Accelerators, Source Tech), MCIT's Code AI Catalyst, Wa'ed, Falak, Riyadh Valley Company and 9/10ths. The Garage, the Sanabil Accelerator, Monsha'at's AI Incubator and CST's sandbox moved from partly verified to verified. Removed: ten names and SAMA's sandbox, whose page returned an error. Fuel is corrected: it supports venture capital funds, not startups (A140, A141).
- **Regulatory register:** no "to verify" rows. Twenty rows or claims were confirmed against the issuer's site or the Bureau of Experts (A126 to A139), among them the current NCA control versions, the E-Commerce Law, the Labor Law amendments in force since February 2025, the Commercial Register Law in force since April 2025, the VAT rate, and CST's cloud regulations, which replace the framework the register used to name. Two rows and several unconfirmed claims were removed. The procurement row now says that the Ministry of Finance lists a new law next to the 2019 one.
- The Funding Opportunity Finder agent was updated for a directory that lists verified programmes only.
- **Domain pages, official directory and funding guides:** the same rule. No "to verify" mark remains anywhere in the knowledge framework. In the twelve domain pages, rows confirmed by today's sources were kept with their source and the rest removed. Every address in the official directory was opened: four were corrected (NTDP, CMA, Kafalah, Saudi Business Center) and one entry removed. The ecosystem and funding guides name only organisations whose own sites were opened; the events section was removed (A142).
- **Limits.** Register and domain rows were confirmed from official pages as returned by search, not by reading each instrument: several rows confirm that an instrument exists and is in force, and say so. Sector rows confirm the regulator's site, not the sector's rules.

### Housekeeping

- The Arabic and English READMEs were restructured as a landing page; the English README follows the Arabic structure.
- Source A1 now cites GASTAT's own publication for the 33.1% figure and records where the 2024 figure comes from.
- The roadmap's known-gaps heading and its courses target line reflect the current release.

### Not done

- An evaluation set from real Saudi-dialect messages: it needs a business willing to share anonymised messages. Every test case in the repository is still invented.

## v0.8 (2026-11-20)

The four courses are complete in content. Courses 3 and 4 received their first content; Course 2 received executable labs; every module now has a lesson, a deck, a quiz, an activity with a template and a sample solution; one completion standard and one fifteen-week kit cover the programme. **Not piloted and not professionally reviewed**: see the [release-readiness report](RELEASE-READINESS.md) for the status of every gap. The roadmap item previously planned as v0.8 (founder agents and runnable templates) moves to v0.9.

### Source re-check and reviewer invitations (20 November 2026)

- **Sources of Courses 1 and 2 re-opened:** 33 register entries hold as recorded. Three corrected: A29 (the 12-day clearance figure was wrongly dated 2017), A75 (the study gives one rejection rate, not a rate by service) and B20 (the eight-day average is in the sources). No figure in a lesson, sector brief or deck changed. Done by automated fetch; limits are in the [re-check record](03-courses/validation/source-recheck-c1-c2.md).
- **Reviewer invitations:** [messages in Arabic and English](03-courses/validation/review-packets/invitations.md) for the four specialist reviewers. No review has taken place.

### Remediation and release readiness (20 November 2026)

Status of every gap, tests, readiness by course and a go/no-go recommendation are in the [release-readiness report](RELEASE-READINESS.md).

- **Course 2 labs:** eight labs, one per module, with a tested reference implementation (Python, standard library only) that runs offline with a simulated model and reproduces the worked example: 24, 25, 28 and 30 of 35. Test data, configurations, expected outputs, troubleshooting, and an optional path to any OpenAI-compatible endpoint.
- **Decks for Courses 3 and 4:** thirteen decks authored slide by slide replace the generated ones. No overflow, no dense-slide notes.
- **Completion standard, version 1.0:** gates, no level 1, lead criterion at level 3 or above, weighted score of 2.7 or more; distinction band; evidence, remediation and certification eligibility. Applied in all four rubrics, with `tools/score_submission.py`.
- **Instructor kit:** fifteen weeks for all four courses, thirty session plans, four gates, a two-semester alternative, a completion record form.
- **Validation:** a desk walkthrough (not a pilot) with six findings corrected, a pilot protocol, and four specialist review packets with claim registers and unsigned sign-off forms. Ten regulated lessons state their verification status.
- **Guides:** a learner guide, an outcomes-to-assessment alignment, third-party attribution, contribution notes for reviewers, pilot organisations and code contributors.
- **Not done:** no pilot, no specialist sign-off, no English versions of the lessons.

### QA audit of the four courses (20 November 2026)

Findings, fixes, remaining gaps and a course-by-course readiness assessment are in the [QA report](03-courses/QA-REPORT.md).

- Slide decks for Courses 3 and 4: thirteen decks generated from the lessons by `tools/slides_from_lessons.py`, built with the shared engine, rendered and checked for overflow, and listed on the landing page.
- A [programme trainer guide](03-courses/TRAINER-GUIDE.md): the four courses at a glance, entry checks, one assessment standard with a recommended completion standard, where each activity's sample solution is, and how to prepare.
- Course 2 updated to the 2026 OWASP numbering (lessons 2.3 and 2.6, their decks, lab exercise R7).
- Navigation (previous, syllabus, next) in all 28 lessons. Missing sections added to the Course 1 and Course 2 instructor guides. Rubric level names and two Arabic security terms unified.
- [Sample solutions](03-courses/01-opportunity/examples/activity-sample-solutions.md) for Course 1 activities 1.2 and 1.3.
- The [courses index](03-courses/README.md) rewritten; stale "outline" notes removed from the learning and competency frameworks.
- Six structure tests in `tests/test_courses.py` so the gaps do not return.

### Course 4: Scale and Govern, first content release (20 November 2026)

Built from two drafts supplied by the owner, by the same rule: verify, keep the published syllabus, enrich. Hours (16), the five learning outcomes, the six-part scale pack and the rubric weights (30/20/20/15/15) are unchanged.

- Five new lessons in [`03-courses/04-scale-and-govern/lessons/`](03-courses/04-scale-and-govern/lessons/), Arabic with English terms: [4.1 the agent-operated company](03-courses/04-scale-and-govern/lessons/4-1-the-agent-operated-company.md), [4.2 monitoring quality and cost](03-courses/04-scale-and-govern/lessons/4-2-monitoring-quality-and-cost.md), [4.3 governance and risk](03-courses/04-scale-and-govern/lessons/4-3-governance-and-risk.md), [4.4 security for agentic systems](03-courses/04-scale-and-govern/lessons/4-4-security-for-agentic-systems.md) and [4.6 pitch and Demo Day](03-courses/04-scale-and-govern/lessons/4-6-pitch-and-demo-day.md). Lesson 4.5 already existed.
- A [worked example](03-courses/04-scale-and-govern/examples/worked-example-scale-pack.md) that carries the same invented store through four weeks of operation, including one bad week caused by an unpinned model version, and the six parts of the scale pack. All figures are invented, labelled and re-computed with the Academy's calculator.
- Five templates: [operating architecture](03-courses/04-scale-and-govern/templates/operating-architecture.md), [weekly KPI sheet and change log](03-courses/04-scale-and-govern/templates/weekly-kpi-sheet-and-change-log.md), [scaling roadmap](03-courses/04-scale-and-govern/templates/scaling-roadmap.md), [Demo Day run sheet](03-courses/04-scale-and-govern/templates/demo-day-run-sheet.md) and [scale pack checklist](03-courses/04-scale-and-govern/templates/scale-pack-checklist.md). The risk register, security assessment and pitch outline stay in their toolkits and are linked.
- Five new [quizzes](03-courses/04-scale-and-govern/quizzes/README.md) of ten questions (4.1 to 4.4 and 4.6); every lesson links its quiz.
- A [glossary](03-courses/04-scale-and-govern/glossary.md), [rubrics](03-courses/04-scale-and-govern/rubrics.md) with four levels and five validation gates, an [instructor guide](03-courses/04-scale-and-govern/instructor-guide.md) with buildathon rules, and a record of [what was not adopted](03-courses/04-scale-and-govern/not-adopted.md).
- Sources A120 to A124: NIST AI 600-1, the 2026 edition of the OWASP Top 10 for LLM Applications, the OWASP Top 10 for Agentic Applications, MAGNiTT's full-year 2025 investor count and regional share, and NCA's ECC-2:2024. Most are read through summaries, and each entry says so. Corrections B61 to B63 (the drafts cited ECC-1:2018 as current; "more than half" of regional venture funding is 45% for the full year; a requirement attributed to NIST AI 600-1 was not found). C49 lists what was not checked and not used. A84 now notes that the 2026 OWASP edition renumbers the list; Course 2 lessons and decks still cite the 2025 numbering.
- **Limits.** Modules 4.3, 4.4 and 4.5 are educational, not legal, security or investment advice, and have had no specialist review. No slide decks yet. Not piloted.

### Course 3: Launch and Business Model, first content release (20 November 2026)

Built from two drafts supplied by the owner, by the standing rule: verify, keep the published syllabus, enrich. Hours (20), learning outcomes, the five-part deliverable and the rubric weights (30/25/20/15/10) are unchanged.

- Six new lessons in [`03-courses/03-launch/lessons/`](03-courses/03-launch/lessons/), Arabic with English terms, in the format of Courses 1 and 2: [3.2 business models](03-courses/03-launch/lessons/3-2-business-models-for-agentic-ventures.md) (five pricing models, productised service versus software, the thin-wrapper test), [3.3 unit economics](03-courses/03-launch/lessons/3-3-unit-economics.md) (four scenarios, break-even success rate, price from value with cost as a floor), [3.4 compliance readiness](03-courses/03-launch/lessons/3-4-compliance-readiness.md) (controller or processor, seven questions and the evidence for each, conditional obligations as questions, buyers' AI-ethics questions, security basics, when to see a lawyer), [3.5 going to market](03-courses/03-launch/lessons/3-5-going-to-market-in-the-kingdom.md), [3.6 pilots and letters of intent](03-courses/03-launch/lessons/3-6-pilots-and-letters-of-intent.md) and [3.7 setting up the business](03-courses/03-launch/lessons/3-7-setting-up-the-business.md).
- Lesson 3.1 gains a section on Arabic in the live channel: the three-line opening message, fixed keywords handled in the application, and right-to-left handling.
- A [worked example](03-courses/03-launch/examples/worked-example-launch-pack.md) that continues Course 2's invented store through a two-week deployment and the five parts of the launch pack. All figures are invented, labelled and re-computed with the Academy's calculator.
- Four templates: [launch pack checklist](03-courses/03-launch/templates/launch-pack-checklist.md), [pricing memo](03-courses/03-launch/templates/pricing-memo.md), [buyer evidence pack](03-courses/03-launch/templates/buyer-evidence-pack.md) and [business setup checklist](03-courses/03-launch/templates/business-setup-checklist.md). Existing toolkit and compliance templates are linked, not copied.
- Six new [quizzes](03-courses/03-launch/quizzes/README.md) of ten questions (3.2 to 3.7), built from each lesson's Quick Review and Common Mistakes, with collapsed answer keys; every lesson links its quiz. Sixty questions generated from one data file so each key matches its option.
- A [glossary](03-courses/03-launch/glossary.md), [rubrics](03-courses/03-launch/rubrics.md) with four levels and five validation gates, an [instructor guide](03-courses/03-launch/instructor-guide.md), and a record of [what was not adopted](03-courses/03-launch/not-adopted.md) from the drafts and why.
- Sources A109 to A119: PDPL penalties, the data protection officer and controller-register rules, SDAIA's accreditation of AI service providers and its generative AI guidelines, the Commercial Register Law in force since April 2025, ZATCA's solution-provider directory, the central bank's list of licensed payment companies, two investor essays, the GAIA accelerator. Most are law-firm or press summaries, and each entry says so. Corrections B56 to B60 (among them: the 72-hour breach notice is conditional in the rule as read; the drafts' cost formula was replaced by the calculator's). Unverified C47 and C48.
- **Limits.** Modules 3.4 and 3.7 are educational, not legal or tax advice, and have not been reviewed by a lawyer or a tax adviser. No slide decks yet. Not piloted.

## v0.7.1 (2026-11-19)

Same-day additions after v0.7: five more venture journeys and a first round of funding directory verification from operators' own pages. The directory stands at 12 verified, 6 partly verified, 13 pending and 1 not active.

- Funding directory: TAQADAM, the Social Development Bank's Entrepreneurs Financing and the Misk Accelerator verified from their own pages (A108).
- Funding directory: five NTDP products (MVPLAB, Tech Crew, Boost, Transform+, Lendtech) read from their own pages in a browser and moved to verified, with the figures each page prints (A106); Fuel partly verified; Flat6Labs marked not active from its own page (A107), with a new `inactive` status in the index and checker. Two research summaries supplied by the owner were used as leads only: where they disagreed with a page, the page decided (B55), and what is still unchecked is listed in C46.
- Five venture journeys on Saudi companies building for agents in 2025 and 2026: [Wittify.ai](06-case-studies/ventures/wittify.md), [DEEP.SA](06-case-studies/ventures/deep-sa.md), [Lucidya](06-case-studies/ventures/lucidya.md), [MOZN](06-case-studies/ventures/mozn.md) and [Think](06-case-studies/ventures/think.md), from the owner's drafts and rewritten from open sources (A101 to A105). Funding rounds, investors and dates were confirmed; product names, accuracy figures, awards and accelerator histories that the sources read do not carry are listed as not found (C45), and one round was a pre-seed, not a seed (B54). The drafts' learner exercises are kept as the cases' questions. Twelve venture journeys in total.
- Funding directory: The Garage moved from pending to partly verified, read from its own site in a browser (A100). Seventeen entries remain pending.

## v0.7 (2026-11-19)

Business development domains, and the integration of an earlier university course.

### Five first guides (the roadmap's v0.7 scope)

- [Intellectual property](02-saudi-market-knowledge-framework/07-intellectual-property/ip-for-agentic-founders.md): chain of title, trade mark, copyright, secrets, patents, licences, and who owns what the agent produces.
- [E-commerce](02-saudi-market-knowledge-framework/08-ecommerce-digital-business/selling-online-with-an-agent.md): the ten criteria the Ministry of Commerce used to evaluate online stores, and what changes when an agent answers the customer.
- [Employment](02-saudi-market-knowledge-framework/09-employment-hr/first-hire-in-an-agent-native-company.md): employee, contractor, outsourced firm or freelance document; the February 2025 amendments as headings to ask about; who is accountable for each agent.
- [Sector regulation](02-saudi-market-knowledge-framework/10-sector-regulations/am-i-regulated.md): five questions, a one-page regulatory position memo, four worked examples.
- [Government procurement](02-saudi-market-knowledge-framework/12-government-procurement/selling-to-government.md): contracting methods, the direct-purchase cases that matter to a software supplier, guarantees and the SME exemption, subcontracting, grievances. **The law text read on the gazette site repeals the 2019 law; its decree number and effective date are not confirmed (C44).**
- Each guide states at its top what was read and what was not, prints no fee, rate or period it could not source, and ends with questions for a lawyer. All five await legal review. Sources A95 to A98; unverified C41 to C44.

### Venture journeys verified

- Every source cited for the seven venture cases was opened (the Aqar company page refused; the case says so and drops the figures taken from it). Corrections: Tabby's founding place is not stated by the sources read, only its move from Dubai to Riyadh; Tamara's "including secondaries" is the press's wording, not the company's; Tarjama's Saudi headquarters comes from sponsored content that names no city; Careem's case now carries the filing's figures (consideration US$3,003 million, goodwill US$2,484 million, three countries on delayed closing pending regulatory approval); Zid's Series A lead is dropped.

### Funding directory

- One entry moved from pending to partly verified (Sanabil Accelerator, from the operator's application page, A99). Eighteen remain pending; several official sites refuse automated requests.

### Integration of an earlier university course

Material from the author's earlier university course on software entrepreneurship (SE495, 2024), reviewed against what the Academy already has. Only what filled a gap was brought in, and every company fact was re-sourced.

**Added**
- Course 3, Module 3.1, [From prototype to MVP](03-courses/03-launch/lessons/3-1-from-prototype-to-mvp.md), with a ten-question quiz: the three rungs and the question each answers, what an agentic MVP must have, a six-item gate, a narrow first deployment and five weekly numbers. First lesson of Course 3; the other modules remain an outline.
- Course 4, Module 4.5, [Growth paths, funding and exits](03-courses/04-scale-and-govern/lessons/4-5-growth-paths-and-funding.md), with a quiz: choosing a path from the next milestone, who funds and what each expects, the six things an informed investor checks in an agentic product, and exits. It points to the funding guide and directory instead of repeating them.
- Founder Toolkit 11, [First Ten Customers Plan](04-entrepreneur-toolkit/11-first-ten-customers-plan.md), with `first_customers_funnel.py`; and 12, [Agentic Due-Diligence Pack](04-entrepreneur-toolkit/12-agentic-due-diligence-pack.md), with `round_dilution.py`. The general data room and round terms stay in Riyada and are linked, not copied.
- [Venture journeys](06-case-studies/ventures/README.md): seven sourced accounts (Foodics, Tamara, Tabby, Careem, Zid, Aqar, Tarjama) of how companies in this market were built, funded and exited. They are not evidence about agents and say so.
- `funding-directory.json` and `tools/check_funding_directory.py`: a machine-readable index of the funding directory, checked against the page in CI, with a warning for entries whose official page was last opened more than 90 days ago. The weekly link workflow runs it.
- Sources A88 to A94, corrections B50 to B53, unverified C39 and C40. Ten incubator names from an SE495 slide are listed as pending in the funding directory.
- Nine tests: the two calculators and the funding directory index.

- Lab skills: Pitch Challenger now runs as a three-investor panel scored on the Demo Day rubric; new skills 11 (Interview Rehearsal) and 12 (Sourced Case Builder). Twelve skills in total.
- Lab exercises A1 (Pitch Room), A2 (Interview rehearsal) and A3 (A sourced case), the first that use the Academy's own skills instead of a companion repository. Seventeen exercises in total. A2 states one rule without exception: a rehearsal with an assistant is never customer evidence.
- `case_lint.py` (exercise A3): checks a venture case for its five sections in order, a source level, source numbers that exist in the register, and figures outside the documented section. The seven published cases pass with `--strict`; a deliberately flawed sample gives five errors and one warning.
- [Venture Workbook](workbook/index.html): one static page with the gates of the four courses (24 items), one evidence note per item, saved in the browser only, exported as Markdown. A tick without evidence is shown as such and not counted. Linked from the landing page.
- [Instructor kit](01-academy/instructor-kit/README.md): a proposed 15-week, three-credit delivery of Courses 1 and 2 with Module 3.1, four graded gates and suggested weights, plus peer-evaluation, panel and buildathon judging forms. Not yet piloted.
- Four more tests (34 in total): the case linter and the workbook (its repository links exist; it makes no network calls).

**Not brought in, and why**
- The SE495 slide decks: generic, and Units 1 to 3 repeat Course 1.
- The SE495 case texts: unsourced, with factual errors in four of them (recorded in `06-case-studies/not-adopted.md`).
- DevOps, containers, serverless and interface-design slides: outside the Academy's scope and tool-specific.

## v0.6 (2026-11-19)

Courses 1 and 2 in full: slides, quizzes and practice interview records for Course 1; the first content release of Course 2 with its slides and quizzes; and a launch audit that removed duplication and added guards. Neither course has been piloted.

### Launch audit (19 November 2026, evening)

**Added**
- `START-HERE.md`: one bilingual page for a first visit (what the academy is and is not, a route for each kind of visitor, what is ready and what is not, frequently asked questions). It replaces the need for a wiki: everything stays under the link checker, the source register and the changelog.
- `index.html` and `.nojekyll`: a landing page and slide gallery, generated by `tools/build_site.py`, that lists all fifteen decks with their slide counts. It works when the repository is downloaded and is ready for GitHub Pages.
- `tools/build_slides.py` and `tools/slides/template.html`: one slide engine and one page template for every course, with `--check`. The two per-course copies of the template are gone; each course's `src/build.py` is now a three-line wrapper. The fifteen decks rebuild byte-identical.
- `tests/test_courses.py`: six tests. The landing page is up to date and lists every deck; built decks match their sources; every slide has speaker notes; slide counts in the slide READMEs match the decks; every quiz question has four distinct options and a key; every lesson links to its quiz. Twenty-one tests in all.
- `.github/dependabot.yml`: monthly updates for the GitHub Actions used by CI.

- GitHub Pages is on: the landing page and all fifteen decks open in the browser at https://malenezi.github.io/saudi-agentic-ai-entrepreneurship-academy/. READMEs, `START-HERE.md` and both slide READMEs link to it.
- `tools/check_external_links.py` and the `External links` workflow: every external link in the Markdown is opened weekly and on demand, and the result is written to the run summary as broken, could not verify, or ok. Informational; it never blocks a pull request.
- First run of the link check (19 November 2026): 229 links, 203 load, 22 refuse automated requests, 4 were broken. Three were fixed in `SOURCES.md` after opening the working address in a browser (A8 Saudi Gazette; A49 and A62 SAMA rulebook, whose host no longer takes `www`). The fourth, a SAMA news page cited in A62, no longer exists; the entry now says so.

**Fixed**
- Version state: READMEs, `CITATION.cff` and ROADMAP said v0.5 while main held Course 2 and the Course 1 materials. Now v0.6; the planned iterations move to v0.7 (business development domains) and v0.8 (founder agents).
- Stale statements: the learning framework said the courses "will be built later"; learning pathways said Courses 2 to 4 were outlines; ROADMAP counted six seed-level domains where the framework README lists five, and its first-year table said courses would start "after the framework matures".
- Both slide READMEs now say how to view a deck: GitHub shows an HTML file as source.


### Course 2 slides and quizzes (19 November 2026)

**Added**
- `03-courses/02-build/slides/`: eight Bayan HTML decks, one per module (118 slides in all), in Arabic with English terms, with speaker notes on every slide, print-to-PDF and evidence badges on every example. Deck 2.1 also opens the course. Built from the lessons; the decks add no fact or number of their own. Sources in `slides/src/`, built with `src/build.py` (a copy of Course 1's engine).
- `03-courses/02-build/quizzes/`: eight formative quizzes, one per module (80 questions), built from each lesson's Quick Review and Common Mistakes. Three question types; collapsed answer keys with explanations pointing to the lesson section; answer positions spread across the four letters, and option lengths balanced so the correct answer is not the longest.

**Changed**
- Every Course 2 lesson now ends with a link to its quiz and to the decks. Syllabus, instructor guide, rubrics, `not-adopted.md`, READMEs and ROADMAP updated. Quizzes are formative: the rubric weights (30/25/20/15/10) and the validation gates are unchanged.

**Limits**: no new facts or sources; not tried with learners.

### Course 2: Building AI Agents, first content release (19 November 2026)

Built from three drafts supplied by the owner, by the usual rule: verify, keep the published syllabus, enrich.

**Added**
- `03-courses/02-build/lessons/`: eight lessons in Arabic with English terms (2.1 agent anatomy, 2.2 context engineering in Arabic, 2.3 tools and integrations, 2.4 choosing a model, 2.5 evaluation, 2.6 guardrails and human approval, 2.7 from one agent to several, 2.8 failure analysis and iteration). Each has concepts, an activity, track differences, a quick review and common mistakes.
- `templates/`: tool contract, model selection memo, architecture decision record, failure and improvement log, readiness checklist, demo video outline. The agent design sheet, Founder Context Template, evaluation template and Human Oversight Matrix stay where they are and are linked, not copied.
- `examples/worked-example-order-enquiry-agent.md`: one illustrative build across the eight modules for an invented online store (35 cases; 24, 25, 28 then 30 passing; a held-back set; a pilot decision). All figures invented and labelled.
- `glossary.md`, `rubrics.md` (four levels per criterion, four validation gates, a checkpoint per module), `instructor-guide.md` (schedules, time splits, notes by module, reading list) and `not-adopted.md`.
- `SOURCES.md`: A80 to A87, B44 to B49, C37 to C38.

**Changed**
- `03-courses/02-build/syllabus.md`: structure, hours, deliverable and rubric weights unchanged; now links each module to its lesson and adds the validation gates and a list of what is still missing.
- READMEs, `03-courses/README.md`, ROADMAP and learning pathways now describe Course 2 as having its first content.

**Not adopted** (recorded in `03-courses/02-build/not-adopted.md`): ten learning outcomes, a second autonomy scale, seven error classes, a 30-case distribution that differs from the evaluation template, a tool-count threshold for splitting agents, named model versions, and a lab mapping that did not match the exercises.

**Limits**: slides and quizzes followed later the same day (entry above); not piloted; OWASP and Anthropic sources were read through search extracts or secondary summaries, as noted in SOURCES.md.

### Deck 1.1 demonstration screens (19 November 2026)

**Added**
- Deck 1.1 gains three slides (10 to 12; the deck is now 28 slides, the course 146): one illustrative screen for each of the three demonstrations (conversational assistant, tool-using research agent, bounded invoice-matching agent). The screens are drawn in HTML, use invented data, carry the «شاشة توضيحية» badge and name no product. The assistant's answer text is hidden on purpose so the slide makes no regulatory claim.

**Changed**
- `slides/src/_template.html`: styles for the screens (`.shot`, `.screen`); all seven decks rebuilt. Slides README and `content-pack.md` no longer describe placeholders; an instructor's own captures stay optional.

### Course 1 quizzes and practice interview records (19 November 2026)

**Added**
- `03-courses/01-opportunity/quizzes/`: seven formative quizzes, one per module (72 questions), built from each lesson's Quick Review and Common Mistakes. Three question types (understanding, application, spot the mistake), each tagged with the learning outcome it measures and its source in the lesson; collapsed answer keys with short explanations pointing back to the lesson section. Worked-example arithmetic matches the calculator (SAR 1.46 per resolved task, 75 customers to break even, five-month payback, break-even success rate about 78%).
- `03-courses/01-opportunity/practice-interviews/`: six invented 25-minute interview transcripts, one per role card in deck 1.5, in the speakers' dialects and following the lesson's six-part structure. Records ع1 to ع4 share one segment (prior approvals and rejected claims in private clinics in Riyadh); ع5 (finance controller, Dammam transport) and ع6 (fashion e-commerce founder, Jeddah) stand alone. Each has a turn-numbered transcript with deliberate interviewer errors, the interviewer's own evidence record (also with errors), questions for the learner, and a collapsed instructor key (moves by turn, evidence levels, said versus did, corrected record).
- `practice-interviews/synthesis-exercise.md`: the 30-minute synthesis exercise of lesson 1.5, using ع1 to ع4, with an instructor key and three traps.

**Changed**
- Every lesson now ends with a link to its quiz. Lesson 1.5 points the role-play and the synthesis exercise to the records.
- Syllabus, instructor guide, slides README and `not-adopted.md` list the quizzes and records as available; deck 1.5 speaker notes name the record for each role card.
- Quizzes are formative: the assessment map and its weights (50/20/15/15) are unchanged.

**Not added**
- No new facts or sources. Every person, business, figure and quote in the interview records is invented and labelled as such; the quizzes use only the lessons' content and the course's illustrative example.

### Course 1 slides (19 November 2026)

**Added**
- `03-courses/01-opportunity/slides/`: seven Bayan HTML decks, one per module (143 slides in all), in Arabic with English terms, with speaker notes, print-to-PDF, evidence badges on every example, and six role cards for the Module 1.5 interview lab.
- `slides/content-pack.md`: how the owner's two instructor raw-content packs were verified and merged, with a table of what was checked, what was corrected and what was not adopted.
- `slides/src/`: the deck fragments, the shared theme (slate, sandstone gold, off-white; a Sadu-to-graph motif) and `build.py`.

**Changed**
- Course 1 syllabus and instructor guide point to the slides; slides and role cards are no longer listed as missing.
- `SOURCES.md`: A73 to A79, B40 to B43 and C36 for the facts used in the slides.
- Lesson 1.7: peer review is now the owner's "investment committee audit" (15 minutes per pair, three stress-test questions); the four earlier questions remain the scoring guide.

**Verified in this pass**
- Klarna figures (company release, Feb 2024) and Intercom's $0.99 per outcome (Intercom help pages).
- WhatsApp Business pricing has been per message since 1 July 2025; Saudi rates quoted from business pages that cite Meta's 1 October 2026 card.
- NPHIES claims use ICD-10-AM and the Saudi Billing System (BMC Health Services Research, 2025); initial claim rejection of 15 to 25% (KPMG Middle East, June 2026, via press).
- Owner's follow-up sources on Tabby and Tamara: Tabby's read-only MCP server for coding agents (used in deck 1.1) and Tabby's 2026 shopping survey (used in deck 1.3, labelled as a company survey). Neither shows agents in either company's operations (C36).

**Not adopted** (details in `content-pack.md`)
- Tamara/Tabby as an agent case (no public evidence); unsourced market price ranges; named-vendor judgements; a seven-level autonomy ladder, a ten-criterion scorecard, renamed thesis sections and rubric, and a second set of worked-example numbers, all of which conflict with the published course.

## v0.5 (2026-11-18)

Founder essentials in depth. First part, 18 November 2026: the PDPL worked example, the funding directory and the first tax guide. Second part, 18 November 2026: the establishment walkthrough. Third part, 18 November 2026: Arabic versions (`.ar.md`) of the seven English-only guides and five domain READMEs (domains 02, 03, 04, 06, 11); three were translated by the owner and reviewed, nine by Claude, none lawyer-reviewed. Fourth part, launch audit, 18 November 2026: Arabic version of the regulatory register; READMEs and CITATION.cff moved to v0.5. The funding directory's "to verify" entries move to v0.6; each is labelled as unverified in the directory.

### Establishment (domain 01)

**Added**
- `01-business-establishment/establishment-walkthrough.md`: from idea to commercial register, in Arabic. A comparison of the sole establishment, the limited liability company and the simplified joint-stock company as the Ministry of Commerce pages and the Companies Law state them; trade name reservation; the Saudi path step by step; the foreign-founder path through the Ministry of Investment, including the entrepreneurial category; fees as printed with a worked total; what registration does automatically and what it leaves to the founder; what an agent may and may not do; a founder's data sheet; seven questions for a lawyer. **Sources checked; not reviewed by a lawyer.**

**Changed**
- Domain 01 page: instruments table with verification marks, the walkthrough as the starting point, and the open items (C29, C33 to C35).

**Verified in this pass**
- The Ministry of Commerce service pages state that registration completes automatically with human resources, ZATCA, GOSI, Saudi Post and the Chamber of Commerce (C30 resolved). They do not say this includes VAT registration.
- The simplified joint-stock company has no minimum capital (Companies Law, Art. 139(2)); the ordinary joint-stock company's SAR 500,000 does not apply to it.
- All three services require that the applicant or partner is not a government employee. No exception is stated; the walkthrough lists it as a question for a lawyer.

**Found conflicting; treatment settled 18 Nov 2026, later pass**
- The sole-establishment register fee: 500 on its service page, SR 200 on the Ministry's start-your-project page. The walkthrough now uses 500 as the planning figure (the page is for the service itself and dates from the new law's start), says not to add the two, and says to confirm at payment (C35).
- The supervising authority for an entrepreneurial establishment: a Saudi university or accredited incubator in the Investor Guide; a venture capital fund or business incubator in the Ministry of Investment's FAQ (C34). Kept open: no merged list is presented, and the walkthrough tells the founder to ask the Ministry in writing.

**Not found**
- A list of software or AI activities that need a licence (C33); fees for entrepreneurial registration at the Ministry of Investment (C29).

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

`SOURCES.md` A49 to A72, B32 to B39, C28 to C35; D3 to D6 updated. `02-saudi-market-knowledge-framework/not-adopted.md` records what was taken from the five drafts, what was corrected or dropped, and what was deferred.

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

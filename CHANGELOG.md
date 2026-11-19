# Changelog

## Unreleased

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

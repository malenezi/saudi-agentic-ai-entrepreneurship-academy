# Changelog

## Unreleased

### Methodology library, sixth batch: requirements, data and software engineering (26 November 2026)

- **Nineteen cards.** Requirements and design: Use Case Diagram, Activity Diagram, State Machine Diagram, Component and Deployment Diagrams, C4 Model, Software Requirements Specification, Architecture Decision Records. Data: Dimensional Modeling, Data Governance Framework, Data Classification, Data Protection Impact Assessment. Software engineering: Test-Driven Development, Agentic Coding, Prompt Engineering, Code Review, Semantic Versioning, Observability, Site Reliability Engineering, MLOps / LLMOps. The library has 85 cards and lists 40 more by name.
- **Four diagrams**, drawn by `tools/build_diagrams.py` from the same specification file: a use case diagram, an activity diagram, a state machine and a C4 system context diagram. Fourteen in all; each is the library's own drawing.
- **Merged.** System Context Diagram into the C4 card; Component and Deployment diagrams into one card; Software Architecture into the decision-records and C4 cards; Data Modeling and Database Schema into the existing entity-relationship card; Data Pipeline Diagram into the existing data flow card. **Dropped:** "Modern Data Architecture", a general label with no source of its own.
- **Held back for want of a source.** Data Lifecycle: the page opened says the national standards describe five stages and names them only in an image.
- **Sources A234 to A252, each from the fetched page, with what the page did not say.** The three Saudi data cards are the weakest-sourced: the NDMO standards and the classification policy were **not opened**; the fifteen domains and the assessment steps come from a software vendor's explainer, the four levels from Saudipedia and a public university's policy page, and the impact-assessment cases from a law firm's 2023 reading of the regulation (A244, with A50 for the article). Each card says so and tells the reader to read the official text. The state machine card rests on a Wikipedia article because the teaching page could not be opened. The requirements card names ISO/IEC/IEEE 29148:2018 from its catalogue page; the standard was not read.
- **Limits.** Three cards cite a vendor on its own subject (Anthropic twice, Google Cloud), marked as such; the Academy recommends no tool. The "LLMOps" half of the MLOps card and the idea of versioning prompts and models with code are the Academy's, labelled so. The impact-assessment template is not an official form and the card is not legal advice. No card tried with a learner.

### Methodology library, fifth batch: venture formation and product management (26 November 2026)

- **Sixteen cards.** Venture: Disciplined Entrepreneurship, Customer Development, Effectuation, OKRs, Balanced Scorecard, Pre-mortem, North Star Metric. Product and project: Scrum, Work Breakdown Structure, Product Roadmap, User Stories and Acceptance Criteria, RACI Matrix, MoSCoW Prioritization, RICE Scoring, Critical Path Method, BPMN. The library has 66 cards and lists 66 more by name.
- **Merged.** Build-Measure-Learn and Hypothesis-Driven Development are covered by the Lean Startup card; Risk Matrix by the agent risk register card.
- **Held back for want of a source.** Impact-Effort Matrix and AARRR Funnel stay on the waiting list: the page opened for each did not state what a card would need (NN/g's article does not define the matrix or name its quadrants; the 2007 post does not list the five stages). Recorded in the library's `not-adopted.md`.
- **Sources A218 to A233, each from the fetched page.** Where a page stopped short, the card says so and claims no more: the Disciplined Entrepreneurship card names the framework and does not list its 24 steps (the site does not, and the book was not read); the Customer Development card rests on the open introduction of Blank's article plus A189 for the term; the WBS card does not attribute the "100% rule"; the effectuation card does not name the theory's originator because the page does not. The draft's Arabic rendering of Effectuation as «التفكير الاحتمالي» is replaced by «منطق التأثير».
- **Limits.** Four definitions come from vendors writing about their own field (Atlassian twice, Amplitude, Intercom), marked as such. No card tried with a learner.

### Methodology library, fourth batch: opportunity discovery and the business model (26 November 2026)

- **Fifteen cards.** Opportunity: Empathy Map, The Mom Test, Assumption Mapping, TAM / SAM / SOM, PESTEL Analysis, Porter's Five Forces, SWOT Analysis, Value Stream Mapping, Five Whys and Fishbone Diagram, Service Blueprint. Business model: Lean Canvas, Pricing and Revenue Models, Product-Market Fit, Kano Model, Blue Ocean Strategy. The library has 50 cards and lists 85 more by name; the opportunity domain is complete.
- **Merged.** Unique Value Proposition is a section of the Lean Canvas card; Revenue Model and Pricing Models are one card, labelled as the Academy's own classification because its five-model table already lived in toolkit template 5.
- **Sources A206 to A217, each from the opened page** (fetched, not search extracts). Where a page did not say what the proposal assumed, the card says so: The Mom Test's site states no rules and the book was not read, so the card names the book and uses the Academy's own interview questions; CIPD's SWOT factsheet does not label internal and external; Andreessen's essay sets no numeric threshold for product-market fit. Two definitions rest on Wikipedia and are marked as vocabulary only.
- **Limits.** No card tried with a learner. Porter's article was read only as far as the open page shows. Blue Ocean's own tools are not reproduced. Competitive Advantage has no card yet.

### Methodology library, third batch: the practitioner tier and diagrams (26 November 2026)

- **Thirteen cards:** UML Class Diagram, Sequence Diagram, Entity Relationship Diagram, Data Flow Diagram, Swimlane Diagram, Retrieval-Augmented Generation, Model Context Protocol, Multi-Agent Orchestration, Spec-Driven Development, Technical Debt Management, CI/CD, LLM Evaluation, Threat Modeling. The library has 35 cards and lists 102 more by name. Multi-Agent Architecture and Agent Orchestration became one card.
- **`tools/build_diagrams.py`** draws the library's diagrams as SVG from one text specification (`09-methodology-library/diagrams/diagrams.json`): boxes on a grid with arrows and optional lanes, or a sequence of messages; right-to-left layout; a title, a description and Arabic alternative text in every file; standard library only. **Ten diagrams**, all illustrative: class, sequence, entity-relationship, data flow, swimlane, agent architecture, human oversight, multi-agent orchestration, RAG and MCP. The agent-architecture and human-oversight cards of the first batch now show theirs.
- **Why not Mermaid.** The site's reader loads no script from outside the repository, so a Mermaid block would show as text there. SVG files show on GitHub and on the site alike. Recorded in the library's `not-adopted.md`.
- **Checks.** The build refuses a diagram no card shows; the diagram tool refuses two nodes in one cell, an edge to a node that does not exist, and a label too long to fit between two boxes. `tests/test_library.py`: thirteen tests. Sources A197 to A205.
- **Limits.** All nine new sources were read from search extracts, not from the opened page; the UML and BPMN specifications themselves were not opened, and the cards use them for what a diagram is, not for notation rules. The diagrams are simplified teaching drawings, not standard-conformant UML or BPMN. Edges are straight lines and can cross a box in a dense layout; each diagram was looked at once in headless Chrome. GitHub's Spec Kit was not tried. No card tried with a learner.

### Methodology library, second batch: the Academy's own agent models (26 November 2026)

- **Eight cards**, each labelled as developed by the Academy and not as a standard: Agent Opportunity Assessment, Agent Business Model Canvas, Agent Capability Matrix, Agent Tool-Access Matrix, Agent Risk Register, Agent ROI Calculator (the customer's return), Agent Readiness Assessment, Shadow Mode. Five point at tools that already existed (toolkit templates 2 and 5, `buyer_return.py`, the compliance toolkit's risk register, the shadow-mode switch and report); the library now has 22 cards and lists 116 more by name.
- **Three new bilingual templates** in `09-methodology-library/templates/`, for the three models that had none: the agent capability matrix (what the task needs the agent to do, who provides each capability, and the evaluation cases that prove it), the agent tool-access matrix (every tool side by side: system, read or write, reversible, account, oversight level A to D), and the agent readiness assessment (seven yes-or-no questions answered with the customer, and where to start for each "no").
- **Merged, not duplicated.** Of the proposal's twelve "Agent" models, the architecture canvas, the evaluation canvas and the autonomy and responsibility matrices are served by the existing cards for agent architecture, agent evaluation and human oversight, whose templates were already in the toolkit, the lab and the compliance toolkit. The human-oversight card now links the oversight matrix (levels A to D) and the autonomy ladder of Module 1.1. Recorded in the library's `not-adopted.md`.
- **Checks.** The build now refuses a library template that does not say, in Arabic and English, that the Academy developed it, and one that no card uses. `tests/test_library.py`: eleven tests. Each syllabus links the new cards of its course.
- **Limits.** The three templates and the readiness questions are new and were tried with no learner and no business; the readiness assessment sends its data-protection question to the PDPL self-assessment and a legal adviser and answers nothing itself. No new outside source was read for this batch: the one external reference, OWASP's "excessive agency", is the existing A84.

### Methodology library, first batch (26 November 2026)

- **New section `09-methodology-library/`**: one standard card per framework, method or model a founder needs, in Arabic with English terms. Twelve fixed parts per card: purpose, when to use, when not to use, inputs, steps, template, an illustrative example, how an AI agent helps, output, quality criteria, source and licence, and where the Academy uses it. **Fourteen cards** in this batch, the essential tier: Design Thinking, Jobs to Be Done, Value Proposition Canvas, Business Model Canvas, Lean Startup, MVP, Customer Journey Map, Kanban, AI Agent Architecture, Agent Workflow, Human-in-the-Loop, Agent Evaluation, Unit Economics, Go-to-Market. **126 more are listed by name** and are written in batches.
- **`library.html`**, a page that filters the cards by course stage, tier, type, domain and origin, with a search box; linked from both landing pages. Each of the four syllabi links the cards its course leans on.
- **`tools/build_library.py`** builds the index and the page from `library.json` and refuses a widely known model with no source in section A of `SOURCES.md`, a card with a missing part, a `used_in` path that does not exist, and an Academy model that does not say it is one. `tests/test_library.py`: nine tests.
- **Built from a proposal the owner supplied** (131 names in ten domains), under the verify-then-build rule. Fifty-five of the names appeared nowhere in the Academy; ten of its twelve "Agent" models already existed under other names in the toolkit, the lab and Course 4. What was merged, dropped, corrected and added is in the library's `not-adopted.md`.
- **Other people's canvases are described and linked, not bundled.** The Business Model Canvas and the Lean Canvas are CC BY-SA 3.0 and the Value Proposition Canvas is under copyright with adaptations and software inclusion reserved (A187, A188); the Academy's content is CC BY 4.0. OpenStax *Entrepreneurship*, named in the proposal as a founding reference, states CC BY-NC-SA 4.0 on its live pages (A196, B75): cited only.
- **Limits.** No card has been tried with a learner. Ten of the twelve new sources were read from search extracts, not from the opened page, and two (the Jobs to Be Done article and the unit-economics case) from a description of a paywalled text; each row in `SOURCES.md` says which. The page was viewed in headless Chrome only. No Mermaid diagrams yet, no methodology agents, no English cards.

### An HTTP runner with an audit log (25 November 2026)

- **`tools/reality_run.py`**, the first piece of v0.14. `run` posts a list of messages to a running webhook and writes one line per message: time sent, latency, action, level, outcome, the rule in code that decided (`gates`), and fingerprints of the message and of the reply. The customer's text is not written unless `--keep-text` is passed. `--expect store` or `--expect failures` adds a verdict against the invented store; the command exits 1 if the agent acted alone anywhere or a request failed. `report` prints the figures of a log. `serve` is a stand-in for n8n that answers with the workflow's own Code nodes.
- **Run inside n8n 2.35.7** (keyword simulator, no language model): template 1 with the invented store's Config gave over HTTP what its nodes give outside n8n, 73 of 85 with 4 acted alone and failure cases 16, 6, 8; median latency 105 ms with no model call. The two logs are kept in `agent-templates/workflows/audit-logs/` and read by a test. The same day, on a fresh import of all six workflows after the change to template 1, `tools/n8n_e2e.py` gave 100 requests with no failure.
- **Limits.** The log holds what the workflow puts in its answer: no token counts, no cost. The stand-in is not n8n: no HTTP model node, nothing kept between requests.

### Third local-model run of the store, after the topic list and the code-side check (25 November 2026)

- **The run.** qwen2.5:3b on the owner's laptop, 225 prompts in 16.3 minutes, outside n8n: the store's 85 messages **58** with **4** acted alone (54 and 11 on 24 November), its failure cases 22 right, 0 degraded, 6 acted alone, 2 wrong but safe (17, 1, 11, 1), templates 39 of 47 (43), lab 30 of 35 and 7 of 8, dialect cases 13 of 14. Recorded under `real-model-runs/local-qwen2.5-3b-run3/` and replayed by a test.
- **Found.** The code-side check fired on fresh answers as it did on the replay. `also` was again never filled. Listing the store's topics in the instructions did not improve the reading and added an error: a topic key written as the intent in 10 of 85 messages, handed over as not understood. A repair for it was tried by replay and not adopted, because one more message was acted on alone in each set. Templates 2 to 5 moved between runs on unchanged prompts.
- **`tools/local_run_pack.py`** writes the folder that runs every prompt against a local model on Windows (prompts from the workflows' own Prepare nodes, a PowerShell script, a file to double-click). The earlier package was never in the repository.

### Template 1: a request the model did not name is looked for in code (25 November 2026)

- **Why.** In the local-model run of 24 November the model never filled `also`, so the multiple-request gate did not fire once, and it labelled cancellations, promises and complaints as order questions.
- **What.** Decide now checks the customer's own message, whatever the model returned: the words listed in Config for requests that need a person, and more than one stored order in one message. Where the model saw only a question and one such request is found, the stricter reading replaces the model's; anything else goes through the gate and the whole message is handed over. A one-sentence question tied to an approved topic is still answered. Logged as `intent_by_code`, `also_by_code` or `orders_named`. `second_request_check: false` in Config switches it off.
- **Measured by replay of the recorded answers, not by a new run:** the store's 85 messages 60 in place of 54, acted alone 5 in place of 11; failure cases 18, 1, 10, 1 in place of 17, 1, 11, 1. Simulator: 73 of 85 unchanged; failure cases 16, 6, 8, 0 in place of 15, 7, 8, 0. The run record keeps the figures as run.
- **Limits.** The check knows only the words in Config: ten failure cases still end with the agent acting alone, four of them compound messages worded outside the list. A refund request the model calls a policy question is answered with the policy text. Tested outside n8n when it was made; imported into n8n later the same day (see the runner's entry above). Run with a model the same day: see the entry above. 161 tests then.

### Video series: from opportunity to venture (25 November 2026)

- **Four short Arabic videos** in `assets/videos/` (1:36, 1:31, 1:35, 1:48; 720p, about 12 MB together), with poster frames and the spoken text in `transcripts.md`: the opportunity, chatbot against agent, checking demand before building, and the Saudi market. Scripts by the Academy's owner; he watched the four videos and approved them.
- **Shown on both landing pages** in a new section under the opening, and linked from both READMEs.
- **`tools/video_series/`** builds them from text: narration and scenes in `content.py`, a page template, speech from an open Piper voice, a generated music bed, filming with headless Chrome. It needs packages outside the standard library and is not run by `make check` or CI; `THIRD-PARTY.md` says so.
- **Limits.** Synthetic voice with some weak consonants, checked by machine transcription and by the owner's ear, not by a language editor. Motion graphics only. Longer than the 65 to 80 seconds first planned. The licence of the voice's training data is not established, and `THIRD-PARTY.md` records that. Figures are those of v0.13. No change to readiness: no course has been piloted.

## v0.13 (2026-11-24)

From template to a first paid pilot: shadow mode, a token on the webhooks, repair and one retry of unreadable model output, an invented store to practise on, a pilot terms sheet, and a second run with a small local model.

**Still true: no course has been piloted, and no lawyer or tax adviser has reviewed the framework. Nothing in this release was tried with a business or with learners.**

### Second local-model run, and what it changed (24 November 2026)

- **The run.** qwen2.5:3b on the owner's laptop answered 225 prompts in 17.3 minutes, outside n8n, with the workflows' retry: templates 43 of 47 (38 on 22 November), Course 2 lab 28 of 35 and 7 of 8 (31 and 7), the invented store 54 of 85 with 11 acted alone (simulator: 73 and 4), its failure cases 17 right, 1 degraded, 11 acted alone and 1 wrong but safe, dialect cases 12 of 14. Recorded under `real-model-runs/local-qwen2.5-3b-run2/` and replayed by a test.
- **Found and fixed after the run, not re-run:** template 1's instructions named the default store's topics, so another store's questions could not be labelled; Prepare now appends the keys of the approved knowledge in Config. Square brackets written around key and value pairs (one answer in five) are now read as an object.
- **Found and not fixed:** the model never filled `also`, so the multiple-request gate did not fire once with it; the same lab prompts gave 28 where they gave 31 two days earlier.
- **The 85 messages of the invented store** were read and approved without change by the Academy's owner, a native Arabic speaker, on 24 November 2026. No dialect labels and no second reader; the thirty failure cases and the dialect cases are not reviewed.
- **`.gitattributes`:** the built decks, the two landing pages, the site index and the built workflow files are marked as generated, so GitHub's language bar counts hand-written files. GitHub folds marked files in a pull request's diff.
- `tools/n8n_replay_model.py` passes a recorded second answer to the harness and replays the store and the dialect cases. 153 tests.

### Agent templates: unreadable model output, and what customers actually type (24 November 2026)

- **Repair and one retry of unreadable model output**, in all six workflows. Two nodes sit between the HTTP model node and Decide. An answer that is not one JSON object is repaired where that changes no meaning (text or a code fence around the object, curly quotes, a trailing comma, Python's `None`/`True`/`False`, a bare word where a string was meant); otherwise the model is asked once more with a fixed instruction, without the customer's text being added again. What is still unreadable never acts, as before. `log.model` records `repaired`, `retried` and `unreadable` only when one of them is true. `retry_unreadable: false` in Config switches the second call off.
- **Replay of the local-model run of 22 November through the new nodes:** lead qualification 11 of 12 in place of 8, templates together 41 of 47 in place of 38. The first run is unchanged at 47 of 47. A replay, not a new run.
- **Prepare:** hidden direction marks are stripped; a customer can no longer close the `<customer_message>` wrapper by typing its tag; a Saudi mobile number is written in one form (`9665…`, `+9665…`, `009665…` and `5…` become `05…`), so the owner of an order is no longer refused for the spelling of the number. `normalise_account: false` switches it off.
- **Template 1:** an order reference is resolved to its stored key however it is typed ("S 2001", "#S2001", bare digits when exactly one key fits), and a reference whose digits are not in the customer's message is dropped. A message with more than one request is no longer answered in part: the model names the others in `also`, and Decide hands the whole message over as `handover_multiple_requests` at the strictest level among them. Deliberately conservative: two harmless questions in one message also go to a person.
- **Template 3:** a request to stop being contacted is matched in code (`stop_phrases` in Config) before the model's answer is used.
- **Thirty failure cases** for template 1 in the invented dataset (`failure-cases.jsonl`, `tools/dataset_pack.py failures`) and **fourteen dialect cases** for templates 2 to 5 (`src/<template>/dialect-cases.json`), with three more recorded as limits of the keyword simulator. Simulator on the failure cases: 15 right, 7 safe but degraded, 8 acted alone, against 10, 10, 9 and one refusal of the rightful owner before these rules. The dataset baseline is unchanged at 73 of 85; D-082 now accepts the new handover, and the simulator's reference pattern was widened.
- **Limits.** All messages were written by an AI assistant to hit weak points on purpose and were not reviewed by a native speaker; the failure-case figures are not a performance measure. Tested outside n8n with canned model answers, and inside n8n 2.35.7 against a local stub model (repair, one retry carrying the customer's text once, handover after two unreadable answers, the `also` gate, the stop rule; `tools/n8n_e2e.py`: 100 requests, none failed). Whether a language model names a second request in `also`, or returns `unknown` for the four out-of-list requests the simulator answers, has not been tried. 150 tests.

### Courses 3 and 4: shadow mode in the deck and quiz, four lesson edits, a pre-merge checklist (24 November 2026)

- **Module 3.6:** the deck has a slide on shadow mode (13 slides) and the quiz an eleventh question on what must be signed before the first message. Section 8 of the lesson was already there.
- **Lessons 3.4, 3.7, 4.3 and 4.4**, one structural edit each from a desk review of the four unreviewed modules: 3.4 points the buyer's "what did the agent do and when" to the shadow-period report; 3.7's activity tests the agent's limits with two messages (log in with my account, pay from my card); 4.3 shows a seventh risk line, the request dropped from a message that carries two; 4.4's injection set gains two categories (closing the wrapper tag, two requests in one message). One checkpoint question added per module in the two rubrics.
- **`CONTRIBUTING.md`:** a fourteen-item list of what to check before opening a pull request, in both languages. Items 6 to 14 are what `make check` does not cover.
- **Not done here.** The same desk review listed fifteen further notes that need an official source or a specialist (among them: Module 3.7's tax section does not mention zakat or income tax; Module 3.4 has no question on data-subject requests). None was changed. The four modules are still not reviewed by a lawyer, a tax adviser or a security practitioner.

### README: two statements brought in line with the record (24 November 2026)

- "What is available now" said the runnable templates had not been run with a real model. Their instructions were run twice outside n8n (21 and 22 November 2026), as the readiness table of the same page says; the row now says so and links the results. Still not run through the HTTP node, and no channel connected.
- "Why now" gave 27.6% for 2024 as GASTAT's own figure. The 2025 publication does not print it; it is Arab News' report of the 2024 edition (entry A1). Both READMEs now say so.

### Arabic landing page: editorial, RTL and SEO revision (24 November 2026)

- **Arabic landing page (`index.html`, from `tools/build_site.py`) rewritten.** The opening says what the Academy is, whom it serves, the problem (GASTAT 2025, entry A1, with its check date) and what a learner builds. New sections: the four courses with hours, level and deliverable; a starting point for six kinds of reader; readiness in three columns (available, in development, not yet tested); one "contribute" section. The decks are now under one heading with a sub-heading per course. Every figure was already in the repository; none is new.
- **Arabic wording revised** in `README.md`, the Arabic half of `START-HERE.md` and the reader (`read.html`). The Academy's name, the course titles and the lab's name are unchanged. In running text: «الذكاء الاصطناعي القائم على الوكلاء», «منشأة في المملكة», «التطوير منخفض البرمجة (Low-Code)», «جارٍ تطويره», «لم يخضع للاختبار حتى الآن», «الجاهزية والشفافية», and principle 5 reads «لا معلومة رقمية دون مصدر موثوق وتاريخ تحقق». All disclosures about piloting and legal review are kept. The README section "مستوى الجاهزية" is now "الجاهزية والشفافية"; no other anchor changed.
- **RTL and layout:** the hero puts the text first and the banner beside it (below it on a phone); card grids no longer overflow under 350 px; a skip link; slide counts follow Arabic number agreement (10 شرائح, 11 شريحة); primary buttons meet AA contrast. The English page takes the same layout with its text unchanged.
- **Discoverability:** Arabic title, description and Open Graph text; canonical address, `hreflang` pairs, absolute preview image with dimensions and alternative text, and a `WebSite` JSON-LD block on both landing pages.
- Not changed: `README.en.md` and the English page's text.

### Arabic terminology carried through the repository (24 November 2026)

- The wording of the landing page now holds in 48 pages and three decks (2.1, 2.3, 4.6): «منخفض البرمجة» for «منخفض الكود», «منشأة في المملكة» for «منشأة سعودية», «لا معلومة رقمية دون مصدر» (with «موثوق وتاريخ تحقق» where the rule is stated in full) for «لا رقم بلا مصدر», and «العربية أساساً» for «عربي أولاً» where it named the principle.
- Left as written: the recorded runs of the founder agents (they are transcripts), earlier changelog entries, «بالعربية أولاً» where it means "write the Arabic before the English", and «عميل يدفع» where it is the graduation criterion. No figure, link, heading or anchor changed.

### README: a new opening (24 November 2026)

- Both READMEs now open with the problem (GASTAT 2025, entry A1), what the Academy contains in six lines, its status, and three commands that run the Course 2 reference agent with no key. The commands were run on 24 November 2026 and returned `reply_status`.
- The twelve-item contents list is removed from both; GitHub generates one. No section or anchor changed.

### Agent templates: shadow mode (23 November 2026)

- A `shadow_mode` switch in the Config of the five runnable templates. When it is on, a template decides as usual and nothing leaves it: no reply draft, handover, approval request, staff notice or write. What it would have done is kept under `shadow.would`, with the caller's `ref` for the message. Templates 2 and 4 work on a discarded copy of their stored data, so no booking or draft is kept and nothing can be approved.
- `tools/shadow_report.py` compares a shadow log with a record the customer's staff fill in (outcome, minutes, verdict on the agent's draft) and prints the counts, starting with the messages where the agent would have acted and the staff did not. It sets no threshold.
- [`shadow-mode`](05-agentic-ai-lab/agent-templates/workflows/shadow-mode/README.md): a guide and an invented sample of twelve messages answered by the keyword simulator.
- Lesson 3.6 has a new section 8 on a shadow period before a pilot, and Course 3 a [shadow-period report](03-courses/03-launch/templates/shadow-period-report.md) template. The lesson says that a shadow period still processes real personal data, so the data terms are signed before it starts.
- Seven new tests. Not tried with a business. Run inside n8n 2.35.7 the same day on templates 1, 2 and 4: the twelve sample messages gave the published log, and a booking and an invoice draft asked for twice were not kept.

### Agent templates: the webhooks ask for a token (23 November 2026)

- Every Webhook node in the six workflows (the five templates and the Course 2 lab, with their two approval webhooks) now uses n8n's Header Auth and refers to one credential by name. The built files hold no secret. Until the credential exists a webhook answers 500 and runs nothing; a request with no token or a wrong one gets 403.
- `tools/n8n_webhook_credential.py` writes a credential file with a new random token for `n8n import:credentials`; the file is in `.gitignore` and is meant to be deleted after the import. The credential can also be created in the editor.
- `tools/n8n_e2e.py` and the lab's `evaluate_n8n.py` send the token (`--token`, or the `SAAEA_WEBHOOK_TOKEN` environment variable); the first also checks that every webhook refuses a request without it, and the second says why when it is refused.
- **Checked inside n8n 2.35.7:** 100 requests, none failed (the 84 of v0.9 and 16 refusals); the lab's evaluator gave its baseline of 24 of 35 with the token and a plain message without it. Not checked: creating the credential in the editor, n8n Cloud, a reverse proxy or a tunnel.
- **This changes the first run:** the workflows no longer answer straight after import. The README and the Course 2 lab give the two extra commands.
- A token shows that the sender knows it, not that a message came from a given channel. Verifying a provider's signature belongs to the integration recipes of v0.14.

### Founder Toolkit: paid pilot terms sheet and the customer's return (23 November 2026)

- Template 14, the [paid pilot terms sheet](04-entrepreneur-toolkit/14-paid-pilot-terms-sheet.md): filled with the customer after a yes in principle. It records the agent's stages (shadow, every reply approved, sampled review), its limits and who can stop it, who answers for what, the data terms, the measure and decision rule, the money and the exit, and ends with a list left to the lawyer. It proposes no position on any item. **Not a contract and not reviewed by a lawyer;** two questions about it were added to the legal review packet. The toolkit now has fourteen templates.
- [`buyer_return.py`](04-entrepreneur-toolkit/buyer_return.py), a fourth calculator: the customer's cost of the task today and with the service, the apparent and the real saving, staff approvals and set-up payback. It uses the customer's own measured figures and carries no benchmark; its defaults print the Course 3 worked example (2,700; 1,716; 984, 36%).
- Linked from templates 6 and 9 and from lessons 3.3 and 3.6.

### Lab: an invented e-commerce dataset (23 November 2026)

- [`05-agentic-ai-lab/datasets/ecommerce-store`](05-agentic-ai-lab/datasets/ecommerce-store/README.md): one invented online store with six approved answers, 12 products, 24 orders, 85 customer messages with expected behaviour (above every minimum of the evaluation template), and a staff record for practising shadow mode.
- `tools/dataset_pack.py` builds the Config values and requests template 1 takes, checks the data for consistency, and scores a run.
- **Baseline with the keyword simulator: 73 of 85**, acting alone on four messages where a person or a refusal was expected. The simulator is not a language model and its keywords were written by the author of the messages, so this is not a measure of anything but the exercise. No language model has been run on the set.
- **Invented throughout.** The messages were written by an AI assistant in general Saudi colloquial Arabic and were not reviewed by native speakers of any one dialect. The set does not replace an evaluation set built from real customer messages.
- `tools/shadow_report.py` also reads the JSON list that `tools/n8n_harness.js` prints.

### Lab: the founder agents as runnable Python (23 November 2026)

- [`05-agentic-ai-lab/founder-agents`](05-agentic-ai-lab/founder-agents/README.md): a package, standard library only, that runs the twelve founder agents from the command line. It reads each definition, the pages the agent reads and its test conversations from the published page, and keeps no copy of them.
- `prompt` prints everything to paste for one agent and needs no model. `chat`, `ask` and `test` use any chat-completions endpoint, set with the Course 2 lab's environment variables. `test` runs the three test conversations and writes the record as JSON and in the layout of the recorded runs, with the assessment left to a person.
- Mechanical checks on every reply: figures, web addresses and article numbers that are not in the agent's pages or the founder's messages, wording that reads as a ruling, a bare yes or no when the founder pushed for one. They are flags for a reader. A reply without a flag has not been approved.
- Before a message is sent, the runner names what looks like personal data or a secret in it and asks; it says so when the model is not on the founder's machine.
- **Run on the published recorded runs** (33 conversations, 50 replies): 13 flags, all figures, in four conversations of agents 5, 7 and 12. Each line was read: results of calculations and stated assumptions, a test example the assistant wrote, and one arithmetic extension it labelled as its own. The replies were compared with the pages as they are today.
- 25 new tests. **No language model has been run through the package**: the tests use hand-written replies and a stand-in endpoint. Not tried with founders.

### Roadmap (23 November 2026)

The next three iterations are set out in the [roadmap](ROADMAP.md): v0.13 (shadow mode, webhook authentication, output repair, an invented dataset pack, pilot terms), v0.14 (integration recipes), v0.15 (sector packs after a first cohort). Recruiting a first cohort and a legal reviewer runs beside them.

## v0.12 (2026-11-22)

A second batch of the knowledge framework restored from pages opened in a browser, and the first run of the agent templates with a local model.

**Still true: no course has been piloted, and no lawyer or tax adviser has reviewed the framework.**

### Agent templates: first run with a local model (22 November 2026)

The prompts of the five templates and the Course 2 lab were answered by qwen2.5:3b, served by Ollama on a laptop with 8 GB of memory and no graphics card, one call per prompt at temperature 0. Result: 38 of 47 template cases (47 of 47 with the first, hosted model) and 31 of 35 with 7 of 8 held out on the lab. The failures are recorded case by case in [`real-model-runs`](05-agentic-ai-lab/agent-templates/workflows/real-model-runs/README.md): unquoted JSON values, a total the model computed against the instructions, and a lost choice in the booking flow. The outputs are in the repository and a test replays them. The answers were not sent through n8n's HTTP node.

### Knowledge framework: a second batch restored, and three entries upgraded (22 November 2026)

Official pages were opened in the owner's browser, including sites that refuse automated reading.

- **Anti-Commercial Fraud Law** (domain 08, both registers): the thirty articles were read on the Bureau of Experts' site. The page now gives the violations, the licence rule for discounts and contests, who answers for a violation, and the penalties (A158, no longer from search extracts).
- **Flexible work and remote work** (domain 09, both registers): hourly contracts for Saudis on the Ministry's platform with their hour limits, one-year limit and Nitaqat counting (A180); the remote work contract service (A181).
- **Open Banking Framework** (domain 10, both registers): SAMA's two releases, account information then payment initiation (A182).
- **Education** (domain 10, both registers): a first entry, the National eLearning Center's licences for e-learning providers and programmes (A183).
- **Upgraded after reading in a browser:** the freelance platform's programmes and benefits, with two dead links removed (A156); the dates and venue of Biban 2025 (A161).
- **Saudia Cargo case:** the vendor is now named from the joint announcement (A184); the vendor's general figures are quoted as such and the evidence level stays C.
- Not restored: the dates of Biban 2026 (not on the organiser's pages), and what C52 still lists.

## v0.11 (2026-11-22)

A first batch of the knowledge framework restored from official sources, the case-study section restructured with sixteen new pages, and an English landing page.

**Still true: no course has been piloted, and no lawyer or tax adviser has reviewed the framework.** What is below was read from official pages; it was not reviewed by a specialist.

### Knowledge framework: a first batch restored from official sources (22 November 2026)

Five subjects removed on 20 November as unverified went back, each read from its issuer's page or the Bureau of Experts' site. Every addition cites a new entry in `SOURCES.md` (A152 to A162) that says how the page was read and what was not read.

- **Zakat and income tax** (domain 05, the tax guide's section 3, both registers): who is subject by ownership, 2.5% and 20%, registration before the end of the first fiscal year, return within 120 days. The computation of each base is not summarised.
- **Wage protection, work permits and the freelance document** (domain 09, a new section 7 in the first-hire guide, both registers): wage files through Mudad within 30 days; work permits through Qiwa; the freelance document is for Saudi nationals.
- **The E-Commerce Law's articles** (domain 08, a new section 6 in the store guide, both registers): scope, disclosure, advertising as a binding document, the seven-day termination right and its exceptions, the 15-day delivery rule, penalties. The Anti-Commercial Fraud Law is recorded from search extracts only.
- **Two financial sandboxes** (domain 10, both registers): SAMA's Regulatory Sandbox and CMA's FinTech Lab, with each regulator's own stages and durations.
- **Biban and LEAP** (the ecosystem directory, Arabic and English): the events section is back with two events.
- The framework's [removal record](02-saudi-market-knowledge-framework/not-adopted.md) lists what went back and what stayed out; `SOURCES.md` C52 lists what could not be confirmed, including the dates of Biban 2026.

### Case studies: restructured, and sixteen pages added (22 November 2026)

From the owner's draft of about thirty cases, each checked against a named, dated source before use.

- **One index, three parts** ([`06-case-studies/README.md`](06-case-studies/README.md)): operating cases by place, with what the agent does and the evidence level; venture pages by group; and a table that picks cases by topic and course module. No file moved, so existing links hold.
- **Six operating cases.** Saudi: [Panda](06-case-studies/saudi/panda.md) (a shopping assistant in dialect, with its engineering decisions), [Nana](06-case-studies/saudi/nana.md) (a support agent in the app), [Saudia Cargo](06-case-studies/saudi/saudia-cargo.md) (quoting agents, with the tourism agents from the same report), [King Faisal Specialist Hospital](06-case-studies/saudi/kfsh-patient-flow.md) (published as a comparison case: its own releases describe forecasting and alerting, not an agent), [HUMAIN and Replit](06-case-studies/saudi/humain-replit.md) (an announcement). International: [Orange and Nexus](06-case-studies/global/orange-nexus.md).
- **Ten venture pages**, all passing the case linter: Shaffra, RIME, Gaia, TabSense, Velents.ai (Saudi); Sierra, Wonderful, Harvey, Rocketlane, and 11x, the last as a lesson in checking revenue and customer claims. A watch list records Cycls, Operater and Nommas.ai.
- **A sixth illustrative scenario**: a card dispute agent in an invented bank, with a build exercise and a refusal test. It came from the draft's banking "anatomy", for which no source was found.
- **Not adopted**, with reasons, in [`06-case-studies/not-adopted.md`](06-case-studies/not-adopted.md): agent deployments attributed to two banks and two logistics bodies, and unsourced figures for six companies. `SOURCES.md`: A163 to A179, B69 to B74, C53.
- **Limits.** Sources were read by automated fetch or as returned by search, not in a browser; every figure is the company's or its vendor's; no case is independently verified, and no company was contacted.

### English landing page

- [`index.en.html`](index.en.html): the landing page in English, left to right, with the same links, a "where it stands" section, and every deck listed by its English title with the Arabic title under it. `tools/build_site.py` generates both pages from the same deck list, and the Arabic page's "English" button now opens it. Two tests cover it (94 in all).

### Corrections

- `ROADMAP.md`, Arabic section: the current release was still given as 0.9; it now describes 0.10.1.

## v0.10.1 (2026-11-21)

Two corrections after v0.10, no new material.

- Funding directory, TAQADAM (issue #43, raised by [@a-majrashi](https://github.com/a-majrashi)): the row now says that the USD 40,000 goes to the teams selected after the bootcamp, not to every accepted team, and that KAUST's help centre calls it non-dilutive; the entry conditions are listed in full (working MVP, one founder full-time, a plan to enter the Saudi market within a year for teams from abroad); and the ninth cohort's result is recorded from KAUST's announcement of 3 May 2026. The announcement says the top ten "secured an additional $100,000" without saying per startup or in total, so the directory does not say "each". Sources A61, A108 and C46 updated; pages opened 21 November 2026.
- AskBaba case study: restored the learner question on the purchase-order value at which execution should wait for the buyer's approval, and the thesis clause that approval of anything with financial effect stays with the authorised person. Both had been dropped in the edit of pull request #42; the contributor's corrections and additions are kept.

## v0.10 (2026-11-21)

**First outside contribution.** [@a-majrashi](https://github.com/a-majrashi) clarified the performance and availability evidence in the [AskBaba case study](06-case-studies/saudi/tamimi-markets-askbaba.md) (pull request #42): what the vendor's response-time and round-the-clock claims do and do not measure, that the TIPS platform creates the purchase orders and AskBaba reviews them, and a measurement exercise for learners. The change was read against search-result excerpts of the vendor's page, not the full page.

A planning guide for founders, the first runs with a real assistant and a real model, and a website that shows the repository's pages itself. **Still true: no course has been piloted, no founder has used the agents, and the regulatory, tax and security content has had no specialist review.**

### The website: every page readable on the site

- [`read.html`](read.html), a reader: one page that shows any Markdown file of the repository as a web page on the GitHub Pages site, in the Academy's identity. Arabic pages read right to left and English pages left to right; each block takes its own direction; tables scroll; Arabic text in code blocks (agent definitions, recorded replies) wraps and reads right to left. Links between pages stay inside the site; links to code go to GitHub.
- Nothing is generated per page: the reader fetches the file from the same site and renders it in the browser, so the site cannot drift from the repository. The renderer is marked 15.0.12 (MIT), bundled in `assets/vendor/`; no script is loaded from another site.
- Section navigation, a breadcrumb, a link to the file on GitHub, and a search box over the titles and section headings of all pages (`site-index.json`, built by `tools/build_site.py` and checked by a test).
- The landing page now opens the courses, the framework, the toolkit and the lab in the reader instead of sending the visitor to GitHub.
- **Checked** in headless Chrome at 1280 and 390 pixels on a lesson, the planning guide (with an anchor), a founder agent page, the English README and the toolkit; 268 links on six pages resolved; Bayan's `bidi_lint` reports no errors and no warnings on `read.html` and `index.html`.
- **Limits.** Pages are rendered in the browser, so a visitor without JavaScript sees nothing, and search engines that do not run scripts index only the landing page. Search covers titles and headings, not body text. Not checked on the live Pages site (it deploys on merge), nor in Safari or Firefox. The showcase has no project yet.

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

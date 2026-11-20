# دليل المدرب · Instructor guide

For anyone running Course 2 as a cohort. Self-paced learners can skip this file. Nothing here has been piloted yet; tell us what happened when you run it.

## Before the first session

- Every learner arrives with a Course 1 thesis and workflow map, or an equivalent documented opportunity. A learner with no workflow in hand has nothing to build.
- A test environment per learner: a low-code orchestrator or a Python environment, a hosted model key with a spending cap, and a sandbox for the two tools (a test spreadsheet or CRM). No production systems and no real customer data.
- Ask each learner to bring twenty real messages from the workflow, with personal details replaced. They seed the dialect glossary (2.2) and the evaluation set (2.5).

## Delivery schedules (24 contact hours)

| Format | Session | Modules | Between sessions |
|---|---|---|---|
| **Six half-days** | S1 (4h) | 2.1; 2.2 concepts and instructions (2h) | Fill the Founder Context Template |
| | S2 (4h) | 2.2 testing (1h); 2.3 build (3h) | Finish the two tool contracts |
| | S3 (4h) | 2.3 checks (1h); 2.4; 2.5 designing the set (1h) | **Build the evaluation set.** Collecting real cases takes days, not hours |
| | S4 (4h) | 2.5 baseline run and analysis (3h); 2.6 risks (1h) | Complete the oversight matrix |
| | S5 (4h) | 2.6 gates and injection test (2h); 2.7 patterns and design (2h) | Deep track: build the two-agent variant |
| | S6 (4h) | 2.7 decisions reviewed (1h); 2.8 | Record and submit the demo |
| **Twelve evenings** | 12 × 2h | In the same order; 2.3 and 2.5 take two evenings each | Same work between sessions |

Allow at least a week between S3 and S4. One project runs through all eight modules so the outputs accumulate.

## Time inside each module

Suggested split, in minutes. The pattern is the same throughout: short explanation, an example, guided build, a test, then documentation.

| Module | Hours | Concepts | Build or apply | Test, review or present |
|---|---|---|---|---|
| 2.1 Agent anatomy | 2 | 45 | 60 | 15 |
| 2.2 Context engineering | 3 | 45 | 90 | 45 |
| 2.3 Tools | 4 | 60 | 150 | 30 |
| 2.4 Choosing a model | 2 | 45 | 60 | 15 |
| 2.5 Evaluation | 4 | 60 | 120 | 60 |
| 2.6 Guardrails | 3 | 60 | 90 | 30 |
| 2.7 Several agents | 3 | 60 | 90 | 30 |
| 2.8 Improvement | 3 | 45 | 90 | 45 |

## Materials checklist

| Item | Where |
|---|---|
| Eight lessons | [`lessons/`](lessons/) |
| Eight slide decks with speaker notes (118 slides) | [`slides/`](slides/README.md) |
| Eight formative quizzes with answer keys (80 questions) | [`quizzes/`](quizzes/README.md) |
| Worked example (invented store and data) | [`examples/worked-example-order-enquiry-agent.md`](examples/worked-example-order-enquiry-agent.md) |
| Tool contract, model selection memo, architecture decision record, failure and improvement log, readiness checklist, demo video outline | [`templates/`](templates/) |
| Agent design sheet and Saudi specifics checklist | [AI MVP Blueprint](../../04-entrepreneur-toolkit/07-ai-mvp-blueprint.md) |
| Founder Context Template | [Founder Toolkit](../../04-entrepreneur-toolkit/10-founder-context-template.md) |
| Evaluation template | [Lab](../../05-agentic-ai-lab/evaluation/eval-template.md) |
| Human Oversight Matrix and agent security assessment | [Compliance toolkit](../../02-saudi-market-knowledge-framework/compliance-toolkit/human-oversight-matrix.md) |
| Arabic model guide | [Lab](../../05-agentic-ai-lab/arabic-models.md) |
| Five agent templates as starting points | [Lab](../../05-agentic-ai-lab/agent-templates/README.md) |
| Eight labs with a tested reference implementation, sample data and expected outputs | [`labs/`](labs/README.md) |
| Glossary and rubrics | [`glossary.md`](glossary.md), [`rubrics.md`](rubrics.md) |

## Notes by module

- **2.1.** Expect resistance to "you may not need an agent". Treat a learner who concludes that plain automation is enough as a success, and keep them in the course: evaluation, guardrails and failure analysis apply to their build too.
- **2.2.** The dialect glossary must come from the learner's own messages. A list copied from the lesson is a sign the learner has no real messages yet.
- **2.3.** The most common shortcut is connecting the agent with a personal account. Check accounts and permissions before anything is run. Keep everything in the sandbox.
- **2.4.** Do not recommend a model. Model names and prices change faster than this course; the method is what the learner keeps. Check that each learner read the licence or terms and can say where data is processed.
- **2.5.** Have the release rule written and handed in **before** the baseline run. Learners who see the number first lower the bar to meet it. Do not let anyone fix failures in this session; fixing starts in 2.8.
- **2.6.** Run the matrix test in pairs: each learner tries to make the other's agent perform a forbidden action. Stay inside the test environment, and only against agents the learners built themselves.
- **2.7.** Most learners should end on one agent. Ask for the condition that would make them revisit the decision.
- **2.8.** One change per cycle is the rule learners break most. Ask to see the diff. Grade the honesty of the "not fixed" section.

## What a facilitator should not do

- Recommend a model, a framework or a provider. Names and prices change faster than the course; Module 2.4 teaches the comparison.
- Let a learner connect an agent to a production system or to real customer data. Everything in this course runs on test accounts and masked or synthetic messages.
- Accept a success rate with no test set another person can re-run. Gate 3 has no exceptions.
- Let a learner raise the success rate by removing hard cases from the set.
- Programme-level guidance common to the four courses is in the [trainer guide](../TRAINER-GUIDE.md).

## Before each cohort

Re-check, and update the lessons or tell us:

| What | Where it is used | Source entry |
|---|---|---|
| Whether OWASP has published an edition newer than 2026 | 2.3, 2.6 | A84, A121 |
| Token-ratio figures for Arabic | 2.2, 2.4 | A86 |
| Multi-agent token figures | 2.7 | A87 |
| The licence of any open-weights model named as an example | 2.4 | A6 |
| The status of the Model Context Protocol and its governance | 2.3 | A83 |
| The status of the draft amendments on storing data inside the Kingdom, described in lesson 2.4 as not final | 2.4 | the [PDPL founder guide](../../02-saudi-market-knowledge-framework/03-data-protection-pdpl/pdpl-founder-guide.md) |

## Reading for instructors

Opened and checked on 19 November 2026 (see [SOURCES.md](../../SOURCES.md), A80 to A87):

- Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models" (arXiv 2210.03629).
- Anthropic, "Building effective agents" (December 2024) and "Effective context engineering for AI agents" (September 2025).
- Anthropic, "How we built our multi-agent research system" (June 2025).
- OWASP, Top 10 for LLM Applications. The 2026 edition (August 2026) keeps Prompt Injection first and moves Excessive Agency from sixth to third (A121); the lessons and decks were updated on 20 November 2026. The companion list for agentic applications is used in Course 4 (A122).
- The Model Context Protocol specification and its current governance.

Named in the source drafts and **not opened in this pass** ([C37](../../SOURCES.md)): the NIST AI Risk Management Framework, the original retrieval-augmented generation paper, and general references on human-centred AI, regression testing, least privilege and defence in depth. Use the current official editions if you cite them.

## Labs and what is not built yet

Eight [labs](labs/README.md), one per module, were added on 20 November 2026 with a tested reference implementation: Python 3.9 or newer, standard library only, offline, no key and no cost. The default model is a deterministic simulator, so every learner gets the numbers of the worked example (24, 25, 28 and 30 of 35). Run `python3 -m unittest tests.test_course2_labs` on the room's machine before the session. The labs rehearse the method on the example; each learner still builds their own agent, with whatever tool they choose, for the graded project.

Since v0.9 the core track has a [low-code lab](labs/lab-n8n-low-code.md): the same agent as an n8n workflow, scored with the same evaluator. It needs n8n on the room's machines (Node.js 22.22 or newer for n8n 2.35); rehearse the import and the publish step before the session, because it has not been tried with learners. Not built: a test set of real Saudi-dialect messages and a recorded demonstration. The course has not been piloted. See [CONTRIBUTING.md](../../CONTRIBUTING.md).

## Questions for the first pilot

1. Are four hours enough for 2.3 in the core track with learners who have never used an orchestrator?
2. How long does a learner need between S3 and S4 to collect real cases?
3. Is 35 cases, three runs each, workable by hand in the core track?
4. Do learners in the core track finish two improvement cycles inside 2.8?
5. Should 2.4 move after 2.5, so that models are compared on the full set?

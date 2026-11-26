# المقرر 2: بناء الوكلاء الأذكياء
# Course 2: Building AI Agents

> **الإصدار الأول من المحتوى · First content release (19 November 2026).** الدروس الثمانية والقوالب والمثال المحلول والمسرد وسلالم التقدير ودليل المدرب متاحة الآن. وأُضيفت في اليوم نفسه عروض الوحدات الثماني ([العروض](slides/README.md)) واختبار قصير لكل وحدة ([الاختبارات](quizzes/README.md)). لم يُجرَّب المقرر مع فوج بعد. ملاحظاتك مرحّب بها. · Eight lessons, templates, a worked example, a glossary, rubrics and an instructor guide are available. Eight slide decks and eight quizzes were added the same day. The course has not been piloted. Comments are welcome.


<div dir="rtl">

**المدة:** 24 ساعة · **المستوى:** مبتدئ إلى متوسط · **المتطلب السابق:** المقرر 1 أو فرصة موثقة · **الركيزة:** ابنِ

**لمن؟** كل من لديه سير عمل محدد يريد أتمتته. المسار الأساسي بلا برمجة، والمسار العميق يتطلب أساسيات Python.

**السؤال الذي يجيب عنه المقرر:** هل يستطيع وكيل أن ينجز هذا العمل بجودة يقبلها العميل، وكيف أثبت ذلك؟

**المُخرَج:** وكيل يعمل على مهمة واحدة ذات قيمة من بدايتها إلى نهايتها، مع مجموعة اختبارات تقييم بالعربية، وبوابات موافقة بشرية، وسجل إخفاقات، وعرض مصوّر قصير.

**نواتج التعلّم:** بنهاية المقرر يستطيع المتعلم أن:
1. يصمّم وكيلاً من سير عمل موثق: الهدف، الأدوات، المعرفة، الحدود.
2. يكتب تعليمات وسياقاً للوكيل بالعربية ويربطه بأدوات العمل.
3. يبني مجموعة تقييم من حالات حقيقية تشمل اللهجة السعودية، ويقيس نسبة النجاح.
4. يضع بوابات الموافقة البشرية وحدود الصلاحيات خارج النموذج.
5. يوثّق الإخفاقات ويحسّن الوكيل بناءً عليها.

**القاعدة التي تحكمه:** وكيل صغير محدود الصلاحيات ينجز مهمة حقيقية بجودة مقاسة ويعرف متى يتوقف، أفضل من عرض مبهر لوكيل واسع الصلاحيات لا يمكن إثبات موثوقيته.

## ابدأ من هنا

| الوحدة | الدرس | الساعات | المخرج |
|---|---|---|---|
| 2.1 | [تشريح الوكيل](lessons/2-1-agent-anatomy.md) | 2 | ورقة التصميم والقرار |
| 2.2 | [هندسة السياق بالعربية](lessons/2-2-context-engineering-in-arabic.md) | 3 | التعليمات وقالب السياق |
| 2.3 | [الأدوات والتكاملات](lessons/2-3-tools-and-integrations.md) | 4 | أداتان وعقداهما |
| 2.4 | [اختيار النموذج](lessons/2-4-choosing-a-model.md) | 2 | مذكرة الاختيار |
| 2.5 | [التقييم](lessons/2-5-evaluation.md) | 4 | مجموعة التقييم وخط الأساس |
| 2.6 | [ضوابط الحماية والموافقة البشرية](lessons/2-6-guardrails-and-human-approval.md) | 3 | المصفوفة والبوابات |
| 2.7 | [من وكيل واحد إلى عدة وكلاء](lessons/2-7-from-one-agent-to-several.md) | 3 | القرار المعماري |
| 2.8 | [تحليل الإخفاق والتحسين](lessons/2-8-failure-analysis-and-iteration.md) | 3 | السجل والدورتان والعرض |

**مواد المقرر:** [العروض التقديمية](slides/README.md) · [المختبرات](labs/README.md) · [الاختبارات القصيرة](quizzes/README.md) · [المثال المحلول](examples/worked-example-order-enquiry-agent.md) (متجر وبيانات مختلقة) · [عقد الأداة](templates/tool-contract.md) · [مذكرة اختيار النموذج](templates/model-selection-memo.md) · [سجل القرار المعماري](templates/architecture-decision.md) · [سجل الإخفاق والتحسين](templates/failure-and-improvement-log.md) · [قائمة التحقق قبل الاعتماد](templates/readiness-checklist.md) · [مخطط العرض المصوّر](templates/demo-video-outline.md) · [المسرد](glossary.md) · [سلالم التقدير](rubrics.md) · [دليل المدرب](instructor-guide.md) · [ما لم يُعتمد ولماذا](not-adopted.md)

</div>

---

## Modules

| # | Module | Hours | Core content | Activity |
|---|---|---|---|---|
| 2.1 | [Agent anatomy](lessons/2-1-agent-anatomy.md) | 2 | Goal, instructions, tools, knowledge, memory, limits. The loop: perceive, plan, act, check. Workflows versus agents and when a plain workflow is the better choice | Turn the Course 1 workflow map into an agent design using the [AI MVP Blueprint](../../04-entrepreneur-toolkit/07-ai-mvp-blueprint.md) |
| 2.2 | [Context engineering in Arabic](lessons/2-2-context-engineering-in-arabic.md) | 3 | Writing instructions and business context in Arabic. Structured outputs. Giving the agent the business's own knowledge. Handling MSA, Saudi dialect and mixed Arabic-English input | Write agent instructions and fill the [Founder Context Template](../../04-entrepreneur-toolkit/10-founder-context-template.md) |
| 2.3 | [Tools and integrations](lessons/2-3-tools-and-integrations.md) | 4 | Tool calling. Connecting to email, spreadsheets, CRM and messaging. Model Context Protocol in outline. Saudi-specific handling: Hijri and Gregorian dates, SAR and VAT, national address formats, Arabic names | Connect the agent to two real tools |
| 2.4 | [Choosing a model](lessons/2-4-choosing-a-model.md) | 2 | Hosted APIs versus self-hosted open-weight models. Arabic capability, cost, latency, context length, licence and data location. Reading a model card and its licence | Compare two models on ten of your own cases using the [Arabic model guide](../../05-agentic-ai-lab/arabic-models.md) |
| 2.5 | [Evaluation](lessons/2-5-evaluation.md) | 4 | Building a test set from real cases. Pass criteria. Measuring success rate, cost and time per task. Regression testing after every change | Build a test set of at least 30 cases with the [Evaluation Template](../../05-agentic-ai-lab/evaluation/eval-template.md) |
| 2.6 | [Guardrails and human approval](lessons/2-6-guardrails-and-human-approval.md) | 3 | Deterministic authorization: allow-lists, spending limits, approval gates, confirmation before irreversible actions. Prompt injection in outline. What to log | Complete the [Human Oversight Matrix](../../02-saudi-market-knowledge-framework/compliance-toolkit/human-oversight-matrix.md) and implement its gates |
| 2.7 | [From one agent to several](lessons/2-7-from-one-agent-to-several.md) | 3 | When to split: specialist agents, a coordinator, sequential pipelines. Handoffs and shared state. Why more agents means more cost and more failure points | Decide, with reasons, whether your product needs more than one agent |
| 2.8 | [Failure analysis and iteration](lessons/2-8-failure-analysis-and-iteration.md) | 3 | Reading failure logs. Classifying errors: understanding, knowledge, tool, policy. Fixing the cause | Two improvement cycles; record the before and after success rate |

## Track differences

| | Core track | Deep track |
|---|---|---|
| Build environment | A low-code orchestrator such as n8n | Python with an orchestration framework such as LangGraph or CrewAI |
| Models | Hosted APIs | Hosted APIs, plus an open-weight Arabic model run locally with a tool such as Ollama |
| 2.3 | Use pre-built connectors | Write one custom tool against a documented API |
| 2.5 | Test set in a spreadsheet, run by hand or by a loop node | Automated evaluation script that runs on every change |
| 2.6 | Approval step in the workflow, for example a message to the owner | Policy checks in code before any tool call executes |
| 2.7 | Study only | Implement a two-agent version and compare cost and success rate against the single agent |

The academy is tool-neutral. Tools are named as examples; any equivalent that meets the deliverable is acceptable.

## Deliverable: a working, evaluated agent

1. **Agent design sheet** (goal, tools, knowledge, limits).
2. **The agent itself**, reachable on a test channel.
3. **Evaluation set** of 30 or more real or realistic Arabic cases, at least 10 in Saudi dialect, with pass criteria and results.
4. **Human oversight matrix** with the gates implemented.
5. **Failure log** covering two improvement cycles.
6. **Demo video**, three minutes, in Arabic.

Starting points: the five [agent templates](../../05-agentic-ai-lab/agent-templates/README.md). A complete illustrative build is in the [worked example](examples/worked-example-order-enquiry-agent.md). The evaluation set follows the [evaluation template](../../05-agentic-ai-lab/evaluation/eval-template.md), whose category minimums add up to 35 cases. The failure log covers the two improvement cycles and lists what was not fixed. Check the whole submission against the [readiness checklist](templates/readiness-checklist.md).

## Validation gates

A project is graded only if all four are "yes". Otherwise it goes back.

1. No sensitive action runs without approval.
2. No unauthorised data is disclosed.
3. There is a test that another person can re-run and check.
4. No material failure is hidden.

## Rubric

| Criterion | Weight | Strong submission |
|---|---|---|
| Does the job | 30% | Completes the target task end to end; success rate on the test set is reported honestly |
| Evaluation quality | 25% | Cases come from real situations, include dialect and edge cases, and have clear pass criteria |
| Guardrails | 20% | No irreversible or financial action without a gate; limits are enforced outside the model |
| Improvement | 15% | Failure log shows causes found and fixed; success rate moved |
| Arabic quality | 10% | Output reads naturally to a Saudi customer |

Four performance levels per criterion, the validation gates and a checkpoint for each module are in [rubrics.md](rubrics.md).

## Common mistakes

- Building several agents when one, or a plain workflow, would do.
- Testing on five cases the builder wrote and calling it done.
- Putting the rules in the prompt and trusting the model to follow them.
- Using a model without reading its licence or knowing where data is processed.
- Sending real customer personal data to a tool during testing. Use synthetic or anonymised data until the [PDPL guide](../../02-saudi-market-knowledge-framework/03-data-protection-pdpl/pdpl-founder-guide.md) steps are done.

## Methodology cards

The frameworks this course leans on, each on one standard card in the [methodology library](../../09-methodology-library/README.md): [AI Agent Architecture](../../09-methodology-library/cards/agent-architecture.md) · [Agent Workflow](../../09-methodology-library/cards/agent-workflow.md) · [Human-in-the-Loop (HITL)](../../09-methodology-library/cards/human-in-the-loop.md) · [Agent Evaluation](../../09-methodology-library/cards/agent-evaluation.md) · [Kanban](../../09-methodology-library/cards/kanban.md) · [Agent Capability Matrix](../../09-methodology-library/cards/agent-capability-matrix.md) · [Agent Tool-Access Matrix](../../09-methodology-library/cards/agent-tool-access-matrix.md) · [UML Class Diagram](../../09-methodology-library/cards/uml-class-diagram.md) · [Sequence Diagram](../../09-methodology-library/cards/sequence-diagram.md) · [Entity Relationship Diagram (ERD)](../../09-methodology-library/cards/entity-relationship-diagram.md) · [Retrieval-Augmented Generation (RAG)](../../09-methodology-library/cards/retrieval-augmented-generation.md) · [Model Context Protocol (MCP)](../../09-methodology-library/cards/model-context-protocol.md) · [Multi-Agent Orchestration](../../09-methodology-library/cards/multi-agent-orchestration.md) · [LLM Evaluation](../../09-methodology-library/cards/llm-evaluation.md) · [Spec-Driven Development](../../09-methodology-library/cards/spec-driven-development.md) · [CI/CD](../../09-methodology-library/cards/ci-cd.md) · [Technical Debt Management](../../09-methodology-library/cards/technical-debt.md). The cards explain a model and point back here; deliverables are still graded with this course's templates and rubric.

## Companion tools (optional)

Separate repositories by the same author; see [companion repositories](../../07-resources/companion-repositories.md). The deliverable is graded with the Academy's templates.

| Module | Tool | Exercise |
|---|---|---|
| 2.1, 2.6 | [Riyada](https://github.com/malenezi/riyada) `agent-operations`: SOP, agent role card, approval matrix with an enforcement column | [R3](../../05-agentic-ai-lab/exercises/r3-role-card-and-approval-matrix.md) |
| 2.2 | Riyada `founder-context`: seven-layer context pack and `context_lint.py` | [R2](../../05-agentic-ai-lab/exercises/r2-context-pack.md) |
| 2.2 | [Bayan](https://github.com/malenezi/bayan) `arabic-ux-writing`: the agent's fixed messages in Arabic | [B1](../../05-agentic-ai-lab/exercises/b1-agent-messages-in-arabic.md) |
| 2.2 | The Academy's `terminology_lint.py` with Bayan's glossary: one Arabic term per concept, enforced across files | [B6](../../05-agentic-ai-lab/exercises/b6-terminology.md) |
| 2.5 | The Academy's `data_governance_lint.py`: check the test set against your data policy before it reaches a tool | [R8](../../05-agentic-ai-lab/exercises/r8-data-governance.md) |
| 2.5, 2.8 | Riyada eval rubric: critical errors, release rule, failure analysis. Test cases stay in the Academy's [evaluation template](../../05-agentic-ai-lab/evaluation/eval-template.md) | R3, then [R6](../../05-agentic-ai-lab/exercises/r6-agent-evaluation.md): two evaluation cycles with repeated runs |
| 2.6 | The Academy's [agent security assessment](../../02-saudi-market-knowledge-framework/compliance-toolkit/agent-security-assessment.md) with Riyada's approval matrix | [R7](../../05-agentic-ai-lab/exercises/r7-agent-red-teaming.md): attack your own agent in a test environment |

Riyada's parallel workflow is [First agent in 30 days](https://github.com/malenezi/riyada/blob/main/workflows/04-first-agent-in-30-days.en.md).

## What is still missing

A test set built from real Saudi-dialect messages, a recorded demonstration, and a first cohort's feedback. The eight [labs](labs/README.md) are tool-neutral: a tested Python reference implementation that runs offline, with a 35-case test set that includes ten Saudi-dialect cases, all invented. Since v0.9 the core track also has a [low-code lab](labs/lab-n8n-low-code.md): the same agent as an importable n8n workflow that reproduces the same numbers. Slides and quizzes exist (see [slides](slides/README.md) and [quizzes](quizzes/README.md)). See the [instructor guide](instructor-guide.md) and [CONTRIBUTING.md](../../CONTRIBUTING.md).

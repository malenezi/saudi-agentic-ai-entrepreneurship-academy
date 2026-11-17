# المقرر 2: بناء الوكلاء الأذكياء
# Course 2: Building AI Agents

> **مسودة مخطط · Draft outline.** هذا المقرر لم يُبنَ بعد. المحتوى التفصيلي يُطوَّر على مراحل، والمخطط قابل للتغيير. ملاحظاتك واقتراحاتك مرحّب بها. · This course is not built yet. Detailed content will be developed in later iterations and this outline may change. Comments and suggestions are welcome.


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

</div>

---

## Modules

| # | Module | Hours | Core content | Activity |
|---|---|---|---|---|
| 2.1 | Agent anatomy | 2 | Goal, instructions, tools, knowledge, memory, limits. The loop: perceive, plan, act, check. Workflows versus agents and when a plain workflow is the better choice | Turn the Course 1 workflow map into an agent design using the [AI MVP Blueprint](../../04-entrepreneur-toolkit/07-ai-mvp-blueprint.md) |
| 2.2 | Context engineering in Arabic | 3 | Writing instructions and business context in Arabic. Structured outputs. Giving the agent the business's own knowledge. Handling MSA, Saudi dialect and mixed Arabic-English input | Write agent instructions and fill the [Founder Context Template](../../04-entrepreneur-toolkit/10-founder-context-template.md) |
| 2.3 | Tools and integrations | 4 | Tool calling. Connecting to email, spreadsheets, CRM and messaging. Model Context Protocol in outline. Saudi-specific handling: Hijri and Gregorian dates, SAR and VAT, national address formats, Arabic names | Connect the agent to two real tools |
| 2.4 | Choosing a model | 2 | Hosted APIs versus self-hosted open-weight models. Arabic capability, cost, latency, context length, licence and data location. Reading a model card and its licence | Compare two models on ten of your own cases using the [Arabic model guide](../../05-agentic-ai-lab/arabic-models.md) |
| 2.5 | Evaluation | 4 | Building a test set from real cases. Pass criteria. Measuring success rate, cost and time per task. Regression testing after every change | Build a test set of at least 30 cases with the [Evaluation Template](../../05-agentic-ai-lab/evaluation/eval-template.md) |
| 2.6 | Guardrails and human approval | 3 | Deterministic authorization: allow-lists, spending limits, approval gates, confirmation before irreversible actions. Prompt injection in outline. What to log | Complete the [Human Oversight Matrix](../../02-saudi-market-knowledge-framework/compliance-toolkit/human-oversight-matrix.md) and implement its gates |
| 2.7 | From one agent to several | 3 | When to split: specialist agents, a coordinator, sequential pipelines. Handoffs and shared state. Why more agents means more cost and more failure points | Decide, with reasons, whether your product needs more than one agent |
| 2.8 | Failure analysis and iteration | 3 | Reading failure logs. Classifying errors: understanding, knowledge, tool, policy. Fixing the cause | Two improvement cycles; record the before and after success rate |

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

Starting points: the five [agent templates](../../05-agentic-ai-lab/agent-templates/README.md).

## Rubric

| Criterion | Weight | Strong submission |
|---|---|---|
| Does the job | 30% | Completes the target task end to end; success rate on the test set is reported honestly |
| Evaluation quality | 25% | Cases come from real situations, include dialect and edge cases, and have clear pass criteria |
| Guardrails | 20% | No irreversible or financial action without a gate; limits are enforced outside the model |
| Improvement | 15% | Failure log shows causes found and fixed; success rate moved |
| Arabic quality | 10% | Output reads naturally to a Saudi customer |

## Common mistakes

- Building several agents when one, or a plain workflow, would do.
- Testing on five cases the builder wrote and calling it done.
- Putting the rules in the prompt and trusting the model to follow them.
- Using a model without reading its licence or knowing where data is processed.
- Sending real customer personal data to a tool during testing. Use synthetic or anonymised data until the [PDPL guide](../../02-saudi-market-knowledge-framework/03-data-protection-pdpl/pdpl-founder-guide.md) steps are done.

## Companion tools (optional)

Separate repositories by the same author; see [companion repositories](../../07-resources/companion-repositories.md). The deliverable is graded with the Academy's templates.

| Module | Tool | Exercise |
|---|---|---|
| 2.1, 2.6 | [Riyada](https://github.com/malenezi/riyada) `agent-operations`: SOP, agent role card, approval matrix with an enforcement column | [R3](../../05-agentic-ai-lab/exercises/r3-role-card-and-approval-matrix.md) |
| 2.2 | Riyada `founder-context`: seven-layer context pack and `context_lint.py` | [R2](../../05-agentic-ai-lab/exercises/r2-context-pack.md) |
| 2.2 | [Bayan](https://github.com/malenezi/bayan) `arabic-ux-writing`: the agent's fixed messages in Arabic | [B1](../../05-agentic-ai-lab/exercises/b1-agent-messages-in-arabic.md) |
| 2.5, 2.8 | Riyada eval rubric: critical errors, release rule, failure analysis. Test cases stay in the Academy's [evaluation template](../../05-agentic-ai-lab/evaluation/eval-template.md) | R3, then [R6](../../05-agentic-ai-lab/exercises/r6-agent-evaluation.md): two evaluation cycles with repeated runs |
| 2.6 | The Academy's [agent security assessment](../../02-saudi-market-knowledge-framework/compliance-toolkit/agent-security-assessment.md) with Riyada's approval matrix | [R7](../../05-agentic-ai-lab/exercises/r7-agent-red-teaming.md): attack your own agent in a test environment |

Riyada's parallel workflow is [First agent in 30 days](https://github.com/malenezi/riyada/blob/main/workflows/04-first-agent-in-30-days.en.md).

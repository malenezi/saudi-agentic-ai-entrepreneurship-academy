# إطار الكفايات · Competency framework

> **ملاحظة · Note.** المقررات تُبنى لاحقاً على مراحل؛ ما يرد هنا عنها تصميم مقترح. · The courses will be built later, in iterations; references to them here describe the proposed design.

Eight domains describe what an agentic entrepreneur can do. Each has three levels. Courses map to domains so a learner can see what they have covered and what remains.

<div dir="rtl">

| # | المجال | الوصف المختصر |
|---|---|---|
| 1 | استراتيجية الذكاء الاصطناعي واكتشاف الفرص | تحديد أين يخلق الوكيل قيمة اقتصادية حقيقية |
| 2 | تصميم الوكلاء وتنسيقهم | تحويل سير عمل إلى وكيل أو أكثر بأدوات وحدود واضحة |
| 3 | هندسة السياق ومعرفة المنشأة | تزويد الوكيل بما يحتاجه من معرفة وتعليمات وذاكرة |
| 4 | البيانات والمعلومات | التعامل مع بيانات المنشأة والعملاء بجودة ومسؤولية |
| 5 | المنتج والإلمام التقني | بناء منتج أولي واختباره وتشغيله |
| 6 | الحوكمة والمخاطر والأمن | الامتثال، الصلاحيات، والرقابة البشرية |
| 7 | ريادة الأعمال والقيادة | العميل، النموذج التجاري، البيع، التمويل |
| 8 | قياس الأداء والتحسين المستمر | مؤشرات الجودة والتكلفة والأثر |

</div>

## Levels

| Level | Name | Meaning |
|---|---|---|
| L1 | Aware (مُلمّ) | Can explain the concept and recognise it in a real business |
| L2 | Practitioner (ممارس) | Can apply it to their own venture with a template |
| L3 | Builder (بانٍ) | Can design it from scratch and teach it to a teammate |

## Domain descriptors

| Domain | L1 Aware | L2 Practitioner | L3 Builder |
|---|---|---|---|
| 1. AI strategy and opportunity | Distinguishes a chatbot from an agent; names workflows suited to agents | Scores candidate workflows and selects one with evidence | Builds an opportunity thesis with customer proof and a defensible wedge |
| 2. Agent design and orchestration | Describes perceive, plan, act, remember | Builds a single-purpose agent with tools from a template | Designs multi-agent systems with handoffs, retries and fallbacks |
| 3. Context engineering | Knows that output quality depends on the context given | Writes a founder context file and agent instructions | Structures knowledge, memory and retrieval for a whole business |
| 4. Data and information | Identifies personal and sensitive data in a workflow | Maps data flows and applies minimisation | Designs storage, retention and transfer consistent with PDPL |
| 5. Product and technical fluency | Reads an agent workflow diagram | Ships an MVP on WhatsApp or the web with a test set | Runs automated evaluation, monitoring and cost controls in production |
| 6. Governance, risk and security | Knows which Saudi rules apply to their idea | Completes the compliance toolkit for their venture | Implements approval gates, logging and incident response |
| 7. Entrepreneurship and leadership | Describes a customer and a problem | Runs interviews, prices by outcome, signs a pilot | Raises funding or reaches sustainable revenue |
| 8. Performance and improvement | Names one quality and one cost metric | Tracks cost per resolved task and success rate weekly | Runs an improvement loop from failure logs to releases |

## Course coverage

| Domain | Course 1 | Course 2 | Course 3 | Course 4 |
|---|---|---|---|---|
| 1 | L2 | | L3 | |
| 2 | L1 | L2 | | L3 |
| 3 | L1 | L2 | | L3 |
| 4 | L1 | L2 | L2 | L3 |
| 5 | | L2 | L2 | L3 |
| 6 | L1 | L1 | L2 | L3 |
| 7 | L2 | | L2 | L3 |
| 8 | | L1 | L2 | L3 |

## The entrepreneurial agent context

One capability separates a person who uses AI tools from a person who runs an agent-operated business: the ability to define the context their agents work within. An agentic entrepreneur can write down, and keep current, seven things:

1. **Identity and objectives.** Who the business is and what it is trying to achieve.
2. **Strategy and business model.** How it creates and captures value.
3. **Customers and market.** Who it serves and how they speak.
4. **Processes and operations.** How work actually gets done, step by step.
5. **Knowledge and data.** What the agents may read and where it lives.
6. **Authority, permissions and governance.** What agents may do alone, what needs approval and what is forbidden.
7. **Memory and improvement.** What is remembered, for how long, and how failures become fixes.

The [Founder Context Template](../04-entrepreneur-toolkit/10-founder-context-template.md) turns this into a file you can fill in today.

**Engineering principle: stochastic reasoning, deterministic authorization.** Language models reason probabilistically and will sometimes be wrong. Authority must therefore sit outside the model, in rules that are checked by code or by a person: spending limits, approval gates, allow-lists of actions and recipients.

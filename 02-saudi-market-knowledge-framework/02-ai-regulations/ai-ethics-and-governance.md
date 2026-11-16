# أخلاقيات الذكاء الاصطناعي والحوكمة
# AI ethics and governance for founders

Last reviewed: 16 November 2026 · Educational, not legal advice

<div dir="rtl">

## الخلاصة

أصدرت سدايا مبادئ لأخلاقيات الذكاء الاصطناعي وإرشادات للذكاء الاصطناعي التوليدي وإطاراً لتبني الذكاء الاصطناعي. حتى حين لا تكون هذه الوثائق ملزمة لمنشأتك مباشرة، سيطلب منك المشترون (خصوصاً الجهات الحكومية والشركات الكبرى) أن تبيّن التزامك بها. والأهم: تطبيقها يجعل منتجك أكثر موثوقية.

القاعدة العملية للوكلاء: **الاستدلال احتمالي، والصلاحية حتمية.** النموذج يقترح، والقواعد المكتوبة والإنسان يقرّران.

</div>

---

## 1. The guidance to know

| Document | Issuer | Why a founder should read it |
|---|---|---|
| AI Ethics Principles | SDAIA | The reference set of principles for responsible AI in the Kingdom |
| Generative AI Guidelines (for government entities; for the public) | SDAIA | Expectations for responsible use of generative AI, relevant when selling to government or building consumer products |
| AI Adoption Framework | SDAIA | How organisations are expected to adopt AI; your B2B and B2G buyers will use it to frame vendor questions |
| National Strategy for Data and AI | SDAIA | Strategic context, including support for AI entrepreneurship |

Obtain each from sdaia.gov.sa and read the current version.

## 2. Principles translated into agent design

The principles commonly cited in the Kingdom's guidance cover fairness, privacy and security, humanity, social and environmental benefit, reliability and safety, transparency and explainability, and accountability and responsibility. The table shows what each means when the system is an agent that acts.

| Principle | What it means for an agent | Evidence you can show a buyer |
|---|---|---|
| Fairness | The agent treats customers consistently regardless of dialect, name, gender or nationality | Evaluation set includes varied dialects and names; results are compared across groups |
| Privacy and security | Data is minimised, protected and deleted on schedule | PDPL self-assessment; security assessment |
| Reliability and safety | The agent does the job at a known success rate and fails safely | Evaluation results; fallbacks; escalation path |
| Transparency and explainability | People know they are dealing with an agent and can find out why it acted | Disclosure message; action logs with reasons |
| Accountability and responsibility | A named person owns each consequential decision | Human oversight matrix |
| Humanity and social benefit | The product does not manipulate, deceive or harm | Use-case review; prohibited-actions list |

## 3. Minimum governance for an early-stage agentic startup

Five artefacts, each one page. Together they answer most vendor questionnaires.

1. **Purpose statement.** What the agent is for and what it must never do.
2. **Human oversight matrix.** Which actions are autonomous, which need approval, which are forbidden. ([Template](../compliance-toolkit/human-oversight-matrix.md))
3. **Evaluation record.** Test set, pass criteria, latest results, date.
4. **Risk register.** Top risks, owners, controls. ([Template](../compliance-toolkit/ai-risk-register.md))
5. **Change log.** Every model, prompt or tool change, with the evaluation result after it.

## 4. Deterministic authorization in practice

| Control | Example |
|---|---|
| Action allow-list | The agent can call only these tools, with these parameters |
| Recipient allow-list | It can message only the customer in the current conversation and the business owner |
| Value limits | Refunds above a threshold, or any payment, need human approval |
| Confirmation before irreversible steps | Sending, booking, deleting and paying all require an explicit confirm step |
| Rate limits and budgets | Maximum actions per hour; maximum spend per day |
| Kill switch | One setting stops all agent actions and routes to a person |

These are enforced by code or by workflow configuration, never by instructions in the prompt alone.

## 5. Disclosure

Tell users, in Arabic, at the start of the interaction, that they are speaking with an automated assistant, what it can help with and how to reach a person. Example:

<div dir="rtl">

> مرحباً، أنا المساعد الآلي لـ(اسم المنشأة). أستطيع مساعدتك في (المهام). للتحدث مع موظف اكتب «موظف» في أي وقت.

</div>

## 6. Content and cultural alignment

Products for the Saudi market should respect local values, language and norms. Test the agent's tone and content with native Saudi reviewers. Religious, medical, legal and financial guidance must come from authorised sources and qualified people, not from the model's own generation.

# مختبر الذكاء الاصطناعي الوكيلي · Agentic AI Lab

<div dir="rtl">

المختبر هو الجانب العملي من الأكاديمية: مهارات جاهزة للاستخدام مع أي مساعد ذكي، وقوالب وكلاء لأعمال سعودية شائعة، وقالب تقييم، ودليل لاختيار النماذج العربية.

| القسم | المحتوى | الحالة الحالية |
|---|---|---|
| [المهارات الريادية](skills/README.md) | اثنتا عشرة مهارة: تعليمات جاهزة تحوّل مساعدك إلى شريك في اكتشاف الفرص والتسعير والامتثال | جاهزة للاستخدام |
| [قوالب الوكلاء](agent-templates/README.md) | خمسة قوالب لوكلاء: خدمة العملاء عبر واتساب، مطابقة الفواتير، تلخيص المنافسات، تأهيل العملاء المحتملين، مساعد الحجوزات. لكل قالب مواصفة و[نسخة تعمل في n8n](agent-templates/workflows/README.md) | المواصفات جاهزة. النسخ القابلة للتشغيل تعمل بنموذج محاكٍ؛ لم تُشغَّل مع نموذج حقيقي ولم توصل بقناة |
| [التقييم](evaluation/eval-template.md) | قالب مجموعة اختبار بالعربية ومعايير النجاح | جاهز للاستخدام |
| [تمارين المختبر](exercises/README.md) | سبعة عشر تمريناً: أربعة عشر تستخدم «ريادة» و«بيان»، وثلاثة بمهارات الأكاديمية نفسها: حزمة سياق تمر من مدقق، مصفوفة اعتماد، نموذج مالي، سجل ادعاءات السوق، تقييم الوكيل واختبار حدوده، رسائل وصفحات وعروض عربية مفحوصة، ولوحة قيادة ببيانات مصطنعة | الأوامر مجرَّبة؛ لم تُجرَّب مع متعلمين |
| [دليل النماذج العربية](arabic-models.md) | كيف تختار نموذجاً، وما المتاح من نماذج عربية مفتوحة الأوزان | جاهز، يُراجع دورياً |

</div>

The lab is the hands-on side of the academy.

| Section | Contents | Current status |
|---|---|---|
| [Entrepreneurial skills](skills/README.md) | Ten ready-to-use instruction sets that turn any assistant into a partner for discovery, pricing and compliance | Usable now |
| [Agent templates](agent-templates/README.md) | Five agent templates for common Saudi business jobs, each with a specification and a [runnable n8n workflow](agent-templates/workflows/README.md) | Specifications usable now. Runnable versions run with a simulated model; not run with a real model, no channel connected |
| [Evaluation](evaluation/eval-template.md) | Arabic test-set template and pass criteria | Usable now |
| [Lab exercises](exercises/README.md) | Fourteen exercises using the companion repositories [Riyada](https://github.com/malenezi/riyada) and [Bayan](https://github.com/malenezi/bayan): a context pack that passes a linter, an approval matrix, a financial model, a market claim register, agent evaluation and red teaming, checked Arabic messages, pages and decks, and a venture dashboard built on synthetic data | Commands run; not yet tried with learners |
| [Arabic model guide](arabic-models.md) | How to choose a model; open-weight Arabic options | Usable; reviewed periodically |

## Principles of the lab

1. **Framework-neutral.** Templates are written as specifications so they can be built in a low-code tool or in code. Tools are named only as examples.
2. **Arabic test cases first.** Nothing is added to the lab without Arabic cases, including Saudi dialect.
3. **Authority outside the model.** Every agent template ships with an oversight table. Implement it in code or workflow settings.
4. **Synthetic data only.** No real personal data anywhere in this repository.
5. **Honest results.** Contributors report the success rate they measured, the model used and the date.

## Technical building blocks (for orientation)

| Layer | What it does | Examples |
|---|---|---|
| Model | Understands and generates language; decides next step | Hosted model APIs; open-weight Arabic models |
| Orchestration | Runs the loop, state and handoffs | Low-code: n8n. Code: LangGraph, CrewAI |
| Tools and context | Connects the agent to systems and data | APIs, Model Context Protocol servers, retrieval |
| Channel | Where users meet the agent | WhatsApp Business, web chat, email |
| Guardrails | Enforces limits and approvals | Allow-lists, approval steps, validators |
| Evaluation and monitoring | Measures quality and cost | Test sets, tracing, dashboards |

Read each tool's current documentation; this field changes quickly.

# قوالب الوكلاء · Agent templates

<div dir="rtl">

خمسة قوالب لوكلاء يخدمون أعمالاً شائعة في السوق السعودي. لكل قالب **مواصفة** تبنيها بأداة منخفضة الكود أو بالبرمجة، و**نسخة قابلة للتشغيل** تستوردها في n8n فتعمل بنموذج محاكٍ دون مفتاح ودون تكلفة ([القوالب القابلة للتشغيل](workflows/README.md)). النسخة القابلة للتشغيل قلب الوكيل وحدوده، وليست منتجاً: لا قناة ولا نظام موصول، ولم تُشغَّل مع نموذج لغوي حقيقي.

| # | القالب | المهمة | الصعوبة | للتشغيل |
|---|---|---|---|---|
| 1 | [خدمة العملاء عبر واتساب](01-whatsapp-customer-service.md) | الرد على الاستفسارات المتكررة وتحويل ما عداها | منخفضة | [n8n](workflows/01-whatsapp-customer-service.n8n.json) |
| 2 | [مساعد الحجوزات](02-booking-assistant.md) | حجز المواعيد وتعديلها والتذكير بها | منخفضة إلى متوسطة | [n8n](workflows/02-booking-assistant.n8n.json) |
| 3 | [تأهيل العملاء المحتملين](03-lead-qualification.md) | طرح أسئلة التأهيل وتسليم العميل الجاهز للمبيعات | منخفضة إلى متوسطة | [n8n](workflows/03-lead-qualification.n8n.json) |
| 4 | [مطابقة الفواتير](04-invoice-reconciliation.md) | مطابقة الفواتير مع كشف الحساب وإبراز الفروقات | متوسطة | [n8n](workflows/04-invoice-reconciliation.n8n.json) |
| 5 | [تلخيص المنافسات](05-tender-summariser.md) | قراءة كراسات الشروط وتلخيصها وتقييم الملاءمة | متوسطة | [n8n](workflows/05-tender-summariser.n8n.json) |

</div>

Five templates for agents serving common Saudi business jobs. Each has a **specification** that can be built in a low-code tool or in code, and, since v0.9, a **runnable version**: an [n8n workflow](workflows/README.md) that runs on import with a simulated model, no key and no cost. The runnable version is the agent's core and its limits, not a product: no channel or system is connected, and it has not been run with a real language model.

## Every template has the same parts

1. **The job** and when it starts and ends
2. **Tools** the agent needs
3. **Knowledge** it answers from
4. **Flow** step by step
5. **Oversight table**: autonomous, notify, approve, forbidden
6. **Instruction skeleton** in Arabic
7. **Test cases to include**
8. **Cost drivers**
9. **Data notes**

## Before you build from a template

- Complete the [AI MVP Blueprint](../../04-entrepreneur-toolkit/07-ai-mvp-blueprint.md) for your own customer; the template is a starting point, not your product.
- Implement the oversight table **outside the model**.
- Build your [evaluation set](../evaluation/eval-template.md) before showing the agent to anyone.
- Use synthetic data until the [PDPL self-assessment](../../02-saudi-market-knowledge-framework/compliance-toolkit/pdpl-self-assessment.md) is done.
- Messaging platforms have their own business policies and template-approval rules. Read them before designing the conversation.

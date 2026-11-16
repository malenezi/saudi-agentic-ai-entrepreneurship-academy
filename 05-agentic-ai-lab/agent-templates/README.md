# قوالب الوكلاء · Agent templates

<div dir="rtl">

خمسة مواصفات لوكلاء يخدمون أعمالاً شائعة في السوق السعودي. كل قالب **مواصفة** يمكن بناؤها بأداة منخفضة الكود أو بالبرمجة، وليس ملفاً جاهزاً للتشغيل. النسخ القابلة للتشغيل تصدر في إصدار لاحق.

| # | القالب | المهمة | الصعوبة |
|---|---|---|---|
| 1 | [خدمة العملاء عبر واتساب](01-whatsapp-customer-service.md) | الرد على الاستفسارات المتكررة وتحويل ما عداها | منخفضة |
| 2 | [مساعد الحجوزات](02-booking-assistant.md) | حجز المواعيد وتعديلها والتذكير بها | منخفضة إلى متوسطة |
| 3 | [تأهيل العملاء المحتملين](03-lead-qualification.md) | طرح أسئلة التأهيل وتسليم العميل الجاهز للمبيعات | منخفضة إلى متوسطة |
| 4 | [مطابقة الفواتير](04-invoice-reconciliation.md) | مطابقة الفواتير مع كشف الحساب وإبراز الفروقات | متوسطة |
| 5 | [تلخيص المنافسات](05-tender-summariser.md) | قراءة كراسات الشروط وتلخيصها وتقييم الملاءمة | متوسطة |

</div>

Five specifications for agents serving common Saudi business jobs. Each is a **specification** that can be built in a low-code tool or in code; runnable versions follow in a later iteration.

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

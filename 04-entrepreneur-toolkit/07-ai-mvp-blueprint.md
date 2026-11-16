# مخطط المنتج الأولي · AI MVP Blueprint

Design the agent and the smallest product around it before building. One job, done reliably.

**المشروع · Venture:** ____________  **التاريخ · Date:** ____________

## 1. المهمة · The job

| | |
|---|---|
| المهمة الواحدة التي ينجزها المنتج · The one job the product does | |
| يبدأ عند · Starts when (trigger) | |
| ينتهي عند · Ends when (definition of "resolved") | |
| خارج النطاق في هذا الإصدار · Out of scope for this version | |

## 2. سير العمل · Workflow

One row per step. Mark who does it: الوكيل (agent), إنسان (human), نظام (system).

| # | الخطوة · Step | المنفّذ · Who | الأداة أو النظام · Tool or system | البيانات المستخدمة · Data used | ماذا لو فشلت · If it fails |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |

## 3. ورقة تصميم الوكيل · Agent design sheet

| العنصر · Element | الوصف · Description |
|---|---|
| **الهدف · Goal** | |
| **الدور والنبرة · Role and tone** (فصحى مبسطة، لهجة، رسمي، ودود) | |
| **المعرفة · Knowledge** (ما المصادر التي يقرأ منها؟) | |
| **الأدوات · Tools** (ماذا يستطيع أن يفعل؟) | |
| **الذاكرة · Memory** (ماذا يتذكر، وكم المدة؟) | |
| **الحدود · Limits** (ما الذي لا يفعله أبداً؟) | |
| **التصعيد · Escalation** (متى يحوّل إلى إنسان، وإلى من؟) | |
| **صيغة المخرجات · Output format** | |

Then complete the [Human Oversight Matrix](../02-saudi-market-knowledge-framework/compliance-toolkit/human-oversight-matrix.md) for every tool listed.

## 4. المعمارية · Architecture choice

| القرار · Decision | الخيار · Choice | السبب · Reason |
|---|---|---|
| أتمتة عادية، سير عمل بخطوة نموذج، وكيل واحد، أم عدة وكلاء؟ · Plain automation, workflow with a model step, one agent or several? | | |
| منخفض الكود أم برمجي؟ · Low-code or code? | | |
| النموذج: مستضاف أم مفتوح الأوزان ذاتي الاستضافة؟ · Hosted model or self-hosted open weights? | | |
| أين تُعالَج البيانات؟ · Where is data processed? | | |
| القناة: واتساب، ويب، بريد؟ · Channel? | | |

Default to the simplest option that does the job. Record why you rejected the simpler one.

## 5. خصوصيات السوق السعودي · Saudi specifics checklist

- [ ] يفهم الفصحى واللهجة السعودية والكتابة المختلطة عربي/إنجليزي · Understands MSA, Saudi dialect and mixed Arabic/English
- [ ] يتعامل مع التاريخ الهجري والميلادي · Handles Hijri and Gregorian dates
- [ ] يعرض المبالغ بالريال ويحسب ضريبة القيمة المضافة حين يلزم · Shows SAR amounts and VAT where relevant
- [ ] يتعامل مع أرقام الجوال والعناوين بالصيغة المحلية · Handles local phone and address formats
- [ ] يراعي أوقات العمل وأيام نهاية الأسبوع والمواسم (رمضان، الحج) · Respects local working hours, weekend and seasons
- [ ] النبرة مناسبة ثقافياً، راجعها شخص سعودي · Tone reviewed by a Saudi native speaker
- [ ] واجهة من اليمين إلى اليسار · Right-to-left interface

## 6. التقييم · Evaluation plan

| | |
|---|---|
| عدد حالات الاختبار ومصدرها · Number of test cases and their source | |
| معيار النجاح للحالة · Pass criterion per case | |
| نسبة النجاح المطلوبة قبل أول عميل · Success rate required before the first customer | |
| من يراجع المخرجات · Who reviews outputs | |

See the [Evaluation Template](../05-agentic-ai-lab/evaluation/eval-template.md).

## 7. ما يجب أن يتوفر في المنتج الأولي · MVP must-haves

- [ ] ينجز المهمة الواحدة من البداية إلى النهاية · Completes the one job end to end
- [ ] رسالة إفصاح بأنه مساعد آلي · Discloses that it is an automated assistant
- [ ] طريق واضح للوصول إلى إنسان · A clear path to a person
- [ ] سجل للإجراءات والتكلفة لكل مهمة · Action and cost log per task
- [ ] مفتاح إيقاف · Kill switch
- [ ] سياسة خصوصية · Privacy notice
- [ ] وسيلة لجمع ملاحظات المستخدم · A way to collect user feedback

## 8. خطة الأسبوعين · Two-week plan

| اليوم · Day | الهدف · Goal |
|---|---|
| 1 to 2 | ورقة التصميم ومصفوفة الرقابة · Design sheet and oversight matrix |
| 3 to 6 | نسخة تعمل على حالات بسيطة · Working version on simple cases |
| 7 to 8 | مجموعة التقييم وأول قياس · Test set and first measurement |
| 9 to 11 | إصلاح الإخفاقات · Fix failures |
| 12 | النشر على قناة اختبار · Deploy to a test channel |
| 13 to 14 | تجربة مع مستخدم حقيقي · Trial with a real user |

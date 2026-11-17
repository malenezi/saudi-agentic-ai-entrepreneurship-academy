# قاموس المؤشرات · KPI dictionary

Exercise [B5](../b5-venture-dashboard.md). These are the definitions `compute_metrics.py` uses. Change a definition only if you also write down why.

<div dir="rtl">

قبل أي مؤشر، ثلاث وحدات عدّ لا تُخلط:

| الوحدة | معناها | في البيانات |
|---|---|---|
| المهمة (Task) | عمل تجاري مطلوب: طلب خدمة، فاتورة، استفسار | سطر في `tasks.csv` |
| التشغيل (Agent run) | محاولة واحدة من الوكيل لتنفيذ مهمة | سطر في `agent_usage.csv` |
| استدعاء الأداة (Tool call) | نداء واحد لأداة داخل تشغيل | عمود `tool_calls` |

مهمة واحدة قد تحتاج تشغيلين وسبعة استدعاءات. عدّها سبع مهام يضخّم الإنتاجية.

**المقام:** «المهام النهائية» هي المكتملة والفاشلة بعد حذف الأسطر المكررة. المعلّقة والملغاة تُعرض ولا تدخل أي نسبة.

</div>

| المؤشر · KPI | المعادلة · Formula | الوحدة | ملاحظة · Note |
|---|---|---|---|
| المهام النهائية · Final tasks | completed + failed | عدد | بعد حذف المكرر |
| نسبة النجاح · Success rate | completed ÷ final × 100 | % | الحالة ليست الجودة: اقرأها مع درجة الجودة |
| نسبة الأتمتة · Automation rate | completed with no human intervention ÷ final × 100 | % | ارتفاعها بتقليل المراجعة ليس تحسناً |
| نسبة التدخل البشري · Human intervention rate | tasks with human intervention ÷ final × 100 | % | |
| نسبة إعادة المحاولة · Retry rate | tasks with retry_count > 0 ÷ final × 100 | % | |
| متوسط زمن الإنجاز · Average resolution time | mean(completed_at − created_at) for completed tasks | ساعة | يشمل انتظار المراجعة البشرية |
| متوسط الجودة · Average quality score | mean(quality_score) for completed tasks | 1 إلى 5 | من عيّنة يراجعها إنسان في الواقع |
| تكلفة النموذج · Model cost | Σ model_cost over all runs | ريال | كل التشغيلات، ومنها الفاشلة والمعادة |
| تكلفة الأدوات · Tool cost | Σ tool_cost over all runs | ريال | |
| تكلفة المراجعة البشرية · Human review cost | Σ review_minutes ÷ 60 × hourly rate | ريال | السعر في `params.json`، وهو افتراض |
| التكلفة المباشرة · Direct cost | model + tool + human review | ريال | لا رواتب ولا منصات ولا تطوير |
| تكلفة المهمة الناجحة · Cost per successful task | direct cost ÷ completed | ريال | تكلفة الفاشلة تتحملها الناجحة |
| الإيراد · Revenue | Σ revenue of completed tasks | ريال | التسعير بالمهمة؛ المبيعات والدعم بلا إيراد |
| الهامش الإجمالي · Gross margin | (revenue − direct cost) ÷ revenue × 100 | % | هامش المهمة، وليس ربح المنشأة |
| محاولات غير مصرّح بها أُوقفت · Unauthorized attempts blocked | blocked events for actions outside the agent's allow-list | عدد | محاولة موقوفة دليل على عمل الضابط |
| تنفيذ بلا موافقة لازمة · Executed without required approval | approval_required = 1, result = executed, approved_by empty | عدد | المستهدف صفر دائماً |
| موافقات معلّقة · Approvals pending | result = pending_approval | عدد | |
| تغطية سجل التدقيق · Audit coverage | final tasks with a task_closed event ÷ final × 100 | % | |
| العملاء الجدد · New customers | signup_date within the period | عدد | |
| معدل الانسحاب الشهري · Monthly churn | churned in period ÷ customers at period start × 100 | % | |
| متوسط كلفة الاستحواذ · Average acquisition cost | mean(acquisition_cost) of new customers | ريال | |
| تحويل العملاء المحتملين · Lead to customer | new customers ÷ completed lead_qualification tasks × 100 | % | تقريب: العميل قد يأتي من شهر سابق |
| الإيراد لكل عميل نشط · Revenue per active customer | revenue ÷ active customers at period end | ريال | |

<div dir="rtl">

## ما ليس في القاموس، ولماذا

- **الإيراد الشهري المتكرر (MRR):** الشركة في التمرين تسعّر بالمهمة، فلا اشتراك يتكرر. إن كان نموذجك اشتراكاً فأضفه.
- **القيمة العمرية للعميل (LTV):** شهر واحد من البيانات لا يكفي لحسابها.
- **العائد على الأتمتة (ROI):** يحتاج تكلفة العمل اليدوي قبل الوكيل وتكلفة البناء، وهما ليسا في البيانات. إن أضفتهما فاكتب أنهما افتراض، وحدد المدة.
- **رضا العملاء:** لا استبيان في البيانات. درجة الجودة تقدير مراجع، وليست رأي العميل.

## المستهدفات

اكتب مستهدفاً لكل مؤشر قبل أن ترى الأرقام، مع حد يُطلق تنبيهاً. مستهدف يُكتب بعد رؤية النتيجة وصف لها.

</div>

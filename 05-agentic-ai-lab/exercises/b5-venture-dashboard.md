# B5: لوحة قيادة المشروع الوكيلي
# B5: Agentic venture dashboard

**Tool:** [Bayan](https://github.com/malenezi/bayan) · `arabic-rtl-web`, with the Academy's [data and metrics script](b5-venture-dashboard/README.md) · **Course 4**, Module 4.2, and **Course 3**, Module 3.3 · **Time:** 3 to 4 hours

<div dir="rtl">

## الغرض

بنيت وكيلاً وعرفت أنه يعمل. السؤال التالي سؤال مؤسس: هل يصنع قيمة، وبأي تكلفة، وأين يحتاج إلى إنسان؟ في هذا التمرين تبني لوحة قيادة ثنائية اللغة لشركة افتراضية يشغّلها خمسة وكلاء، كل رقم فيها محسوب من سجلات، ثم تقرأ بها ثلاثة أشهر مختلفة وتكتب قراراً في كل منها.

التمرين عن القرار. لوحة جميلة بلا قرار لا تجتاز.

## الشركة

**مِرساة لخدمات الأعمال** شركة افتراضية تقدّم خدمات إدارية للمنشآت الصغيرة وتسعّر بالمهمة. الاسم والعملاء والأسعار والنماذج كلها مخترعة.

| الوكيل | العمل | إيراد؟ |
|---|---|---|
| المبيعات | تأهيل العملاء المحتملين | لا |
| خدمة العملاء | الرد على الاستفسارات | لا |
| العمليات | تنفيذ طلبات الخدمة | نعم |
| المالية | إعداد الفواتير | نعم |
| التقارير | تقرير أسبوعي لكل عميل | نعم |

## ما تحتاجه

- [ملفات التمرين](b5-venture-dashboard/README.md): شهر من البيانات في أربعة ملفات CSV، وبرنامج يحسب المؤشرات.
- [القالب ثنائي اللغة](https://github.com/malenezi/bayan/blob/main/skills/arabic-rtl-web/assets/starter-bilingual.html) من «بيان»، ومرجع [الأرقام والتواريخ](https://github.com/malenezi/bayan/blob/main/skills/arabic-rtl-web/references/numbers-dates-forms.md).
- Python 3.9 أو أحدث.

## الخطوات

### 1. المؤشرات قبل البيانات (30 دقيقة)

اقرأ [قاموس المؤشرات](b5-venture-dashboard/kpi-dictionary.md). اختر من 12 إلى 15 مؤشراً، ووزّعها على أربعة أصناف: تشغيلي، مالي، تجاري، وحوكمة. اكتب لكل مؤشر مستهدفاً وحداً يُطلق تنبيهاً، **قبل** أن ترى الأرقام.

### 2. نظّف البيانات (30 دقيقة)

افتح `tasks.csv`. فيه أسطر مكررة ومهام مفتوحة بخانات فارغة. قرر: ما الذي يُحذف، وما الذي يُعرض ولا يدخل النسب؟ ثم عُدّ: كم مهمة، كم تشغيلاً، كم استدعاء أداة؟ الثلاثة أرقام مختلفة، واللوحة تعرض الأول.

### 3. احسب (30 دقيقة)

</div>

```bash
cd 05-agentic-ai-lab/exercises/b5-venture-dashboard
python3 compute_metrics.py data/baseline --out metrics.json --js metrics.js
```

<div dir="rtl">

- **قليل البرمجة:** استخدم `metrics.js` الناتج مصدراً للوحة. اقرأ البرنامج لتعرف من أين جاء كل رقم.
- **المسار العميق:** احسب المؤشرات ببرنامجك أو بجدولك، واحفظها بالأسماء نفسها في `my_metrics.json`، ثم قارن:

</div>

```bash
python3 compute_metrics.py data/baseline --compare my_metrics.json
```

<div dir="rtl">

للمعايرة، شهر الأساس: 961 مهمة نهائية نُفّذت في 1,163 تشغيلاً و3,746 استدعاء أداة؛ نسبة النجاح 93.3%؛ تكلفة المهمة الناجحة 1.43 ريال؛ الهامش الإجمالي 72.1%.

### 4. ابنِ اللوحة (60 إلى 90 دقيقة)

ستة أقسام في ملف HTML واحد، بالعربية أساساً مع تبديل إلى الإنجليزية:

| القسم | يجيب عن | الحد الأدنى |
|---|---|---|
| الملخص التنفيذي | ما حال المشروع؟ | خمسة مؤشرات وأهم تنبيهين |
| أداء الوكلاء | أي وكيل يحتاج عناية؟ | جدول للوكلاء الخمسة: النجاح، التدخل البشري، تكلفة المهمة، الجودة |
| كفاءة التشغيل | أين يتعطل العمل؟ | المهام النهائية والمعلّقة، إعادة المحاولة، زمن الإنجاز |
| اقتصاديات الوكلاء | هل المهمة مربحة؟ | التكلفة بمكوّناتها الثلاثة، تكلفة المهمة الناجحة، الهامش |
| الحوكمة والمخاطر | هل يعمل الوكلاء ضمن حدودهم؟ | محاولات أُوقفت، تنفيذ بلا موافقة، موافقات معلّقة، تغطية التدقيق |
| النمو التجاري | هل ينمو العمل؟ | عملاء جدد ومنسحبون، كلفة الاستحواذ |

قواعد البناء:

- لا رقم مكتوب باليد في HTML. الأرقام تُملأ من `metrics.js`. [الهيكل المرفق](b5-venture-dashboard/skeleton.html) يريك الطريقة بمؤشرين.
- كل رقم وعملة ونسبة داخل `<bdi dir="ltr">`.
- شارة «بيانات مصطنعة» ظاهرة في رأس اللوحة.
- اللوحة تعمل بفتح الملف مباشرة. المتصفح يمنع قراءة CSV من `file://`، ولهذا يُخرج البرنامج ملف `metrics.js`.
- التنبيه يُبنى على الحد الذي كتبته في الخطوة 1.

افحص حتى يصفو المخرج:

</div>

```bash
python3 bayan/shared/scripts/bidi_lint.py my-venture/dashboard/index.html --strict
python3 bayan/shared/scripts/i18n_parity.py my-venture/dashboard/index.html
```

<div dir="rtl">

### 5. ثلاثة أشهر مختلفة (45 دقيقة)

ولّد ثلاثة سيناريوهات، واحسب مؤشرات كل منها، واعرضها في لوحتك:

</div>

```bash
for s in cost-spike quality-drop volume-up; do
  python3 generate_data.py --scenario $s --out data/$s
  python3 compute_metrics.py data/$s --js metrics-$s.js
done
```

<div dir="rtl">

لكل سيناريو املأ مدخلاً في [سجل قرارات المؤسس](b5-venture-dashboard/founder-decision-log.md): الملاحظة، الدليل، التشخيص، القرار، ومن ينفّذ ومتى تراجع. اكتب ملاحظتك من اللوحة أولاً، ثم اقرأ وصف السيناريو في رأس `generate_data.py`.

أحد الثلاثة تبدو أرقامه الأولى أفضل من شهر الأساس، وحال الشركة فيه أسوأ. إن لم تكشفه لوحتك فينقصها مؤشر.

### 6. اعرض (20 دقيقة)

ثلاث دقائق كأنك أمام مجلس إدارة: ما حال المشروع، ما أكبر مشكلة، وما القرار الذي توصي به ولماذا.

## ما تعلّمه بيانات شهر الأساس

- المراجعة البشرية 62% من التكلفة المباشرة، والنموذج 12%. من يراقب تكلفة النموذج وحدها يراقب أصغر البنود.
- وكيلان من خمسة بلا إيراد. تكلفتهما تُحمَّل على المهام المدفوعة.
- أعلى نسبة نجاح لا تعني أفضل وكيل: قارن النجاح بالتكلفة والجودة والتدخل البشري معاً.
- محاولة موقوفة ليست حادثة. الحادثة فعل يحتاج موافقة ونُفّذ بدونها، ومستهدفها صفر.

## ما ليست هذه اللوحة

- **ليست مراقبة.** البيانات مولَّدة. المراقبة الفعلية تحتاج سجلات تنفيذ من بيئة تشغيل وكيلك، وهذا عمل المسار العميق في الوحدة 4.2.
- **الهامش هنا هامش المهمة**، بلا رواتب ولا منصات ولا تطوير. هل تعيش المنشأة؟ سؤال [R4](r4-financial-model.md).
- **الأسعار وتكاليف النماذج مخترعة.** لا تنقل منها رقماً إلى نموذجك؛ قِس أرقامك.

## معيار الإنجاز

- [ ] مستهدف وحدّ تنبيه لكل مؤشر، مكتوبان قبل الحساب.
- [ ] `compute_metrics.py --compare` يخرج بـ`[OK]` (المسار العميق)، أو اللوحة تقرأ من `metrics.js` بلا رقم مكتوب باليد.
- [ ] الأقسام الستة موجودة، وشارة «بيانات مصطنعة» ظاهرة.
- [ ] `bidi_lint.py --strict` و`i18n_parity.py` بلا ملاحظات.
- [ ] ثلاثة مداخل في سجل القرارات، في كل منها مؤشر ورقم وموعد مراجعة.
- [ ] السيناريو المضلِّل مكشوف، والمؤشر الذي كشفه مسمّى.

## بعده

استبدل بالبيانات المصطنعة سجلات وكيلك: نتائج [R6](r6-agent-evaluation.md)، ومحاولات [R7](r7-agent-red-teaming.md)، وتكلفة المهمة من [الحاسبة](../../04-entrepreneur-toolkit/06-unit-economics.md). ورقة المؤشرات الأسبوعية وسجل التغييرات هما مخرج الوحدة 4.2 في [المقرر 4](../../03-courses/04-scale-and-govern/syllabus.md).

</div>

---

**English.** Build a single-file, Arabic-first dashboard with an English toggle for a fictional five-agent services company, with every figure computed from four synthetic CSV files. Write targets and alert thresholds before computing, clean the deliberate duplicates, compute the KPIs (or check your own with `compute_metrics.py --compare`), build six sections on Bayan's bilingual starter, and pass `bidi_lint.py --strict` and `i18n_parity.py`. Then generate three scenarios and write one founder decision for each. One scenario looks better on the headline figures while the company is worse off; a dashboard that does not reveal it is missing a KPI. The data is generated, so this is practice in reading a dashboard, not monitoring.

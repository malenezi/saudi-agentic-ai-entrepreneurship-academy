# R8: فحص جودة البيانات وحوكمتها قبل أن تغادر جهازك
# R8: Data quality and governance check before data leaves your machine

**Tool:** the Academy's [`data_governance_lint.py`](r8-data-governance/data_governance_lint.py), with [Riyada](https://github.com/malenezi/riyada) context layer 5 (knowledge and data) · **Course 2**, Module 2.5, and **Course 3**, Module 3.4 · **Time:** 2 hours

<div dir="rtl">

## الغرض

من أخطاء المقرر 2 الشائعة: إرسال بيانات عملاء حقيقية إلى أداة أثناء الاختبار. في هذا التمرين تكتب سياسة بيانات لملف واحد، هو مجموعة اختبار وكيلك أو عيّنة من بيانات عميل، وتفحصه ببرنامج قبل أن يدخل أي نموذج أو أداة خارجية.

## ما يثبته البرنامج وما لا يثبته

البرنامج يقرأ أسماء الأعمدة والقيم. يثبت أن الملف يطابق **السياسة التي كتبتها أنت**. لا يثبت امتثالاً لنظام حماية البيانات الشخصية: الأساس النظامي، والغرض، ومدة الحفظ، وإمكان إعادة تحديد هوية شخص، كلها خارج ما يراه برنامج. لهذه: [التقييم الذاتي](../../02-saudi-market-knowledge-framework/compliance-toolkit/pdpl-self-assessment.md) و[دليل المؤسس](../../02-saudi-market-knowledge-framework/03-data-protection-pdpl/pdpl-founder-guide.md)، ثم مختص.

## ما تحتاجه

- [ملفات التمرين](r8-data-governance/): البرنامج، وسياسة مثال `policy.json`، وعيّنة مصطنعة `dataset_sample.csv` فيها أخطاء مقصودة.
- Python 3.9 أو أحدث، بلا مكتبات إضافية.

## الخطوات

1. **شغّل الفحص على العيّنة كما هي:**

</div>

```bash
cd 05-agentic-ai-lab/exercises/r8-data-governance
python3 data_governance_lint.py dataset_sample.csv policy.json
```

<div dir="rtl">

للمعايرة: 13 خطأً وتحذيران، ورمز خروج 1.

2. **اقرأ كل ملاحظة واتخذ قراراً.** القرار لك وليس للبرنامج:

| القاعدة | ما وجده | قراراتك الممكنة |
|---|---|---|
| `DG002` | عمود بلا تصنيف | صنّفه في السياسة. مستويات التصنيف في المثال توضيحية؛ خذ مستوياتك من سياسة منشأتك أو عميلك |
| `DG003` | مفتاح مكرر | احذف المكرر، أو اعرف لماذا تكرر |
| `DG004` | خانات فارغة فوق الحد | املأ من المصدر، أو احذف الأسطر، أو ارفع الحد واكتب السبب |
| `DG005` | قيمة خارج القائمة | صحّحها، أو أضفها إلى القائمة إن كانت مشروعة |
| `DG006` و`DG009` | عمود حساس حاضر | احذفه إن لم تحتجه المهمة. هذا هو الجواب في أغلب الحالات |
| `DG007` | قيمة تشبه رقم هوية أو جوالاً أو بريداً أو آيبان داخل نص | احذفها أو استبدل بها رمزاً. انتبه: الأرقام العربية تُكشف أيضاً |
| `DG008` | فئة ممثَّلة بأقل من الحد | أضف حالات لها، أو اكتب أن نتائجك لا تشملها |

3. **أصلح الملف** حتى يمر مع `--strict`. لا تُسكت قاعدة بتعديل السياسة إلا بسبب مكتوب في حقل `description`.
4. **طبّقه على ملفك:** مجموعة الاختبار من [R6](r6-agent-evaluation.md)، بسياسة تكتبها من نسخة المثال. أول سؤال: هل يحتاج الوكيل هذا العمود ليؤدي المهمة؟
5. **سجّل النتيجة** في الطبقة الخامسة من حزمة السياق ([R2](r2-context-pack.md)): ما البيانات، وما تصنيفها، ومن المسؤول عنها، وتاريخ آخر فحص.

## حدود `DG008`

هذا فحص تمثيل: هل كل فئة حاضرة بما يكفي لتُختبر؟ ليس تدقيق تحيز. وكيل قد يخطئ مع فئة حاضرة بكثرة. التحقق من ذلك بمقارنة نسب النجاح بين الفئات في R6.

## معيار الإنجاز

- [ ] العيّنة تمر مع `--strict` بعد إصلاحها، وكل تعديل على السياسة له سبب مكتوب.
- [ ] ملفك أنت يمر بسياستك أنت.
- [ ] لا عمود في ملفك لا تحتاجه المهمة.
- [ ] الطبقة الخامسة محدَّثة بالتصنيف والمسؤول وتاريخ الفحص.
- [ ] جملة مكتوبة بخطك: «اجتياز الفحص لا يعني الامتثال؛ بقي كذا وكذا» من التقييم الذاتي.

## بعده

[التقييم الذاتي لنظام حماية البيانات الشخصية](../../02-saudi-market-knowledge-framework/compliance-toolkit/pdpl-self-assessment.md) و[تقييم المزوّد](../../02-saudi-market-knowledge-framework/compliance-toolkit/third-party-provider-assessment.md) في الوحدة 3.4. المسار العميق: شغّل الفحص في CI على مجلد مجموعات الاختبار.

</div>

---

**English.** Write a data policy for one file (your agent's test set or a customer sample) and check the file with `data_governance_lint.py` before it reaches any model or external tool. The script checks required columns, classification, duplicate keys, empty cells, allowed values, restricted column names, values that look like ID numbers, mobiles, emails or IBANs (Arabic digits included), group representation and columns above the shareable level. The shipped sample produces 13 errors and 2 warnings; a cleaned copy passes with `--strict`. A pass means the file meets the policy you wrote. It is not a finding of compliance with the Personal Data Protection Law.

# معمارية التشغيل · Operating architecture

For [Module 4.1](../lessons/4-1-the-agent-operated-company.md). Four tables and a diagram. The test at the end is a rubric criterion: nothing consequential is unowned. A worked version is in the [example](../examples/worked-example-scale-pack.md).

**المنشأة · Venture:** ____________  **التاريخ · Date:** ____________  **آخر مراجعة · Last review:** ____________

## 1. الوظائف · Functions

| الوظيفة · Function | مهام يحملها وكيل أو أتمتة اليوم · Carried by an agent or automation today | ما يبقى عند إنسان · Stays with a person | لماذا · Why |
|---|---|---|---|
| المبيعات · Sales | | | |
| المنتج والدعم · Product and support | | | |
| العمليات · Operations | | | |
| المالية · Finance | | | |
| التقارير · Reporting | | | |

## 2. سجل الوكلاء · Agent register

One row per agent. A rule-based automation is listed too, and marked as such.

| الوكيل · Agent | الوظيفة · Function | المستوى 1 إلى 4 وسببه · Level 1 to 4 and why | المالك (اسم) · Owner (a name) | الأدوات والصلاحيات · Tools and permissions | ما لا يفعله · What it does not do | النموذج وإصداره · Model and version | آخر تقييم ونتيجته · Last evaluation and result |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |

Levels are the Academy's, from the [governance playbook](../../../02-saudi-market-knowledge-framework/02-ai-regulations/agentic-ai-governance-playbook.md): 1 informs, 2 recommends, 3 acts reversibly, 4 acts with material effect.

## 3. السياق المشترك · Shared context

| نوع السياق · Kind | مصدر الحقيقة · Source of truth | من يقرأ · Who reads | من يكتب · Who writes | الاحتفاظ · Retention |
|---|---|---|---|---|
| سياق المنشأة · Company context | | | | |
| سجل العميل · Customer record | | | | |
| حالة المهمة · Task state | | | | |
| الذاكرة طويلة الأمد · Long-term memory | | | | |

- [ ] لا يرى وكيل يخدم عميلاً سجل عميل آخر · No agent serving one customer can read another's record
- [ ] ما يُكتب في الذاكرة يُتحقق منه، ويمكن مراجعته وحذفه · Memory writes are validated and can be reviewed and deleted

## 4. التسليمات ونقاط الموافقة · Handoffs and approval points

| من ← إلى · From → to | ما يُسلَّم (حقول) · What is handed over (fields) | الشرط · Condition | المالك (اسم) · Owner (a name) | إن لم يُستلم: بعد كم، وإلى من · If not picked up: after how long, to whom |
|---|---|---|---|---|
| | | | | |
| | | | | |

## 5. القرارات المؤثرة · Consequential decisions

A decision is consequential if it moves money, binds the company, discloses data, changes a permission or cannot be undone.

| القرار · Decision | المالك (اسم) · Owner (a name) | كيف يُوثَّق · How it is recorded | من ينوب · Deputy |
|---|---|---|---|
| تغيير تعليمات وكيل أو أدواته في الإنتاج · Changing an agent's instructions or tools in production | | | |
| إضافة مزوّد أو تغييره · Adding or changing a provider | | | |
| رفع مستوى استقلالية وكيل · Raising an agent's level | | | |
| | | | |

## 6. المخطط · The diagram

<div dir="rtl">

مربع لكل وكيل، ومربع لكل دور بشري، ومربع لكل نظام، وسهم لكل تسليم. علّم نقاط الموافقة. ألصق الصورة أو رابطها هنا: ____________

**اختبار المالك:** لكل سهم يحمل قراراً مؤثراً، اسم إنسان بجواره. عدد الأسهم بلا اسم: ______ (المطلوب صفر).

</div>

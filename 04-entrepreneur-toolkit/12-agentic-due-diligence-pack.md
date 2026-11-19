# ملف الفحص التقني لمشروع وكيلي · Agentic Due-Diligence Pack

<div dir="rtl">

> ما يطلبه مستثمر أو مشترٍ أو عميل مؤسسي حين يفحص منتجاً قائماً على الوكلاء. ستة أسئلة، ولكل سؤال دليل. ما لا دليل عليه يُكتب **مفتوح**، ولا يُجمَّل. هذا الملف يكمل غرفة البيانات العامة ولا يغني عنها: [قائمة غرفة البيانات في «ريادة»](https://github.com/malenezi/riyada/blob/main/templates/fundraising/data-room-checklist.ar.md).
>
> **تنبيه:** قالب تعليمي، وليس استشارة قانونية ولا استثمارية.

</div>

What an investor, acquirer or enterprise buyer asks when examining an agent-based product: six questions, each with evidence. Anything without evidence is written **open**. It complements a general data room (incorporation, cap table, contracts) and does not replace one. Educational template; not legal or investment advice.

**Prepared on · تاريخ الإعداد:** ____ · **Product version · إصدار المنتج:** ____ · **Prepared by · أعدّه:** ____

## 1. هل يعمل؟ · Does it work?

| البند · Item | دليلك · Your evidence | الحالة · Status |
|---|---|---|
| المهمة الواحدة التي يؤديها الوكيل وحدودها · The one job and its limits | | جاهز · مفتوح |
| مجموعة الاختبار: عدد الحالات، مصدرها، كم منها محجوز · Test set: size, origin, held-back share | | |
| نسبة النجاح: خط الأساس، وآخر ثلاثة قياسات بتواريخها · Success rate: baseline and last three dated runs | | |
| سجل الإخفاقات مصنّفاً، وما لم يُصلح · Classified failure log, including what is not fixed | | |
| نسبة النجاح في الواقع مقابل الاختبار · Production success versus test success | | |

## 2. هل يربح؟ · Does it earn?

| البند · Item | دليلك · Your evidence | الحالة · Status |
|---|---|---|
| تكلفة المهمة المنجزة ومكوّناتها · Cost per resolved task and its parts ([calculator](cost_per_resolved_task.py)) | | |
| تكلفة المراجعة البشرية والمهام الفاشلة ضمن الحساب · Human review and failed tasks included | | |
| السعر وطريقته · Price and pricing model | | |
| الهامش لكل مهمة، وحساسيته لنسبة النجاح وسعر النموذج · Margin per task and its sensitivity | | |

## 3. هل يُستخدم؟ · Is it used?

| البند · Item | دليلك · Your evidence | الحالة · Status |
|---|---|---|
| عدد المنشآت المستخدمة، ومن منها يدفع · Businesses using it, and how many pay | | |
| المهام الأسبوعية لآخر ثمانية أسابيع · Weekly task volume, last eight weeks | | |
| العملاء الذين عادوا بعد الشهر الأول · Customers still active after month one | | |
| خطابات نوايا أو عقود (بلا بيانات شخصية) · LOIs or contracts, personal data removed | | |
| أكبر عميل كنسبة من الإيراد · Largest customer as a share of revenue | | |

## 4. ماذا لو تغيّر المزوّد؟ · What if the provider changes?

| البند · Item | دليلك · Your evidence | الحالة · Status |
|---|---|---|
| المزوّدون: النموذج، الاستضافة، المراسلة، وما يعتمد على كل منهم · Providers and what depends on each | | |
| نتيجة مجموعة الاختبار على نموذج بديل واحد على الأقل · Test-set result on at least one alternative model | | |
| خطة التبديل: الخطوات والمدة المقدّرة · Switching plan: steps and estimated time | | |
| ضبط تغيير النموذج والتعليمات: من يوافق، وكيف يُختبر · Change control for model and prompt | | |
| شروط كل مزوّد في البيانات والتدريب والاحتفاظ · Each provider's data, training and retention terms ([assessment](../02-saudi-market-knowledge-framework/compliance-toolkit/third-party-provider-assessment.md)) | | |

## 5. هل هو آمن ومتوافق؟ · Is it safe and compliant?

| البند · Item | دليلك · Your evidence | الحالة · Status |
|---|---|---|
| صلاحيات الوكيل: ما يقرأ، ما يكتب، ما لا يستطيعه · Permissions: read, write, cannot | | |
| الإجراءات التي تحتاج موافقة إنسان · Actions needing human approval ([matrix](../02-saudi-market-knowledge-framework/compliance-toolkit/human-oversight-matrix.md)) | | |
| خريطة البيانات الشخصية: ماذا، أين، كم يُحتفظ به · Personal-data map ([PDPL self-assessment](../02-saudi-market-knowledge-framework/compliance-toolkit/pdpl-self-assessment.md)) | | |
| نتيجة اختبار حقن التعليمات على وكيلك · Prompt-injection test result ([assessment](../02-saudi-market-knowledge-framework/compliance-toolkit/agent-security-assessment.md)) | | |
| سجل الحوادث وما تغيّر بعدها · Incident log and what changed after each | | |
| سجل المخاطر · Risk register ([template](../02-saudi-market-knowledge-framework/compliance-toolkit/ai-risk-register.md)) | | |

## 6. ما الذي تملكه؟ · What do you own?

| البند · Item | دليلك · Your evidence | الحالة · Status |
|---|---|---|
| ما لا ينسخه منافس بإصدار نموذج جديد · What a new model release does not give a competitor | | |
| بيانات التقييم: من يملكها، وهل يجوز استخدامها · Evaluation data: ownership and right to use | | |
| التكاملات والعقود التي يصعب تكرارها · Integrations and contracts that are hard to replicate | | |
| الشيفرة والتعليمات: من كتبها، وتحت أي ترخيص · Code and prompts: authorship and licences | | |
| هل تعمل الشركة إن غاب المؤسس شهراً؟ · Does it run if the founder is away for a month? | | |

## الخلاصة · Summary

| | العدد · Count |
|---|---|
| بنود جاهزة · Items ready | |
| بنود مفتوحة · Items open | |
| أخطر ثلاثة بنود مفتوحة، وصاحب كل منها وتاريخه · Three most serious open items, each with owner and date | |

<div dir="rtl">

**قواعد:** لا رقم بلا تاريخ ومصدر من سجلك. لا تُدخل بيانات شخصية لعملاء أو مستخدمين في الملف. ما يغطيه شرط سرية يُحذف أو يُلخَّص. والبند المفتوح المكتوب بصدق أقوى من بند مجمَّل يسقط عند أول سؤال.

</div>

**Rules.** No number without a date and a source in your own records. No personal data of customers or users. Remove or summarise anything under a confidentiality clause. An honestly open item is stronger than a polished one that fails the first question.

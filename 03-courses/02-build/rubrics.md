# سلالم التقدير · Rubrics

The deliverable rubric keeps the criteria and weights of the [syllabus](syllabus.md). This file adds four performance levels for each criterion, the validation gates, and ungraded checkpoints for each module.

## 1. Assessment

The six-part deliverable is graded as one piece of work with the rubric in section 3. Module outputs are checkpoints: they are reviewed, not graded separately. Self-paced learners use the checkpoints and the [readiness checklist](templates/readiness-checklist.md) as self-checks. The [module quizzes](quizzes/README.md) are formative and carry no weight.

## Completion

The four courses share one [assessment and completion standard](../assessment-standard.md), version 1.0. A deliverable is **complete** when every validation gate is "yes", no criterion is at level 1, the lead criterion (**does the job**) is at level 3 or above, and the weighted score is 2.7 or more out of 4. **Distinction:** no criterion below level 3 and a weighted score of 3.5 or more. Lab results are practice and are not graded. One resubmission after written feedback. Check a set of levels with `python3 tools/score_submission.py 2 --levels … --gates …`.

## 2. Validation gates

Checked before the deliverable is graded. Any "no" returns the project, whatever the score would be.

| # | Gate |
|---|---|
| 1 | No sensitive action runs without approval: every level-C action paused, every level-D action failed when attempted |
| 2 | No unauthorised data was disclosed in any safety or authority case |
| 3 | There is a test another person can re-run and check: the cases, the pass criteria and the run log are submitted |
| 4 | No material failure is hidden: the failure log lists what was not fixed |

<div dir="rtl">

## 3. سلّم تقدير المشروع

| المعيار والوزن | 4 متقن | 3 جيد | 2 نامٍ | 1 غير مكتمل |
|---|---|---|---|---|
| **إنجاز المهمة 30%** | ينجز المهمة من أولها إلى آخرها على حالات متنوعة؛ نسبة النجاح معلنة للمجموعة ولكل فئة، ومعها المتذبذب؛ بلغ قاعدة إطلاق كُتبت قبل التشغيل، أو قال بوضوح إنه لم يبلغها | ينجز المهمة مع قصور محدود معلَن؛ النسبة الكلية معلنة | يعمل في الحالات البسيطة؛ النسبة بلا تفصيل | لا وكيل يعمل، أو لا نسبة |
| **جودة التقييم 25%** | 30 حالة أو أكثر بتركيبة القالب؛ نصفها من مواقف حقيقية؛ عشر باللهجة على الأقل؛ معايير نجاح تُفحص؛ ثلاثة تشغيلات؛ مجموعة محجوزة | 30 حالة بمعايير واضحة ولهجة؛ تشغيل واحد | حالات كتبها الباني، أغلبها فصحى؛ معايير عامة | خمس حالات، أو لا معايير |
| **ضوابط الحماية 20%** | صف لكل فعل؛ الحدود مفروضة خارج النموذج؛ اختبار المصفوفة منفّذ؛ حقن مباشر وغير مباشر مختبران؛ سجلات منقّحة | بوابات منفّذة للأفعال المهمة؛ حقن مباشر مختبر | القواعد في التعليمات، وبوابة واحدة | لا بوابة منفّذة |
| **التحسين 15%** | دورتان، في كل منهما تغيير واحد موثق؛ المجموعة كلها أُعيدت؛ التراجعات فُحصت؛ الجودة والتكلفة والزمن والمخاطر مقارنة؛ ما لم يُعالَج مكتوب | دورتان بنتائج قبل وبعد؛ الأسباب مذكورة | تغييرات بلا تصنيف ولا إعادة كاملة | لا سجل إخفاقات |
| **جودة العربية 10%** | يفهم الفصحى واللهجة والكتابة المختلطة؛ مخرجاته طبيعية لعميل سعودي بحكم مراجع سعودي؛ التواريخ والمبالغ والأسماء سليمة | مخرجات واضحة مع هنات؛ اللهجة مفهومة غالباً | فصحى فقط، أو ترجمة حرفية | مخرجات لا تصلح للإرسال |

مشروع بنسبة نجاح متواضعة معلنة وسجل إخفاقات صادق ينال في «إنجاز المهمة» و«التحسين» أعلى من مشروع بنسبة عالية على خمس حالات.

## 4. نقاط المراجعة في كل وحدة (بلا درجات)

| الوحدة | المخرج | ما ينظر فيه المدرب أو الزميل |
|---|---|---|
| 2.1 | ورقة التصميم والقرار | هل الهدف يُتحقق منه؟ هل رُفض الأبسط بسبب؟ |
| 2.2 | التعليمات وقالب السياق وخمس رسائل | هل مصادر الحقيقة والحدود مكتوبة؟ هل في الرسائل لهجة؟ |
| 2.3 | أداتان وعقداهما | هل الصلاحية أقل ما يلزم؟ هل اختُبر الفشل؟ |
| 2.4 | مذكرة اختيار النموذج | هل ثبتت التعليمات والحالات؟ هل قُرئ الترخيص ومكان المعالجة؟ |
| 2.5 | المجموعة وخط الأساس وقاعدة الإطلاق | هل كُتبت القاعدة قبل التشغيل؟ هل المعايير تُفحص؟ |
| 2.6 | المصفوفة وبوابتان واختبار حقن | هل لكل فعل صف؟ هل الضابط في التطبيق؟ |
| 2.7 | المخطط والقرار | هل أُجيب عن الأسئلة الستة؟ هل هناك شرط لإعادة النظر؟ |
| 2.8 | السجل والدورتان والعرض | هل في كل دورة تغيير واحد؟ هل ذُكر ما بقي؟ |

## 5. معايرة المقيّمين

- قيّما مشروعين معاً قبل التقييم المنفرد. معيار «جودة التقييم» هو الأكثر انحرافاً: اتفقا أولاً على ما يُعدّ معيار نجاح «يُفحص».
- أعيدا تشغيل خمس حالات من مجموعة المتعلم، منها حالة أمان. بوابة التحقق الثالثة لا تُقبل بالقراءة وحدها.
- ليحكم على «جودة العربية» شخص سعودي.

</div>

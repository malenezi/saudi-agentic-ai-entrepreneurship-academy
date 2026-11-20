# سلالم التقدير · Rubrics

The deliverable rubric keeps the criteria and weights of the [syllabus](syllabus.md). This file adds four performance levels for each criterion, the validation gates, and ungraded checkpoints for each module.

## 1. Assessment

The six-part scale pack is graded as one piece of work with the rubric in section 3; the pitch on Demo Day is its window, and counts for 15%. Module outputs are checkpoints: they are reviewed, not graded separately. Self-paced learners use the checkpoints and the [scale pack checklist](templates/scale-pack-checklist.md) as self-checks. The [module quizzes](quizzes/README.md) are formative and carry no weight.

**Graduation condition** (from the syllabus): a signed LOI from a Saudi business, a paying customer, or sustained real usage. Without one of the three the pack is returned, whatever its score.

## Completion

The four courses share one [assessment and completion standard](../assessment-standard.md), version 1.0. A deliverable is **complete** when every validation gate is "yes", no criterion is at level 1, the lead criterion (**customer evidence**) is at level 3 or above, and the weighted score is 2.7 or more out of 4. **Distinction:** no criterion below level 3 and a weighted score of 3.5 or more. The graduation condition below also applies. One resubmission after written feedback. Check a set of levels with `python3 tools/score_submission.py 4 --levels … --gates …`.

## 2. Validation gates

Checked before the pack is graded. Any "no" returns it.

| # | Gate |
|---|---|
| 1 | Graduation evidence is real, checkable and named for what it is (an LOI is not a customer) |
| 2 | The KPI sheet comes from a log, or is plainly labelled pilot or synthetic data, and no week was removed |
| 3 | Every consequential decision has a named owner, and no agent acts with material effect without human approval |
| 4 | The risk register has at least six risks in the product's own words, each with an owner and a control that exists or a dated plan, and no row copied from the template |
| 5 | The pitch states the success rate with its counts and what the agent does not do, has no unsourced number, and presents nothing staged as live |

<div dir="rtl">

## 3. سلّم تقدير حزمة التوسع

| المعيار والوزن | 4 متقن | 3 جيد | 2 نامٍ | 1 غير مكتمل |
|---|---|---|---|---|
| **دليل العميل 30%** | عميل يدفع أو أكثر، بفاتورة وسجل استخدام؛ أو استخدام حقيقي مستمر أربعة أسابيع فأكثر بأعداده؛ كل دليل مسمّى باسمه؛ ما لم يثبت مكتوب | خطاب نوايا موقّع من صاحب صلاحية بشروط محددة، ومعه استخدام من تجربة | تجربة مجانية جارية، أو خطاب اهتمام عام | «مهتمون»، أو دليل لا يُتحقق منه |
| **تصميم التشغيل 20%** | سجل وكلاء بمستوى ومالك مسمّى وما لا يفعله كل وكيل؛ سياق مشترك بمصدر حقيقة وعزل؛ تسليمات بحقولها الخمسة؛ قائمة قرارات مؤثرة بمالكيها؛ لا سهم بلا اسم؛ ما هو أتمتة مسمّى أتمتة | تقسيم واضح ومالكون مسمّون؛ بعض التسليمات بلا «إن لم يُستلم» | مخطط بوكلاء وأدوار، والمالك «الفريق» | قائمة وكلاء بلا أدوار بشرية |
| **الحوكمة والأمن 20%** | ستة مخاطر فأكثر بكلمات المنتج؛ لكل منها مالك وضابط خارج النموذج حيث أمكن، قائم أو مؤرخ؛ تقييم أمن مكتمل وكل «لا» بإجراء؛ خطة حوادث بأسماء؛ مفتاح إيقاف مجرَّب؛ سجل يُراجَع بموعد | مخاطر خاصة بالمنتج بمالكين وضوابط؛ تقييم الأمن مكتمل؛ بعض الضوابط في التعليمات | مزيج من أسطر القالب وأسطر خاصة؛ ضوابط عامة | سجل منسوخ، أو لا تقييم أمن |
| **الاقتصاديات عند التوسع 15%** | جدول الحجم بثلاثة مستويات من أرقام السجل؛ ساعات الإنسان ودرجاتها ظاهرة؛ نقطة التعادل محسوبة وأين المنشأة منها؛ أثر نسبة النجاح مبيَّن؛ الهامش يشمل المراجعة والفشل | هامش المهمة ونقطة التعادل محسوبان، بلا درجات الإنسان | هامش اليوم وحده، أو منحنى بلا تكاليف مراجعة | أرقام بلا حساب |
| **العرض 15%** | سبع محطات في الوقت؛ كل ادعاء بدليله؛ عرض حي لمسار واحد فيه تصعيد وسجل وحالة غير محضّرة؛ الحدود تُقال بأعدادها؛ الطلب ثمن مرحلة؛ «لا نعرف بعد» حيث تصح | عرض مبني على الأدلة مع عرض حي؛ الحدود مذكورة باختصار | عرض مزايا؛ عرض حي بلا حدود؛ طلب مبلغ بلا مرحلة | وعود، أو عرض مرتَّب قُدِّم على أنه حي |

حزمة فيها عميلان يدفعان، وأسبوع سيئ في الورقة، وخطر مكتوب أنه بلا ضابط، تنال أعلى من حزمة فيها عشرة «مهتمين» وورقة بلا عثرة وسجل يدّعي الكمال.

## 4. نقاط المراجعة في كل وحدة (بلا درجات)

| الوحدة | المخرج | ما ينظر فيه المدرب أو الزميل |
|---|---|---|
| 4.1 | معمارية التشغيل | هل لكل سهم يحمل قراراً مؤثراً اسم؟ هل أُضيف وكيل حيث تكفي أتمتة؟ |
| 4.2 | ورقة المؤشرات وسجل التغيير | هل النسب مكتوبة بأعدادها؟ هل في الورقة أسبوع سيئ؟ هل العتبات مكتوبة مسبقاً؟ |
| 4.3 | سجل المخاطر | هل يعرف قارئ غريب ما المنتج من السجل وحده؟ هل «قائم» قائم فعلاً؟ |
| 4.4 | تقييم الأمن وخطة الحوادث | هل لكل «لا» إجراء؟ هل جُرّب مفتاح الإيقاف؟ هل سُحبت صلاحية بلا سبب؟ |
| 4.5 | مذكرة المسار وخارطة التوسع | هل للمرحلة ثمن محسوب؟ هل المسار المستبعد مكتوب بسببه؟ |
| 4.6 | العرض وورقة التشغيل | هل لكل رقم مصدر؟ هل في العرض الحي حالة تصعيد؟ هل الحدود مكتوبة لتُقال؟ |

## 5. معايرة المقيّمين

- قيّما حزمتين معاً قبل التقييم المنفرد. معيار «دليل العميل» هو الأكثر انحرافاً: اتفقا أولاً على ما يُعدّ «استخداماً مستمراً» وما يُعدّ تجربة.
- بوابة التحقق الأولى لا تُقبل بالقراءة: اطلبا الفاتورة أو الخطاب أو السجل، بعد حجب ما يلزم.
- لا يحكم المقيّم على صحة موقف قانوني أو أمني أو استثماري. يحكم على أن السؤال طُرح، وأن ما لم يُحسم مكتوب بمالك وتاريخ.
- أعيدا حساب تكلفة المهمة المنجزة وجدول الحجم من مدخلات المتعلم بالحاسبة.
- في يوم العروض: محكّم واحد على الأقل يكتب الحالة غير المحضّرة.

</div>

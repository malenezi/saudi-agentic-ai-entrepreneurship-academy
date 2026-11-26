# مصفوفة قدرات الوكيل · Agent capability matrix

**Status:** Added 26 November 2026 · Developed by the Academy · **Not tried with learners** · Educational

<div dir="rtl">

> **من تطوير الأكاديمية.** ليست معياراً معتمداً. شرحها في [بطاقة مصفوفة قدرات الوكيل](../cards/agent-capability-matrix.md).

تجيب عن سؤال واحد قبل البناء: ما الذي يجب أن يُحسنه الوكيل ليؤدي هذه المهمة، ومن أين تأتي كل قدرة، وما الدليل على أنها تعمل؟ تُملأ من خريطة سير العمل، سطراً لكل قدرة.

</div>

**المهمة · Task:** ____________  **التاريخ · Date:** ____________  **النسخة · Version:** ____

## 1. القدرات المطلوبة · Capabilities needed

| # | القدرة · Capability | تلزم في أي خطوة · Needed at step | مصدرها · Provided by | الدليل · Evidence | الحالة · Status |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

<div dir="rtl">

**كيف تملأ الأعمدة:**

- **القدرة:** فعل محدد يمكن اختباره. «فهم رسالة عميل باللهجة واستخراج رقم الطلب منها»، لا «فهم اللغة».
- **مصدرها:** واحد من أربعة: النموذج اللغوي، أداة، قاعدة في الشيفرة، إنسان. ما يمكن حسمه بقاعدة لا يُترك للنموذج.
- **الدليل:** أرقام الحالات في [مجموعة التقييم](../../05-agentic-ai-lab/evaluation/eval-template.md) التي تختبر هذه القدرة. قدرة بلا حالة تقييم قدرة مفترضة.
- **الحالة:** مُثبتة (مع النسبة وتاريخ التشغيل)، مفترضة، أو غير متوفرة.

</div>

**How to fill the columns.** *Capability:* one testable act, such as "read a customer message in dialect and extract the order number", not "understand language". *Provided by:* one of four: the language model, a tool, a rule in code, a person; what a rule can settle is not left to the model. *Evidence:* the numbers of the cases in the evaluation set that test this capability; a capability with no case is an assumed one. *Status:* proven (with the rate and the run date), assumed, or not available.

## 2. ما لا يُطلب من الوكيل · What the agent is not asked to do

| القدرة المستبعدة · Capability left out | لماذا · Why | من يتولاها · Who does it instead |
|---|---|---|
| | | |
| | | |

## 3. القرار · Decision

- [ ] كل قدرة لازمة لها مصدر مسمّى · <bdi dir="ltr" lang="en">Every needed capability has a named source</bdi>
- [ ] كل قدرة مصدرها النموذج لها حالات تقييم · <bdi dir="ltr" lang="en">Every capability provided by the model has evaluation cases</bdi>
- [ ] لا قدرة «مفترضة» في خطوة لها أثر خارجي · <bdi dir="ltr" lang="en">No "assumed" capability at a step with an outside effect</bdi>

**أضعف قدرة · Weakest capability:** ____________  **ما الذي يُفعل حيالها · What is done about it:** ____________

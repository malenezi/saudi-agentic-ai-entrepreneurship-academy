# R2: حزمة سياق تمر من المدقق
# R2: A context pack that passes the linter

**Tool:** [Riyada](https://github.com/malenezi/riyada) · `founder-context`, `context_lint.py` · **Course 2**, Module 2.2 · **Time:** 2 to 3 hours

<div dir="rtl">

## الغرض

وكيل بنموذج قوي وبلا سياق يكتب كلاماً عاماً. في هذا التمرين تحوّل [قالب سياق المؤسس](../../04-entrepreneur-toolkit/10-founder-context-template.md) ذا الملف الواحد إلى حزمة من سبع طبقات، وتثبت ببرنامج أنها كاملة ومتسقة.

## متى تنتقل من الملف الواحد إلى الحزمة؟

الملف الواحد يكفي ما دمت تتحدث مع مساعد. انتقل إلى الحزمة حين يبدأ وكيل بتنفيذ عمل: عندها تحتاج طبقة الصلاحيات مستقلة، وتاريخ مراجعة لكل طبقة، وفحصاً آلياً.

## ما تحتاجه

- قالب سياق المؤسس الذي ملأته في المقرر 1، وأطروحتك.
- Python 3.9 أو أحدث.

## الخطوات

1. انسخ القوالب السبعة:

</div>

```bash
mkdir -p my-venture/context
cp riyada/context/0*.ar.md my-venture/context/
python3 riyada/shared/scripts/context_lint.py my-venture/context/
```

<div dir="rtl">

2. سيخرج المدقق بأكثر من مئة خطأ، أغلبها `CTX002` (خانة لم تُملأ). هذا المتوقع. عدد الأخطاء هو قائمة عملك.
3. املأ الطبقات بالترتيب: الهوية، الاستراتيجية، العملاء والسوق، العمليات، المعرفة والبيانات، الصلاحيات والحوكمة، الذاكرة والتعلّم. انقل من قالب الأكاديمية ومن الأطروحة ولا تكتب من جديد.
4. **الطبقة السادسة تكتبها أنت.** لا تترك وكيلاً يستنتج صلاحياته. يجب أن تحوي مصفوفة اعتماد وقاعدة «ممنوع» واحدة على الأقل؛ خذ بوابات الموافقة من القسم الرابع في أطروحتك.
5. أعد تشغيل المدقق حتى يخرج بلا أخطاء.
6. قارن حزمتك بـ[حزمة «موجة»](https://github.com/malenezi/riyada/tree/main/examples/mawja/context/ar)، وهي منشأة خيالية تمر حزمتها من المدقق.

مع وكيل: «ابنِ حزمة السياق من هذين الملفين واسألني عمّا ينقص»، ثم راجع كل حقيقة كتبها.

## تحدٍّ إضافي: ملفان يتعارضان

المدقق يكشف تعارض الحقول المصرَّحة (`CTX009`: الحقل نفسه بقيمتين في ملفين). لا يكشف تعارضاً في جملة أو جدول. اكتب عمداً في الطبقة الثالثة جملة فيها سعر يخالف جدول الأسعار في الطبقة الخامسة. المدقق سيمر. اسأل وكيلك عن السعر وسجّل: أيهما اختار؟ وهل نبّه إلى التعارض؟ ثم احذف الجملة وأحِل إلى الجدول، واملأ حقل «عند تعارض مصدرين» في الطبقة الخامسة بالمرجع المعتمد ومن يُبلَّغ. القاعدة نفسها في [الوحدة 1.4](../../03-courses/01-opportunity/lessons/1-4-workflow-shadowing.md): لكل معلومة نظام سجل واحد.

## ما لا يدخل الحزمة

كلمات مرور، مفاتيح، بيانات شخصية لعملاء، أرقام مالية سرية. المدقق ينبّه إلى ما يشبه سراً، لكن المسؤولية عليك. ولطبقة البيانات راجع [دليل نظام حماية البيانات الشخصية](../../02-saudi-market-knowledge-framework/03-data-protection-pdpl/pdpl-founder-guide.md): قوالب «ريادة» لا تعرف أنظمة المملكة.

## معيار الإنجاز

- [ ] `context_lint.py` يخرج بلا أخطاء (رمز خروج صفر).
- [ ] الطبقة السادسة فيها مصفوفة اعتماد وقاعدة «ممنوع».
- [ ] لكل طبقة تاريخ مراجعة.
- [ ] المسار العميق: المدقق يعمل بوابةً في CI مع `--strict`.

## بعده

[R3](r3-role-card-and-approval-matrix.md)، ثم مسار [أول وكيل في 30 يوماً](https://github.com/malenezi/riyada/blob/main/workflows/04-first-agent-in-30-days.ar.md). قواعد المدقق: [lint-rules.md](https://github.com/malenezi/riyada/blob/main/skills/founder-context/references/lint-rules.md).

</div>

---

**English.** Turn the Academy's one-file Founder Context Template into Riyada's seven-layer context pack and run `context_lint.py` until it reports no errors. Empty templates start with well over a hundred findings; that count is the to-do list. The founder writes layer 6 (authority) personally. Saudi data rules come from the Academy's PDPL guide, not from the pack.

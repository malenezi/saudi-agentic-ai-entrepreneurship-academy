# B6: مسرد المنشأة واتساق المصطلحات
# B6: A venture glossary and consistent terminology

**Tool:** the Academy's [`terminology_lint.py`](b6-terminology/terminology_lint.py), with [Bayan](https://github.com/malenezi/bayan) · `arabic-ux-writing` (glossary) · **Course 2**, Module 2.2, and **Course 3**, Module 3.1 · **Time:** 90 minutes

<div dir="rtl">

## الغرض

صفحتك تقول «الوكيل»، ورسالة الترحيب تقول «المساعد الذكي»، والعرض يقول «العميل الذكي». المشتري يقرأ ثلاثة منتجات. في هذا التمرين تقرر مصطلحاً عربياً واحداً لكل مفهوم، وتكتب ما قررت ألا تستخدمه، ثم يفرض برنامج قرارك على كل ملفاتك.

## القرار لك

المسرد قرار وليس حقيقة. البرنامج لا يحكم بأن مصطلحاً أفصح من آخر؛ يتأكد أنك التزمت بما اخترت. مراجع الاختيار:

- [مسرد «بيان»](https://github.com/malenezi/bayan/blob/main/skills/arabic-ux-writing/references/glossary.md) لمصطلحات الواجهات والتقنية، وفيه قاعدة: مسرد المنتج يغلب دائماً.
- [مسرد المقرر 1](../../03-courses/01-opportunity/glossary.md) لمصطلحات الوكلاء.
- «معجم البيانات والذكاء الاصطناعي» الصادر عن سدايا ومجمع الملك سلمان العالمي للغة العربية مرجع للمصطلح التقني. الأكاديمية لم تفتح صفحته ولم تنقل منه؛ ارجع إليه بنفسك.
- لغة عملائك في المقابلات. الكلمة التي يقولها المشتري تغلب الكلمة الأدق.

## الخطوات

1. انسخ [المسرد المبدئي](b6-terminology/glossary.csv) وعدّله. ثلاثة أعمدة: المصطلح الإنجليزي، العربي المعتمد، والصيغ المتروكة مفصولة بـ`|`. ابدأ بعشرين مصطلحاً على الأكثر: اسم المنتج، ما يفعله، ومن يراجع.
2. جرّب على المثال:

</div>

```bash
cd 05-agentic-ai-lab/exercises/b6-terminology
python3 terminology_lint.py glossary.csv sample-before.md
```

<div dir="rtl">

للمعايرة: أربعة أخطاء وتحذير واحد.

3. شغّله على ملفاتك: الرسائل من [B1](b1-agent-messages-in-arabic.md)، والصفحة من [B2](b2-bilingual-landing-page.md)، والعرض من [B3](b3-pitch-deck.md).

</div>

```bash
python3 terminology_lint.py my-venture/glossary.csv my-venture/messages my-venture/site my-venture/deck.html --strict
```

<div dir="rtl">

4. لكل ملاحظة: أصلح النص، أو غيّر المسرد إن أقنعك النص. سطر مقصود يُستثنى بتعليق `terminology-lint-ignore` وسبب.
5. انقل المسرد إلى الطبقة الأولى في حزمة السياق ([R2](r2-context-pack.md))، ليكتب وكيلك بالمصطلحات نفسها.

## ما لا يفعله البرنامج

- لا يصرّف: يطابق الكلمة ومعها «ال» وحروف العطف والجر الملتصقة، ويتجاهل التشكيل وصور الألف. الجمع والمثنى صيغ تضيفها أنت إلى عمود المتروك إن لزم.
- لا يفحص ردود الوكيل المولَّدة. تلك تُختبر بحالات [R6](r6-agent-evaluation.md).
- لا يعرف السياق: «العميل» بمعنى الزبون صحيحة، ولهذا المتروك في المثال «العميل الذكي» وليس «العميل».

## معيار الإنجاز

- [ ] مسرد من عشرين مصطلحاً على الأكثر، ولكل مصطلح صيغة معتمدة واحدة.
- [ ] `terminology_lint.py --strict` بلا ملاحظات على الرسائل والصفحة والعرض.
- [ ] كل استثناء له سبب مكتوب.
- [ ] المسرد في حزمة السياق.
- [ ] قارئ من جمهورك فهم المصطلحات الخمسة الأهم بلا شرح.

</div>

---

**English.** Decide one Arabic term for each concept your venture uses, list the variants you will not use, and let `terminology_lint.py` enforce that decision across your messages, landing page and deck. The script normalises diacritics and alef forms and matches attached prefixes; it does not inflect, does not judge whether a term is good Arabic, and does not check generated replies. The shipped sample gives four errors and one warning. The SDAIA and KSGAAL Data and AI dictionary is named as a reference for the learner to consult; the Academy has not opened it or copied from it.

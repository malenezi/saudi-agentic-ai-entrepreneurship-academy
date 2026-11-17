# B4: تدقيق اتجاه واجهة قائمة
# B4: RTL audit of an existing interface

**Tool:** [Bayan](https://github.com/malenezi/bayan) · `rtl-audit`, `bidi_lint.py` · **Deep track**, Courses 3 and 4 · **Time:** 2 hours

<div dir="rtl">

## الغرض

لديك واجهة بُنيت بالإنجليزية ثم «عُرّبت»: لوحة مراجعة الوكيل، صفحة تسجيل، أو نافذة محادثة. التمرين يكشف عيوب الاتجاه فيها، يرتبها، ويصلحها حتى يصفو المدقق.

## ما تحتاجه

- واجهة لك: HTML أو CSS أو مكونات JSX/TSX/Vue أو ملفات نصوص JSON. إن لم تكن لديك واجهة فاستخدم [ملف «قبل» في مثال «بيان»](https://github.com/malenezi/bayan/tree/main/examples/03-rtl-audit).

## الخطوات

1. **امسح** واحفظ التقرير:

</div>

```bash
python3 bayan/shared/scripts/bidi_lint.py my-venture/src/ --format md > audit-before.md
```

<div dir="rtl">

2. **رتّب.** الأخطاء أولاً (غياب `lang` و`dir`)، ثم ما يراه العميل (أرقام وروابط مقلوبة)، ثم CSS.
3. **راجع يدوياً** ما لا يراه مدقق: [القائمة اليدوية](https://github.com/malenezi/bayan/blob/main/skills/rtl-audit/references/manual-checklist.md).
4. **أصلح بترتيب الاعتماد:** بنية الصفحة، ثم الخصائص المنطقية بدل الفيزيائية، ثم عزل النص اللاتيني، ثم الطباعة. الوصفات: [fix-recipes.md](https://github.com/malenezi/bayan/blob/main/skills/rtl-audit/references/fix-recipes.md).
5. **أعد المسح** حتى الصفر، واكتب التقرير بـ[قالب التقرير](https://github.com/malenezi/bayan/blob/main/skills/rtl-audit/assets/report-template.md).
6. **اجعله بوابة:**

</div>

```bash
python3 bayan/shared/scripts/bidi_lint.py my-venture/src/ --strict
```

<div dir="rtl">

للمعايرة: ملف «قبل» في مثال «بيان» يخرج بخطأين و24 تحذيراً، وملف «بعد» بلا شيء.

## ما هو صحيح أن يبقى فيزيائياً

المدقق يستثني الأزواج المتماثلة والتوسيط والقواعد تحت محدِّد `[dir]`. ما عدا ذلك يُسكَت في موضعه بـ`bidi-lint-ignore` مع سبب مكتوب. إسكات بلا سبب ليس إصلاحاً.

## معيار الإنجاز

- [ ] تقرير «قبل» وتقرير «بعد» محفوظان.
- [ ] الأخطاء صفر، وكل تحذير باقٍ له سبب مكتوب.
- [ ] القائمة اليدوية مكتملة.
- [ ] المدقق يعمل في CI مع `--strict`.

## استخدام آخر: المساهمة في الأكاديمية

المدقق يقرأ Markdown أيضاً. قبل طلب دمج فيه محتوى عربي:

</div>

```bash
python3 bayan/shared/scripts/bidi_lint.py saudi-agentic-ai-entrepreneurship-academy/03-courses/
```

<div dir="rtl">

هذا فحص اختياري يساعدك، وليس شرطاً لقبول المساهمة. محتوى المقرر 1 يمر منه بلا ملاحظات في تاريخ المراجعة.

</div>

---

**English.** Scan an existing interface with `bidi_lint.py`, triage, review what a scanner cannot see, fix in dependency order, rescan to zero, and gate CI with `--strict`. Bayan's own "before" example reports 2 errors and 24 warnings; its "after" reports none. The same linter reads Markdown, so contributors can optionally run it on Arabic content before a pull request to the Academy.

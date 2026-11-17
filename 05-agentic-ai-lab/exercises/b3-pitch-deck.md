# B3: عرض الأطروحة أو العرض الاستثماري
# B3: Thesis pitch or investor deck

**Tool:** [Bayan](https://github.com/malenezi/bayan) · `arabic-html-slides` · **Course 4**, Module 4.6; optional in **Course 1**, Module 1.7 · **Time:** 3 hours

<div dir="rtl">

## الغرض

عرض بالعربية مع تبديل إلى الإنجليزية، يُقدَّم من المتصفح ويُطبع PDF. نسختان من التمرين: عرض مختصر من ثلاث دقائق لأطروحة المقرر 1، أو العرض الاستثماري في المقرر 4.

## من أين يأتي المحتوى؟

| العرض | الهيكل | المصدر |
|---|---|---|
| عرض الأطروحة (5 إلى 6 شرائح) | العميل، سير العمل، الدليل، الوكيل وحدوده، الاقتصاديات، ما سنثبته تالياً | [قالب الأطروحة](../../03-courses/01-opportunity/templates/thesis-template.md) |
| العرض الاستثماري | [هيكل العرض](../../04-entrepreneur-toolkit/08-pitch-deck-outline.md) من اثنتي عشرة شريحة | الأكاديمية؛ وللمقارنة [هيكل «ريادة»](https://github.com/malenezi/riyada/blob/main/templates/fundraising/pitch-deck-outline.ar.md) |

«بيان» يعطيك المحرك والصنعة. المحتوى مسؤوليتك.

## الخطوات

1. **الخط السردي قبل أي HTML.** رسالة واحدة حاكمة، ثم عناوين الشرائح جملاً كاملة تُقرأ وحدها كحجة. المنهج: [storytelling.md](https://github.com/malenezi/bayan/blob/main/skills/arabic-html-slides/references/storytelling.md).
2. اختبر العناوين: اقرأها متتالية على شخص لم يرَ مشروعك. إن لم يفهم الطلب فأعد الكتابة.
3. انسخ [محرك العرض](https://github.com/malenezi/bayan/blob/main/skills/arabic-html-slides/assets/deck-starter.html) واستبدل المحتوى. فكرة واحدة لكل شريحة. أنماط الشرائح: [slide-patterns.md](https://github.com/malenezi/bayan/blob/main/skills/arabic-html-slides/references/slide-patterns.md).
4. كل رقم على شريحة له مصدر أو كلمة «تقدير» بجانبه. لا حجم سوق منقول.
5. الحركة آخر شيء، وبأقل قدر.
6. افحص:

</div>

```bash
python3 bayan/shared/scripts/bidi_lint.py my-venture/deck.html --profile deck --strict
python3 bayan/shared/scripts/i18n_parity.py my-venture/deck.html
```

<div dir="rtl">

7. تصفّح العرض كاملاً بكل لغة. في العربية السهم الأيسر يتقدم، و`L` يبدّل اللغة، و`P` يطبع.

مثال مكتمل: [عرض تنفيذي في «بيان»](https://github.com/malenezi/bayan/tree/main/examples/02-executive-deck).

## معيار الإنجاز

- [ ] العناوين جمل كاملة، والطلب في الشريحة الأخيرة.
- [ ] `--profile deck --strict` بلا ملاحظات.
- [ ] `i18n_parity.py` بلا مشكلات.
- [ ] كل رقم له مصدر أو معلَّم بأنه تقدير.
- [ ] شريحة للحوكمة: ما يفعله الوكيل وحده، وما يحتاج موافقة.
- [ ] نسخة PDF مطبوعة ومراجَعة.

## بعده

في المقرر 4: غرفة البيانات وتحديث المستثمرين من [مهارة التمويل في «ريادة»](https://github.com/malenezi/riyada/tree/main/skills/fundraising)، والمشهد المحلي من [التمويل والاستثمار](../../02-saudi-market-knowledge-framework/06-funding-investment/README.md).

</div>

---

**English.** Build an Arabic-first HTML deck with an English switch on Bayan's deck engine: a short thesis pitch for Course 1, or the investor deck for Course 4 using the Academy's twelve-slide outline. Storyline first, titles as sentences, motion last. Done when `bidi_lint.py --profile deck --strict` and `i18n_parity.py` report nothing and every number carries a source or is labelled an estimate.

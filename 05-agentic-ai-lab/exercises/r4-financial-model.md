# R4: من تكلفة المهمة إلى نموذج 36 شهراً
# R4: From cost per task to a 36-month model

**Tool:** [Riyada](https://github.com/malenezi/riyada) · `financial-modeling`, `build_model.py` · **Course 3**, Module 3.3, and **Course 4**, Module 4.5 · **Time:** 90 minutes

<div dir="rtl">

## الغرض

[حاسبة الأكاديمية](../../04-entrepreneur-toolkit/06-unit-economics.md) تجيب: هل أربح في **المهمة** الواحدة؟ نموذج «ريادة» يجيب: هل تعيش **المنشأة**، ومتى ينفد النقد؟ التمرين يربط الاثنين.

## الربط بين الأداتين

| من حاسبة الأكاديمية | إلى ملف الافتراضات في «ريادة» |
|---|---|
| السعر للمهمة × المهام الشهرية للعميل | `revenue_per_customer` |
| الهامش الإجمالي للمهمة (نسبة) | `gross_margin` |
| لا يوجد | `new_customers_month_1`، `new_customer_growth`، `monthly_churn`، `acquisition_cost_per_customer`، `team`، `funding` |

الهامش في النموذج يجب أن يكون هامش الحاسبة **بعد** المراجعة والتصعيد والمحاولات الفاشلة. هامش مرتفع جداً علامة على أن تكلفة النموذج والمراجعة سقطت من الحساب، والبرنامج ينبّه إلى ذلك.

## الخطوات

1. شغّل حاسبة الأكاديمية بأرقامك وسجّل السعر والهامش.
2. انسخ [ملف الافتراضات](https://github.com/malenezi/riyada/blob/main/templates/finance/assumptions.json) واملأه. المعدلات كسور عشرية شهرية.
3. ابنِ النموذج:

</div>

```bash
python3 riyada/shared/scripts/build_model.py my-venture/assumptions.json --out my-venture/model --lang ar
```

<div dir="rtl">

4. اقرأ `model.md`: أول شهر تعادل، أدنى رصيد نقدي وشهره، ومدة استرداد كلفة الاستحواذ.
5. إن صار النقد سالباً يطبع البرنامج تحذيراً مانعاً ويخرج برمز غير صفري. لا تعدّل الافتراضات لتُسكته. قرر: سعر أقرب إلى القيمة، عميل أكبر، مراجعة أقل، أو تمويل.
6. أعد البناء بثلاثة سيناريوهات تقابل ما في [الوحدة 1.6](../../03-courses/01-opportunity/lessons/1-6-scoring-and-economics.md): الهامش بعد مضاعفة المراجعة، نصف معدل اكتساب العملاء، وضعف معدل الانسحاب.

## مثال للتجربة (أرقام افتراضية)

بأرقام المثال المحلول في المقرر 1 (1,300 فاتورة × 2.00 ريال = 2,600 ريال للعميل شهرياً، وهامش 27%)، مع افتراضات مخترعة للتوضيح: نقد ابتدائي 150,000 ريال، عميلان في الشهر الأول بنمو 8% شهرياً، انسحاب 3%، كلفة استحواذ 1,500 ريال، مؤسس بتكلفة 8,000 ريال، ومصاريف أخرى 4,000 ريال:

| المؤشر | النتيجة |
|---|---|
| أول شهر تعادل | 11 |
| أدنى رصيد نقدي | 76,022 ريالاً في الشهر 10 |
| العملاء في نهاية السنة الثالثة | 284 |

الدرس في السطر الأخير: النموذج يفترض 284 مجموعة مطاعم، والأطروحة النموذجية تعرف طريقاً إلى 12 فقط. البرنامج يطبع هذا التنبيه بنفسه: قارن العدد بالسوق الممكن الوصول إليه.

## معيار الإنجاز

- [ ] كل افتراض له مصدر أو مكتوب بجانبه «افتراض».
- [ ] `gross_margin` مأخوذ من الحاسبة لا مخمَّن.
- [ ] النموذج يُبنى، وإن صار النقد سالباً فالسبب والقرار مكتوبان.
- [ ] عدد العملاء في الشهر 36 مقارَن بالسوق الممكن الوصول إليه.
- [ ] ثلاثة سيناريوهات محفوظة.

## تنبيه

النموذج توقعات مبنية على افتراضاتك، وليس استشارة مالية. الزكاة والضريبة والفوترة الإلكترونية ليست فيه؛ راجع [الضرائب والمحاسبة والتمويل](../../02-saudi-market-knowledge-framework/05-tax-accounting-finance/README.md) ومستشاراً مرخّصاً.

## بعده

النموذج يدخل غرفة البيانات والعرض الاستثماري في المقرر 4 ([B3](b3-pitch-deck.md)). دليل البنية: [model-guide.md](https://github.com/malenezi/riyada/blob/main/skills/financial-modeling/references/model-guide.md).

</div>

---

**English.** The Academy's calculator answers whether one task is profitable; Riyada's model builder answers whether the company survives. Carry price and gross margin per task into the assumptions file, build the 36-month model, and compare the month-36 customer count with the reachable market from the thesis. The sample figures are invented and reproducible with the command shown.

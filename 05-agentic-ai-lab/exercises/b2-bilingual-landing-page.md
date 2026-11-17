# B2: صفحة هبوط ثنائية اللغة للتجربة
# B2: A bilingual landing page for the pilot

**Tool:** [Bayan](https://github.com/malenezi/bayan) · `arabic-rtl-web` · **Course 3**, Module 3.5 · **Time:** 2 to 3 hours

<div dir="rtl">

## الغرض

صفحة واحدة تعرض خدمتك على أول عشرة عملاء: عربية أولاً، مع تبديل إلى الإنجليزية، وتمر من المدققين. الصفحة تصلح أيضاً «اختبار صفحة هبوط» في بطاقة التجربة ([R1](r1-evidence-scorecard-and-experiment.md)).

## ما تحتاجه

- جملة الفرصة والقسم الخامس من أطروحتك.
- إن وُجد: [التموضع والرسائل](https://github.com/malenezi/riyada/blob/main/templates/gtm/positioning-messaging.ar.md) و[ملف العميل المثالي](https://github.com/malenezi/riyada/blob/main/templates/gtm/icp-profile.ar.md) من «ريادة». المحتوى من هناك، والبناء هنا.

## الخطوات

1. انسخ [القالب ثنائي اللغة](https://github.com/malenezi/bayan/blob/main/skills/arabic-rtl-web/assets/starter-bilingual.html) في ملف واحد.
2. اكتب المحتوى بالعربية أولاً، بلغة المشتري لا بلغة التقنية (راجع [الوحدة 1.7](../../03-courses/01-opportunity/lessons/1-7-writing-the-thesis.md)):

| القسم | المحتوى |
|---|---|
| العنوان | النتيجة التي يحصل عليها العميل، في سطر |
| المشكلة | الألم بكلمات عملائك من المقابلات، بلا أسماء |
| كيف تعمل | ثلاث خطوات، وفيها أين يوافق الإنسان |
| السعر | وحدة التسعير والسعر، أو «تجربة مدفوعة لمدة كذا» |
| الثقة | أين تُعالج البيانات، ومن يراجع، وكيف يتوقف العميل |
| الطلب | فعل واحد: احجز تجربة |

3. اكتب الإنجليزية نصاً أصيلاً، لا ترجمة حرفية.
4. اعزل كل ما هو لاتيني داخل النص العربي: أرقام الجوال، الروابط، البريد، الأسعار بنطاق. التفاصيل في [bidi-text.md](https://github.com/malenezi/bayan/blob/main/skills/arabic-rtl-web/references/bidi-text.md).
5. افحص وأصلح حتى يصفو المخرج:

</div>

```bash
python3 bayan/shared/scripts/bidi_lint.py my-venture/site/index.html
python3 bayan/shared/scripts/i18n_parity.py my-venture/site/index.html
```

<div dir="rtl">

6. افتح الصفحة في المتصفح باللغتين وعلى جوال. المدقق لا يرى ما تراه العين.

مع وكيل: «ابنِ صفحة هبوط لـ(الخدمة). عربية أولاً مع تبديل إلى الإنجليزية، في ملف HTML واحد»، ثم راجع كل ادعاء في النص.

## تحدٍّ إضافي: اختبر التحويل

صفحة تمر من المدققين صحيحة، وليست بالضرورة مقنعة. قبل أن ترسل الرابط، اكتب في [بطاقة التجربة](https://github.com/malenezi/riyada/blob/main/templates/discovery/experiment-card.ar.md): كم زائراً سترسل، ومن أي قناة، وأي نسبة منهم تضغط «احجز تجربة» تجعلك تمضي، وأيها يوقفك. عُدّ الزيارات والضغطات بوسيلة لا تجمع بيانات شخصية. مع عشرات الزوار، النسبة إشارة وليست قياساً.

## قبل النشر

هذه قائمة للبحث، وليست رأياً قانونياً:

- لا رقم ولا شهادة عميل بلا أساس. «نستهدف» غير «نحقق».
- نموذج يجمع بيانات شخصية يحتاج إشعار خصوصية: [دليل نظام حماية البيانات الشخصية](../../02-saudi-market-knowledge-framework/03-data-protection-pdpl/pdpl-founder-guide.md).
- متطلبات المتاجر والإفصاح: [التجارة الإلكترونية والأعمال الرقمية](../../02-saudi-market-knowledge-framework/08-ecommerce-digital-business/README.md).
- القالب يحمّل الخطوط من خدمة خارجية. راجع ذلك إن كانت سياستك تمنع الاتصال بطرف ثالث.

## معيار الإنجاز

- [ ] `bidi_lint.py` بلا أخطاء ولا تحذيرات.
- [ ] `i18n_parity.py` بلا مشكلات: كل عنصر له مقابله.
- [ ] فعل واحد مطلوب من الزائر.
- [ ] الصفحة تقول أين يوافق الإنسان وأين تُعالج البيانات.
- [ ] جُرّبت على جوال باللغتين.

## بعده

عرض التجربة المدفوعة وخطاب النوايا: [القالب 9](../../04-entrepreneur-toolkit/09-pilot-and-loi-outline.md). ولتدقيق واجهة قائمة: [B4](b4-rtl-audit.md).

</div>

---

**English.** Build a single-file, Arabic-first landing page with an English toggle from Bayan's bilingual starter, using positioning content from the thesis (and from Riyada's go-to-market templates if available). Done when `bidi_lint.py` and `i18n_parity.py` report nothing and the page has been checked on a phone in both languages. A pre-publication list points to the Academy's PDPL and e-commerce guidance.

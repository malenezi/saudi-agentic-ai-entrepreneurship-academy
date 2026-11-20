# عروض المقرر 3 · Course 3 slides

<div dir="rtl">

سبعة عروض، عرض لكل وحدة، بالعربية مع المصطلحات الإنجليزية، بمحرك العروض والهوية البصرية نفسيهما في المقررين 1 و2 (من [بيان](https://github.com/malenezi/bayan)، `arabic-html-slides`). كل عرض ملف HTML واحد يعمل في المتصفح دون تثبيت.

> **عروض مؤلَّفة شريحة شريحة (20 نوفمبر 2026).** حلّت محل العروض المولَّدة آلياً من الدروس. كل شريحة فكرة واحدة بتخطيط يناسبها: سلّم أو مسار، مقارنة، جدول قصير، أعمدة، أرقام كبيرة، أو قائمة. والتفصيل في ملاحظات المتحدث وفي الدرس. لا تضيف العروض معلومة ولا رقماً ليس في الدرس أو المثال المحلول.

| الوحدة | العرض | الشرائح |
|---|---|---|
| 3.1 | [من النموذج الأولي إلى المنتج الأولي](3-1-from-prototype-to-mvp.html) | 12 |
| 3.2 | [نماذج الأعمال للمشاريع الوكيلية](3-2-business-models-for-agentic-ventures.html) | 13 |
| 3.3 | [اقتصاديات الوحدة](3-3-unit-economics.html) | 12 |
| 3.4 | [جاهزية الامتثال](3-4-compliance-readiness.html) | 13 |
| 3.5 | [الوصول إلى السوق في المملكة](3-5-going-to-market-in-the-kingdom.html) | 12 |
| 3.6 | [التجارب وخطابات النوايا](3-6-pilots-and-letters-of-intent.html) | 12 |
| 3.7 | [تأسيس العمل](3-7-setting-up-the-business.html) | 12 |

**للمشاهدة:** افتح [صفحة العروض](https://malenezi.github.io/saudi-agentic-ai-entrepreneurship-academy/) في المتصفح. الروابط في الجدول أعلاه تعرض شيفرة الملف داخل GitHub لا العرض نفسه. وللعمل دون اتصال: نزّل المستودع وافتح [`index.html`](../../../index.html).

**التنقل:** السهم الأيسر أو المسافة للتقدم (الاتجاه يتبع القراءة العربية)، `N` لملاحظات المتحدث، `F` لملء الشاشة، `P` للطباعة إلى PDF (فعّل «رسومات الخلفية»). رقم الشريحة في الرابط: `#5`.

**ملصقات الدليل:** «مثال المقرر · أرقام مختلقة» على كل شريحة تحمل شيئاً من مثال المقرر، وهو نفسه في [المثال المحلول](../examples/worked-example-launch-pack.md). و«مصدر منشور» لما له مدخل في [سجل المصادر](../../../SOURCES.md)، مع حدّه في سطر المصدر.

**مواد مرافقة:** لكل عرض [درسه](../lessons/) و[اختباره القصير](../quizzes/README.md) بإجاباته. و[دليل المدرب](../instructor-guide.md) يحمل توزيع الوقت وملاحظات كل وحدة.

</div>

## For instructors and contributors

- **Shape of every deck:** a title slide, the idea, one slide per teaching point with a layout chosen for it, the course example where the lesson has one, the activity with its minutes, common mistakes, and a bridge to the next module. Ten to thirteen slides. Detail the room does not need on screen is in the speaker notes.
- **Content source:** the lessons of 20 November 2026. The decks add no fact and no number that is not in a lesson, the worked example or [SOURCES.md](../../../SOURCES.md). Slides on regulated topics carry a source line with the entry and its limit.
- **Editing:** edit the fragments in `src/` (one per module) and run `python3 src/build.py`, or `python3 tools/build_slides.py` from the repository root. A test fails if a committed deck differs from its source. Shorthand: `‹term›` for an English term inside Arabic, `⟦27%⟧` for a number or range that must keep its order, `<notes>…</notes>` for speaker notes.
- **Checks run on 20 November 2026:** every slide rendered at 1600 × 900 in headless Chrome and checked by script for overflow and clipped content (none), with a sample inspected by eye; every slide has speaker notes; Bayan's `bidi_lint.py --profile deck` reports no errors, no warnings and no dense-slide notes.
- **Limits:** no drawn demo screens or photographs, unlike some Course 1 decks; nothing here has been used in a room.

Licence: content CC BY 4.0; the deck engine is from Bayan (MIT).

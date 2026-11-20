# عروض المقرر 2 · Course 2 slides

<div dir="rtl">

ثمانية عروض، عرض لكل وحدة، بالعربية مع المصطلحات الإنجليزية، مبنية بمحرك العروض في [بيان](https://github.com/malenezi/bayan) (`arabic-html-slides`). كل عرض ملف HTML واحد يعمل في المتصفح دون تثبيت.

| الوحدة | العرض | الشرائح |
|---|---|---|
| 2.1 | [تشريح الوكيل](2-1-agent-anatomy.html) (يفتتح المقرر كله) | 18 |
| 2.2 | [هندسة السياق بالعربية](2-2-context-engineering-in-arabic.html) | 15 |
| 2.3 | [الأدوات والتكاملات](2-3-tools-and-integrations.html) | 15 |
| 2.4 | [اختيار النموذج](2-4-choosing-a-model.html) | 12 |
| 2.5 | [التقييم](2-5-evaluation.html) | 16 |
| 2.6 | [ضوابط الحماية والموافقة البشرية](2-6-guardrails-and-human-approval.html) | 14 |
| 2.7 | [من وكيل واحد إلى عدة وكلاء](2-7-from-one-agent-to-several.html) | 14 |
| 2.8 | [تحليل الإخفاق والتحسين](2-8-failure-analysis-and-iteration.html) | 14 |

**للمشاهدة:** افتح [صفحة العروض](https://malenezi.github.io/saudi-agentic-ai-entrepreneurship-academy/) في المتصفح. الروابط في الجدول أعلاه تعرض شيفرة الملف داخل GitHub لا العرض نفسه. وللعمل دون اتصال: نزّل المستودع وافتح [`index.html`](../../../index.html).

**التنقل:** السهم الأيسر أو المسافة للتقدم (الاتجاه يتبع القراءة العربية)، `N` لملاحظات المتحدث، `F` لملء الشاشة، `P` للطباعة إلى PDF (فعّل «رسومات الخلفية»). رقم الشريحة في الرابط: `#5`.

**ملصقات الدليل على الشرائح:** «مثال المقرر» و«سيناريو توضيحي» و«شاشة توضيحية» و«أرقام مختلقة» لكل ما هو مخترع للتعليم، ومنه متجر «مِسكة» وكل أرقامه؛ و«دراستان منشورتان» و«رواية الشركة» لما له مصدر في [سجل المصادر](../../../SOURCES.md)، مع حدّه. لا يُعرض مثال مختلق على أنه قياس.

**مواد مرافقة:** لكل عرض [اختبار قصير](../quizzes/README.md) بإجاباته، و[المثال المحلول](../examples/worked-example-order-enquiry-agent.md) يحمل أرقام العروض كلها.

</div>

## For instructors and contributors

- **Content source:** the eight [lessons](../lessons/) of 19 November 2026. The decks add no fact and no number that is not in a lesson, the worked example or [SOURCES.md](../../../SOURCES.md) (A6, A80 to A87 and A121). What the lessons left out of the owner's drafts, and why, is in [not-adopted.md](../not-adopted.md).
- **Editing:** edit the fragments in `src/` (one per module) and run `python3 src/build.py`, or `python3 tools/build_slides.py` from the repository root to build every course. One engine and one page template (`tools/slides/template.html`) serve all courses, and a test fails if a committed deck differs from its source. The generated `.html` files are committed so the decks open straight from the repository. Shorthand in the fragments: `‹term›` for an English term inside Arabic, `⟦27%⟧` for a number or range that must keep its order, `<notes>…</notes>` for speaker notes.
- **Checks run on 19 November 2026:** Bayan's `bidi_lint.py --profile deck` on all eight decks (no errors, no warnings); every slide rendered at 1600 × 900 in headless Chrome and checked by script for overflow and clipped content, with a sample inspected by eye; every slide has speaker notes; the worked-example figures match the lessons (24, 25, 28 and 30 of 35; 68.6%, 71.4%, 80.0% and 85.7%; 6 of 8 held back; 1.25 against 1.40; 0.729).
- **Before each cohort:** re-check the token-ratio figures in deck 2.4 and the multi-agent figures in deck 2.7 against newer sources, the status of the data-residency amendments mentioned in deck 2.4, and whether OWASP has published an edition newer than 2026 (decks 2.3 and 2.6 were updated to the 2026 numbering on 20 November 2026).
- **Fonts:** the decks load IBM Plex Sans Arabic and Noto Kufi Arabic from Google Fonts and fall back to system Arabic fonts offline.

Licence: content CC BY 4.0; the deck engine is from Bayan (MIT).

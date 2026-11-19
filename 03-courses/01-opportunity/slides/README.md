# عروض المقرر 1 · Course 1 slides

<div dir="rtl">

سبعة عروض، عرض لكل وحدة، بالعربية مع المصطلحات الإنجليزية، مبنية بمحرك العروض في [بيان](https://github.com/malenezi/bayan) (`arabic-html-slides`). كل عرض ملف HTML واحد يعمل في المتصفح دون تثبيت.

| الوحدة | العرض | الشرائح |
|---|---|---|
| 1.1 | [من المحادث الآلي إلى الوكيل](1-1-from-chatbots-to-agents.html) (يفتتح المقرر كله) | 28 |
| 1.2 | [المنشأة القائمة على الوكلاء](1-2-agent-native-business.html) | 19 |
| 1.3 | [أين تبحث في السوق السعودي؟](1-3-where-to-look.html) | 20 |
| 1.4 | [مراقبة سير العمل](1-4-workflow-shadowing.html) | 24 |
| 1.5 | [اكتشاف العملاء](1-5-customer-discovery.html) (ومعه ست بطاقات أدوار) | 20 |
| 1.6 | [التقييم والاقتصاديات الأولى](1-6-scoring-and-economics.html) | 19 |
| 1.7 | [كتابة أطروحة الفرصة](1-7-writing-the-thesis.html) | 16 |

**للمشاهدة:** افتح [صفحة العروض](https://malenezi.github.io/saudi-agentic-ai-entrepreneurship-academy/) في المتصفح. الروابط في الجدول أعلاه تعرض شيفرة الملف داخل GitHub لا العرض نفسه. وللعمل دون اتصال: نزّل المستودع وافتح [`index.html`](../../../index.html).

**التنقل:** السهم الأيسر أو المسافة للتقدم (الاتجاه يتبع القراءة العربية)، `N` لملاحظات المتحدث، `F` لملء الشاشة، `P` للطباعة إلى PDF (فعّل «رسومات الخلفية»). رقم الشريحة في الرابط: `#5`.

**ملصقات الدليل على الشرائح:** «حالة منشورة» بمستواها (أ، ب، ج كما في دراسات الحالة)، و«سيناريو توضيحي» لكل مثال مختلق بأرقام مصطنعة، و«فرضية للتحقق» لما يجب أن يختبره المتعلم. لا يُعرض مثال مختلق على أنه بحث سوقي.

**مواد مرافقة:** لكل عرض [اختبار قصير](../quizzes/README.md) بإجاباته، ولكل بطاقة من بطاقات الأدوار الست في عرض الوحدة 1.5 [سجل مقابلة تدريبي](../practice-interviews/README.md) مع مفتاح للمدرب.

</div>

## For instructors and contributors

- **Content source:** [content-pack.md](content-pack.md) records how the two instructor raw-content packs of 19 November 2026 were verified and merged: what was checked, what was corrected, what was not adopted and why, and the open items.
- **Editing:** edit the fragments in `src/` (one per module) and run `python3 src/build.py`, or `python3 tools/build_slides.py` from the repository root to build every course. One engine and one page template (`tools/slides/template.html`) serve all courses, and a test fails if a committed deck differs from its source. The generated `.html` files are committed so the decks open straight from the repository. Shorthand in the fragments: `‹term›` for an English term inside Arabic, `⟦27%⟧` for a number or range that must keep its order, `<notes>…</notes>` for speaker notes.
- **Checks run on 19 November 2026:** Bayan's `bidi_lint.py --profile deck` on all seven decks (no errors, no warnings); every slide rendered at 1600 × 900 in headless Chrome and inspected; the worked-example arithmetic re-computed (cost per resolved task SAR 1.46, review and escalation SAR 0.94 against model SAR 0.20, break-even success 78%, 75 customers, five-month payback).
- **Before each cohort:** re-check prices that change (WhatsApp rates in deck 1.6, outcome pricing in deck 1.2) and, if you have them, show your own captures of working products beside the three illustrative screens in deck 1.1 (slides 10 to 12). Those screens are drawn in HTML with invented data and are labelled «شاشة توضيحية»; they make no claim about any product.
- **Fonts:** the decks load IBM Plex Sans Arabic and Noto Kufi Arabic from Google Fonts and fall back to system Arabic fonts offline.

Licence: content CC BY 4.0; the deck engine is from Bayan (MIT).

# عروض المقرر 4 · Course 4 slides

<div dir="rtl">

ستة عروض، عرض لكل وحدة، بالعربية مع المصطلحات الإنجليزية، بمحرك العروض نفسه المستخدم في المقررين 1 و2 (من [بيان](https://github.com/malenezi/bayan)، `arabic-html-slides`). كل عرض ملف HTML واحد يعمل في المتصفح دون تثبيت.

> **عروض مولَّدة من الدروس (20 نوفمبر 2026).** كل شريحة تحمل بنداً من درسها: جدوله أو قائمته أو جمله الأساسية، ثم النشاط وفرق المسارين والأخطاء الشائعة والمراجعة السريعة. لا تضيف العروض معلومة ولا رقماً ليس في الدرس. هي أبسط تصميماً من عروض المقررين 1 و2 المصمَّمة يدوياً، وتحسينها مرحّب به.

| الوحدة | العرض | الشرائح |
|---|---|---|
| 4.1 | [المنشأة التي يشغّلها الوكلاء](4-1-the-agent-operated-company.html) | 14 |
| 4.2 | [مراقبة الجودة والتكلفة](4-2-monitoring-quality-and-cost.html) | 18 |
| 4.3 | [الحوكمة والمخاطر](4-3-governance-and-risk.html) | 13 |
| 4.4 | [أمن الأنظمة الوكيلية](4-4-security-for-agentic-systems.html) | 15 |
| 4.5 | [مسارات النمو والتمويل والتخارج](4-5-growth-paths-and-funding.html) | 12 |
| 4.6 | [العرض ويوم العروض](4-6-pitch-and-demo-day.html) | 15 |

**للمشاهدة:** افتح [صفحة العروض](https://malenezi.github.io/saudi-agentic-ai-entrepreneurship-academy/) في المتصفح. الروابط في الجدول أعلاه تعرض شيفرة الملف داخل GitHub لا العرض نفسه. وللعمل دون اتصال: نزّل المستودع وافتح [`index.html`](../../../index.html).

**التنقل:** السهم الأيسر أو المسافة للتقدم (الاتجاه يتبع القراءة العربية)، `N` لملاحظات المتحدث، `F` لملء الشاشة، `P` للطباعة إلى PDF (فعّل «رسومات الخلفية»). رقم الشريحة في الرابط: `#5`.

**ملصق «مثال المقرر · أرقام مختلقة»** يظهر على كل شريحة تحمل شيئاً من مثال المقرر. منشأته وأرقامه مخترعة للتعليم، وهي نفسها في [المثال المحلول](../examples/worked-example-scale-pack.md).

**مواد مرافقة:** لكل عرض [درسه](../lessons/) و[اختباره القصير](../quizzes/README.md) بإجاباته. ملاحظات المتحدث في كل شريحة مأخوذة من الدرس، و[دليل المدرب](../instructor-guide.md) يحمل توزيع الوقت وملاحظات كل وحدة.

</div>

## For instructors and contributors

- **How these decks were made:** `python3 tools/slides_from_lessons.py 4` writes one fragment per lesson into `src/`, and `python3 tools/build_slides.py` builds the decks with the shared engine and page template. One slide per numbered section of the lesson, then the activity, track differences, common mistakes and quick review; the first paragraph of each section becomes the speaker notes. Long tables and lists are cut at a clause boundary, never mid-clause, and the notes say when the full table is in the lesson.
- **Editing:** edit a fragment in `src/` and rebuild; a test fails if a committed deck differs from its source. **Once you hand-edit a fragment, do not regenerate it**, or the edit is lost. `src/fit.json` records which slides needed tighter limits to fit the stage.
- **Checks run on 20 November 2026:** every slide rendered at 1600 × 900 in headless Chrome and checked by script for overflow (none after tightening); a sample inspected by eye; every slide has speaker notes; Bayan's `bidi_lint.py --profile deck` on every deck.
- **Known limits:** plainer layouts than Courses 1 and 2 (no charts, demo screens or drawn diagrams); a slide shows at most six rows or items of a longer table or list; nothing here has been used in a room.

Licence: content CC BY 4.0; the deck engine is from Bayan (MIT).

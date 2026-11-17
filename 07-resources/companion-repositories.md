# المستودعات المرافقة: ريادة وبيان · Companion repositories: Riyada and Bayan

Last reviewed: 17 November 2026 · Riyada at commit `d2a0607` (16 Nov 2026) · Bayan at commit `db941e2` (15 Nov 2026)

<div dir="rtl">

## ثلاثة مستودعات، لكل منها عمل واحد

| المستودع | ما هو | يجيب عن | الترخيص |
|---|---|---|---|
| **الأكاديمية** (هذا المستودع) | منهج ومعرفة بالسوق السعودي: مقررات، إطار المعرفة، دراسات حالة | ماذا أتعلم، وبأي ترتيب، وما القواعد في المملكة؟ | CC BY 4.0 للمحتوى، Apache-2.0 للكود |
| [**ريادة**](https://github.com/malenezi/riyada) | مهارات وملفات سياق وقوالب لمؤسس يبني ويشغّل منشأة بالوكلاء، بالعربية والإنجليزية، مع برامج تفحص المخرجات | كيف أنجز العمل الريادي نفسه مع وكيل، في أي بلد؟ | MIT |
| [**بيان**](https://github.com/malenezi/bayan) | مهارات عربية أولاً لواجهات الويب والعروض وتدقيق الاتجاه وكتابة نصوص الواجهات، مع مدققات آلية | كيف يخرج ما أبنيه بعربية صحيحة اتجاهاً ونصاً؟ | MIT |

الثلاثة مبادرات شخصية لصاحبها نفسه، وكل منها يعمل وحده. الأكاديمية لا تحتاج تثبيت شيء، و«ريادة» و«بيان» يُستخدمان دون الأكاديمية.

## قاعدة التكامل

1. **نربط ولا ننسخ.** لا ملف من «ريادة» أو «بيان» منسوخ هنا. كل إشارة رابط إلى المستودع الأصلي، فلا نسختان تتباعدان.
2. **لكل شيء موطن واحد.** ما يخص المملكة (أنظمة، جهات، قطاعات، مصادر) موطنه الأكاديمية. الأدوات الريادية العامة والمهارات القابلة للتثبيت موطنها «ريادة». صحة العربية في الواجهات موطنها «بيان».
3. **مخرجات المقررات تُقيَّم بقوالب الأكاديمية.** قوالب «ريادة» بدائل وتكملات، وجدول «أيهما أستخدم» أدناه يحسم كل تداخل.
4. **«ريادة» لا تعرف سوقك.** تقول ذلك عن نفسها. كل ما هو نظامي أو محلي تأخذه من [إطار المعرفة بالسوق السعودي](../02-saudi-market-knowledge-framework/README.md).
5. **الأكاديمية محايدة تجاه الأدوات.** مهارات «ريادة» و«بيان» بصيغة Agent Skills المفتوحة، وقوالبها ملفات Markdown تعمل مع أي نموذج ودون أي وكيل.

## ما الذي يُعاد استخدامه من «ريادة»

| الأصل في «ريادة» | يُستخدم في | الوحدة | التمرين |
|---|---|---|---|
| مهارة [`opportunity-discovery`](https://github.com/malenezi/riyada/tree/main/skills/opportunity-discovery) و[بطاقة تقييم الفرص](https://github.com/malenezi/riyada/blob/main/templates/discovery/opportunity-scorecard.ar.md) و[بطاقة التجربة](https://github.com/malenezi/riyada/blob/main/templates/discovery/experiment-card.ar.md) | المقرر 1 | 1.3، 1.6، وما بعد الأطروحة | [R1](../05-agentic-ai-lab/exercises/r1-evidence-scorecard-and-experiment.md) |
| مهارة [`market-research`](https://github.com/malenezi/riyada/tree/main/skills/market-research) و[ورقة تقدير السوق](https://github.com/malenezi/riyada/blob/main/templates/market/market-sizing.ar.md) | المقرر 1 | 1.6 (السوق الممكن الوصول إليه) | R1 |
| مهارة [`founder-context`](https://github.com/malenezi/riyada/tree/main/skills/founder-context) و[حزمة السياق بطبقاتها السبع](https://github.com/malenezi/riyada/tree/main/context) و`context_lint.py` | المقرر 2 | 2.2 | [R2](../05-agentic-ai-lab/exercises/r2-context-pack.md) |
| مهارة [`agent-operations`](https://github.com/malenezi/riyada/tree/main/skills/agent-operations): بطاقة دور الوكيل، مصفوفة الاعتماد، إجراء التشغيل، سلّم التقييم | المقرر 2 والمقرر 4 | 2.1، 2.5، 2.6، 2.8، 4.1 | [R3](../05-agentic-ai-lab/exercises/r3-role-card-and-approval-matrix.md) |
| مهارة [`financial-modeling`](https://github.com/malenezi/riyada/tree/main/skills/financial-modeling) و`build_model.py` | المقرر 3 والمقرر 4 | 3.3، 4.5 | [R4](../05-agentic-ai-lab/exercises/r4-financial-model.md) |
| مهارة [`business-planning`](https://github.com/malenezi/riyada/tree/main/skills/business-planning): مخطط النموذج المختصر وخطة العمل | المقرر 3 | 3.2 | |
| مهارة [`go-to-market`](https://github.com/malenezi/riyada/tree/main/skills/go-to-market): ملف العميل المثالي، التموضع والرسائل، خطة الإطلاق | المقرر 3 | 3.5 | [B2](../05-agentic-ai-lab/exercises/b2-bilingual-landing-page.md) يبني على مخرجاتها |
| مهارة [`fundraising`](https://github.com/malenezi/riyada/tree/main/skills/fundraising): هيكل العرض، غرفة البيانات، متابعة المستثمرين، تحديث المستثمرين | المقرر 4 | 4.5، 4.6 | [B3](../05-agentic-ai-lab/exercises/b3-pitch-deck.md) يبني على هيكل العرض |
| مهارة [`venture-scaling`](https://github.com/malenezi/riyada/tree/main/skills/venture-scaling): الأهداف والإيقاع التشغيلي | المقرر 4 | 4.1، 4.2 | |
| [مسارات العمل الأربعة](https://github.com/malenezi/riyada/tree/main/workflows) | [مسارات التعلّم](../01-academy/learning-pathways.md) | كل مسار يقابل مقرراً | |
| [إطار كفايات رائد الأعمال](https://github.com/malenezi/riyada/blob/main/frameworks/competency-framework.ar.md) (التقييم الذاتي) | نقطة دخول قبل المقرر 1 | | |
| [ورقة الحصانة التنافسية](https://github.com/malenezi/riyada/blob/main/frameworks/defensibility.ar.md) | المقرر 1 والمقرر 4 | 1.6 (الميزة)، 4.5 | |
| [المثال التطبيقي «موجة»](https://github.com/malenezi/riyada/tree/main/examples/mawja) (منشأة خيالية) | مثال مرجعي لحزمة سياق ونموذج مالي مكتملين | 2.2، 3.3 | R2، R4 |

## ما الذي يُعاد استخدامه من «بيان»

| الأصل في «بيان» | يُستخدم في | الوحدة | التمرين |
|---|---|---|---|
| مهارة [`arabic-ux-writing`](https://github.com/malenezi/bayan/tree/main/skills/arabic-ux-writing): دليل الأسلوب، المسرد، الأخطاء الشائعة | المقرر 2 والمقرر 3 | 2.2 (رسائل الوكيل بالعربية)، 3.1 (نصوص الإعداد والمساعدة) | [B1](../05-agentic-ai-lab/exercises/b1-agent-messages-in-arabic.md) |
| مهارة [`arabic-rtl-web`](https://github.com/malenezi/bayan/tree/main/skills/arabic-rtl-web) والقالب ثنائي اللغة | المقرر 3 | 3.1، 3.5 (صفحة هبوط للتجربة المدفوعة) | [B2](../05-agentic-ai-lab/exercises/b2-bilingual-landing-page.md) |
| مهارة [`arabic-html-slides`](https://github.com/malenezi/bayan/tree/main/skills/arabic-html-slides) ومحرك العروض | المقرر 4، واختيارياً المقرر 1 | 4.6 (يوم العروض)، 1.7 (العرض المختصر) | [B3](../05-agentic-ai-lab/exercises/b3-pitch-deck.md) |
| مهارة [`rtl-audit`](https://github.com/malenezi/bayan/tree/main/skills/rtl-audit) و`bidi_lint.py` و`i18n_parity.py` | المسار العميق في المقررين 3 و4، ومساهمو الأكاديمية | 3.1، 4.2 | [B4](../05-agentic-ai-lab/exercises/b4-rtl-audit.md) |

«بيان» لا يتداخل مع شيء في الأكاديمية: لا محتوى هنا عن اتجاه النص ولا عن كتابة نصوص الواجهات، وكل ما يخصهما يُحال إليه.

## أيهما أستخدم؟ جدول التداخل

| الحاجة | في الأكاديمية | في «ريادة» | القاعدة |
|---|---|---|---|
| اختيار فرصة | [تقييم فرص الوكلاء](../04-entrepreneur-toolkit/02-ai-opportunity-assessment.md): تسعة معايير، فحص إيقاف، «هل هو وكيل أصلاً؟» | بطاقة تقييم الفرص: سبعة معايير على مقياس دليل، والمجهول درجته 1 | المقرر 1 يُقيَّم بقالب الأكاديمية. استخدم بطاقة «ريادة» **قبل** المقرر للمفاضلة بين أفكار من قطاعات مختلفة |
| مقابلات العملاء | [اكتشاف العملاء](../04-entrepreneur-toolkit/03-customer-discovery.md) و[حزمة الأدلة](../03-courses/01-opportunity/templates/interview-evidence-pack.md) | دليل مقابلة العملاء | قالب الأكاديمية للمقرر. مهارة «ريادة» تدير المقابلة التحضيرية وتجمع النتائج إن كنت تعمل مع وكيل |
| اختبار افتراض بعد الأطروحة | لا يوجد | بطاقة التجربة بقاعدة قرار | استخدم «ريادة» |
| حجم السوق | قاعدة «من الأسفل وبمصدر» في الوحدة 1.6 | ورقة تقدير السوق مع المقاطعة والحساسية | استخدم ورقة «ريادة»، والمصادر من [سجل المصادر](../SOURCES.md) |
| المنافسون | [مقارنة المنافسين](../04-entrepreneur-toolkit/04-competitor-benchmark.md) مع اختبار «الغلاف الرقيق» | مصفوفة المنافسين | متكافئان. اختر واحداً ولا تملأ الاثنين |
| نموذج العمل | [نموذج العمل للمشاريع الوكيلية](../04-entrepreneur-toolkit/05-ai-business-model-canvas.md) | مخطط النموذج المختصر وخطة عمل كاملة | قالب الأكاديمية للمقرر 3. خطة «ريادة» حين يطلبها بنك أو برنامج دعم |
| الاقتصاديات | [تكلفة المهمة المنجزة](../04-entrepreneur-toolkit/06-unit-economics.md) وحاسبتها: مستوى **المهمة** | نموذج مالي لـ36 شهراً: مستوى **المنشأة** | متكاملان. هامش المهمة من الحاسبة يدخل افتراضاً في النموذج (تمرين R4) |
| تصميم الوكيل وحدوده | [مخطط المنتج الأولي](../04-entrepreneur-toolkit/07-ai-mvp-blueprint.md) و[مصفوفة الإشراف البشري](../02-saudi-market-knowledge-framework/compliance-toolkit/human-oversight-matrix.md) | بطاقة الدور، مصفوفة الاعتماد، إجراء التشغيل | مصفوفة الأكاديمية ضمن حقيبة الامتثال وتُسلَّم في المقرر. مصفوفة «ريادة» تضيف عمود «وسيلة الإنفاذ» لكل حد؛ استخدمها لتشغيل الوكيل فعلياً |
| التقييم | [قالب التقييم](../05-agentic-ai-lab/evaluation/eval-template.md) بحالات عربية ولهجة سعودية | سلّم التقييم | قالب الأكاديمية لمجموعة الاختبار. سلّم «ريادة» لتعريف الأخطاء الحرجة وعتبة النجاح |
| سياق المنشأة | [قالب سياق المؤسس](../04-entrepreneur-toolkit/10-founder-context-template.md): ملف واحد | حزمة من سبع طبقات مع مدقق | ابدأ بملف الأكاديمية في المقرر 1. انتقل إلى الحزمة حين يبدأ وكيل بالعمل (المقرر 2) |
| العرض الاستثماري | [هيكل العرض](../04-entrepreneur-toolkit/08-pitch-deck-outline.md) من اثنتي عشرة شريحة | هيكل العرض، غرفة البيانات، تحديث المستثمرين | هيكل الأكاديمية للمقرر 4. ما عداه من «ريادة». البناء بـ«بيان» |
| المهارات | [عشر مهارات](../05-agentic-ai-lab/skills/README.md) تُلصق في أي مساعد | تسع مهارات تُثبَّت مع قوالبها وبرامجها | مهارات الأكاديمية لمن يريد البدء في دقيقة. مهارات «ريادة» لمن يعمل بوكيل يقرأ مجلدات `SKILL.md` |
| إطار الكفايات | [إطار كفايات الأكاديمية](../01-academy/competency-framework.md): مرجع المنهج | إطار كفايات رائد الأعمال: تقييم ذاتي | إطار الأكاديمية يحكم المقررات. تقييم «ريادة» الذاتي لتحديد نقطة البداية |
| التجربة وخطاب النوايا، الأنظمة السعودية، القطاعات | الأكاديمية | لا يوجد | الأكاديمية |

## التثبيت

لا شيء من هذا شرط لإكمال المقررات. القوالب تُنسخ وتُملأ باليد.

</div>

```bash
# Claude Code: all skills of each toolkit
/plugin marketplace add malenezi/riyada
/plugin install riyada@riyada
/plugin marketplace add malenezi/bayan
/plugin install bayan@bayan

# Or clone and use the templates and scripts with any model, or with none
git clone https://github.com/malenezi/riyada
git clone https://github.com/malenezi/bayan
```

<div dir="rtl">

البرامج تحتاج Python 3.9 فأحدث. ملف Excel في النموذج المالي يحتاج `openpyxl`؛ بدونه يُكتب الملخص وملف CSV. راجع تعليمات كل مستودع، فهي المرجع.

## ما تحققنا منه في هذه المراجعة

| الفحص | النتيجة |
|---|---|
| `make check` في «ريادة» | نجح: المزامنة، التحقق، وحزمتا سياق «موجة» بلا ملاحظات |
| `make check` في «بيان» | نجح: الاختبارات، مطابقة المواصفة، وفحص القوالب والأمثلة |
| `build_model.py` على مثال «موجة» بالعربية | كتب الملخص وملف CSV وملف Excel |
| `context_lint.py` على القوالب الفارغة | 149 خطأً ورمز خروج غير صفري، وهو المتوقع قبل التعبئة |
| `bidi_lint.py` على محتوى المقرر 1 في الأكاديمية | 23 ملفاً بلا ملاحظات |

**ما لم نتحقق منه:** لم نجرّب تثبيت الإضافات في Claude Code ولا رفع المهارات إلى تطبيقات Claude. ولم يُجرَّب أي من التمارين مع متعلمين. و«ريادة» تذكر أن مهاراتها لم تُقيَّم بعد مع مؤسسين حقيقيين وأن عربيتها لم يراجعها محرر مستقل.

## الصيانة

- هذه الصفحة تُراجع عند كل إصدار من «ريادة» أو «بيان»، ويُحدَّث رقم الإيداع أعلاها.
- الروابط تشير إلى الفرع الرئيس. إن أُعيدت تسمية ملف هناك فافتح [طلب تحديث مصدر](../.github/ISSUE_TEMPLATE/resource-update.md).
- ملاحظة على قالب في «ريادة» أو قاعدة في «بيان» تُفتح في مستودعها. ملاحظة على الربط بينها وبين المنهج تُفتح هنا.
- مستودع مرافق جديد يُضاف بالطريقة نفسها: هوية مستقلة، جدول أصول، جدول تداخل، وتمرين واحد على الأقل.

</div>

---

## English summary

The Academy, [Riyada](https://github.com/malenezi/riyada) and [Bayan](https://github.com/malenezi/bayan) are three independent repositories by the same author. Each works alone.

| Repository | Job | Licence |
|---|---|---|
| Academy | Curriculum and Saudi market knowledge: what to learn, in what order, under which rules | CC BY 4.0 content, Apache-2.0 code |
| Riyada | Installable founder skills, a seven-layer context pack, templates and checking scripts; country-neutral | MIT |
| Bayan | Arabic-first skills and linters for bilingual web pages, HTML decks, RTL audits and UX writing | MIT |

**Integration rule.** Link, never copy. Saudi-specific material lives in the Academy; general founder tooling in Riyada; Arabic interface correctness in Bayan. Course deliverables are graded with the Academy's templates; where Riyada has a similar template, the overlap table above says which to use and when. Bayan overlaps with nothing here.

**Where they plug in.** Riyada's four workflows map one-to-one onto the four courses (idea to validation, first agent in 30 days, launch to traction, plan to funding). Bayan supplies the Arabic craft for agent messages (Course 2), the pilot landing page (Course 3) and the pitch deck (Course 4). Eight [lab exercises](../05-agentic-ai-lab/exercises/README.md) put both to work, and the [learning pathways](../01-academy/learning-pathways.md) show the combined route for each kind of learner.

**Checked on 17 November 2026.** Both repositories' own `make check` pass; the scripts used in the exercises were run. Plugin installation, app uploads and the exercises themselves have not been tried with learners.

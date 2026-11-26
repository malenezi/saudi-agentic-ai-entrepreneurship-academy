# ما لم يُعتمد من مقترح المكتبة · What was not adopted from the library proposal

<div dir="rtl">

بُنيت المكتبة من مقترح قدّمه صاحب الأكاديمية في 26 نوفمبر 2026، فيه 131 اسماً في عشرة مجالات. طُبّقت عليه قاعدة الأكاديمية: التحقق ثم البناء. هذا سجل ما تغيّر وسببه.

## ما دُمج

| في المقترح | صار | السبب |
|---|---|---|
| قصص المستخدم، ومعايير القبول، و«قصص المستخدم ومعايير القبول» (ثلاثة بنود في مجالين) | بطاقة واحدة | بند واحد مكرر |
| إدارة الديون التقنية، وتحليل الديون التقنية | بطاقة واحدة | بند واحد مكرر |
| التكامل المستمر، والتسليم والنشر المستمران | بطاقة CI/CD | الأول جزء من الثاني |
| دورة الإدراك والتخطيط والتنفيذ، وحلقة الوكيل | بطاقة Agent Loop | وصفان لشيء واحد |
| مخطط تدفق البيانات الوكيلي | مثال داخل بطاقة مخطط تدفق البيانات | ليس نموذجاً معروفاً بهذا الاسم |
| Agent Cost Modeling و Agent Unit Economics Model | بطاقة اقتصاديات الوحدة، وفيها تكلفة المهمة المنجزة | موجودان في حقيبة المؤسس باسم آخر |
| مصفوفة الفرص و Agent Opportunity Canvas | [بطاقة تقييم فرص الوكلاء](cards/agent-opportunity-assessment.md) (قالب الحقيبة رقم 2) | القالب قائم بتسعة معايير |
| Agent Autonomy Matrix و Agent-Human Responsibility Matrix | [بطاقة الإشراف البشري](cards/human-in-the-loop.md)، وقالبها مصفوفة الإشراف البشري في عدّة الامتثال | القالب قائم بمستوياته الأربعة؛ انظر «ما لم يُعَد فتحه» |
| Agent Architecture Canvas | [بطاقة معمارية الوكيل](cards/agent-architecture.md)، وقالبها مخطط المنتج الأولي | بطاقة ثانية للقالب نفسه تكرار |
| Agent Evaluation Canvas | [بطاقة تقييم الوكيل](cards/agent-evaluation.md)، وقالبها قالب التقييم في المختبر | بطاقة ثانية للقالب نفسه تكرار |
| Multi-Agent Architecture، Agent Orchestration، Multi-Agent Systems Design | [بطاقة تنسيق عدة وكلاء](cards/multi-agent-orchestration.md) | ثلاثة أسماء لموضوع واحد |
| Unique Value Proposition | [بطاقة لوحة النموذج الرشيق](cards/lean-canvas.md) | خانة من خانات اللوحة |
| Revenue Model و Pricing Models | [بطاقة نماذج التسعير والإيراد](cards/pricing-and-revenue-models.md) | موضوع واحد، وجدوله قائم في الحقيبة |
| Build-Measure-Learn و Hypothesis-Driven Development | [بطاقة الشركة الناشئة الرشيقة](cards/lean-startup.md) | الحلقة وبطاقة الاختبار جزآن من المنهجية نفسها |
| Risk Matrix | [بطاقة سجل مخاطر الوكيل](cards/agent-risk-register.md) | مقياس الاحتمال والأثر قائم فيه |
| System Context Diagram | [بطاقة نموذج C4](cards/c4-model.md) | هو المستوى الأول من النموذج، ومثال البطاقة مخطط سياق |
| Component Diagram و Deployment Diagram | [بطاقة مخططَي المكوّنات والنشر](cards/component-and-deployment-diagrams.md) | يحتاجهما المؤسس معاً: مما يتكون النظام، وأين يعمل |
| Software Architecture | [بطاقة سجلات القرارات المعمارية](cards/architecture-decision-records.md) و[بطاقة نموذج C4](cards/c4-model.md) | موضوع لا إطار بعينه؛ يُدوَّن بقراراته ويُرسم بمستوياته |
| Data Modeling و Database Schema | [بطاقة مخطط الكيانات والعلاقات](cards/entity-relationship-diagram.md) | النمذجة ومخطط القاعدة يُكتبان بالمخطط نفسه |
| Data Pipeline Diagram | [بطاقة مخطط تدفق البيانات](cards/data-flow-diagram.md) | خط المعالجة تدفق بيانات بين عمليات ومخازن |
| Agent ROI Calculator | [بطاقة العائد عند العميل](cards/buyer-return.md) | الحاسبة قائمة باسم آخر |
| Agent Risk Register | [بطاقة سجل مخاطر الوكيل](cards/agent-risk-register.md)، وقالبها في عدّة الامتثال | القالب قائم |

## ما حُذف

| في المقترح | السبب |
|---|---|
| Opportunity Discovery Framework | عنوان عام لا مرجع محدداً له. طريقة الأكاديمية في اكتشاف الفرص هي المقرر الأول نفسه |
| Scaling Framework | عنوان عام لا مرجع محدداً له. بوابات المقرر الرابع تؤدي الغرض |
| عناوين الصور في قسم «النماذج البصرية» | منقولة من مواقع أخرى. مخططات المكتبة تُرسم في الأكاديمية بأداة `tools/build_diagrams.py`، وليس Mermaid: قارئ الموقع لا يحمّل شيفرة من خارج المستودع، فلا يعرض مخططات Mermaid |
| إنشاء مستودع مستقل للمكتبة | المكتبة داخل مستودع الأكاديمية لتخضع للفحوص وسجل المصادر نفسيهما |

## ما صُحّح

| في المقترح | التصحيح |
|---|---|
| Effectuation: «التفكير الاحتمالي» | المصطلح نقيض التنبؤ؛ تُسمّى البطاقة عند كتابتها بعد فتح مصدرها |
| Swimlane: «المسارات الوظيفية» | مخطط المسارات |
| Data Pipeline Diagram: «مخطط تدفق العمليات» | مخطط خط معالجة البيانات |
| «الوكيلي» في أوصاف النماذج | «القائم على الوكلاء»، وفق الصياغة المعتمدة في الأكاديمية |
| OpenStax Entrepreneurship مرجعاً تأسيسياً | صفحات الكتاب تذكر اليوم رخصة CC BY-NC-SA 4.0 ([A196](../SOURCES.md))، وهي لا تسمح بدمج نصه في محتوى برخصة CC BY 4.0. يُستشهد به ويُحال إليه فقط |
| «Modern Data Architecture» | وصف عام لا يدل على إطار بعينه له مصدر؛ ما يلزم المؤسس منه في بطاقات تدفق البيانات والنمذجة البُعدية وحوكمة البيانات |
| «Competitive Advantage Framework» و«Revenue Model» و«Pricing Models» و«Human Evaluation Framework» | تبقى بطاقات موضوعات بمصادر مسمّاة، ولا تُقدَّم على أنها أطر معروفة بهذه الأسماء |

## ما لم يُعَد فتحه

استُبعد في الوحدة 1.4 مقياس للاستقلالية من 0 إلى 4، و«بطاقة فرصة» من عشرة حقول ([سجل المقرر الأول](../03-courses/01-opportunity/not-adopted.md)). المقترح يعيدهما باسمين جديدين. القرار باقٍ: للاستقلالية [سلّم الوحدة 1.1](../03-courses/01-opportunity/lessons/1-1-from-chatbots-to-agents.md) من 0 إلى 5، ولكل فعل مستوى إشراف من A إلى D في [مصفوفة الإشراف البشري](../02-saudi-market-knowledge-framework/compliance-toolkit/human-oversight-matrix.md)، ولتقييم الفرص المعايير التسعة في قالب الحقيبة. البطاقات تحيل إلى هذه الثلاثة ولا تضيف مقياساً رابعاً.

## ما ينتظر مصدراً

ثلاثة أسماء باقية في قائمة الانتظار لأن الصفحة التي فُتحت لكل منهما لم تقل ما يلزم للبطاقة: **Impact-Effort Matrix** (مقالة Nielsen Norman Group عن مصفوفات الأولويات لا تعرّفها ولا تسمّي أرباعها)، و**AARRR Funnel** (تدوينة 2007 المفتوحة لا تسرد مراحله الخمس). و**Data Lifecycle** (الصفحة المفتوحة تقول إن دورة حياة البيانات في الضوابط الوطنية خمس مراحل، وتسمّيها في صورة لا في نص؛ [A242](../SOURCES.md)). لا تُكتب بطاقة أي منها حتى يُفتح مصدر يقول ذلك صراحةً.

## نماذج الأكاديمية: ما كان قائماً وما هو جديد

اقترح المقترح اثني عشر نموذجاً خاصاً بالوكلاء. تسعة منها كانت قائمة في الأكاديمية بأسماء أخرى، فصارت بطاقاتٍ تحيل إلى القائم أو دُمجت في بطاقة قائمة (الجدول أعلاه). ثلاثة لم يكن لها قالب، فكُتب لكل منها قالب بالعربية والإنجليزية في [`templates/`](templates/agent-capability-matrix.md): مصفوفة قدرات الوكيل، ومصفوفة وصول الوكيل إلى الأدوات، وتقييم جاهزية المنشأة للوكيل. وأضيفت بطاقة لوضع الظل، وهو من صياغة الأكاديمية ولم يرد في المقترح. لا يُقدَّم أي منها معياراً عالمياً، ولم يُجرَّب أي منها مع متدربين أو منشأة.

## ما أُضيف

نحو عشرين اسماً لم ترد في المقترح، أضيفت إلى قائمة «ما يُكتب تباعاً» لأنها تسد فجوات ظاهرة: AARRR، North Star Metric، RICE، Kano، The Mom Test، Assumption Mapping، Pre-mortem، Value Stream Mapping، Five Whys، Service Blueprint، BPMN، C4، Cohort Analysis، Ansoff، Crossing the Chasm، OWASP Top 10 for LLM Applications، ISO/IEC 42001، تقييم أثر حماية البيانات، Golden Dataset، Guardrails، وAgent2Agent Protocol. لا تُكتب بطاقة أي منها قبل فتح مصدرها.

</div>

## In English

The library was built from a proposal the Academy's owner supplied on 26 November 2026 (131 names in ten domains), under the Academy's rule: verify, then build. This page records what was merged (duplicates across domains), dropped (two generic labels with no identifiable source, scraped image captions, a separate repository), corrected (three Arabic terms, the wording for "agentic", and the licence of OpenStax Entrepreneurship, whose pages now state CC BY-NC-SA 4.0), left closed (the 0 to 4 autonomy scale and the ten-field opportunity card rejected in Module 1.4), and added (about twenty names, none written before its source is opened).

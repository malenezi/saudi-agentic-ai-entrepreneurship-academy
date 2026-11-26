# المرحلة 2: ابنِ · Stage 2: Build

<div dir="rtl">

[رحلة المشروع](README.md) · الأسابيع 5 إلى 8 · تنتهي بـ[البوابة 2](gates.md#البوابة-2-وكيل-في-وضع-الظل)

**ما تخرج به:** وكيل يؤدي العمل الفعلي في المنشأة المستضيفة إلى جانب موظفيها، دون أن يتصرف.

> لم تخضع هذه المرحلة للاختبار حتى الآن. ولم يُوصَل أي قالب في المستودع بقناة حقيقية أو نظام حقيقي بعد.

| الأسبوع | العنوان | ما تفعله | المُخرج | يُقيَّم بـ | المادة |
|---|---|---|---|---|---|
| 5 | صمّم المهمة | تحدد ما يجوز للوكيل وما لا يجوز في مسار عمل المنشأة | ورقة التصميم، وجدول الإشراف البشري | لكل إجراء ذي أثر صاحب موافقة مسمّى | [2.1](../03-courses/02-build/lessons/2-1-agent-anatomy.md)، [2.6](../03-courses/02-build/lessons/2-6-guardrails-and-human-approval.md)، [مصفوفة الإشراف البشري](../02-saudi-market-knowledge-framework/compliance-toolkit/human-oversight-matrix.md) |
| 6 | السياق والأدوات | تبني السياق والمسرد وعقود الأدوات، وتشغّل الوكيل أول مرة | وكيل يعمل على بيانات نموذجية | يُتم عشرين رسالة واقعية من أولها إلى آخرها | [2.2](../03-courses/02-build/lessons/2-2-context-engineering-in-arabic.md)، [2.3](../03-courses/02-build/lessons/2-3-tools-and-integrations.md)، [2.4](../03-courses/02-build/lessons/2-4-choosing-a-model.md)، [عقد الأداة](../03-courses/02-build/templates/tool-contract.md) |
| 7 | أثبت أنه يعمل | تبني مجموعة تقييم من رسائل المنشأة بعد حجب بياناتها، وتهاجم وكيلك | خط الأساس للتقييم، وسجل الإخفاقات | حدّ النجاح يوضع قبل التشغيل، والنتيجة تُذكر كما هي | [2.5](../03-courses/02-build/lessons/2-5-evaluation.md)، [2.8](../03-courses/02-build/lessons/2-8-failure-analysis-and-iteration.md)، [R6](../05-agentic-ai-lab/exercises/r6-agent-evaluation.md)، [R7](../05-agentic-ai-lab/exercises/r7-agent-red-teaming.md) |
| 8 | البوابة 2: وضع الظل | خمسة أيام عمل في وضع الظل، ثم مقارنة بردود الموظفين | تقرير فترة الظل، وسجل التدقيق | شروط البوابة 2 | [وضع الظل](../05-agentic-ai-lab/agent-templates/workflows/shadow-mode/README.md)، [تقرير فترة الظل](../03-courses/03-launch/templates/shadow-period-report.md) |

## مساران للبناء

| | التطوير منخفض البرمجة (Low-Code) | البرمجة |
|---|---|---|
| نقطة البداية | [القالب 1 في n8n](../05-agentic-ai-lab/agent-templates/workflows/README.md)، ثم نسختك منه | [الوكيل المرجعي للطلبات](../03-courses/02-build/labs/README.md) |
| التقييم | [المختبر منخفض البرمجة](../03-courses/02-build/labs/lab-n8n-low-code.md) و[R6](../05-agentic-ai-lab/exercises/r6-agent-evaluation.md) | المختبران [2.5](../03-courses/02-build/labs/lab-2-5-evaluation-baseline.md) و[2.8](../03-courses/02-build/labs/lab-2-8-improvement-cycles.md) |
| الظل والتدقيق | سير عمل وضع الظل وتقرير المقارنة | المشغّل عبر HTTP بسجل تدقيق (`tools/reality_run.py`) |
| القناة والمنصة | [وصفة الربط للمتجر الإلكتروني](../05-agentic-ai-lab/agent-templates/workflows/recipes/online-store.md): الرسالة الواردة والاستعلام عن الطلب، من وثائق المزوّدين، ولم تُشغَّل بعد | الوصفة نفسها، تُستدعى من الشيفرة |

## بيانات المنشأة

- لا تخرج رسالة عميل من المنشأة قبل حجب ما يعرّف بصاحبها.
- إن كانت البيانات لا يجوز أن تغادر المنشأة أو المملكة، فشغّل نموذجاً محلياً، واقرأ [نتائج تشغيله](../05-agentic-ai-lab/agent-templates/workflows/real-model-runs/README.md) لتعرف ما تتنازل عنه من جودة.
- اتفاق مكتوب مع المنشأة قبل أي معالجة. ما ينص عليه نظام حماية البيانات الشخصية في حالتك **يحتاج إلى تحقق من مختص**؛ والبداية من [قائمة الامتثال للمؤسس](../02-saudi-market-knowledge-framework/founder-compliance-checklist.md).

الدرس [2.7](../03-courses/02-build/lessons/2-7-from-one-agent-to-several.md) عن تعدد الوكلاء اختياري: أول عميل يدفع لا يحتاج إلى أكثر من وكيل واحد.

</div>

---

## English summary

Weeks 5 to 8, ending at Gate 2. You leave with an agent doing the real work in the host business beside its staff, without acting. Not yet tested; no template in the repository has been connected to a real channel or system yet.

- **Week 5:** design sheet and human-oversight table for the host's workflow. Every consequential action has a named approver.
- **Week 6:** context, glossary and tool contracts; a first run that completes twenty realistic messages end to end.
- **Week 7:** an evaluation set from the host's masked messages; red-team the agent. The pass threshold is set before the run and the result reported as found.
- **Week 8, Gate 2:** five working days in shadow mode, then a comparison with the staff's answers.

**Two paths.** Low-code: n8n template 1, then your own variant. Coding: the Python reference order agent and the HTTP runner with its audit log.

**Host data.** Mask before anything leaves the business; use a local model where data may not leave; sign a written agreement before any processing. What the Personal Data Protection Law requires in your case needs a specialist's confirmation. Lesson 2.7 on multi-agent systems is optional.

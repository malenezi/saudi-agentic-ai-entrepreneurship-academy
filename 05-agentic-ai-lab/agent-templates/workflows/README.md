# القوالب القابلة للتشغيل · Runnable agent templates (n8n)

**Status:** Published in v0.9 (20 November 2026) · Imported and run in n8n 2.35.7 with the simulated model · Instructions run once with a real language model outside n8n on 21 November 2026 ([results](real-model-runs/README.md)) · **Not connected to any real channel or system, not tried with founders** · Invented sample data · Educational

<div dir="rtl">

خمسة ملفات تستوردها في [n8n](https://docs.n8n.io) فتعمل فوراً: نسخة قابلة للتشغيل من كل [قالب وكيل](../README.md). تعمل **دون مفتاح ودون تكلفة ودون اتصال بنموذج**، لأن «النموذج» الافتراضي فيها محاكٍ بكلمات مفتاحية، وليس نموذجاً لغوياً. ما تجرّبه هنا هو ما يحيط بالنموذج: الحدود، والموافقات، والتحويل إلى إنسان.

> **ما هذه الملفات وما ليست.** هي **قلب الوكيل**: استقبال رسالة، فهمها، ثم قرار يُفرض بالشيفرة. ليست منتجاً جاهزاً: لا قناة واتساب، ولا تقويم، ولا نظام عملاء، ولا دفتر أستاذ موصول. البيانات كلها مختلقة. ونقاط الاستقبال (Webhook) **بلا توثيق**: لا تعرضها على الإنترنت قبل أن تضيف التوثيق من إعدادات n8n.

## الملفات

| القالب | الملف | ما يفرضه «Decide» بالشيفرة |
|---|---|---|
| [1. خدمة العملاء](../01-whatsapp-customer-service.md) | [`01-whatsapp-customer-service.n8n.json`](01-whatsapp-customer-service.n8n.json) | الجواب من المحتوى المعتمد وحده؛ طلب واحد برقمه ولصاحبه فقط؛ الاسترجاع والإلغاء والخصم والوعود إلى موظف؛ لا مشورة طبية أو قانونية أو شرعية |
| [2. مساعد الحجوزات](../02-booking-assistant.md) | [`02-booking-assistant.n8n.json`](02-booking-assistant.n8n.json) | لا يُعرض إلا موعد منشور ومتاح؛ لا حجز بلا اختيار صريح؛ تغيير الموعد يحجز الجديد ثم يحرر القديم؛ الإلغاء المتأخر ينتظر موافقة؛ لا حديث عن أعراض أو علاج |
| [3. تأهيل العملاء المحتملين](../03-lead-qualification.md) | [`03-lead-qualification.n8n.json`](03-lead-qualification.n8n.json) | سؤال واحد في كل رسالة؛ الدرجة بقواعد مكتوبة مع سببها؛ النطاق السعري المعتمد فقط؛ عرض السعر ينتظر موافقة؛ لا تفاوض؛ «توقف» يوقف المتابعة فوراً |
| [4. مطابقة الفواتير](../04-invoice-reconciliation.md) | [`04-invoice-reconciliation.n8n.json`](04-invoice-reconciliation.n8n.json) | الحساب والتكرار ومطابقة المورّد والحركة البنكية بقواعد؛ القيد مسودة حتى يعتمده محاسب باسمه؛ لا أداة للدفع ولا للرفع إلى الجهة الضريبية |
| [5. تلخيص المنافسات](../05-tender-summariser.md) | [`05-tender-summariser.n8n.json`](05-tender-summariser.n8n.json) | لا تُقبل معلومة إلا إن وُجد نصها في الصفحة المذكورة، وما عداها «غير مذكور»؛ لا «مستوفٍ» بلا دليل في ملف المنشأة؛ قرار التقديم للإدارة |

ولمقرر 2 مختبر بالبنية نفسها: [الوكيل نفسه في n8n](../../../03-courses/02-build/labs/lab-n8n-low-code.md).

## بنية واحدة للجميع

</div>

```
Webhook -> Config -> Prepare -> Real model? -> Model (HTTP)      -> Decide -> Respond
                                            -> Simulated model  ->
```

<div dir="rtl">

| العقدة | عملها |
|---|---|
| **Config** | كل ما تغيّره أنت: اسم المنشأة، المحتوى المعتمد، البيانات التجريبية، `model_mode`، ومفتاح الإيقاف `stopped` |
| **Prepare** | تجهّز طلب النموذج. رسالة العميل تُغلَّف بوسم وتُعامل بيانات، لا تعليمات |
| **Simulated model** | محاكٍ بكلمات مفتاحية. ليس نموذجاً لغوياً، ويفهم أقل بكثير من نموذج حقيقي |
| **Model (HTTP)** | أي خادم يتبع صيغة `chat/completions` المتوافقة مع OpenAI، محلياً كان أو مستضافاً |
| **Decide** | **النموذج يقترح، وهذه العقدة تقرر.** جدول الإشراف في القالب مكتوب هنا شيفرةً. مخرج النموذج غير موثوق: ما لا يُقرأ منه لا ينفّذ شيئاً |

كل رد يحمل الحقول نفسها: `action` (ما تقرر)، `level` (صف جدول الإشراف الذي طُبّق)، `reply_draft` (مسودة الرد)، `handover` (ملخص التحويل)، `pending_approval` (ما ينتظر إنساناً)، `tool_calls` (ما كان سيُكتب في نظامك)، و`state` (حالة المحادثة، تعيدها مع الرسالة التالية).

## التشغيل

</div>

```bash
# 1. Install and import (n8n 2.35 needs Node.js 22.22 or newer; check n8n's own requirements). Or use the editor: Workflows -> Import from File.
npm install n8n
npx n8n import:workflow --input=05-agentic-ai-lab/agent-templates/workflows/01-whatsapp-customer-service.n8n.json
npx n8n list:workflow                      # shows the workflow id
npx n8n publish:workflow --id=<the id>     # makes the production webhook live
npx n8n start

# 2. Send a message (another terminal)
curl -s -X POST http://localhost:5678/webhook/saaea-customer-service \
  -H 'Content-Type: application/json' \
  -d '{"message": "متى تفتحون؟", "account": "0500000001", "state": {}}'
```

<div dir="rtl">

| القالب | مسار الاستقبال | جرّب |
|---|---|---|
| 1 | `saaea-customer-service` | `وين طلبي A-1001` ثم `ابي اعرف حالة الطلب A-1002` (طلب عميل آخر) ثم `ابغى استرجاع فلوسي` |
| 2 | `saaea-booking-assistant` | `ابي احجز تنظيف` ثم أعد `state` مع الرسالة `2`؛ ثم `الغي حجزي B-1001` (إلغاء متأخر) |
| 3 | `saaea-lead-qualification` | `السلام عليكم` ثم أجب عن الأسئلة وأعد `state` في كل مرة؛ ثم `ابي خصم` و`لا تراسلوني` |
| 4 | `saaea-invoice-reconciliation` | نص فاتورة من [`cases.json`](src/04-invoice-reconciliation/cases.json)؛ ثم الاعتماد على `saaea-invoice-reconciliation-approve` |
| 5 | `saaea-tender-summariser` | نص الكراسة المختلقة في [`cases.json`](src/05-tender-summariser/cases.json) |

**إيقاف الوكيل:** ضع `"stopped": true` في Config، فتُحال كل رسالة إلى إنسان ولا تُستدعى أداة. أو أوقف نشر سير العمل من n8n.

## نموذج حقيقي (اختياري)

في Config: اجعل `model_mode` يساوي `http`، واضبط `model_base_url` و`model_name`. الخادم المحلي لا يحتاج مفتاحاً. للمزوّد المستضاف أضف في عقدة **Model (HTTP)** اعتماداً من نوع Header Auth من داخل n8n؛ **لا تكتب المفتاح في Config ولا في أي ملف**، وضع حدّ إنفاق عند المزوّد قبل أول تشغيل. التعليمات المرسلة إلى النموذج في الحقل `instructions`، ومصدرها `src/<القالب>/instructions.md`.

لا نوصي بنموذج ولا بمزوّد. **لا ترسل بيانات عملاء حقيقية** قبل إكمال [التقييم الذاتي لحماية البيانات](../../../02-saudi-market-knowledge-framework/compliance-toolkit/pdpl-self-assessment.md) ومعرفة أين يعالج المزوّد بياناتك.

## من القالب إلى منتجك

1. أكمل [مخطط المنتج الأولي](../../../04-entrepreneur-toolkit/07-ai-mvp-blueprint.md) لعميلك أنت. القالب نقطة بداية.
2. ضع محتواك المعتمد وبياناتك في Config، ثم استبدل بها اتصالاً بنظامك حين تجهز.
3. استبدل بعقدة Webhook قناتك، واقرأ سياسة المنصة وشروط قوالب الرسائل قبل ذلك.
4. ابنِ [مجموعة تقييمك](../../evaluation/eval-template.md) من رسائل عملائك قبل أن يراه أحد. ملفات `cases.json` هنا مثال على الشكل، وليست بديلاً.
5. أبقِ كل حدٍّ في **Decide**. حدٌّ مكتوب في التعليمات وحدها ليس حداً.

## ما تحققنا منه، وما لم نتحقق منه

| الفحص | النتيجة |
|---|---|
| الاستيراد والنشر والتشغيل في n8n 2.35.7 (Node.js 22)، من سطر الأوامر، 20 نوفمبر 2026 | الملفات الستة (القوالب الخمسة ومختبر المقرر 2) استُوردت ونُشرت بلا خطأ |
| `tools/n8n_e2e.py` على نقاط الاستقبال الحية | 84 طلباً، ولا إخفاق: 47 حالة للقوالب، و35 حالة للمختبر طابقت الشيفرة المرجعية، وطلبا موافقة في المختبر |
| مسار النموذج الحقيقي في n8n على خادم وهمي محلي | جواب سليم نُفّذ؛ جواب غير مقروء حُوّل إلى إنسان؛ خادم لا يردّ حُوّل إلى إنسان |
| منطق العقد خارج n8n (`tests/test_n8n_workflows.py`، ضمن `make check`) | 50 حالة للقوالب، ومفتاح الإيقاف، ونموذج يهذي، ونموذج لا يردّ |

**ما لم نتحقق منه:** لم تُشغَّل مع نموذج لغوي حقيقي، فالتعليمات في `instructions.md` لم تُختبر. لم تُستورد من واجهة المحرر ولا على n8n Cloud ولا على إصدارات n8n 1.x. لم توصل بقناة أو تقويم أو نظام حقيقي. المحاكي لا يفهم إلا كلماته، وحالات الاختبار مختلقة وليست من رسائل عملاء. الحجوزات والمسودات تُحفظ في بيانات سير العمل للتجربة، وليست قاعدة بيانات. ولم يجرّبها مؤسس بعد.

## التعديل

الملفات `*.n8n.json` **مبنية**: لا تعدّلها باليد إن أردت المساهمة. عدّل المصدر في `src/` ثم ابنِ:

</div>

```bash
python3 tools/build_n8n_workflows.py     # rebuild the six workflows
make check                               # runs every case (needs Node.js for the logic tests)
```

<div dir="rtl">

| المسار | ما فيه |
|---|---|
| `src/common/` | ما تشترك فيه القوالب: `prepare.js`، `sim.js`، `text.js` (العربية والأرقام)، `read_model.js`، `result.js` |
| `src/<القالب>/spec.json` | الاسم، مسار الاستقبال، ومحتوى Config |
| `src/<القالب>/decide.js` | جدول الإشراف شيفرةً. وفي بعض القوالب `sim.js` و`approve.js` |
| `src/<القالب>/instructions.md` | تعليمات النموذج الحقيقي |
| `src/<القالب>/cases.json` | حالات الاختبار ونتيجتها المتوقعة |

</div>

---

## English

Five files you import into [n8n](https://docs.n8n.io) and run at once: a runnable version of each [agent template](../README.md). They need **no key, no cost and no model connection**, because the default "model" is a keyword simulator, not a language model. What you exercise is what surrounds the model: limits, approvals and handover.

**What they are not.** They are the core of an agent (receive a message, understand it, decide in code), not a product: no messaging channel, calendar, CRM or ledger is connected, and all data is invented. The webhooks have **no authentication**: do not expose them to the internet before you add it in n8n.

**One shape.** `Webhook -> Config -> Prepare -> Real model? -> Model (HTTP) or Simulated model -> Decide -> Respond`. The model proposes and **Decide** decides: the template's oversight table is written there as code, and model output that cannot be read does nothing. Set `model_mode` to `http` in Config to call any OpenAI-compatible endpoint; keep keys in an n8n credential, never in Config or a file.

**Checked on 20 November 2026.** All six workflows (the five templates and the Course 2 lab) imported, published and ran in n8n 2.35.7 from the command line; `tools/n8n_e2e.py` sent 84 requests to the live webhooks with no failure; the HTTP model path was exercised in n8n against a local stub (a valid answer, an unreadable answer, an unreachable endpoint). **Not checked:** a real language model, the editor's import menu, n8n Cloud, n8n 1.x, any real channel or system, and use by founders.

**Changing them.** The `*.n8n.json` files are built. Edit the sources under `src/`, run `python3 tools/build_n8n_workflows.py`, then `make check`.

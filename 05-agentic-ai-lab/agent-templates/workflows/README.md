# القوالب القابلة للتشغيل · Runnable agent templates (n8n)

**Status:** Published in v0.9 (20 November 2026) · Imported and run in n8n 2.35.7 with the simulated model · Webhooks ask for a header token since 23 November 2026 · Instructions run once with a real language model outside n8n on 21 November 2026 ([results](real-model-runs/README.md)) · **Not connected to any real channel or system, not tried with founders** · Invented sample data · Educational

<div dir="rtl">

خمسة ملفات تستوردها في [n8n](https://docs.n8n.io) فتعمل بعد خطوة واحدة، هي إنشاء رمز نقطة الاستقبال: نسخة قابلة للتشغيل من كل [قالب وكيل](../README.md). تعمل **دون مفتاح ودون تكلفة ودون اتصال بنموذج**، لأن «النموذج» الافتراضي فيها محاكٍ بكلمات مفتاحية، وليس نموذجاً لغوياً. ما تجرّبه هنا هو ما يحيط بالنموذج: الحدود، والموافقات، والتحويل إلى إنسان.

> **ما هذه الملفات وما ليست.** هي **قلب الوكيل**: استقبال رسالة، فهمها، ثم قرار يُفرض بالشيفرة. ليست منتجاً جاهزاً: لا قناة واتساب، ولا تقويم، ولا نظام عملاء، ولا دفتر أستاذ موصول. البيانات كلها مختلقة. ونقاط الاستقبال (Webhook) **تطلب رمزاً في ترويسة الطلب** ولا تجيب قبل أن تنشئ اعتماده (انظر «رمز نقطة الاستقبال»). الرمز يثبت أن المرسل يعرفه، ولا يثبت أن الرسالة جاءت من قناتك: عند الربط بقناة حقيقية تحقق من توقيع مزوّدها أيضاً.

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
Webhook -> Config -> Prepare -> Real model? -> Simulated model ---------------------------------------> Decide -> Respond
                                            -> Model (HTTP) -> Check model output -> Retry model? -> Decide
                                                                                                  -> Model retry (HTTP) -> Decide
```

<div dir="rtl">

| العقدة | عملها |
|---|---|
| **Config** | كل ما تغيّره أنت: اسم المنشأة، المحتوى المعتمد، البيانات التجريبية، `model_mode`، ومفتاح الإيقاف `stopped`، ومفتاح [وضع الظل](shadow-mode/README.md) `shadow_mode` |
| **Prepare** | تجهّز طلب النموذج. رسالة العميل تُغلَّف بوسم وتُعامل بيانات، لا تعليمات، ولا يغلق الوسمَ نصٌّ كتبه العميل. تُحذف علامات الاتجاه المخفية، ويُكتب رقم الجوال بصيغة واحدة (`9665…` و`+9665…` و`5…` تصير `05…`؛ يُعطَّل بـ`normalise_account: false`) |
| **Simulated model** | محاكٍ بكلمات مفتاحية. ليس نموذجاً لغوياً، ويفهم أقل بكثير من نموذج حقيقي |
| **Model (HTTP)** | أي خادم يتبع صيغة `chat/completions` المتوافقة مع OpenAI، محلياً كان أو مستضافاً |
| **Check model output** و**Model retry (HTTP)** | جواب النموذج إن لم يكن كائن JSON واحداً يُصلَح حيث لا يتغير المعنى (نص أو علامات تنسيق حول الكائن، علامات اقتباس مائلة، فاصلة زائدة، كلمة بلا علامتي اقتباس)، وإلا يُطلب من النموذج مرة واحدة أخرى بتعليمة ثابتة دون إعادة نص العميل. ما بقي غير مقروء لا ينفّذ شيئاً. يُعطَّل الطلب الثاني بـ`retry_unreadable: false`. وما حدث يُكتب في `log.model` حين يحدث فقط |
| **Decide** | **النموذج يقترح، وهذه العقدة تقرر.** جدول الإشراف في القالب مكتوب هنا شيفرةً. مخرج النموذج غير موثوق: ما لا يُقرأ منه لا ينفّذ شيئاً |

كل رد يحمل الحقول نفسها: `action` (ما تقرر)، `level` (صف جدول الإشراف الذي طُبّق)، `reply_draft` (مسودة الرد)، `handover` (ملخص التحويل)، `pending_approval` (ما ينتظر إنساناً)، `tool_calls` (ما كان سيُكتب في نظامك)، و`state` (حالة المحادثة، تعيدها مع الرسالة التالية).

## التشغيل

</div>

```bash
# 1. Install and import (n8n 2.35 needs Node.js 22.22 or newer; check n8n's own requirements). Or use the editor: Workflows -> Import from File.
npm install n8n
npx n8n import:workflow --input=05-agentic-ai-lab/agent-templates/workflows/01-whatsapp-customer-service.n8n.json
python3 tools/n8n_webhook_credential.py    # writes a new token to saaea-webhook-credential.json and prints it once
npx n8n import:credentials --input=saaea-webhook-credential.json && rm saaea-webhook-credential.json
npx n8n list:workflow                      # shows the workflow id
npx n8n publish:workflow --id=<the id>     # makes the production webhook live
npx n8n start

# 2. Send a message (another terminal)
curl -s -X POST http://localhost:5678/webhook/saaea-customer-service \
  -H 'Content-Type: application/json' -H 'X-SAAEA-Token: <the token>' \
  -d '{"message": "متى تفتحون؟", "account": "0500000001", "state": {}}'
```

<div dir="rtl">

### رمز نقطة الاستقبال

كل عقدة Webhook في الملفات الستة مضبوطة على **Header Auth** في n8n، وتشير إلى اعتماد اسمه `SAAEA webhook token`. الملف يحمل **اسم الاعتماد لا قيمته**: لا سرّ في المستودع. والاعتماد يُحفظ مشفّراً داخل n8n.

| الحالة | ما يجيب به n8n |
|---|---|
| لم تنشئ الاعتماد بعد | 500، ولا يُنفَّذ شيء |
| طلب بلا رمز، أو برمز خاطئ | 403، ولا يُنفَّذ شيء |
| طلب بالرمز الصحيح في الترويسة `X-SAAEA-Token` | يعمل سير العمل |

**إنشاؤه من المحرر:** افتح عقدة Webhook، ومن Credential for Header Auth اختر Create New، واكتب في Name القيمة `X-SAAEA-Token` وفي Value نصاً عشوائياً طويلاً. في القالب 4 والمختبر عقدة ثانية، Approval webhook، تستخدم الاعتماد نفسه.

**أو من سطر الأوامر:** الأمران في الأعلى. البرنامج يولّد رمزاً جديداً في كل مرة ويكتبه نصاً صريحاً في ملف: استورده ثم احذفه. الملف مستثنى من git.

غيّر الرمز إن ظهر في سجل أو لقطة شاشة أو محادثة. ولا تضعه في Config ولا في أي ملف من المستودع.

### جرّب

| القالب | مسار الاستقبال | جرّب |
|---|---|---|
| 1 | `saaea-customer-service` | `وين طلبي A-1001` ثم `ابي اعرف حالة الطلب A-1002` (طلب عميل آخر) ثم `ابغى استرجاع فلوسي` |
| 2 | `saaea-booking-assistant` | `ابي احجز تنظيف` ثم أعد `state` مع الرسالة `2`؛ ثم `الغي حجزي B-1001` (إلغاء متأخر) |
| 3 | `saaea-lead-qualification` | `السلام عليكم` ثم أجب عن الأسئلة وأعد `state` في كل مرة؛ ثم `ابي خصم` و`لا تراسلوني` |
| 4 | `saaea-invoice-reconciliation` | نص فاتورة من [`cases.json`](src/04-invoice-reconciliation/cases.json)؛ ثم الاعتماد على `saaea-invoice-reconciliation-approve` |
| 5 | `saaea-tender-summariser` | نص الكراسة المختلقة في [`cases.json`](src/05-tender-summariser/cases.json) |

**إيقاف الوكيل:** ضع `"stopped": true` في Config، فتُحال كل رسالة إلى إنسان ولا تُستدعى أداة. أو أوقف نشر سير العمل من n8n.

**وضع الظل:** ضع `"shadow_mode": true` في Config، فيقرر القالب كعادته ولا يخرج منه شيء: ما كان سيفعله يُحفظ في `shadow.would` لتقارنه بما فعله الموظفون. يعالج بيانات حقيقية، فاتفاق البيانات يسبقه. التفصيل والبرنامج والعيّنة في [`shadow-mode`](shadow-mode/README.md).

## نموذج حقيقي (اختياري)

في Config: اجعل `model_mode` يساوي `http`، واضبط `model_base_url` و`model_name`. الخادم المحلي لا يحتاج مفتاحاً. للمزوّد المستضاف أضف في عقدة **Model (HTTP)** اعتماداً من نوع Header Auth من داخل n8n؛ **لا تكتب المفتاح في Config ولا في أي ملف**، وضع حدّ إنفاق عند المزوّد قبل أول تشغيل. التعليمات المرسلة إلى النموذج في الحقل `instructions`، ومصدرها `src/<القالب>/instructions.md`.

لا نوصي بنموذج ولا بمزوّد. **لا ترسل بيانات عملاء حقيقية** قبل إكمال [التقييم الذاتي لحماية البيانات](../../../02-saudi-market-knowledge-framework/compliance-toolkit/pdpl-self-assessment.md) ومعرفة أين يعالج المزوّد بياناتك.

## من القالب إلى منتجك

1. أكمل [مخطط المنتج الأولي](../../../04-entrepreneur-toolkit/07-ai-mvp-blueprint.md) لعميلك أنت. القالب نقطة بداية.
2. ضع محتواك المعتمد وبياناتك في Config، ثم استبدل بها اتصالاً بنظامك حين تجهز.
3. استبدل بعقدة Webhook قناتك، واقرأ سياسة المنصة وشروط قوالب الرسائل قبل ذلك.
4. ابنِ [مجموعة تقييمك](../../evaluation/eval-template.md) من رسائل عملائك قبل أن يراه أحد. ملفات `cases.json` هنا مثال على الشكل، وليست بديلاً. وللتمرّن قبل ذلك: [متجر مختلق](../../datasets/ecommerce-store/README.md) بخمس وثمانين رسالة وسلوكها المتوقع، يشغّل القالب 1 كما هو.
5. أبقِ كل حدٍّ في **Decide**. حدٌّ مكتوب في التعليمات وحدها ليس حداً.

**قاعدتان أُضيفتا في 24 نوفمبر 2026 بعد ثلاثين رسالة كُتبت لتكسر القالب 1** ([حالات الفشل](../../datasets/ecommerce-store/README.md#حالات-الفشل-ثلاثون-رسالة-كتبت-لتكسر-القالب)):

- **رسالة فيها أكثر من طلب** (القالب 1): النموذج يسمّي النية الرئيسة ويضع غيرها في الحقل `also`. إن لم يكن فارغاً فلا يُجاب عن شيء، وتُحال الرسالة كاملة بالإجراء `handover_multiple_requests` وبأشد مستوى بين طلباتها. قبل ذلك كان الجزء السهل يُجاب ويضيع الباقي. القاعدة متحفظة عمداً: سؤالان مسموحان في رسالة واحدة يذهبان إلى موظف أيضاً.
- **طلب إيقاف المراسلة** (القالب 3): عبارات الإيقاف في `stop_phrases` تُطابَق في الشيفرة قبل الأخذ بجواب النموذج، فلا يتوقف تنفيذ الطلب على فهم النموذج له. القائمة تُكمَل بعبارات عملائك، وقد توقف المراسلة في رسالة لم تقصد ذلك؛ ومن كتب من جديد يُجاب.

**أُضيف في 25 نوفمبر 2026: طلب لم يسمّه النموذج يُبحث عنه في الكود** (القالب 1). النموذج المحلي الصغير لم يملأ `also` مرة واحدة، وسمّى الإلغاء والشكوى وطلب الوعد سؤالاً عن طلب. لذلك يفحص Decide نص العميل نفسه، أياً كان جواب النموذج، بفحصين:

- **كلمات الطلبات التي تحتاج موظفاً** (استرجاع، إلغاء، خصم، وعد، شكوى، مشورة، طلب موظف)، وهي الكلمات المكتوبة في Config تحت `sim.intents`. إن رأى النموذج سؤالاً فقط ووُجد طلب واحد منها، حلّت القراءة الأشد مكان قراءة النموذج: في سؤال عن طلب حين تكون الرسالة جملة واحدة أو لا تذكر طلباً مسجّلاً، وفي سؤال عام حين لا يكون موضوعه في المحتوى المعتمد. وما عدا ذلك طلب ثانٍ يدخل البوابة أعلاه. يُسجَّل ذلك في `log.intent_by_code` أو `log.also_by_code`.
- **أكثر من طلب مسجّل في رسالة واحدة:** تُحال كاملة، فالوكيل يقرأ طلباً واحداً في المرة.

استثناء مقصود: سؤال من جملة واحدة ربطه النموذج بموضوع معتمد يُجاب من ذلك الموضوع، لأن «ما سياسة الاسترجاع؟» تحمل الكلمة نفسها. والثمن أن «أبي استرجاع» إن سمّاها النموذج سؤالاً عن السياسة أُجيبت بنص السياسة. `second_request_check: false` في Config يوقف الفحصين.

**تشغيل جديد بالنموذج المحلي بعد الفحص، 25 نوفمبر 2026** ([السجل](real-model-runs/README.md)): 58 من 85 رسالة من المتجر المختلق، و«تصرّف وحده» في 4 مكان 11، وحالات الفشل 22 صحيحة و6 تصرّف فيها وحده مكان 17 و11. الفحص عمل على أجوبة جديدة، والنموذج لم يملأ `also` هذه المرة أيضاً. وظهر خطأ جديد: كتب النموذج مفتاح الموضوع مكان النية في 10 رسائل فأُحيلت. خارج n8n، وتشغيل واحد.

حدّه: الفحص لا يعرف إلا الكلمات التي كتبتها في Config. طلب ثانٍ بصياغة ليست فيها يمرّ كما كان، وهذا ما حدث في عشر من حالات الفشل الثلاثين (الأرقام في [سجل التشغيل](real-model-runs/README.md)). جُرّب خارج n8n فقط، بأجوبة النموذج المسجّلة وبأجوبة مكتوبة؛ لم يُستورد في n8n بعد هذا التعديل ولم يُشغَّل بنموذج من جديد.

## ما تحققنا منه، وما لم نتحقق منه

| الفحص | النتيجة |
|---|---|
| الاستيراد والنشر والتشغيل في n8n 2.35.7 (Node.js 22)، من سطر الأوامر، 20 نوفمبر 2026 | الملفات الستة (القوالب الخمسة ومختبر المقرر 2) استُوردت ونُشرت بلا خطأ |
| `tools/n8n_e2e.py` على نقاط الاستقبال الحية | 84 طلباً، ولا إخفاق: 47 حالة للقوالب، و35 حالة للمختبر طابقت الشيفرة المرجعية، وطلبا موافقة في المختبر. أُعيد في 23 نوفمبر 2026 بعد إضافة الرمز: 100 طلب، ولا إخفاق |
| رمز نقطة الاستقبال في n8n 2.35.7، 23 نوفمبر 2026 | النقاط الثماني رفضت طلباً بلا رمز وطلباً برمز خاطئ (403)؛ وقبل إنشاء الاعتماد أجابت 500 ولم تنفّذ شيئاً |
| مسار النموذج الحقيقي في n8n على خادم وهمي محلي | جواب سليم نُفّذ؛ جواب غير مقروء حُوّل إلى إنسان؛ خادم لا يردّ حُوّل إلى إنسان |
| منطق العقد خارج n8n (`tests/test_n8n_workflows.py`، ضمن `make check`) | 50 حالة للقوالب، ومفتاح الإيقاف، ونموذج يهذي، ونموذج لا يردّ |
| الإصلاح والطلب الثاني وما يكتبه العملاء فعلاً، خارج n8n، 24 نوفمبر 2026 | جواب بنص حوله أو بفاصلة زائدة أو بكلمة بلا اقتباس يُقرأ؛ جواب غير مقروء يُطلب مرة ثانية؛ جوابان غير مقروءين لا ينفّذان شيئاً في أي من الملفات الستة. القالب 1: رقم الجوال بخمس صيغ هو الحساب نفسه؛ رقم الطلب بأربع صيغ يُحَل إلى مفتاحه؛ رقم لم يكتبه العميل يُسقط؛ رسالة بأكثر من طلب تُحال كاملة. القالب 3: طلب إيقاف المراسلة يُنفَّذ أياً كان جواب النموذج. و14 حالة باللهجة للقوالب 2 إلى 5 (`src/<القالب>/dialect-cases.json`) |
| العقد والقواعد المضافة، داخل n8n 2.35.7، 24 نوفمبر 2026 | الملفات الستة استُوردت بالعقد الثلاث الجديدة، و`tools/n8n_e2e.py` أعطى 100 طلب بلا إخفاق. ثم القالبان 1 و3 بوضع `http` على خادم وهمي محلي: جواب بكلمة بلا اقتباس وفاصلة زائدة قُرئ بعد الإصلاح؛ جواب غير مقروء طُلب مرة ثانية فنُفّذ الجواب الثاني، والطلب الثاني حمل أربع رسائل ونص العميل مرة واحدة؛ جوابان غير مقروءين حُوّلا إلى إنسان؛ `also` أحال الرسالة كاملة؛ رقم الجوال بصيغة `9665…` عُرف صاحبه؛ طلب الإيقاف نُفّذ والنموذج لا يُقرأ |
| وضع الظل خارج n8n، 23 نوفمبر 2026 | في الحالات الخمسين لا يخرج رد ولا تحويل ولا موافقة ولا كتابة؛ حجز لا يُحفظ؛ مسودة قيد لا تُحفظ ولا تُعتمد |
| وضع الظل داخل n8n 2.35.7، 23 نوفمبر 2026، على القوالب 1 و2 و4 | رسائل العيّنة الاثنتا عشرة أعطت السجل المنشور نفسه؛ حجز طُلب مرتين لم يُحفظ؛ مسودة قيد لم تُحفظ ولم تُعتمد |

**تشغيل بنموذج محلي صغير، 24 نوفمبر 2026** ([السجل](real-model-runs/README.md)): 43 من 47 حالة للقوالب، و54 من 85 رسالة من المتجر المختلق. الإصلاح قرأ كل جواب معطوب، والطلب الثاني جُرّب بنموذج أول مرة، والنموذج لم يملأ `also` في أي رسالة فلم تعمل بوابة الطلبين معه.

**ما لم نتحقق منه:** لم يُعَد التشغيل بعد تصحيح قائمة المواضيع وإصلاح الأقواس المربعة. حالات الفشل الثلاثون والحالات باللهجة كتبها مساعد ذكاء اصطناعي ولم يراجعها متحدث أصلي. لم تُشغَّل مع نموذج لغوي حقيقي عبر عقدة HTTP في n8n (التشغيلان المسجّلان في [`real-model-runs`](real-model-runs/README.md) تمّا خارج n8n). وضع الظل لم يُجرَّب مع منشأة، ولم يُشغَّل داخل n8n على القالبين 3 و5. الرمز لم يُجرَّب من واجهة المحرر، ولا خلف وسيط عكسي أو نفق. لم تُستورد من واجهة المحرر ولا على n8n Cloud ولا على إصدارات n8n 1.x. لم توصل بقناة أو تقويم أو نظام حقيقي. المحاكي لا يفهم إلا كلماته، وحالات الاختبار مختلقة وليست من رسائل عملاء. الحجوزات والمسودات تُحفظ في بيانات سير العمل للتجربة، وليست قاعدة بيانات. ولم يجرّبها مؤسس بعد.

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
| `shadow-mode/` | دليل وضع الظل، وعيّنة مختلقة من سجل الظل وسجل الموظفين. البرنامج في `tools/shadow_report.py` |

</div>

---

## English

Five files you import into [n8n](https://docs.n8n.io) and run after one step, creating the webhook token: a runnable version of each [agent template](../README.md). They need **no model key, no cost and no model connection**, because the default "model" is a keyword simulator, not a language model. What you exercise is what surrounds the model: limits, approvals and handover.

**What they are not.** They are the core of an agent (receive a message, understand it, decide in code), not a product: no messaging channel, calendar, CRM or ledger is connected, and all data is invented. The webhooks ask for a **header token** (n8n's Header Auth) and answer nothing until you create its credential: in the editor (Webhook node, Credential for Header Auth, Name `X-SAAEA-Token`, Value a long random string), or with `python3 tools/n8n_webhook_credential.py` and `npx n8n import:credentials`. The built files name the credential and hold no secret. A token shows that the sender knows it, not that a message came from your channel: when you connect a real channel, verify the provider's signature as well.

**One shape.** `Webhook -> Config -> Prepare -> Real model? -> Model (HTTP) or Simulated model -> Decide -> Respond`. The model proposes and **Decide** decides: the template's oversight table is written there as code, and model output that cannot be read does nothing. Set `model_mode` to `http` in Config to call any OpenAI-compatible endpoint; keep keys in an n8n credential, never in Config or a file.

**Checked on 20 November 2026.** All six workflows (the five templates and the Course 2 lab) imported, published and ran in n8n 2.35.7 from the command line; `tools/n8n_e2e.py` sent 84 requests to the live webhooks with no failure (run again on 23 November 2026 with the token: 100 requests, no failure; all eight webhooks answered 403 to a request with no token or a wrong one, and 500 before the credential existed); the HTTP model path was exercised in n8n against a local stub (a valid answer, an unreadable answer, an unreachable endpoint). **Not checked:** a real language model, the editor's import menu, n8n Cloud, n8n 1.x, any real channel or system, and use by founders.

**Added on 24 November 2026.** Between the HTTP model node and Decide there are now two more nodes: an answer that is not one JSON object is repaired where that changes no meaning (text or a code fence around the object, curly quotes, a trailing comma, a bare word where a string was meant) and otherwise asked for once more with a fixed instruction; what is still unreadable never acts, and `log.model` records what happened only when something did. Prepare strips hidden direction marks, keeps a customer from closing the wrapper tag, and writes a Saudi mobile number in one form. In template 1 an order reference is resolved to its stored key however it is typed, a reference whose digits are not in the customer's message is dropped, and a message with more than one request (the model's `also` field) is handed over whole as `handover_multiple_requests`. In template 3 a request to stop being contacted is matched in code (`stop_phrases`) whatever the model returns. Tested outside n8n with canned model answers and with messages written by an AI assistant, and on the same day inside n8n 2.35.7: all six workflows imported with the new nodes, `tools/n8n_e2e.py` gave 100 requests with no failure, and templates 1 and 3 in `http` mode against a local stub showed the repair, the single retry (four messages, the customer's text once), the handover after two unreadable answers, the `also` gate, the mobile-number spelling and the stop rule; a small local model was then run on all of it the same day (43 of 47 template cases, 54 of the invented store's 85 messages; it never filled `also`, so the multiple-request gate did not fire with it: see [the run record](real-model-runs/README.md)). The thirty failure cases and the dialect cases were not reviewed by a native speaker.

**Added on 25 November 2026.** In template 1, Decide now looks in the customer's own message for a request the model did not name, whatever the model returned: the words listed in Config (`sim.intents`) for requests that need a person, and more than one stored order in one message. Where the model saw only a question and one such request is found, the stricter reading replaces the model's (an order question of one sentence or naming no stored order; a general question whose topic is not approved); anything else is a second request and the whole message is handed over. A one-sentence question tied to an approved topic is still answered, on purpose. `second_request_check: false` switches it off. The recorded answers of the local model of 24 November, replayed through it: 60 of the store's 85 messages in place of 54, acting alone on 5 in place of 11; failure cases 18 right and 10 acted alone in place of 17 and 11. A replay, not a new run, outside n8n. The check knows only the words in Config. A fresh run of the same model the same day, through the check: 58 of 85, acting alone on 4; failure cases 22 right and 6 acted alone; `also` still never filled, and in 10 messages the model wrote a topic key where the intent belongs ([run record](real-model-runs/README.md)).

**Shadow mode (23 November 2026).** With `shadow_mode: true` in Config a template decides as usual and nothing leaves it; what it would have done is kept under `shadow.would` for comparison with the staff's record. It processes real data, so the data agreement comes first. Guide, report script and an invented sample: [`shadow-mode`](shadow-mode/README.md). Run inside n8n 2.35.7 on templates 1, 2 and 4; not tried with a business.

**Changing them.** The `*.n8n.json` files are built. Edit the sources under `src/`, run `python3 tools/build_n8n_workflows.py`, then `make check`.

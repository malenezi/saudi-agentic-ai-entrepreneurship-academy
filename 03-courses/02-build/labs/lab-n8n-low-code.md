# مختبر المسار الأساسي: الوكيل نفسه في n8n
# Core-track lab: the same agent in n8n

<div dir="rtl">

**الوحدات:** [2.3](../lessons/2-3-tools-and-integrations.md) و[2.5](../lessons/2-5-evaluation.md) و[2.6](../lessons/2-6-guardrails-and-human-approval.md) و[2.8](../lessons/2-8-failure-analysis-and-iteration.md) · **الزمن:** 90 دقيقة · **تحتاج:** مختبر 2.5، و[n8n](https://docs.n8n.io) على جهازك · **تنتهي بـ:** 24 ثم 25 ثم 28 ثم 30 من 35 في n8n، وهي أرقام الشيفرة المرجعية نفسها

> كل ما في المختبر مختلق للتعليم، والنموذج الافتراضي محاكٍ وليس نموذجاً لغوياً. اخترنا n8n لأنه الأداة التي يسميها المقرر للمسار الأساسي، وليس توصية به: ما تتعلمه هنا يصح في أي أداة منخفضة الكود. جُرّب المختبر على n8n 2.35.7 من سطر الأوامر، ولم يُجرَّب مع متعلمين.

## الهدف

بنيت في المختبرات السابقة وكيل الاستفسار عن الطلبات بالشيفرة. هنا تشغّل **الوكيل نفسه** في أداة منخفضة الكود، وتتحقق من أمرين: أن الحدود تُفرض خارج النموذج في أي أداة، وأن مجموعة تقييمك تحكم على الوكيل أياً كانت طريقة بنائه.

## الخطوات

**1. استورد وشغّل.** من جذر المستودع:

</div>

```bash
npm install n8n                                   # n8n 2.35 needs Node.js 22.22 or newer
npx n8n import:workflow --input=03-courses/02-build/labs/n8n/order-agent.n8n.json
npx n8n list:workflow                             # shows the workflow id
npx n8n publish:workflow --id=<the id>
npx n8n start                                     # leave it running; the editor is at http://localhost:5678
```

<div dir="rtl">

أو من المحرر: Workflows ثم Import from File، ثم انشر سير العمل.

**2. اقرأ المخطط قبل أن ترسل شيئاً.** افتح سير العمل في المحرر وتتبّع المسار:

</div>

```
Webhook -> Config -> Prepare -> Real model? -> Model (HTTP)      -> Decide -> Respond
                                            -> Simulated model  ->
```

<div dir="rtl">

قارنه بورقة تصميمك من مختبر 2.1. عقدة **Decide** هي `agent.py`، وعقدة **Simulated model** هي `model.py`، وعقدة **Config** هي ملفات `config/` و`data/` معاً. لاحظ أن النموذج لا يتصل بأي أداة: مخرجه يذهب إلى Decide وحدها.

**3. رسالة واحدة.** في طرفية ثانية:

</div>

```bash
curl -s -X POST http://localhost:5678/webhook/saaea-order-agent \
  -H 'Content-Type: application/json' \
  -d '{"message": "ما حالة طلبي رقم 84522؟", "account": "0500000001"}'
```

<div dir="rtl">

المتوقع: `"action": "reply_status"` ومسودة فيها «خرج للتوصيل»، كما في مختبر 2.1.

**4. خط الأساس.** شغّل مجموعة التقييم نفسها على الوكيل الذي في n8n:

</div>

```bash
python3 03-courses/02-build/labs/n8n/evaluate_n8n.py
```

<div dir="rtl">

المتوقع: **24 من 35**، والأمان 4 من 5، وقاعدة الإطلاق غير محققة. هو رقم مختبر 2.5 بالضبط، لأن المقيّم واحد والوكيل واحد.

**5. الضابط خارج النموذج.** افتح عقدة Config وغيّر `"ownership_check": "prompt"` إلى `"app"`، ثم انشر سير العمل من جديد وأعد التقييم.

المتوقع: **25 من 35**، والأمان 5 من 5. ثم افتح عقدة Decide وابحث عن `ownership_check`: الضابط سطران يسبقان قراءة الطلب، كما في `agent.py`. الأداة تغيّرت، وموضع الضابط لم يتغير.

**6. الدورة الأولى.** في Config: انسخ المصطلحات الأربعة من [`data/glossary.json`](reference/data/glossary.json) إلى `"glossary"`، واجعل `"rules"` تساوي `["conditional_cancel"]`. انشر وأعد التقييم.

المتوقع: **28 من 35**.

**7. الدورة الثانية.** في Config: احذف النسخة الملغاة من `"policy"`، فتبقى النسخة المعتمدة وحدها، كما في [`policy-v2-approved-only.json`](reference/data/policy-v2-approved-only.json). انشر وأعد التقييم، ثم شغّل المجموعة المحجوزة:

</div>

```bash
python3 03-courses/02-build/labs/n8n/evaluate_n8n.py
python3 03-courses/02-build/labs/n8n/evaluate_n8n.py --cases data/heldout.json
```

<div dir="rtl">

المتوقع: **30 من 35** وقاعدة الإطلاق محققة، ثم **6 من 8** في المجموعة المحجوزة.

**8. الموافقة البشرية.** الطلب 84521 متأخر، فيقترح الوكيل فتح طلب متابعة ولا يفتحه:

</div>

```bash
curl -s -X POST http://localhost:5678/webhook/saaea-order-agent \
  -H 'Content-Type: application/json' -d '{"message": "وين طلبي 84521", "account": "0500000001"}'
curl -s -X POST http://localhost:5678/webhook/saaea-order-agent-approve \
  -H 'Content-Type: application/json' -d '{"order_id": "84521", "approved_by": ""}'
curl -s -X POST http://localhost:5678/webhook/saaea-order-agent-approve \
  -H 'Content-Type: application/json' -d '{"order_id": "84521", "approved_by": "اسمك"}'
```

<div dir="rtl">

المتوقع: في الأول `pending_approval` فيها `create_followup_ticket`. في الثاني رفض، لأن الموافقة بلا اسم. في الثالث `"ticket": "T-84521"`. مسار الموافقة يبدأ من نقطة استقبال مستقلة، ولا يصل إليه شيء من محادثة العميل.

**9. مفتاح الإيقاف.** في Config اجعل `"stopped": true`، وانشر، وأرسل أي رسالة.

المتوقع: `"action": "stopped"` و`tool_calls` فارغة. ثم أعده إلى `false`.

## ما تسلّمه

1. لقطة للمخطط وعليها ثلاثة أسهم: أين يُفهم الطلب، وأين يُتحقق من ملكيته، وأين تنتظر الموافقة.
2. مخرجات التقييم الأربعة (24، 25، 28، 30) من جهازك.
3. فقرة: ما الذي كسبته بالأداة منخفضة الكود، وما الذي بقي شيفرةً لا مفر منها؟

## تحدٍّ إضافي

- **نموذج حقيقي.** اجعل `model_mode` يساوي `http` واضبط `model_base_url` و`model_name` على خادم محلي أو مستضاف (اقرأ [القسم 5 من صفحة المختبرات](README.md) أولاً، ولا تكتب مفتاحاً في Config). أعد التقييم وقارن: أي الحالات تغيّرت، ولماذا؟
- **الدورة الثالثة.** ابحث في الحالات الخمس الباقية عن سبب واحد تعالجه بإعداد في Config، كما فعلت في مختبر 2.8.

## حين يتعطل شيء

| ما تراه | السبب الغالب | ما تفعله |
|---|---|---|
| `Could not reach the workflow` | n8n لا يعمل، أو سير العمل غير منشور | `npx n8n start`، وانشر سير العمل |
| الرقم لم يتغير بعد تعديل Config | لم تنشر التعديل | انشر سير العمل من جديد |
| `404` من نقطة الاستقبال | تستخدم مسار الاختبار، أو المسار خطأ | المسار المنشور يبدأ بـ`/webhook/` |
| أرقام مختلفة عن المتوقع | Config ليست في المرحلة التي تظنها | قارنها بملف المرحلة في [`reference/config/`](reference/config/) |

## ما في المجلد

| المسار | ما فيه |
|---|---|
| [`n8n/order-agent.n8n.json`](n8n/order-agent.n8n.json) | سير العمل، مبنياً. يبدأ عند خط الأساس |
| `n8n/src/` | مصدره: `spec.json` و`sim.js` و`decide.js` و`approve.js`. يُبنى بـ`python3 tools/build_n8n_workflows.py` |
| [`n8n/evaluate_n8n.py`](n8n/evaluate_n8n.py) | المقيّم: يرسل الحالات إلى n8n ويحكم عليها بقواعد المقيّم المرجعي |

اختبار آلي يتحقق من أن عقد سير العمل تعطي نتيجة الشيفرة المرجعية نفسها في كل حالة وكل مرحلة (`tests/test_n8n_workflows.py`). ونقاط الاستقبال هنا **بلا توثيق**: هذا مختبر على جهازك، فلا تعرضه على الإنترنت.

</div>

---

## English summary

The order-enquiry agent of the Course 2 labs, as an importable n8n workflow for the low-code core track. Import it, publish it, and run the same 35-case test set against it with `evaluate_n8n.py`: the baseline is **24 of 35**; moving the ownership check into the application gives **25**; the glossary and the conditional-cancel rule give **28**; removing the revoked policy version gives **30** and meets the launch rule, with **6 of 8** on the held-out set. These are the numbers of the Python reference, because the workflow's nodes are a port of it and a test compares the two on every case at every stage. The default model is a keyword simulator, not a language model. n8n is used because the course names it for the core track; it is not a recommendation. Run on n8n 2.35.7 from the command line on 20 November 2026; not tried with learners, and not run with a real model.

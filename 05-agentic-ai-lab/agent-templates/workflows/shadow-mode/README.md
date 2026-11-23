# وضع الظل · Shadow mode

**Status:** Added 23 November 2026 · Logic tested outside n8n on the fifty template cases · Run inside n8n 2.35.7 on templates 1, 2 and 4 · **Not tried with a business** · The sample is invented and was answered by the keyword simulator · Educational

<div dir="rtl">

في وضع الظل يستقبل القالب الرسائل ويقرر كعادته، ثم **لا يخرج منه شيء**: لا مسودة رد، ولا تحويل، ولا طلب موافقة، ولا إشعار، ولا كتابة. ما كان سيفعله يُحفظ في حقل واحد اسمه `shadow.would`، لتقارنه بما فعله الموظفون في المدة نفسها.

الغرض: أن يرى عميل متردد ما كان الوكيل سيفعله برسائله هو، قبل أن يسمح له بالرد على أحد. شرحه في [الوحدة 3.6، البند 8](../../../../03-courses/03-launch/lessons/3-6-pilots-and-letters-of-intent.md#8-وضع-الظل-الوكيل-يعمل-ولا-يرسل-شيئاً).

> **وضع الظل يعالج بيانات حقيقية.** الوكيل يقرأ الرسالة ويبحث في الطلبات ليعرف ما كان سيفعله. عدم الإرسال لا يُسقط شيئاً من التزامات حماية البيانات: أكمل [التقييم الذاتي](../../../../02-saudi-market-knowledge-framework/compliance-toolkit/pdpl-self-assessment.md) واتفق كتابةً مع العميل على المعالجة **قبل** أول رسالة. وإن كان النموذج عند مزوّد، فالرسائل تصل إليه.

## التشغيل

1. في عقدة **Config** اجعل `shadow_mode` يساوي `true`.
2. أرسل مع كل رسالة حقل `ref`: رقمك أنت للرسالة، وبه تُربط بسجل الموظفين.
3. احفظ كل رد في ملف، سطراً لكل رد. **القالب لا يحفظه لك:** أضف بعد **Decide** عقدة تكتب إلى مخزنك، أو احفظه من الطرف الذي يستدعي نقطة الاستقبال.

</div>

```bash
curl -s -X POST http://localhost:5678/webhook/saaea-customer-service \
  -H 'Content-Type: application/json' -H 'X-SAAEA-Token: <the token>' \
  -d '{"message": "وين طلبي A-1001", "account": "0500000001", "ref": "M-002"}' >> shadow-log.jsonl
```

<div dir="rtl">

شكل الرد (مختصراً):

</div>

```json
{
  "mode": "shadow", "action": "shadow_observed", "level": "shadow",
  "reply_draft": "", "handover": null, "pending_approval": [], "notify_staff": [], "tool_calls": [],
  "shadow": {
    "ref": "M-002",
    "would": { "action": "answer_order_status", "level": "autonomous", "reply_draft": "...", "tool_calls": [{ "tool": "order_lookup", "input": "A-1001" }] }
  }
}
```

<div dir="rtl">

## ما يتغيّر في وضع الظل

| | التشغيل العادي | وضع الظل |
|---|---|---|
| مسودة الرد والتحويل والموافقات والإشعارات | في الرد | فارغة. الأصل في `shadow.would` |
| الحجوزات ومسودات القيود (القالبان 2 و4) | تُحفظ في بيانات سير العمل | تُحسب على نسخة تُهمل. لا يُحفظ شيء، ولا يوجد ما يُعتمد |
| حالة المحادثة `state` | تتقدم | تعود كما وردت. الحالة التي كان سيبلغها في `shadow.would.state` |
| القراءة (البحث عن طلب، قراءة التقويم) | تحدث | **تحدث** |
| مفتاح الإيقاف `stopped` | يحيل كل شيء إلى إنسان | يعمل كما هو، ويُسجَّل |

## سجل الموظفين

ملف CSV يملؤه فريق العميل للرسائل نفسها. سطر لكل رسالة، وإلا لن يُملأ:

| العمود | القيم |
|---|---|
| `ref` | رقم الرسالة نفسه |
| `staff_outcome` | `answered` أجاب بنفسه · `handed` أحال أو احتاج قراراً · `refused` رفض |
| `staff_minutes` | الدقائق التي أخذتها الرسالة (اختياري) |
| `draft_ok` | حكم الموظف على مسودة الوكيل: `yes` أو `no`، أو فارغ إن لم يحكم |
| `note` | سطر حر |

## التقرير

</div>

```bash
python3 tools/shadow_report.py shadow-log.jsonl staff-record.csv
python3 tools/shadow_report.py      # the invented sample in this folder
```

<div dir="rtl">

العيّنة هنا اثنتا عشرة رسالة مختلقة لمتجر مختلق ([الرسائل](sample-messages.json)، [سجل الظل](sample-shadow-log.jsonl)، [سجل الموظفين](sample-staff-record.csv))، أجاب عنها المحاكي بالكلمات المفتاحية لا نموذج لغوي:

| المقياس | القيمة في العيّنة |
|---|---|
| رسائل رآها الوكيل، وما سجّله الموظفون منها | 12، 11 |
| كان سيتصرف وحده · سيحيل · سيرفض | 5 · 4 · 2 |
| النتيجة نفسها عند الموظف | 9 من 11 |
| مسودات حكم عليها الموظف، والصحيح منها | 5، 4 |
| رسائل أجاب عنها الموظف وكان الوكيل سيجيب عنها صحيحاً، ودقائقها | 4 رسائل، 12 دقيقة من 39 |

**اقرأ أولاً الصف الذي تصرّف فيه الوكيل حيث لم يتصرف الموظف.** في العيّنة هو الرسالة M-012: عميل يشكو من طلب وصل مكسوراً، والمحاكي قرأها سؤالاً عن حالة الطلب فكان سيطلب رقم الطلب. رسالة واحدة كهذه تهمّ العميل أكثر من نسبة التطابق كلها.

## حدود التقرير

- الدقائق **حد أعلى** لما قد ينتقل إلى الوكيل: وقت مراجعة ردوده لم يُطرح منها.
- كل رسالة تُحكم كما وردت. الوكيل لم يُجرِ محادثة، فالقوالب متعددة الرسائل (2 و3) تُقارن مقارنة أضعف من القالب 1 والقالبين 4 و5.
- مسودة لم يحكم عليها أحد لا تُعدّ صحيحة.
- التقرير يعدّ ولا يحكم. لا حدّ مبنياً فيه: قاعدة القرار تُكتب مع العميل قبل البدء.
- وضع الظل لا يثبت أن عملاء العميل سيقبلون رداً من وكيل. هذا تختبره المرحلة التالية: تشغيل يوافق فيه موظف على كل رد.

</div>

---

## English

With `shadow_mode: true` in Config, a template receives messages and decides as usual, and then **nothing leaves it**: no reply draft, handover, approval request, staff notice or write. What it would have done is kept under `shadow.would`, to be compared with what the staff did over the same period. The purpose is to let a cautious customer see what the agent would have done with its own messages before the agent answers anyone ([Module 3.6, section 8](../../../../03-courses/03-launch/lessons/3-6-pilots-and-letters-of-intent.md#8-وضع-الظل-الوكيل-يعمل-ولا-يرسل-شيئاً)).

**Shadow mode processes real data.** The agent reads the message and looks things up to know what it would do. Sending nothing removes no data-protection obligation: complete the [PDPL self-assessment](../../../../02-saudi-market-knowledge-framework/compliance-toolkit/pdpl-self-assessment.md) and agree the processing in writing with the customer before the first message. If the model is hosted, the messages reach the provider.

**Use.** Set `shadow_mode` to `true`; send a `ref` with every message; save each response as one line of a file (the template does not store it for you). The customer's team fills a CSV for the same messages: `ref`, `staff_outcome` (`answered`, `handed`, `refused`), `staff_minutes`, `draft_ok` (`yes`, `no` or empty), `note`. Then run `python3 tools/shadow_report.py shadow-log.jsonl staff-record.csv`.

**What changes.** Outward fields are empty and the original is in `shadow.would`. Templates 2 and 4 work on a discarded copy of the stored data, so no booking or draft is kept and nothing can be approved. Conversation state is returned as it came. Reads still happen. The stop switch works as before.

**The sample** is twelve invented messages answered by the keyword simulator: 11 recorded by the staff, the same outcome on 9, 4 of 5 judged drafts correct, and one message (M-012, a complaint read as an order-status question) where the agent would have acted and the staff handed over. Read that row first.

**Limits.** The staff minutes are an upper bound, because review time is not subtracted. Each message is judged as it arrived, so multi-message templates (2 and 3) are compared weakly. A draft nobody judged is not counted as correct. The report counts and does not judge: the decision rule is written with the customer before the period starts. Shadow mode does not show that end customers accept an agent's reply; the next stage, with a person approving every reply, tests that. Run inside n8n 2.35.7 on templates 1, 2 and 4 (23 November 2026): the twelve sample messages gave the published log, and a booking and an invoice draft were not kept. Not tried with a business.

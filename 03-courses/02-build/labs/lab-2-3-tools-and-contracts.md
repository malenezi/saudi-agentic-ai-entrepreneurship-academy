# مختبر 2.3: الأدوات وعقودها
# Lab 2.3: Tools and their contracts

<div dir="rtl">

**الوحدة:** [2.3 الأدوات والتكاملات](../lessons/2-3-tools-and-integrations.md) · **الزمن:** 60 دقيقة · **تحتاج:** مختبر 2.1 · **تنتهي بـ:** عقد أداة مكتوب، ومدخل مرفوض، وإجراء ينتظر الموافقة

> كل ما في المختبر مختلق للتعليم، والنموذج الافتراضي محاكٍ وليس نموذجاً لغوياً. الإعداد وحلول الأعطال في [صفحة المختبرات](README.md). نفّذ الأوامر من داخل `reference/`.

## الهدف

النموذج يطلب، والتطبيق يتحقق وينفّذ. ترى هنا العقد وهو يرفض مدخلاً، وترى إجراءً يكتب وهو ينتظر إنساناً مسمّى.

## الخطوات

**1. استدعاء سليم.** أرسل استفساراً واقرأ `tool_calls`:

</div>

```bash
python3 -m order_agent.cli "وين طلبي 84522؟"
```

<div dir="rtl">

**2. العقد يرفض.** استدعِ الأداة مباشرةً بمدخل لا يطابق الصيغة:

</div>

```bash
python3 -c "
from order_agent.evaluate import build_agent, load
agent = build_agent(load('config/stage-3-cycle-2.json'))
agent.store.get_order_status('رقم 84522')"
```

<div dir="rtl">

المتوقع: `ToolInputError: order_id must be five digits, got 'رقم 84522'`. التحقق في الأداة، وليس في تعليمات النموذج.

**3. إجراء من المستوى B ينتظر الموافقة.** الطلب 84521 لم يتحرك منذ ستة أيام، والسياسة تقول ثلاثة:

</div>

```bash
python3 -m order_agent.cli "ما حالة طلبي 84521؟"
python3 -m order_agent.cli "ما حالة طلبي 84521؟" --approve "نورة"
```

<div dir="rtl">

في الأولى: `pending_approval` فيها `create_followup_ticket` ولم يُفتح شيء. في الثانية: `"ticket": "T-84521"` و`"approved_by": "نورة"`.

**4. لا أداة لما لا يجوز.** اطلب استرداداً وتغيير عنوان، وتحقق أن `tool_calls` فارغة في الحالتين:

</div>

```bash
python3 -m order_agent.cli "أريد استرداد المبلغ للطلب 84540"
python3 -m order_agent.cli "أريد تغيير عنوان التوصيل للطلب 84523"
```

<div dir="rtl">

**5. اكتب العقد.** املأ [قالب عقد الأداة](../templates/tool-contract.md) للأداة `create_followup_ticket` من قراءة `tools.py`: الغرض، المدخلات وصيغتها، المخرجات، الصلاحية، شرط الاستدعاء، ما يحدث عند التكرار، ومن يوافق.

## تحقق

- [ ] رأيت الخطأ `ToolInputError` بنصه.
- [ ] الإجراء لم يُنفَّذ إلا مع `--approve` واسم.
- [ ] عقدك يذكر أن الطلب الواحد لا يُفتح له أكثر من طلب متابعة (اقرأ `create_followup_ticket`).

## فرق المسارين

| الأساسي | العميق |
|---|---|
| عقد الأداة مكتوباً من قراءة الشيفرة | أضف أداة خامسة للقراءة فقط، `get_exchange_policy`، بعقدها واختبار واحد لها في `tests/`. لا تضف أداة تكتب |

## ثم مشروعك

اكتب عقداً لكل أداة في وكيلك. إن لم تستطع كتابة شرط الاستدعاء في سطر، فالأداة أوسع مما يجب.

</div>

---

**English summary.** A valid tool call, a contract that rejects malformed input, a level B action that waits for a named approver, the absence of any tool for refunds or address changes, and a written contract for one tool.

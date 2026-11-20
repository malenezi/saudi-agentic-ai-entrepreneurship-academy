# مختبر 2.2: السياق وقائمة المصطلحات
# Lab 2.2: Context and the dialect glossary

<div dir="rtl">

**الوحدة:** [2.2 هندسة السياق بالعربية](../lessons/2-2-context-engineering-in-arabic.md) · **الزمن:** 45 دقيقة · **تحتاج:** مختبر 2.1 · **تنتهي بـ:** رسائل باللهجة قبل القائمة وبعدها، ومصطلح أضفته أنت

> كل ما في المختبر مختلق للتعليم، والنموذج الافتراضي محاكٍ وليس نموذجاً لغوياً. الإعداد وحلول الأعطال في [صفحة المختبرات](README.md). نفّذ الأوامر من داخل `reference/`.

## الهدف

ترى بالتجربة أن ما تضعه في السياق يغيّر ما يفهمه الوكيل، وأن قائمة المصطلحات تُجمع من رسائل العملاء، لا من ظنّك.

## الخطوات

**1. جرّب رسالتين باللهجة بلا قائمة مصطلحات** (إعداد «بعد الضوابط»):

</div>

```bash
python3 -m order_agent.cli "طلبي معلّق من أمس، عطنا العلم" --config config/stage-1-guardrails.json
python3 -m order_agent.cli "الطلب تأخر مرة، إذا ما وصل اليوم كنسلوه، ترى عندي مناسبة بكره" --config config/stage-1-guardrails.json
```

<div dir="rtl">

المتوقع: الأولى `"intent": "unknown"` وتُحال، والثانية `"intent": "cancel"`، أي أنه عدّها إلغاءً فورياً. كلاهما خطأ فهم.

**2. أعدهما بقائمة المصطلحات وقاعدة الإلغاء المشروط** (إعداد «بعد الدورة 1»):

</div>

```bash
python3 -m order_agent.cli "طلبي معلّق من أمس، عطنا العلم" --config config/stage-2-cycle-1.json
python3 -m order_agent.cli "الطلب تأخر مرة، إذا ما وصل اليوم كنسلوه، ترى عندي مناسبة بكره" --config config/stage-2-cycle-1.json
```

<div dir="rtl">

المتوقع: الأولى `order_status` و`ask_order_id`، والثانية `conditional_cancel` و`"urgent": true`.

**3. قارن الإعدادين.** افتح الملفين في `config/` وابحث عن الفرق: سطر `glossary` وسطر `rules`. ثم افتح `data/glossary.json`.

**4. أضف مصطلحاً.** الرسالة «ما جاني شي للحين، وش الطبخة؟» ما زالت لا تُفهم. انسخ القائمة وأضف إليها:

</div>

```bash
cp data/glossary.json data/my-glossary.json          # add:  "ما جاني": "order_status"
cp config/stage-2-cycle-1.json config/my-context.json  # change "glossary" to "data/my-glossary.json"
python3 -m order_agent.cli "ما جاني شي للحين، وش الطبخة؟" --config config/my-context.json
```

<div dir="rtl">

المتوقع بعد الإضافة: `order_status` و`ask_order_id`.

**5. اقرأ `instructions.md`**: تعليمات النموذج الحقيقي. قابلها ببنية التعليمات في [الدرس 2.2](../lessons/2-2-context-engineering-in-arabic.md) جزءاً جزءاً. أي أجزاء البنية موجود فيها، وأيها ناقص؟

## تحقق

- [ ] رأيت `unknown` و`cancel` قبل القائمة، و`order_status` و`conditional_cancel` بعدها.
- [ ] مصطلحك الجديد جعل الرسالة تُفهم.
- [ ] تستطيع أن تقول من أين يأتي كل مصطلح في قائمتك.

## تنبيه

المحاكي لا يفهم إلا ما في قائمته، فأثر المصطلح الواحد فيه أوضح مما في نموذج حقيقي. النموذج الحقيقي يفهم كثيراً من اللهجة بلا قائمة، ويخطئ في مواضع لا تتوقعها. لذلك تُقاس اللهجة على حالات حقيقية في الوحدة 2.5.

## فرق المسارين

| الأساسي | العميق |
|---|---|
| تعديل ملف القائمة وملف الإعداد | أضف: اقرأ `SimModel.understand` في `model.py`، واشرح لماذا تسبق كلمات «خارج النطاق» غيرها في الترتيب |

## ثم مشروعك

اجمع عشرين رسالة حقيقية من سير عملك، **بعد استبدال كل بيان شخصي**، واستخرج منها قائمتك.

</div>

---

**English summary.** The same dialect messages before and after a glossary and one rule are placed in the context, then a term the learner adds, then a reading of the instructions file against the lesson's structure.

# B1: رسائل الوكيل بالعربية
# B1: Agent messages in Arabic

**Tool:** [Bayan](https://github.com/malenezi/bayan) · `arabic-ux-writing`, `i18n_parity.py`, `bidi_lint.py` · **Course 2**, Module 2.2, and **Course 3**, Module 3.1 · **Time:** 90 minutes

<div dir="rtl">

## الغرض

أول ما يراه عميلك من وكيلك رسالة. رسالة تبدو مترجمة، أو يظهر فيها رقم الجوال مقلوباً، تُفقد الثقة قبل أن يعمل الوكيل. في هذا التمرين تكتب رسائل الوكيل الثابتة بعربية سليمة وتفحصها آلياً.

## ما تحتاجه

- بطاقة الدور ومصفوفة الاعتماد من [R3](r3-role-card-and-approval-matrix.md)، أو أحد [قوالب الوكلاء](../agent-templates/README.md).
- الجمهور والنبرة من الطبقة الأولى في حزمة السياق ([R2](r2-context-pack.md)).

## الخطوات

1. **اجمع الرسائل الثابتة** في ملفين: `ar.json` و`en.json` بالمفاتيح نفسها. الحد الأدنى:

| المفتاح | متى تُرسل |
|---|---|
| `greeting` | أول تواصل، وفيها إفصاح بأن المتحدث نظام آلي |
| `ask_missing` | طلب معلومة أو مستند ناقص |
| `confirm_before_action` | قبل أي فعل يحتاج موافقة العميل |
| `handover` | التحويل إلى موظف، مع ما يتوقعه العميل ومتى |
| `cannot_help` | طلب خارج النطاق |
| `error_retry` | تعذّر التنفيذ |
| `privacy_notice` | ما البيانات التي تُجمع ولماذا |

2. **اكتب العربية أولاً**، لا ترجمة عن الإنجليزية. استند إلى [دليل الأسلوب](https://github.com/malenezi/bayan/blob/main/skills/arabic-ux-writing/references/style-guide.md) و[الأخطاء الشائعة](https://github.com/malenezi/bayan/blob/main/skills/arabic-ux-writing/references/common-mistakes.md)، ووحّد المصطلحات من [المسرد](https://github.com/malenezi/bayan/blob/main/skills/arabic-ux-writing/references/glossary.md).
3. **المتغيرات** (`{name}`، `{amount}`) بالأسماء نفسها في اللغتين.
4. افحص:

</div>

```bash
python3 bayan/shared/scripts/i18n_parity.py --json my-venture/messages/ar.json my-venture/messages/en.json
python3 bayan/shared/scripts/bidi_lint.py my-venture/messages/ar.json
```

<div dir="rtl">

5. أصلح ما يظهر: مفتاح ناقص، نص لم يُترجم، متغير مختلف الاسم، علامات ترقيم لاتينية بعد نص عربي، أرقام وروابط غير معزولة.
6. اقرأ الرسائل بصوت مسموع على شخص من جمهورك. المدقق لا يحكم على النبرة ولا على اللهجة.

للمقارنة: [مثال «بيان» الرابع](https://github.com/malenezi/bayan/tree/main/examples/04-ui-strings) فيه ملف قبل الإصلاح وبعده.

## ما لا يغطيه «بيان»

- **اللهجة السعودية** في ردود الوكيل المولَّدة: تُختبر بحالات [قالب التقييم](../evaluation/eval-template.md).
- **مضمون إشعار الخصوصية:** من [دليل نظام حماية البيانات الشخصية](../../02-saudi-market-knowledge-framework/03-data-protection-pdpl/pdpl-founder-guide.md). «بيان» يضبط الصياغة لا الحكم النظامي.
- **شروط قوالب الرسائل** لدى مزوّد المراسلة: من توثيق المزوّد.

## معيار الإنجاز

- [ ] `i18n_parity.py` بلا مشكلات.
- [ ] `bidi_lint.py` بلا أخطاء ولا تحذيرات.
- [ ] رسالة الترحيب تفصح بأن المتحدث نظام آلي.
- [ ] رسالة التحويل تقول من سيرد ومتى.
- [ ] قارئ من الجمهور لم يتعثر في أي رسالة.

</div>

---

**English.** Write the agent's fixed messages (greeting with an automation disclosure, missing-document request, confirmation, handover, refusal, error, privacy notice) Arabic-first using Bayan's style guide and glossary, then check them with `i18n_parity.py --json` and `bidi_lint.py`. Bayan covers wording and bidi correctness; Saudi dialect in generated replies is tested with the Academy's evaluation template, and the content of the privacy notice comes from the PDPL guide.

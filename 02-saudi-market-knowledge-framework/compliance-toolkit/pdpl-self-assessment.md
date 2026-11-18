# التقييم الذاتي لنظام حماية البيانات الشخصية · PDPL self-assessment

Educational tool, not legal advice. Complete before the first real customer's data enters your product. Review every quarter and after any change of provider. A filled-in example: [customer-service agent with a CRM](../03-data-protection-pdpl/worked-example-customer-service-agent.md).

**المشروع · Venture:** ____________  **التاريخ · Date:** ____________  **المسؤول · Owner:** ____________

## الجزء 1: خريطة البيانات · Part 1: Data map

One row per category of personal data the agent touches.

| البيانات · Data | المصدر · Source | الغرض · Purpose | الأساس النظامي · Lawful basis | أين تُخزَّن · Stored where | من يستلمها · Recipients | بلد المعالجة · Processing country | مدة الحفظ · Retention |
|---|---|---|---|---|---|---|---|
| مثال: رقم الجوال · Phone number | العميل عبر واتساب | تأكيد الموعد | تنفيذ اتفاق | قاعدة البيانات | مزوّد الرسائل | | 12 شهراً |
| | | | | | | | |
| | | | | | | | |

Remember to include: conversation logs, agent memory, vector stores, debugging traces, backups.

## الجزء 2: قائمة التحقق · Part 2: Checklist

Answer نعم / لا / جزئي (Yes / No / Partly). Every "No" or "Partly" becomes an action with an owner and a date.

### أ. الأساس والشفافية · Basis and transparency

| # | السؤال · Question | الإجابة | الإجراء |
|---|---|---|---|
| 1 | هل لكل فئة بيانات غرض محدد وأساس نظامي؟ · Does each data category have a defined purpose and lawful basis? | | |
| 2 | هل توجد سياسة خصوصية منشورة بالعربية؟ · Is there a published privacy notice in Arabic? | | |
| 3 | هل يُبلَّغ المستخدم بأنه يتعامل مع وكيل آلي؟ · Are users told they are dealing with an automated agent? | | |
| 4 | إن كانت الموافقة هي الأساس، هل هي صريحة ويمكن سحبها؟ · Where consent is the basis, is it explicit and withdrawable? | | |
| 5 | هل تلتزم الرسائل التسويقية بشروطها؟ · Do marketing messages meet their conditions? | | |

### ب. تقليل البيانات والحفظ · Minimisation and retention

| # | السؤال · Question | الإجابة | الإجراء |
|---|---|---|---|
| 6 | هل نجمع فقط ما تحتاجه المهمة؟ · Do we collect only what the task needs? | | |
| 7 | هل تُحجب المعرّفات قبل إرسال النص إلى النموذج حين يمكن؟ · Are identifiers redacted before text goes to the model where possible? | | |
| 8 | هل لكل فئة مدة حفظ محددة وحذف آلي؟ · Does each category have a retention period and automatic deletion? | | |
| 9 | هل تخلو بيئات الاختبار من بيانات حقيقية؟ · Are test environments free of real personal data? | | |

### ج. حقوق الأفراد · Individual rights

| # | السؤال · Question | الإجابة | الإجراء |
|---|---|---|---|
| 10 | هل توجد قناة واضحة لاستقبال طلبات الأفراد؟ · Is there a clear channel for individuals' requests? | | |
| 11 | هل نستطيع استخراج بيانات شخص واحد وتسليمه نسخة؟ · Can we retrieve one person's data and give them a copy? | | |
| 12 | هل نستطيع حذف بيانات شخص من القاعدة والذاكرة والمتجهات والسجلات؟ · Can we delete one person from the database, memory, vector store and logs? | | |
| 13 | هل نستطيع تصحيح بيانات خاطئة؟ · Can we correct inaccurate data? | | |

### د. المعالِجون والنقل · Processors and transfers

| # | السؤال · Question | الإجابة | الإجراء |
|---|---|---|---|
| 14 | هل لدينا قائمة بكل مزوّد يستلم بيانات شخصية؟ · Do we have a list of every provider receiving personal data? | | |
| 15 | هل نعرف بلد المعالجة لكل مزوّد؟ · Do we know each provider's processing country? | | |
| 16 | هل شروط كل مزوّد تمنع استخدام بياناتنا للتدريب؟ · Do each provider's terms prevent training on our data? | | |
| 17 | إن خرجت البيانات من المملكة، هل تحققنا من ضوابط النقل؟ · If data leaves the Kingdom, have we checked the transfer conditions? | | |
| 18 | إن كنا معالِجاً لعميل، هل وقّعنا اتفاقية معالجة بيانات؟ · If we are a processor for a client, is a data processing agreement signed? | | |

### هـ. الأمن والحوادث · Security and incidents

| # | السؤال · Question | الإجابة | الإجراء |
|---|---|---|---|
| 19 | هل البيانات مشفّرة أثناء النقل والتخزين؟ · Is data encrypted in transit and at rest? | | |
| 20 | هل الوصول مقيّد بالحاجة ومسجَّل؟ · Is access need-based and logged? | | |
| 21 | هل توجد خطة مكتوبة للتعامل مع تسرب البيانات؟ · Is there a written data-breach plan? | | |
| 22 | هل نعرف متى وكيف نُبلّغ الجهة المختصة والأفراد؟ · Do we know when and how to notify the authority and individuals? | | |

### و. فئات لها أحكام خاصة · Categories with their own rules

Three separate questions, because the law treats them separately. Sensitive data is a defined list; credit data is not on that list and has its own article; a minor's data is not a category of data at all, it is about who may consent ([SOURCES.md](../../SOURCES.md), A41, A45, A50).

| # | السؤال · Question | الإجابة | الإجراء |
|---|---|---|---|
| 23 | هل نعالج بيانات حساسة بتعريف النظام: الأصل العرقي أو الإثني، المعتقد الديني أو الفكري أو السياسي، البيانات الأمنية والجنائية، السمات الحيوية، البيانات الوراثية، البيانات الصحية، ما يدل على أن الفرد مجهول الأبوين أو أحدهما؟ · Do we process sensitive data as the law defines it: racial or ethnic origin; religious, intellectual or political belief; security and criminal data; biometric identifiers; genetic data; health data; data indicating that one or both parents are unknown? | | |
| 24 | هل نعالج بيانات ائتمانية (طلب تمويل، قدرة على السداد، تاريخ ائتماني)؟ · Do we process credit data (a financing request, ability to repay, credit history)? | | |
| 25 | هل يُحتمل أن يكون بعض أصحاب البيانات قاصرين أو ناقصي الأهلية؟ وإن كان، فكيف نتحقق من موافقة الولي ومن صفته؟ · Could some of the individuals be minors or lack full legal capacity? If so, how do we obtain the guardian's consent and verify guardianship? | | |
| 26 | إن كان الجواب نعم في أي من الثلاثة، هل حصلنا على استشارة قانونية قبل البناء؟ · If yes to any of the three, have we taken legal advice before building? | | |
| 27 | هل قيّمنا حاجتنا إلى تقييم أثر أو مسؤول حماية بيانات أو تسجيل؟ · Have we assessed whether an impact assessment, a DPO or registration is required? | | |

## الجزء 3: خطة الإجراءات · Part 3: Action plan

| الفجوة · Gap | الإجراء · Action | المسؤول · Owner | التاريخ · Due |
|---|---|---|---|
| | | | |

**متى تستعين بمحامٍ · When to call a lawyer:** any "Yes" to questions 23 to 25; any transfer outside the Kingdom you cannot avoid; your first enterprise or government contract; any breach.

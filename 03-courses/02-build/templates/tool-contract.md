# عقد الأداة · Tool contract

Used in [Module 2.3](../lessons/2-3-tools-and-integrations.md). One contract per tool, written before the tool is connected. Every action a tool makes possible also needs a row in the [Human Oversight Matrix](../../../02-saudi-market-knowledge-framework/compliance-toolkit/human-oversight-matrix.md).

<div dir="rtl">

| البند · Item | القيمة · Value |
|---|---|
| **الاسم · Name** | |
| **الغرض في جملة · Purpose in one sentence** (هذا ما يقرؤه النموذج ليختار الأداة) | |
| **المدخلات · Inputs** (الاسم، النوع، الصيغة المقبولة) | |
| **المخرجات · Outputs** | |
| **الصلاحية · Access** (قراءة / مسودة / كتابة) | |
| **الحساب المستخدم · Account used** (حساب خدمة محدود) | |
| **شرط الاستدعاء · Precondition** | |
| **شرط التوقف · Stop condition** | |
| **الأخطاء المتوقعة والتصرف · Expected errors and response** | |
| **إعادة المحاولة · Retries** (العدد، وهل تُكرر العملية أثرها؟) | |
| **مفتاح منع التكرار · Idempotency key** (إن دعمه النظام) | |
| **مستوى الإشراف · Oversight level** (A / B / C / D) | |
| **ما يُسجَّل · What is logged** | |
| **بيانات شخصية؟ · Personal data?** (ما هي، وأين تُعالج) | |

## اختبارات الأداة · Tool tests

| # | الحالة · Case | المتوقع · Expected | النتيجة · Result |
|---|---|---|---|
| 1 | مدخل صحيح · Valid input | | |
| 2 | مدخل ناقص · Missing input | يطلب الاستكمال | |
| 3 | مدخل خاطئ الصيغة · Malformed input | يُرفض قبل الاستدعاء | |
| 4 | سجل غير موجود · Not found | يصرّح ولا يخمّن | |
| 5 | غير مصرّح · Not authorised | يتوقف ويصعّد | |
| 6 | فشل اتصال · Connection failure | إعادة محدودة ثم تصعيد | |
| 7 | بيان محلي (تاريخ هجري، مبلغ، عنوان وطني، رقم بأرقام عربية) · Local data item | يمر صحيحاً | |

</div>

# مصفوفة الرقابة البشرية والصلاحيات · Human oversight and authorization matrix

<div dir="rtl">

**القاعدة:** الاستدلال احتمالي، والصلاحية حتمية. كل إجراء يستطيع الوكيل تنفيذه يُصنَّف في أحد أربعة مستويات، ويُفرض التصنيف بالشيفرة أو بإعدادات سير العمل، وليس بالتعليمات النصية.

</div>

Complete before the agent takes any real action. Enforce every row in code or workflow configuration, not in the prompt.

## المستويات · Levels

| المستوى · Level | المعنى · Meaning |
|---|---|
| **A مستقل · Autonomous** | ينفّذ الوكيل ويسجّل · Agent acts and logs |
| **B إشعار · Notify** | ينفّذ ثم يُبلّغ إنساناً · Agent acts, then informs a person |
| **C موافقة · Approve** | لا ينفّذ إلا بعد موافقة إنسان محدد · Acts only after a named person approves |
| **D محظور · Forbidden** | لا ينفّذه الوكيل أبداً · Agent never does this |

## كيف تصنّف · How to classify

Raise the level when any of these is true: money moves; the action cannot be undone; a message leaves the business in its name; personal or sensitive data is disclosed; the law or a contract assigns the decision to a qualified person; an error would harm a customer.

## المصفوفة · Matrix

| # | الإجراء · Action | المستوى · Level | الحد · Limit | المعتمِد · Approver | كيف يُفرض · How enforced | السجل · Logged |
|---|---|---|---|---|---|---|
| 1 | الرد على استفسار عام · Answer a general enquiry | A | من قاعدة المعرفة فقط | | Retrieval scope | ✔ |
| 2 | حجز موعد · Book an appointment | A | ضمن الأوقات المتاحة | | Calendar tool rules | ✔ |
| 3 | إلغاء حجز · Cancel a booking | B | | المالك | Notification step | ✔ |
| 4 | تقديم خصم · Offer a discount | C | حتى ___٪ | المالك | Approval node | ✔ |
| 5 | استرداد مبلغ · Issue a refund | C | أي مبلغ | المالك | Approval node; payment key not available to agent | ✔ |
| 6 | إرسال عرض سعر · Send a quotation | C | | المبيعات | Draft-only permission | ✔ |
| 7 | تعديل سجل عميل · Edit a customer record | B | حقول محددة | | Field allow-list | ✔ |
| 8 | حذف بيانات · Delete data | D | | | No delete permission | ✔ |
| 9 | مشورة طبية أو قانونية أو شرعية · Medical, legal or religious advice | D | | | Policy check + escalation | ✔ |
| 10 | مراسلة جهة خارج المحادثة · Message a third party | D | | | Recipient allow-list | ✔ |
| | | | | | | |

Rows 1 to 10 are examples. Replace them with every action your agent's tools make possible. If a tool can do it, it needs a row.

## ضوابط عامة · Global controls

| الضابط · Control | القيمة · Value |
|---|---|
| أقصى عدد خطوات للمهمة · Max steps per task | |
| أقصى إنفاق يومي على النماذج · Max daily model spend | |
| أقصى عدد إجراءات في الساعة · Max actions per hour | |
| مهلة الموافقة، وماذا يحدث بعدها · Approval timeout and what happens then | |
| مفتاح الإيقاف: من يملكه وكيف يُفعَّل · Kill switch: who holds it and how | |
| التصعيد إلى إنسان: متى وإلى من · Escalation: when and to whom | |

## الاختبار · Test

- [ ] حاولنا جعل الوكيل ينفّذ كل إجراء من المستوى D، وفشل · We tried to make the agent perform each level-D action and it could not
- [ ] كل إجراء من المستوى C توقف فعلاً بانتظار الموافقة · Every level-C action actually paused for approval
- [ ] جُرّب مفتاح الإيقاف · The kill switch was tested
- [ ] السجل يبيّن من وافق ومتى · The log shows who approved and when

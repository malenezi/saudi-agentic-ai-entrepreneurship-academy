# تقرير مرحلة الظل · Shadow-period report

What you hand the customer at the end of a shadow period: what the agent would have done with the customer's own messages, beside what the staff did. Used in [Module 3.6, section 8](../lessons/3-6-pilots-and-letters-of-intent.md#8-وضع-الظل-الوكيل-يعمل-ولا-يرسل-شيئاً). The figures in section 2 come from [`tools/shadow_report.py`](../../../05-agentic-ai-lab/agent-templates/workflows/shadow-mode/README.md). Not a legal document; not reviewed by a lawyer.

<div dir="rtl">

> **ثلاث قواعد.** اتفاق البيانات يُوقَّع قبل أول رسالة. قاعدة القرار تُكتب قبل البدء ولا تُعدَّل بعد رؤية الأرقام. والقسم 3 يُكتب قبل القسم 2.

</div>

**المشروع · Venture:** ____________  **العميل · Customer:** ____________  **التاريخ · Date:** ____________

## 1. ما اتُّفق عليه قبل البدء · Agreed before the start

| # | البند · Item | القيمة · Value |
|---|---|---|
| 1 | المهمة الواحدة، وما هو خارج النطاق · The one task, and what is out of scope | |
| 2 | من تاريخ إلى تاريخ · From and to | |
| 3 | اتفاق معالجة البيانات: تاريخ توقيعه ومن وقّعه · Data processing agreement: date signed and by whom | |
| 4 | أين عولجت الرسائل، ومن المزوّدون · Where messages were processed, and the providers | |
| 5 | من ملأ سجل الموظفين، ولأي عيّنة · Who filled the staff record, and for which sample | |
| 6 | قاعدة القرار كما كُتبت قبل البدء · The decision rule as written before the start | |

## 2. الأرقام · Figures

| # | المقياس · Measure | القيمة · Value |
|---|---|---|
| 7 | رسائل رآها الوكيل · Messages the agent observed | |
| 8 | ما سجّله الموظفون منها · Of these, recorded by the staff | |
| 9 | كان سيتصرف وحده · Would have acted alone | |
| 10 | كان سيحيل إلى موظف · Would have handed to a person | |
| 11 | كان سيرفض · Would have refused | |
| 12 | النتيجة نفسها عند الموظف · Same outcome as the staff | |
| 13 | مسودات حكم عليها الموظف، والصحيح منها · Drafts judged by the staff, and those judged correct | |
| 14 | رسائل أجاب عنها الموظف وكان الوكيل سيجيب عنها صحيحاً · Messages the staff answered that the agent would have answered correctly | |
| 15 | دقائق الموظفين في تلك الرسائل (حد أعلى: وقت المراجعة لم يُطرح) · Staff minutes on those messages (an upper bound: review time is not subtracted) | |

## 3. حيث كان الوكيل سيتصرف ولم يتصرف الموظف · Where the agent would have acted and the staff did not

كل صف هنا يُقرأ مع العميل. Every row is read with the customer.

| الرقم · Ref | ما كان سيفعله · What it would have done | ما فعله الموظف · What the staff did | السبب · Cause | الإصلاح، ومتى · Fix, and when |
|---|---|---|---|---|
| | | | | |
| | | | | |

## 4. مسودات حكم الموظف بخطئها · Drafts the staff judged wrong

| الرقم · Ref | الخطأ بكلمات الموظف · The error in the employee's words | السبب · Cause | الإصلاح · Fix |
|---|---|---|---|
| | | | |
| | | | |

## 5. القرار · Decision

| # | البند · Item | القيمة · Value |
|---|---|---|
| 16 | النتيجة مقابل قاعدة القرار في الصف 6 · The result against the decision rule in row 6 | |
| 17 | القرار: تشغيل بموافقة موظف على كل رد، أو تمديد مرة واحدة بتغيير واحد، أو توقف · Decision: live with a person approving every reply, one extension with one change, or stop | |
| 18 | من قرّر، وبأي صفة · Who decided, and in what capacity | |
| 19 | ما يحدث للبيانات والسجلات الآن · What happens to the data and the logs now | |

## 6. ما لا يقوله هذا التقرير · What this report does not say

<div dir="rtl">

- لا يقول إن عملاء العميل سيقبلون رداً من وكيل: لم يصل إليهم رد.
- لا يقول كم سيوفّر الوكيل: وقت مراجعة ردوده لم يُحسب.
- لا يحكم على محادثة من عدة رسائل: كل رسالة حُكمت كما وردت.
- مسودة لم يحكم عليها أحد لم تُعدّ صحيحة.

</div>

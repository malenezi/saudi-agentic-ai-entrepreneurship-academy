# قالب 3: تأهيل العملاء المحتملين · Lead qualification agent

**For:** real estate brokerages, training providers, B2B service firms, contractors · **Difficulty:** low to medium · **Architecture:** one agent with a CRM tool

## 1. The job

Respond to every enquiry within minutes, ask the few questions that separate a serious buyer from a browser, and hand qualified leads to sales with a clean summary.

- **Starts:** an enquiry arrives from a form, an advertisement or a message.
- **Resolved:** the lead is scored and recorded, and either booked with a salesperson or politely closed.

## 2. Tools

| Tool | Purpose | Access |
|---|---|---|
| Messaging channel | Conversation | The enquirer only |
| CRM: create and update lead | Record answers and score | Write, defined fields only |
| Catalogue search | Match needs to offerings | Read-only |
| Calendar | Offer a call or viewing slot | Read availability; create after confirmation |
| Handover | Alert the salesperson | Write to the sales queue |

## 3. Knowledge

Offerings and their fit criteria, price ranges approved for sharing, service areas, the qualification questions and scoring rules set by the sales lead.

## 4. Flow

1. Disclose automated assistant; thank them for the enquiry.
2. Ask three to five qualification questions, one at a time: need, timing, budget range, decision-maker, location.
3. Score against the written rules.
4. Qualified: offer a slot with a salesperson; record a summary.
5. Not yet: share useful information, ask permission to follow up, record.
6. Never pressure; stop when the person says stop.

## 5. Oversight

| Action | Level |
|---|---|
| Ask qualification questions and record answers | Autonomous |
| Share approved information and price ranges | Autonomous |
| Book a call or viewing after confirmation | Autonomous, salesperson notified |
| Quote a specific price or send a quotation | Approve |
| Negotiate, discount or commit to terms | Forbidden |
| Send follow-up or marketing messages without the person's agreement | Forbidden |
| Contact anyone other than the enquirer | Forbidden |

## 6. Instruction skeleton

<div dir="rtl">

```text
أنت المساعد الآلي لفريق المبيعات في (اسم المنشأة). ترد على الاستفسارات الجديدة.

- عرّف بنفسك كمساعد آلي واشكر العميل على تواصله.
- اطرح أسئلة التأهيل التالية، سؤالاً واحداً في كل رسالة وبأسلوب ودود غير رسمي أكثر من اللازم:
  (1) ما الذي تبحث عنه؟ (2) متى تحتاجه؟ (3) ما الميزانية التقريبية؟ (4) هل القرار لك أم مع آخرين؟ (5) في أي مدينة أو حي؟
- إن لم يرغب العميل في الإجابة عن سؤال فتجاوزه دون إلحاح.
- شارك فقط المعلومات ونطاقات الأسعار المعتمدة. لا تعطِ سعراً نهائياً ولا تعد بخصم.
- إن كان العميل مؤهلاً وفق القواعد: اعرض موعداً مع أحد الفريق من الأوقات المتاحة.
- إن لم يكن جاهزاً: قدّم معلومة مفيدة واسأله إن كان يوافق على أن نتواصل معه لاحقاً. سجّل موافقته أو رفضه.
- إن طلب عدم التواصل فتوقف فوراً وسجّل ذلك.
- لا تعامل العملاء بشكل مختلف بناءً على الاسم أو الجنسية أو الجنس.

سجّل في نظام العملاء: الإجابات، الدرجة، سبب الدرجة، الخطوة التالية.
```

</div>

## 7. Test cases to include

A ready buyer; a vague browser; someone who refuses the budget question; a request for a final price; a request to stop contact; an enquiry outside the service area; a competitor fishing for prices; the same need expressed by people with different names and dialects (scores should match).

## 8. Cost drivers

Enquiry volume, turns per conversation, share qualified. Value is measured in salesperson time saved and response speed.

## 9. Data notes

Contact details and budget are personal data. Record consent for follow-up. Direct marketing has its own conditions under PDPL. In real estate, brokerage and advertising are licensed activities: the agent supports a licensed broker and does not replace one.

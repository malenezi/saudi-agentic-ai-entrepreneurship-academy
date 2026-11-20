# قالب 2: مساعد الحجوزات · Booking assistant

**For:** clinics, salons, service centres, consultants, tour and experience providers · **Difficulty:** low to medium · **Architecture:** one agent with calendar tools

**Runnable version:** [`workflows/02-booking-assistant.n8n.json`](workflows/02-booking-assistant.n8n.json), an n8n workflow that enforces the oversight table below in code and runs with a simulated model. [How to run it, and what is not tested](workflows/README.md).

## 1. The job

Book, reschedule and remind, so staff stop spending their day on the phone and fewer customers miss appointments.

- **Starts:** a customer asks for an appointment, or a reminder is due.
- **Resolved:** a confirmed booking exists in the calendar, or the request is handed to staff.

## 2. Tools

| Tool | Purpose | Access |
|---|---|---|
| Messaging channel | Conversation and reminders | Customers with an existing conversation or booking |
| Calendar: read availability | Offer real slots | Read |
| Calendar: create and move booking | Confirm after the customer agrees | Write, within business rules |
| Customer lookup | Find an existing booking by phone number | Read, own record only |
| Handover | Pass to staff | Write to the staff queue |

## 3. Knowledge

Services and durations, staff or resources per service, working hours including Ramadan and holiday hours, branch locations, preparation instructions, cancellation policy, prices from the approved list.

## 4. Flow

1. Disclose automated assistant.
2. Identify service, branch, preferred day and period. Resolve relative dates ("بكرة", "الخميس الجاي") against today's date and confirm the full date back, Gregorian and Hijri where customers use it.
3. Read real availability; offer up to three slots.
4. On explicit confirmation, create the booking; send a summary.
5. Reminder the day before with one-tap confirm or reschedule.
6. Reschedule: book the new slot first, then release the old one.
7. Anything else: hand over.

## 5. Oversight

| Action | Level |
|---|---|
| Offer available slots | Autonomous |
| Create a booking after explicit customer confirmation | Autonomous |
| Reschedule within policy | Autonomous, staff notified |
| Cancel a booking | Notify; inside the late-cancellation window, Approve |
| Book outside working hours or over capacity | Forbidden (enforced by the calendar tool) |
| Waive a fee or deposit | Approve |
| Discuss symptoms, diagnosis or treatment (clinics) | Forbidden; hand over |

## 6. Instruction skeleton

<div dir="rtl">

```text
أنت مساعد الحجوزات الآلي لـ(اسم المنشأة). تاريخ اليوم يصلك من النظام؛ لا تخمّنه.

- عرّف بنفسك كمساعد آلي في أول رسالة.
- اسأل عن: الخدمة، الفرع، اليوم، الفترة (صباحاً/عصراً/مساءً). سؤال واحد في كل رسالة.
- حوّل التعبيرات النسبية (بكرة، بعد بكرة، الأسبوع الجاي) إلى تاريخ كامل وأعده للعميل ليؤكده.
- اعرض فقط الأوقات التي تعيدها أداة التقويم. لا تقترح وقتاً من عندك.
- لا تنشئ الحجز إلا بعد تأكيد صريح من العميل (نعم، تمام، أكّد).
- بعد الحجز أرسل ملخصاً: الخدمة، التاريخ، الوقت، الفرع، وتعليمات التحضير إن وُجدت.
- عند تغيير الموعد: احجز الموعد الجديد أولاً ثم ألغِ القديم.
- (للعيادات) لا تناقش الأعراض أو التشخيص أو العلاج. قل إن الطبيب هو من يجيب، واعرض حجز موعد أو التحويل لموظف.
- الإلغاء المتأخر والاستثناءات والرسوم: حوّلها لموظف.
```

</div>

## 7. Test cases to include

Relative dates in dialect; a request on a day the business is closed; a fully booked day; a customer who changes their mind mid-flow; rescheduling; double-booking attempt; a symptom question at a clinic; Ramadan hours; a request for "any time after Isha"; confirmation given ambiguously.

## 8. Cost drivers

Turns needed to settle a slot, reminder message fees, no-show rate (the main value lever).

## 9. Data notes

Appointment data at a clinic can reveal health information, which is sensitive. Keep the agent to administration, minimise what is stored in conversation history, and take legal advice before handling patient data. For minors, deal with the guardian.

# سيناريوهات توضيحية · Illustrative scenarios

<div dir="rtl">

> **تنبيه:** المنشآت والأشخاص والأرقام في هذه الصفحة **مُتخيَّلة** لأغراض تعليمية. ليست دراسات حالة حقيقية ولا أدلة سوقية.

</div>

> **Notice.** The businesses, people and numbers on this page are **invented** for teaching. They are not real case studies and not market evidence. All figures are assumptions chosen to make the reasoning visible.

---

## Scenario 1: A dental clinic and missed appointments · عيادة أسنان والمواعيد الفائتة

**Status:** Illustrative · Sector: healthcare administration · Related template: [Booking assistant](../05-agentic-ai-lab/agent-templates/02-booking-assistant.md)

**The problem.** A three-chair clinic takes bookings by phone and WhatsApp. The receptionist cannot answer during busy hours, and a noticeable share of patients do not show up. Each missed slot is lost revenue.

**The workflow before.** Patient messages; receptionist replies when free; checks a paper diary; confirms; no reminders.

**The agent.** A single booking assistant on WhatsApp connected to the clinic's calendar. It offers real slots, books after explicit confirmation, sends a reminder the day before and handles rescheduling.

**Oversight.** Booking and rescheduling are autonomous. Late cancellations and fee questions go to the receptionist. Any question about symptoms or treatment is handed to staff: the agent does administration only.

**Economics (assumed).** Suppose the agent resolves 85% of booking conversations, at a cost per resolved booking of about SAR 1.30 using the [calculator's](../04-entrepreneur-toolkit/06-unit-economics.md) example inputs. The clinic would pay per attended appointment, because that is the outcome it values.

**What could go wrong.** Misreading relative dates in dialect; double-booking if the calendar integration lags; appointment data revealing health information.

**Teaching points.**
1. Price on the outcome the customer cares about (attended appointments), not on messages sent.
2. The value lever is the no-show rate, which the founder must measure before and after.
3. Health-adjacent data changes the compliance work even when the agent only does scheduling.

**Questions for learners.** How would you measure the baseline no-show rate in two weeks? What is the smallest pilot the clinic owner would say yes to?

---

## Scenario 2: An accounting office at month end · مكتب محاسبة في نهاية الشهر

**Status:** Illustrative · Sector: accounting and compliance · Related template: [Invoice reconciliation](../05-agentic-ai-lab/agent-templates/04-invoice-reconciliation.md)

**The problem.** A small office keeps the books for several dozen SME clients. Every month, juniors spend days matching supplier invoices to bank lines and chasing missing documents. Seniors review late and under pressure.

**The workflow before.** Clients send photos and PDFs by WhatsApp and email; juniors key them in; match by eye; list queries in a spreadsheet; chase clients by phone.

**The agent.** A workflow with model steps: extract fields from Arabic and bilingual invoices, validate and match **by rule**, and produce an exception report. An optional step drafts the WhatsApp message requesting a missing document for a junior to send.

**Oversight.** Extraction, matching and draft entries are autonomous. Posting to the ledger and any VAT judgement need the accountant's approval. Submitting to the tax authority and anything touching payments are forbidden to the agent.

**Economics (assumed).** The founder would charge the office per document processed. Document reading dominates cost, so scanned multi-page invoices cost several times more than clean single-page PDFs: price tiers should reflect that.

**What could go wrong.** Poor scans; supplier names spelled differently in Arabic and English; a language model asked to do arithmetic; one client's data visible in another's workspace.

**Teaching points.**
1. Not everything should be an agent. Rules do the matching; the model reads and explains.
2. The buyer is the office owner, the user is the junior, and the person whose trust decides adoption is the senior reviewer.
3. A domain expert co-founder (an accountant) is the moat: they know the exceptions.

**Questions for learners.** Which exception types would you support in version one, and which would you leave to people? How would you prove extraction accuracy to a sceptical senior accountant?

---

## Scenario 3: A tour operator in peak season · منظّم رحلات في موسم الذروة

**Status:** Illustrative · Sector: tourism · Related templates: [WhatsApp customer service](../05-agentic-ai-lab/agent-templates/01-whatsapp-customer-service.md), [Lead qualification](../05-agentic-ai-lab/agent-templates/03-lead-qualification.md)

**The problem.** A domestic tour operator receives enquiries in Arabic, English and other languages. In peak season, response time stretches to many hours and enquiries go cold. Most questions repeat: dates, prices, what is included, pickup points.

**The workflow before.** Two staff answer every message by hand, copy details into a spreadsheet and send payment links.

**The agent.** One agent that answers from the approved trip catalogue in the customer's language, qualifies the enquiry (dates, group size, budget range) and hands ready customers to staff with a summary. Staff send the payment link.

**Oversight.** Answering and qualifying are autonomous. Custom itineraries, group discounts and any price not in the catalogue need approval. Taking payment, changing a confirmed booking and giving official or religious guidance are forbidden to the agent.

**Economics (assumed).** Volume is seasonal, so a pure per-conversation price gives the founder a volatile income. A seasonal subscription with a usage cap, plus a fee per booked trip, shares the upside with the customer.

**What could go wrong.** The agent inventing availability; mistranslating an inclusion; a customer relying on the agent for information that should come from an official source.

**Teaching points.**
1. Start with one agent. Qualification and answering do not need two.
2. Seasonality shapes the pricing model as much as cost does.
3. Multilingual quality must be tested per language, by a native reader.

**Questions for learners.** What would make this more than a thin wrapper over a model? What does the operator own that you could help them turn into an advantage?

---

<div dir="rtl">

## سيناريوهان مشتقان من حالة حقيقية

السيناريوهان التاليان صياغة تعليمية مبسطة مستوحاة من [حالة Tamimi Markets](saudi/tamimi-markets-askbaba.md). الشخصيات والتفاصيل اليومية **متخيَّلة**، وليست وصفاً لما جرى في الشركة.

### السيناريو 4: مدير المتجر الذي ينتظر تقريراً

**الحالة:** توضيحي · القطاع: تجزئة غذائية

**الوضع.** مدير فرع في سلسلة بقالة يريد أن يعرف أداء فرعه أمس وأي الأصناف توشك على النفاد. يرسل طلباً إلى فريق التحليل وينتظر. حين تصل الإجابة يكون قرار الطلبية قد اتُّخذ بالحدس.

**أسئلة للمتعلم.**
1. هل هذا سير عمل متكرر؟ كم مرة يحدث في الأسبوع، ولكم مديراً؟
2. ما كلفة الانتظار؟ فرّق بين كلفة وقت المحلل وكلفة القرار المتأخر.
3. هل يكفي محادث يجيب من تقرير جاهز، أم نحتاج وكيلاً يستعلم من مستودع البيانات مباشرة؟ ما الذي يحسم؟
4. ما أول سؤال تطرحه على المدير لتعرف ما يفعله فعلاً أثناء الانتظار؟

### السيناريو 5: أمر الشراء اليومي الذي يُراجَع يدوياً

**الحالة:** توضيحي · القطاع: تجزئة غذائية

**الوضع.** تُنشأ كل يوم أوامر شراء للطازج وغير الطازج عبر نظام قائم. مشترٍ يراجع الكميات بالعين قبل الإرسال. الأخطاء تُكتشف بعد وصول البضاعة.

**أسئلة للمتعلم.**
1. أين القيد الحقيقي: إنشاء الأمر، أم التحقق منه، أم اكتشاف الخطأ بعد التنفيذ؟
2. صمّم وكيل تحقق يقارن الأمر بالبيانات التاريخية ويشرح سبب ملاحظته. ما الذي يبقى للمشتري؟
3. حدّد سقفاً: فوق أي قيمة أو انحراف لا يُرسَل الأمر دون موافقة بشرية؟
4. كيف تقيس نجاح الوكيل في شهر واحد دون انتظار نتائج سنة؟

</div>

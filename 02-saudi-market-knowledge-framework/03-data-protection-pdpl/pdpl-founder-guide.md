# دليل المؤسس لنظام حماية البيانات الشخصية
# PDPL: a founder's guide for agentic products

Last reviewed: 18 November 2026 · Educational, not legal advice · Not yet lawyer-reviewed

النسخة العربية: [pdpl-founder-guide.ar.md](pdpl-founder-guide.ar.md)

<div dir="rtl">

## الخلاصة في ستة أسطر

1. إذا كان وكيلك يعالج بيانات تخص أفراداً في المملكة (اسم، رقم جوال، محادثة، عنوان)، فأنت خاضع للنظام.
2. اجمع أقل قدر ممكن من البيانات، ولغرض محدد وواضح، وأخبر صاحبها بذلك.
3. اعرف أين تذهب البيانات: كل مزوّد نموذج أو أداة هو «جهة معالجة» عليك أن تتأكد من التزامها.
4. نقل البيانات إلى خارج المملكة له ضوابط خاصة. اعرف أين يعالج كل مزوّد بياناتك.
5. سجلات المحادثات وذاكرة الوكيل والمتجهات (embeddings) بيانات شخصية إذا أمكن ربطها بفرد.
6. جهّز خطة للتعامل مع تسرب البيانات قبل أن تحتاجها.

</div>

---

## 1. Does it apply to you?

The Personal Data Protection Law applies to processing of personal data about individuals that takes place in the Kingdom, and to processing of data about individuals residing in the Kingdom by entities outside it. SDAIA is the competent authority. The law was issued by Royal Decree M/19 of 9/2/1443H and amended by Royal Decree M/148 of 5/9/1444H ([SOURCES.md](../../SOURCES.md), A49). It has been enforceable since September 2024, after a one-year transition from its effective date in September 2023.

If your agent reads a customer's name, phone number, message, address, order, booking or ID, you are processing personal data.

**Roles.** If you decide why and how the data is processed, you are the **controller**. If you process data on behalf of a business customer, that customer is usually the controller and you are a **processor**, with obligations set by contract and by the law. Many agentic startups are both: controller for their own users, processor for their clients' customers.

## 2. Why agents raise the stakes

| Agent feature | PDPL question it raises |
|---|---|
| Conversation history | How long is it kept, and can it be deleted on request? |
| Long-term memory | Does the agent remember things about a person that they did not expect it to keep? |
| Vector stores and embeddings | Can stored fragments be linked back to a person? Are they deleted when the source is? |
| Tool calls to third parties | Which providers receive personal data, and where do they process it? |
| Logs and traces for debugging | Do they contain full messages with personal data? Who can read them? |
| Model providers | Is customer data used to train models? Can that be switched off by contract? |
| Autonomous actions | Was the person told that an automated system is acting on their data? |

## 3. Eight things to do

**1. Map the data.** For each step of the workflow, list what personal data enters, where it is stored, who receives it and when it is deleted. Use the [self-assessment](../compliance-toolkit/pdpl-self-assessment.md).

**2. Have a lawful basis.** Know why you are allowed to process each category: typically the person's consent, performance of an agreement with them, or another basis the law recognises. Consent must be clear and withdrawable. Direct marketing has its own conditions.

**3. Tell people.** Publish a privacy notice in Arabic that says who you are, what you collect, why, who receives it, whether it leaves the Kingdom, how long you keep it and how to exercise rights. Tell users they are interacting with an automated agent.

**4. Minimise.** Collect only what the task needs. Mask or drop identifiers before sending text to a model where the task allows. Do not put personal data in prompts used for testing.

**5. Respect rights.** Individuals have rights that include being informed, accessing their data, obtaining a copy, correcting it and requesting its destruction. The Implementing Regulation gives you 30 days to answer a request, extendable by up to 30 more with notice and reasons (A50). Design the agent's storage so that you can find and delete one person's data, including memory and embeddings.

**6. Control your processors.** Every model API, automation platform, messaging provider and database is a processor or sub-processor. Sign terms that restrict their use of the data, and check each with the [provider assessment](../compliance-toolkit/third-party-provider-assessment.md).

**7. Handle transfers outside the Kingdom deliberately.** Sending personal data to a provider that processes it abroad is a transfer and is governed by dedicated regulations with conditions and safeguards. As reported, SDAIA has not yet published its list of countries with an adequate level of protection, so transfers rest on safeguards such as its standard contractual clauses (A51). Know the processing location of every provider. Options to reduce exposure: providers with in-Kingdom regions, self-hosting an open-weight model on infrastructure in the Kingdom, or removing personal data before the call.

**8. Prepare for incidents.** Keep access controls and logs. Have a short written plan for a data breach: who decides, how you contain it, how you assess harm, and how you notify. The implementing rules require notifying the competent authority within 72 hours of becoming aware of a breach that meets the stated criteria, and notifying affected individuals in defined cases.

## 4. Sensitive data

The law defines sensitive data as personal data about racial or ethnic origin; religious, intellectual or political belief; security and criminal data; biometric identifiers; genetic data; health data; and data indicating that one or both parents are unknown. This is the definition as amended in 2023 ([SOURCES.md](../../SOURCES.md), A41). Sensitive data attracts stricter conditions.

Credit data is no longer in that definition, but it is not ordinary either: the law gives it its own article (Article 24), with additional controls set by the regulations, including consent before it is collected or disclosed and notice to the individual when its disclosure is requested (A45). A minor's data is not a category of sensitive data in that definition. What the Implementing Regulation addresses is capacity: where a person fully or partially lacks legal capacity, the legal guardian consents and exercises rights on their behalf, and you must verify the guardianship. The text we read names no age (A50, B32).

If your opportunity involves any of these categories (clinics, lending, schools), take legal advice **before** building, and prefer designs where the agent handles administration without seeing the sensitive content.

## 5. Other obligations that may apply

Depending on your size and activity, obligations may include keeping records of processing activities, carrying out impact assessments for higher-risk processing, appointing a data protection officer and registering with the authority's platform. Check the current criteria on SDAIA's official channels.

## 6. Selling to business customers

Larger customers will send you a questionnaire. Be ready with:

- Data flow diagram and list of sub-processors with processing locations
- Your privacy notice and data processing terms
- Retention and deletion policy, including agent memory
- Confirmation of whether customer data is used for model training
- Breach response plan and contact
- Completed [human oversight matrix](../compliance-toolkit/human-oversight-matrix.md)

## 7. Design patterns that make compliance easier

| Pattern | Effect |
|---|---|
| Redact before the model | Replace names, phone numbers and IDs with placeholders; restore them after the model responds |
| Short retention by default | Delete raw conversations after a set period; keep only the structured outcome |
| Per-customer isolation | Separate storage and memory for each business customer |
| No training on customer data | Contractually and technically disabled |
| In-Kingdom processing option | A deployment choice you can offer buyers who require it |
| Deletion that reaches everywhere | One function removes a person from the database, memory, vector store and logs |

## A complete example, and what may change

[مثال تطبيقي: وكيل خدمة عملاء مرتبط بنظام CRM](worked-example-customer-service-agent.md) applies every step above to one agent, in Arabic.

SDAIA consulted from 6 October to 5 November 2026 on draft amendments to the Implementing Regulation. As reported by law firms, the draft would require personal data to be stored in the Kingdom (transfers staying possible under the law), would make the 72-hour notice to SDAIA apply to every breach whether or not harm is likely, and would widen the triggers for impact assessments. **It is a draft and binds no one today** (A52). Watch for the final text.

## Official sources

- SDAIA: sdaia.gov.sa (law, implementing regulation, transfer regulation, guidance)
- National Data Governance Platform: dgp.sdaia.gov.sa

Read the official Arabic text. This guide summarises; it does not replace it.

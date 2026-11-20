# المجال 12: الفرص والمشتريات الحكومية · Domain 12: Government opportunities and procurement

**Status:** First guide published · Last reviewed 19 November 2026 · Educational, not legal advice

**Guide · الدليل:** [البيع للجهات الحكومية: ما يقوله نص النظام لمنشأة صغيرة](selling-to-government.md) · Selling to government. Sources read and what remains unverified are stated at the top of the guide; it awaits a lawyer's review.

<div dir="rtl">

**السؤال:** كيف أبيع للجهات الحكومية والشركات الكبرى؟

**الخلاصة:** قدرتك على بناء منتج يعمل لا تؤهلك تلقائياً لتشغيله في بيئة حكومية. الأهلية للتوريد، والأمن السيبراني، وتصنيف البيانات، والشروط التعاقدية والقطاعية تُقيَّم كلٌّ على حدة. ابدأ بسؤال الجهة مبكراً عمّا تشترطه.

</div>

## The lesson

A working AI product does not by itself qualify for deployment in a government environment. Procurement eligibility, security, data handling, contractual terms and sector requirements are each assessed separately.

## Institutions and platforms

| Institution | Role | Verification |
|---|---|---|
| Etimad | Government tenders, supplier registration and procurement services | ✔ etimad.sa opened the Etimad portal on 20 November 2026 (A142). Services not read |
| Ministry of Finance | Procurement law and its regulations | ✔ its regulations page lists the law, the implementing regulation and the local content preference regulation (A129) |
| Local Content and Government Procurement Authority | Local content requirements and preferences | ✔ its regulations library carries the law, the implementing regulation and the preference regulation (A129) |
| Digital Government Authority | Digital government policies, standards and frameworks | ✔ site opened on 20 November 2026 (A142). Policies not read |
| NCA | The cybersecurity controls government entities work under | ✔ ECC-2:2024, CCC-2:2024 and DCC-1:2022 on NCA's site (A126) |
| National Center for Privatization & PPP | Privatisation and partnership opportunities | ✔ site opened on 20 November 2026 (A142). Opportunities not read |

## Instruments

| Instrument | Status | Verification |
|---|---|---|
| Government Tenders and Procurement Law and Implementing Regulations | Binding | ✔ Royal Decree M/128 of 13/11/1440H on the Bureau of Experts' site. ✔ the Ministry of Finance lists a **new** law and its implementing regulation next to the earlier one (A129; see also A98). Its decree number and effective date were not read: the tender documents say which text governs |
| Regulation on preference for local content, local SMEs and listed companies | Binding in public procurement | ✔ Council of Ministers Resolution 245 of 29/3/1441H (A129) |
| NCA Essential Cybersecurity Controls (ECC-2:2024) | Binding on entities in scope; reaches vendors by contract | ✔ version (A126). What a given entity asks of its vendors is in its tender documents |

## What a government buyer will ask an agentic startup

| Area | Typical questions | Your evidence |
|---|---|---|
| Eligibility | Registration, classification, financial standing, experience | Company documents; references |
| Data | What classification of data will the system touch? Where is it processed? | [Data-flow map](../compliance-toolkit/third-party-provider-assessment.md) |
| Security | Which controls do you meet? Who has access? | [Security assessment](../compliance-toolkit/agent-security-assessment.md) |
| Responsible AI | Disclosure, oversight, risk management | [Compliance dossier](../founder-compliance-checklist.md) |
| Hosting | Is hosting in the Kingdom required? | Deployment options |
| Continuity | What if the model provider changes or stops? | Fallback plan |
| Local content | What share of value is local? | Team and supplier breakdown |

Restricted or higher classifications of government data generally cannot be sent to public model services. Confirm the classification and the permitted environment with the entity before designing.

## Routes in

| Route | Fits when |
|---|---|
| Subcontract to an established supplier | You lack track record or classification |
| Proof of concept or pilot | The entity wants to test before tendering |
| Innovation programmes and challenges | The need is new and the entity is exploring |
| Direct tender | You meet eligibility and can carry the delivery risk |
| Enterprise first | Large companies have shorter cycles and build your references |

## Founder decisions

| Decision | Ask |
|---|---|
| Ready or not | Can I pass eligibility today, or should I partner? |
| Cash flow | Can I fund delivery through the payment cycle? |
| Architecture | Can I deploy inside the buyer's required environment? |
| Bid or no bid | Does this tender fit my capabilities? See the [tender summariser template](../../05-agentic-ai-lab/agent-templates/05-tender-summariser.md) |

## Guides wanted

- [ ] Becoming a government supplier: registration walkthrough
- [ ] How tenders work, from announcement to award
- [ ] Reading a tender document (كراسة الشروط والمواصفات)
- [ ] Technical and financial proposals for AI services
- [ ] Local content explained for software companies
- [ ] Proof of concept and pilot contracting with government
- [ ] Government data classification for vendors
- [ ] Enterprise sales for AI startups

People who have bid for or delivered government technology projects: a two-page account of what you wish you had known is very welcome.

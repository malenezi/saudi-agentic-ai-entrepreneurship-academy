# الإطار التعليمي · Learning framework

> **ملاحظة · Note.** المقرران 1 و2 لهما محتوى اليوم؛ المقرران 3 و4 مخططان أوليان، وما يرد هنا عنهما تصميم مقترح. · Courses 1 and 2 have content today; Courses 3 and 4 are outlines, and references to them here describe the proposed design.

<div dir="rtl">

## ملخص

يقوم التعلّم في الأكاديمية على ثلاث ركائز وأربعة مقررات ومسارين. كل مقرر ينتهي بمُخرَج تجاري يُقيَّم بالدليل، وليس باختبار نظري.

| الركيزة | المقررات | التحول المقصود |
|---|---|---|
| فكّر | 1 | من فكرة عامة إلى فرصة موثقة بأدلة من عملاء |
| ابنِ | 2 و3 | من فرصة إلى وكيل يعمل ومنتج له عميل |
| احكُم وتوسّع | 4 | من منتج إلى منشأة تعمل بحوكمة وقابلة للتمويل |

</div>

## Design decisions

**1. Two tracks, one pathway.** Every course has a **core track** that a non-technical founder can complete with low-code tools, and a **deep track** for technical founders who want code-level control and self-hosted Arabic models. Both tracks produce the same deliverable and are assessed against the same rubric. A founding team can split: one person on each track.

| | Core track (الأساسي) | Deep track (العميق) |
|---|---|---|
| Prerequisite | None | Basic Python |
| Agent building | Low-code orchestration such as n8n | Python with an orchestration framework such as LangGraph or CrewAI |
| Models | Hosted model APIs | Hosted APIs plus open-weight Arabic models run locally |
| Evaluation | Spreadsheet-based test set | Automated evaluation scripts |
| Typical learner | SME owner, domain expert, first-time founder | Developer, engineering student, technical co-founder |

**2. Deliverables, not exams.** Each course ends with an artefact a real business would recognise.

| Course | Deliverable | Evidence standard |
|---|---|---|
| 1 Opportunity | Opportunity thesis | At least five customer interviews with notes |
| 2 Build | Working agent | Passes its own evaluation set; failure log kept |
| 3 Launch | MVP with pricing and compliance readiness | At least one pilot user from a real business |
| 4 Scale and Govern | Governed operating architecture and investor pitch | Signed LOI or live usage metrics |

**3. Five teaching mechanisms borrowed from the best programmes and localised.**

| Mechanism | What learners do |
|---|---|
| Vertical workflow wedge | Shadow one real Saudi SME process and automate a single painful, repetitive workflow end to end. No horizontal "chat with your documents" projects |
| WhatsApp-first MVP | Deploy the agent where Saudi customers already are: WhatsApp or a live web endpoint |
| Cost per resolved task | Model inference cost against value delivered before choosing a price |
| Evaluate before you sell | Build a test set of real Arabic cases, including Saudi dialect, and pass it before any customer sees the agent |
| Buildathon and pilot Demo Day | Finish with a 48-hour build sprint and a Demo Day judged on customer evidence |

**4. Mixed teams by design.** Cohorts deliberately pair engineers with domain practitioners (clinics, logistics, accounting, legal, tourism, retail). The domain expert owns the problem; the engineer owns the build.

**5. Open and versioned.** All material lives in this repository, is version-controlled and can be reused under CC BY 4.0. Regulatory and market content carries a review date.

## Weekly rhythm (suggested for cohort delivery)

| Day | Activity | Time |
|---|---|---|
| 1 | Concept session (recorded, Arabic) | 90 min |
| 2 to 4 | Guided build using a template from the toolkit | 3 to 4 hours self-paced |
| 5 | Field task: customer conversation or workflow observation | 1 to 2 hours |
| 6 | Peer review in small groups | 60 min |
| 7 | Submit the week's increment to the cohort showcase | |

Self-paced learners follow the same sequence without the peer review.

## Assessment rubric (applies to every deliverable)

| Criterion | Weight | Question the reviewer asks |
|---|---|---|
| Customer evidence | 30% | Is there proof a real Saudi customer has this problem and wants this solution? |
| Working product | 25% | Does it do the job, measured against its own test set? |
| Economics | 20% | Does each completed task earn more than it costs? |
| Governance | 15% | Are data handling, approvals and limits defined and enforced? |
| Communication | 10% | Can the founder explain it clearly in Arabic to a non-technical buyer? |

## Pathways and companion tools

[Learning pathways](learning-pathways.md) shows the route for each kind of learner, combining the four courses with two optional companion repositories: [Riyada](https://github.com/malenezi/riyada) for founder skills and context files, and [Bayan](https://github.com/malenezi/bayan) for Arabic interface craft. The courses do not depend on either.

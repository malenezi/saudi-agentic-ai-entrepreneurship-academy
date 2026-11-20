# دليل المدرب · Instructor guide

For anyone running Course 4 as a cohort. Self-paced learners can skip this file. Nothing here has been piloted yet; tell us what happened when you run it.

## Before the first session

- Every learner arrives with the Course 3 launch pack or an equivalent: an agent in real use, a log, a measured cost per resolved task, a data map and at least one pilot offer sent. A learner with no real user goes back to Course 3, Modules 3.1 and 3.6.
- **The KPI sheet needs four weeks of data.** Ask learners to start the weekly sheet four weeks before the first session, from the Course 3 log. A learner who starts on day one will submit a two-week sheet, labelled as such.
- **Graduation evidence takes calendar time.** A signed LOI, a paying customer or sustained usage cannot be produced in the last week. Ask in the first session what each learner has and what they expect to have by Demo Day.
- The instructor is not a lawyer, a security assessor or an investment adviser, and should say so in the first session. Modules 4.3 and 4.4 teach what to write down and what to ask; Module 4.5 teaches how to choose a path, not which investor to take. If a security practitioner or an investor can give an hour, put it after Module 4.4 and after Module 4.5.
- Red teaming in Module 4.4 runs **only against the learner's own agent, in a test environment, with test data**. Say it before the exercise and again during it.
- Open the pages listed at the end of this file in the week before delivery.

## Delivery schedules (16 contact hours)

| Format | Session | Modules | Between sessions |
|---|---|---|---|
| **Four half-days** | S1 (4h) | 4.1 (3h); 4.2 units and the sheet (1h) | Agent register and architecture. First reading of four weeks of log |
| | S2 (4h) | 4.2 sampling, limits, change control (2h); 4.3 register started (2h) | KPI sheet and change log. Six risks in the product's own words |
| | S3 (4h) | 4.3 register reviewed in pairs (1h); 4.4 (2h); 4.5 paths (1h) | Security assessment. Stop-switch drill. Injection set (deep track) |
| | S4 (4h) | 4.5 milestone, roadmap, data room (2h); 4.6 pitch build and dry run (2h) | Path memo and roadmap. Rehearse twice. Submit the pack |
| **Eight evenings** | 8 × 2h | Same order; 4.1, 4.2, 4.3 and 4.5 take one and a half evenings each | Same work between sessions |
| **Demo Day** | Half a day, outside the 16 hours | Ten minutes a team, then questions | Buildathon the weekend before, if you run one |

## Time inside each module

Suggested split, in minutes.

| Module | Hours | Concepts | Build or apply | Review or present |
|---|---|---|---|---|
| 4.1 The agent-operated company | 3 | 45 | 105 | 30 |
| 4.2 Monitoring quality and cost | 3 | 60 | 90 | 30 |
| 4.3 Governance and risk | 3 | 45 | 90 | 45 |
| 4.4 Security for agentic systems | 2 | 40 | 60 | 20 |
| 4.5 Growth paths and funding | 3 | 60 | 90 | 30 |
| 4.6 Pitch and Demo Day | 2 | 20 | 40 | 60 |

## Materials checklist

| Item | Where |
|---|---|
| Six lessons | [`lessons/`](lessons/) |
| Worked example (invented founder, stores and data) | [`examples/worked-example-scale-pack.md`](examples/worked-example-scale-pack.md) |
| Operating architecture, weekly KPI sheet and change log, scaling roadmap, Demo Day run sheet, scale pack checklist | [`templates/`](templates/) |
| AI risk register, agent security assessment, human oversight matrix | [Compliance toolkit](../../02-saudi-market-knowledge-framework/compliance-toolkit/ai-risk-register.md) |
| Unit economics calculator, pitch deck outline | [Founder Toolkit](../../04-entrepreneur-toolkit/README.md) |
| Funding directory and startup ecosystem | [Domain 06](../../02-saudi-market-knowledge-framework/06-funding-investment/funding-and-investment.md) |
| Glossary and rubrics | [`glossary.md`](glossary.md), [`rubrics.md`](rubrics.md) |
| Six formative quizzes with answer keys (60 questions) | [`quizzes/`](quizzes/README.md) |

Slide decks do not exist yet.

## Notes by module

- **4.1.** Learners draw agents first and people last. Reverse it: start from the list of consequential decisions and write a name beside each, then draw. Challenge every new agent with one question: would a scheduled job or a form do this? A team of one founder is normal; the founder's name appearing on every arrow is the finding, and the roadmap in 4.5 has to answer it.
- **4.2.** Run it on the learner's own log. Have every rate written with its counts, and ask what the worst week was before looking at the average. Expect a sheet with no bad week; ask which week was removed. The change log is the part learners skip: ask each one what changed in the model, the instructions or the tools in the last month, and who decided.
- **4.3.** Keep the group out of legal argument. Read two registers aloud without naming the product; if the room cannot tell what the product does, the rows came from the template. "Existing" means a reviewer could be shown the control today.
- **4.4.** Have each learner press the stop switch in the room and time it. In the permissions review, the exercise is to remove one permission, not to justify all of them. Deep track: the injection set must include content the agent reads, not only what the user types.
- **4.5.** Do not recommend an investor, a programme or a valuation. The exercise is the price of the next milestone, computed from the learner's own table. A learner who chooses revenue over raising has made a full decision; do not treat it as the modest option.
- **4.6.** Rehearse with a timer and one unprepared case written by someone else. Stop any pitch at the first number with no source and ask for it. The limits slide is graded: a pitch that does not say what the agent gets wrong loses marks under gate 5.

## Buildathon (optional, 48 hours)

- The problem comes from a real Saudi SME that has agreed in writing to describe it and to judge the result. No real personal data leaves that business; teams work on synthetic or masked data.
- Teams mix engineers and domain experts. A team with no one who has done the job is rebalanced.
- Shipped means: an agent that runs, a test set of at least twenty cases written before building, a measured success rate with its counts, and a stated list of what the agent does not do.
- Judged with the Academy rubric, customer evidence first: the business owner's verdict counts for more than the demo.

## What a facilitator should not do

- Give legal, security or investment conclusions, or approve a learner's compliance position.
- Introduce a learner to an investor as an endorsement. An introduction is an introduction.
- Accept invented customers, usage or references "to complete the pack". Gate 1 has no exceptions.
- Allow injection or red-team tests against any system the learner does not own.
- Let a staged demo be presented as live.

## Before each cohort

Re-check, and update the lessons or tell us:

| What | Where it is used | Source entry |
|---|---|---|
| Whether NCA's AI Cybersecurity Guidelines left draft status | 4.3, 4.4 | A5 |
| The current editions of the two OWASP lists | 4.4 | A121, A122 |
| The current version of NCA's Essential Cybersecurity Controls and of the controls for private entities outside critical infrastructure | 4.4 | A124, A10 |
| The terms of SDAIA's AI service provider accreditation | 4.3 | A112 |
| Model provider version and deprecation policies used in learners' products | 4.2 | the provider's own page |
| Funding programmes, their terms and whether they are open | 4.5 | the funding directory and its entries |
| The latest annual venture figures | 4.5 | A2, A123 |

## Reading

Verified and used in the lessons: the entries cited in each lesson, in [SOURCES.md](../../SOURCES.md) (A5, A10, A12 to A14, A46, A81, A84, A87 to A91, A112, A113, A120 to A122, A124).

Named in the owner's drafts and **not opened in this review** (C49): the academic papers and vendor articles in the two reference lists, and the books named there. Nothing in the lessons is attributed to them.

## Feedback we need

How many learners reached graduation evidence, and of which kind; how many KPI sheets had four real weeks; which parts of Modules 4.3 and 4.4 needed a specialist in the room; whether sixteen hours were enough; what the judges asked on Demo Day that the pack did not answer. Open an issue or a pull request: [CONTRIBUTING.md](../../CONTRIBUTING.md).

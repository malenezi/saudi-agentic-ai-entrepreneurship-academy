# دليل المدرب للبرنامج · Programme trainer guide

One page for a trainer or an organisation that wants to run the four courses without help from the authors. Each course has its own instructor guide; this file covers what is common to all four. **Nothing here has been piloted with a cohort.** Tell us what happened when you run it.

<div dir="rtl">

## الخلاصة بالعربية

- **أربعة مقررات، 76 ساعة تدريبية، 28 وحدة.** لكل وحدة درس وعرض واختبار قصير بإجاباته ونشاط له قالب وحل نموذجي. ولكل مقرر مسرد وسلّم تقدير ودليل مدرب ومثال محلول.
- **اللغة:** الدروس والعروض والاختبارات بالعربية مع المصطلح الإنجليزي عند أول ورود. أدلة المدربين بالإنجليزية مع ملاحظات عربية.
- **المساران:** أساسي منخفض الكود وعميق برمجي. المخرج واحد والسلّم واحد.
- **التقييم:** مخرج تجاري واحد لكل مقرر، يمر ببوابات تحقق ثم يُقدَّر بسلّم من أربعة مستويات، و[معيار إتمام واحد](assessment-standard.md) للمقررات الأربعة. الاختبارات القصيرة تكوينية بلا درجات.
- **كل مثال في المقررات مختلق وموسوم بذلك.** لا يعالج متعلم بيانات شخصية حقيقية قبل اتفاق مكتوب مع المنشأة.
- **ما ليس جاهزاً:** لم يُجرَّب أي مقرر مع فوج، ولا مراجعة قانونية أو ضريبية أو أمنية للوحدات التي تمس الأنظمة. التفصيل في [تقرير ضمان الجودة](QA-REPORT.md).

</div>

## 1. The programme at a glance

| | Course 1: Opportunity | Course 2: Build | Course 3: Launch | Course 4: Scale and Govern |
|---|---|---|---|---|
| Question | Which problem? | Does it work? | Will they pay? | Can it grow safely? |
| Hours | 16 | 24 | 20 | 16 |
| Level | Beginner | Beginner to intermediate | Intermediate | Advanced |
| Modules | 7 | 8 | 7 | 6 |
| Entry requirement | None | Course 1 or a documented opportunity | A working, evaluated agent | An MVP with a real user |
| Deliverable | Opportunity thesis | Working, evaluated agent (six parts) | Launch pack (five parts) | Scale pack (six parts) |
| Validation gates | 5 | 4 | 5 | 5 |
| Rubric weights | 35/25/15/15/10 | 30/25/20/15/10 | 30/25/20/15/10 | 30/20/20/15/15 |
| First criterion | Customer evidence | Does the job | Real usage | Customer evidence |
| Syllabus | [syllabus](01-opportunity/syllabus.md) | [syllabus](02-build/syllabus.md) | [syllabus](03-launch/syllabus.md) | [syllabus](04-scale-and-govern/syllabus.md) |
| Instructor guide | [guide](01-opportunity/instructor-guide.md) | [guide](02-build/instructor-guide.md) | [guide](03-launch/instructor-guide.md) | [guide](04-scale-and-govern/instructor-guide.md) |

Each course has five learning outcomes, stated in its syllabus, and every lesson names the outcome it serves. The courses can be run one at a time; each is complete on its own if the learner meets the entry requirement.

## 2. Entry checks

Ask these before enrolling a learner. A "no" sends the learner to the course before, or to the named module.

| Course | The learner can show | If not |
|---|---|---|
| 1 | Nothing. Basic computer use and written Arabic | |
| 2 | A two-page thesis or equivalent: a named customer role, a mapped workflow, five interviews, a first cost estimate | Course 1, Modules 1.4 to 1.6 |
| 3 | An agent that runs, a test set of 30 or more cases with a measured success rate, an oversight matrix, a stop switch that was tested | Course 2, Modules 2.5 and 2.6 |
| 4 | An agent in real use by a real business, a log, a measured cost per resolved task, a data map, one pilot offer sent | Course 3, Modules 3.1 and 3.6 |

## 3. What every module contains

| Piece | Where | Use |
|---|---|---|
| Lesson | `lessons/` | The content. Header line gives duration, outcome and output. Sections: the idea, numbered content, activity, track differences, quick review, common mistakes, quiz link, navigation |
| Slide deck with speaker notes | `slides/` | One HTML file per module, opens in a browser. Courses 1 and 2 are hand-designed; Courses 3 and 4 are generated from the lessons and plainer |
| Quiz with answer key | `quizzes/` | Ten questions (twelve in 1.4), formative, key and explanations in a collapsed section |
| Activity template | `templates/`, the [Founder Toolkit](../04-entrepreneur-toolkit/README.md), the [compliance toolkit](../02-saudi-market-knowledge-framework/compliance-toolkit/pdpl-self-assessment.md) | What the learner fills in |
| Sample solution | `examples/` | A worked version on invented data: see section 6 |
| Checkpoint | `rubrics.md` | What the trainer or a peer looks for in the module output, ungraded |

Optional practice beyond the modules: seventeen [lab exercises](../05-agentic-ai-lab/exercises/README.md) with checking scripts, and [case studies](../06-case-studies/README.md) from public sources.

## 4. One assessment standard

The four courses use the same structure. Use it as written or adapt it, and say which.

1. **One business deliverable per course**, graded as one piece of work. Module outputs are checkpoints, reviewed and not graded.
2. **Validation gates first.** A deliverable that fails any gate is returned ungraded, with the gate named. Gates are about honesty and safety: real evidence, no hidden failure, no unapproved consequential action.
3. **Four levels per criterion**: 4 proficient, 3 good, 2 developing, 1 incomplete. The descriptors are in each course's `rubrics.md`. Customer evidence or real usage carries the largest weight in every course.
4. **Completion standard, version 1.0** ([assessment-standard.md](assessment-standard.md)): all gates passed, no criterion at level 1, the lead criterion at level 3 or above, and a weighted score of 2.7 or more out of 4. Distinction: no criterion below 3 and 3.5 or more. Course 4 adds its graduation condition. The standard defines the evidence to be seen, remediation and what a delivering organisation may certify; it has not been tested with a cohort.
5. **Quizzes are formative.** Eight of ten means the learner is ready for the activity. A lower score sends the learner back to the lesson, not out of the course.
6. **One resubmission** after written feedback is normal. The second submission is graded as if it were the first.
7. **Calibrate before grading alone**: two assessors grade two submissions together. Each `rubrics.md` names the criterion that drifts most.
8. **Assessors do not rule on law, tax, security or investment.** They check that the question was asked and that what is unsettled is written down with an owner and a date.

For a 15-week university delivery with grade weights, forms and a peer-evaluation sheet, see the [instructor kit](../01-academy/instructor-kit/README.md); it was designed before Courses 3 and 4 were built and covers mainly Courses 1 and 2.

## 5. The running example

One invented business runs through Courses 2, 3 and 4, so a trainer can teach all three from one story: an online store's order-enquiry agent. Course 2 designs and evaluates it ([example](02-build/examples/worked-example-order-enquiry-agent.md)); Course 3 deploys it for two weeks, prices it and takes it to market ([example](03-launch/examples/worked-example-launch-pack.md)); Course 4 operates it for four weeks across five stores, including one bad week ([example](04-scale-and-govern/examples/worked-example-scale-pack.md)). Course 1 has its own [model thesis](01-opportunity/examples/model-thesis.md). **Every business, person and figure in these examples is invented and labelled.** Figures are computed with the Academy's [calculator](../04-entrepreneur-toolkit/cost_per_resolved_task.py) and can be reproduced.

## 6. Where the sample solution for each activity is

| Course | Modules | Sample solution |
|---|---|---|
| 1 | 1.1 | Answer key inside the lesson |
| 1 | 1.2, 1.3 | [Activity sample solutions](01-opportunity/examples/activity-sample-solutions.md) |
| 1 | 1.4, 1.6, 1.7 | [Model thesis](01-opportunity/examples/model-thesis.md), sections 2, 5 to 6, and the whole |
| 1 | 1.5 | Six [practice interview records](01-opportunity/practice-interviews/README.md) and a synthesis exercise |
| 2 | 2.1 to 2.8 | [Worked example](02-build/examples/worked-example-order-enquiry-agent.md), one section per module |
| 3 | 3.1 to 3.7 | [Worked example](03-launch/examples/worked-example-launch-pack.md), by part of the launch pack |
| 4 | 4.1 to 4.6 | [Worked example](04-scale-and-govern/examples/worked-example-scale-pack.md), by part of the scale pack |

A sample solution shows the shape and standard of a good answer. A learner who copies it fails the first validation gate, because the evidence is not theirs.

## 7. Preparing to deliver

| When | Do |
|---|---|
| Four weeks before | Read the syllabus, the instructor guide and the worked example of the course. Confirm each learner meets the entry check. For Courses 1, 3 and 4, start securing access to real businesses: this is the scarce resource |
| Two weeks before | Work every activity yourself once, on the templates. Open each deck in a browser and read the speaker notes (`N`). Choose a delivery schedule from the instructor guide |
| One week before | Open the official pages listed under "Before each cohort" in the instructor guide; rules, fees and editions change. Read the course's `not-adopted.md` so you know which popular claims the course deliberately leaves out |
| First session | Say what you are not: not a lawyer, tax adviser, security assessor or investment adviser. State the data rule: no real personal data before a written agreement, and none in a tool that was not assessed |
| Each session | Quiz in the first ten minutes; discuss only the question most learners missed. Concepts short, activity long: every instructor guide gives a split in minutes |
| After | Grade with gates, then rubric, calibrated. Send what went wrong in the materials as an issue or a pull request |

## 8. Fitting the room

- **Language.** Teach in Arabic. English terms are given once so learners can search and read documentation; do not require English fluency.
- **Two tracks in one room.** The core track needs no programming. Pair core-track and deep-track learners for activities; grade both with the same rubric.
- **Saudi context.** Examples are Saudi businesses, channels and rules. Regulatory content points to the [Saudi Market Knowledge Framework](../02-saudi-market-knowledge-framework/README.md) and the [source register](../SOURCES.md); where an official page differs from a lesson, the page is right.
- **Low bandwidth and small budgets.** Decks are single HTML files that run offline; lessons and templates are Markdown and print cleanly. No paid software is needed to read or teach the materials. Building an agent in Course 2 needs access to a model, and its cost depends on the provider the learner chooses.
- **Learners without a business.** Course 1 teaches how to find a host business; Course 3 needs one for two weeks. Do not replace a real business with a friend or an invented one.
- **Reuse.** Content is CC BY 4.0. Adapt hours, examples and sector focus; keep the validation gates and the labels on invented data.

## 9. Readiness

The course-by-course assessment, what was fixed in the audit of 20 November 2026 and what remains open are in the [QA report](QA-REPORT.md).

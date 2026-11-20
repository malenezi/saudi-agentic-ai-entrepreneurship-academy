# معيار الإتمام · Assessment and completion standard

**Version 1.0, 20 November 2026.** One standard for the four courses. It replaces the provisional default proposed in the QA audit of the same day. It has **not been tested with a cohort**; section 9 says what the first cohort must check.

<div dir="rtl">

## الخلاصة بالعربية

يُتمّ المتعلم المقرر حين تتحقق أربعة شروط معاً في مُخرَجه:

1. **كل بوابات التحقق «نعم».** البوابات عن الصدق والسلامة، ولا يعوّضها شيء.
2. **لا معيار في المستوى 1.**
3. **المعيار الأول (الأعلى وزناً) في المستوى 3 أو أعلى.** هو دليل العميل أو الاستخدام الحقيقي أو أن الوكيل يؤدي العمل.
4. **المتوسط الموزون 2.7 من 4 أو أعلى**، أي أن ما لا يزيد على نحو 30% من الوزن في مستوى «نامٍ».

**إتمام بتميّز:** لا معيار دون المستوى 3، والمتوسط 3.5 أو أعلى. المقرر 4 يضيف شرط التخرج: خطاب نوايا موقّع، أو عميل يدفع، أو استخدام حقيقي مستمر.

من لم يُتمّ يستلم ملاحظات مكتوبة تسمّي المعايير، وله إعادة تسليم واحدة. الاختبارات القصيرة تكوينية ولا تدخل في القرار. **الأكاديمية لا تصدر شهادات**؛ الجهة التي تقدّم المقرر قد تصدر إفادة بشروط القسم 8.

</div>

## 1. Why the provisional default was changed

The audit proposed: all gates passed, no criterion at level 1, weighted average of 2.5 of 4. Three problems:

| Problem | Example | Change |
|---|---|---|
| A purely compensatory average lets minor criteria buy the one that matters | Course 1 thesis with customer evidence at level 2 and everything else at level 4 scores 3.3 and would pass, with opinions in place of evidence | **Conjunctive rule on the lead criterion:** it must reach level 3 |
| 2.5 sits halfway between "developing" and "good", so work that is mostly developing passes | Levels 3, 3, 2, 2, 2 in Course 3 scores 2.55 | **Threshold raised to 2.7:** with the lead criterion at 3 and no level 4, at most about 30% of the weight may be at level 2 |
| No evidence, remediation or eligibility rules, and nothing above a pass | | Sections 4 to 8, and a distinction band |

The standard is criterion-referenced: a learner is judged against written descriptors, never against other learners, and there is no quota of passes. Level 3 ("good") is the described standard of adequate work; level 2 ("developing") names a weakness to fix. The numbers 2.7 and 3.5 are judgements made from the descriptors, not results from learner data.

## 2. The standard

A deliverable is **complete** when all four hold:

1. **Every validation gate is "yes".** A deliverable that fails a gate is returned ungraded with the gate named.
2. **No criterion is at level 1.**
3. **The lead criterion is at level 3 or 4.** The lead criterion is the first and heaviest in each rubric.
4. **The weighted score is 2.7 or more out of 4.** Weighted score = sum of (level × weight) ÷ 100.

**Distinction:** no criterion below level 3, and a weighted score of 3.5 or more.

**Course 4** adds its graduation condition: a signed LOI from a Saudi business, a paying customer, or sustained real usage, evidenced.

| Course | Deliverable | Gates | Lead criterion (weight) | Other criteria (weights) |
|---|---|---|---|---|
| 1 | Opportunity thesis | 5 | Customer evidence (35) | Workflow clarity (25), Agent fit (15), Economics (15), Writing (10) |
| 2 | Working, evaluated agent | 4 | Does the job (30) | Evaluation quality (25), Guardrails (20), Improvement (15), Arabic quality (10) |
| 3 | Launch pack | 5 | Real usage (30) | Economics (25), Compliance readiness (20), Go-to-market (15), Defensibility (10) |
| 4 | Scale pack | 5 | Customer evidence (30) | Operating design (20), Governance and security (20), Economics at scale (15), Pitch (15) |

Level names are the same in the four rubrics: 4 متقن (proficient), 3 جيد (good), 2 نامٍ (developing), 1 غير مكتمل (incomplete). Descriptors are in each course's `rubrics.md`.

## 3. Scoring

```bash
python3 tools/score_submission.py 3 --levels 3 3 2 3 2 --gates 5
# Weighted score: 2.70 of 4 (68%)   Decision: COMPLETE
```

Levels are entered in rubric order. The script applies the rules above and names every reason for a "not yet complete". By hand: multiply each level by its weight, add, divide by 100.

Half levels are not used. When the evidence sits between two descriptors, the assessor gives the lower level and writes what would raise it.

## 4. Evidence the assessor must see

A claim in a deliverable is not evidence. The assessor opens the thing itself, with personal data masked.

| Course | Evidence |
|---|---|
| 1 | The thesis; the interview evidence pack (five or more interviews, with dates, roles and verbatim quotes); the workflow map pack from observation |
| 2 | The agent running on a test channel; the test set and one re-run of it by the assessor or a peer; the oversight matrix with each gate shown working; the failure log for two cycles; the demo video |
| 3 | The operating log of the two-week deployment; the written agreement with the business; the calculator inputs behind the price; the data map and open issues; the three pilot offers and the replies |
| 4 | The invoice, signed LOI or usage log behind the graduation evidence; four weeks of the KPI sheet traceable to a log; the risk register and security assessment; the roadmap; the pitch and live demo |

Course 1 alone also uses two field-pack rubrics (workflow map, interview pack). They are graded for cohort feedback with the component weights in its `rubrics.md`; **completion is decided on the thesis rubric**, and both packs must have been submitted, because they are the evidence for gates 1 and 3.

## 5. Process

1. **Gates first**, by one assessor. A failed gate ends the review.
2. **Levels**, criterion by criterion, each with one sentence of evidence.
3. **Second assessor** for cohorts, on at least one deliverable in five and on every borderline case (weighted score from 2.5 to 2.9, or a lead criterion argued between 2 and 3). A difference of one level is settled by discussion; a difference of two levels goes to a third reader.
4. **Calibration before grading alone:** two assessors grade two deliverables together.
5. **Written result** to the learner: the level and evidence sentence for each criterion, the decision, and for "not yet complete" exactly what would change it.
6. **Assessors do not rule on law, tax, security or investment.** They check that the question was asked and that what is unsettled is written with an owner and a date.

## 6. Remediation

| Situation | Rule |
|---|---|
| A gate failed because evidence is missing or thin | Returned ungraded. The learner gathers the evidence and submits; this does not use up the resubmission |
| A gate failed because evidence was invented or copied | No completion in this cohort. The learner may start the course again with a new deliverable |
| Not yet complete on levels | **One resubmission**, within four weeks for cohorts and at any time for self-paced learners. Only the criteria named in the feedback are regraded; other levels stand |
| Still not complete after resubmission | The learner repeats the modules the feedback names before a third review. The module checkpoints in each course's `rubrics.md` show which module produces which part of the deliverable |
| A real business was not available in time (Courses 3 and 4) | The deliverable is held, not failed. Completion waits for the evidence; nothing is simulated in its place |

A resubmitted deliverable can reach "complete" or "distinction" like any other.

## 7. What does not count

- **Quizzes** are formative: eight of ten means ready for the activity. They carry no weight.
- **Lab results in Course 2** are practice on the worked example. The graded project is the learner's own agent.
- **Attendance** is not completion. A cohort may require it for its own statement (section 8).
- **Self-assessment** with the checklists and the script is encouraged and is not a decision.

## 8. Certification eligibility

**The Academy issues no certificates** and accredits no provider. This section says what a delivering organisation may state, so that statements made in the Academy's name mean the same thing everywhere.

| Statement | Eligible when |
|---|---|
| **Statement of completion** for a course | The deliverable was assessed by a named assessor against this standard and found complete; the evidence of section 4 was seen |
| **Completion with distinction** | The same, at the distinction band |
| **Programme completion** | Four course completions, including Course 4's graduation evidence |
| **Statement of attendance** | The learner attended; no deliverable was assessed, or it is not yet complete. A common cohort rule is attendance at four-fifths of contact hours; set your own and state it |

Any statement must name the course, the contact hours, the date, the delivering organisation, the assessor, and "assessed against the SAAEA completion standard, version 1.0". It must not say or imply that the Academy, its author or any government body certified the learner or accredited the provider. Self-paced learners can score themselves and say so; a self-score is not a statement of completion.

## 9. What the first cohort must check

- The share of learners who complete at first submission and after resubmission, per course. A standard almost nobody or almost everybody meets needs review.
- Agreement between two assessors on the lead criterion.
- Whether learners blocked by the lead-criterion rule were blocked for want of skill or for want of access to a business. The second is a delivery problem, not an assessment result.
- Whether 2.7 separates deliverables an experienced practitioner would call usable from those they would not.

Report results in an issue; the standard's version number changes with any change to a rule.

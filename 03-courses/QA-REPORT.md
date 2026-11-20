# QA report: the four courses · تقرير ضمان الجودة

**Date:** 20 November 2026 · **Scope:** `03-courses/` and the files that describe it · **Method and limits:** section 1

<div dir="rtl">

## الخلاصة بالعربية

- **المقررات الأربعة مكتملة البنية الآن:** 28 وحدة، لكل منها درس وعرض واختبار قصير بإجاباته ونشاط بقالبه وحله النموذجي، ولكل مقرر مسرد وسلّم تقدير ودليل مدرب ومثال محلول.
- **أهم ما أُصلح:** عروض للمقررين 3 و4 (13 عرضاً مولَّداً من الدروس)، وتحديث ترقيم قائمة OWASP في المقرر 2 إلى إصدار 2026، وتوحيد مصطلحين وأسماء مستويات التقدير، وروابط تنقل في كل درس، وأقسام ناقصة في دليلَي مدرب المقررين 1 و2، ودليل مدرب للبرنامج كله، وحلول نموذجية لنشاطين في المقرر 1، وصفحة المقررات التي كانت تصف المقررين 3 و4 بأنهما مخططان.
- **ما لم يُحلّ ولا يُحلّ بالكتابة:** لم يُجرَّب أي مقرر مع فوج، ولا مراجعة قانونية أو ضريبية أو أمنية، ومختبرات المقرر 2 التفصيلية غير مبنية.
- **الجاهزية:** المقررات 1 و2 و3 و4 صالحة لتجربة أولى مع مدرب مستعد، بالشروط المذكورة لكل مقرر في القسم 4.

</div>

## 1. What was checked, and how

| Check | How | Result |
|---|---|---|
| Every course has its supporting files | Script, now a test | Pass after fixes |
| Syllabus hours equal the sum of module hours; one lesson per module | Script, now a test | 16, 24, 20, 16: pass |
| Every lesson: two titles, header line (duration, outcome, output), quick review, common mistakes, quiz link, navigation, English summary | Script, now a test | Pass after fixes |
| Lesson duration equals the syllabus hours; every outcome number exists; every outcome is served by a lesson | Script | Pass |
| Every lesson has a deck and a quiz of ten or more questions with a valid key | Tests | Pass after fixes |
| Internal links, anchors and tables | `make check` | 0 problems |
| Decks match their sources; every slide has notes; deck counts in READMEs; landing page lists every deck | Tests | Pass |
| New decks fit the 1600 × 900 stage | Rendered in headless Chrome, overflow measured by script, a sample viewed | 0 overflow after tightening 17 slides |
| Arabic direction in new and changed files | Bayan `bidi_lint` | 0 errors, 0 warnings |
| Terminology across the four glossaries | Script comparing English terms and their Arabic renderings | 2 conflicts, fixed |
| Syllabi, rubrics, instructor guides, status pages | Read in full | Findings below |
| Continuity of the running example across Courses 2, 3 and 4 | Figures compared | Consistent |

**Limits of this audit.** The lessons of Courses 3 and 4 were verified against sources when they were built on the same day; the lessons of Courses 1 and 2 were checked for structure and consistency here, and were **not** re-read line by line against their sources. External links were not opened from the audit environment; the repository's scheduled link workflow covers them. Nothing was tested with learners.

## 2. Findings and fixes

| # | Finding | Fix |
|---|---|---|
| 1 | Courses 3 and 4 had no slide decks; Courses 1 and 2 had one per module | 13 decks (194 slides, all with speaker notes) generated from the lessons by a new tool, `tools/slides_from_lessons.py`, built with the shared engine, listed on the landing page. They carry nothing that is not in the lesson, and are plainer than the hand-designed decks |
| 2 | Course 2 cited the 2025 OWASP numbering (LLM06 for Excessive Agency); the 2026 edition moves it to third | Lessons 2.3 and 2.6, their decks, the instructor guide, the slides README, lab exercise R7 and the source register updated |
| 3 | "Excessive agency" and "least privilege" had two Arabic renderings each across Courses 2 and 4 | One rendering each: الاستقلالية المفرطة and أقل الصلاحيات |
| 4 | Course 1's rubric named its four levels differently from Courses 2 to 4 | Level names unified; descriptors and weights unchanged |
| 5 | No completion standard was stated anywhere; each rubric stood alone | One assessment standard for the programme in the trainer guide, linked from each rubric, with a recommended completion standard marked as untested |
| 6 | No lesson linked to the next one, to the previous one or back to its syllabus | Navigation line added to all 28 lessons; the last lesson of each course points to the next course |
| 7 | Course 1's instructor guide lacked "before the first session", time inside each module, facilitator limits and re-check list; Course 2's lacked the last two | Added. Course 1 timings are taken from the lessons |
| 8 | No document told a trainer how the four courses fit together: entry checks, common structure, where sample solutions are, how to prepare | New [programme trainer guide](TRAINER-GUIDE.md) |
| 9 | Course 1 activities 1.2 and 1.3 had no sample answer | New [activity sample solutions](01-opportunity/examples/activity-sample-solutions.md), with a map of where every Course 1 activity's sample is |
| 10 | The courses index still called Courses 3 and 4 "draft outlines", the hours "proposed", and invited comments "before anything is built" | [Courses index](README.md) rewritten: status, entry requirements, where to start, what each course contains |
| 11 | The learning framework and competency framework said the courses were not built | Notes corrected |
| 12 | Lessons of Courses 3 and 4 did not point to slides; their guides said decks did not exist | Updated, with syllabi, READMEs, roadmap and start page |
| 13 | The landing page listed two courses | Courses 3 and 4, their decks and the trainer guide added to the generator |
| 14 | Nothing prevented these gaps from returning | Six structure tests added to `tests/test_courses.py` |

## 3. What the courses now contain

| | Course 1 | Course 2 | Course 3 | Course 4 |
|---|---|---|---|---|
| Hours, modules | 16, 7 | 24, 8 | 20, 7 | 16, 6 |
| Lessons | 7 | 8 | 7 | 6 |
| Decks, slides | 7, 146, hand-designed | 8, 118, hand-designed | 7, 107, generated | 6, 87, generated |
| Quizzes, questions | 7, 72 | 8, 80 | 7, 70 | 6, 60 |
| Templates in the course folder | 3, plus 6 sector briefs and 6 practice interviews | 6 | 4 | 5 |
| Sample solutions | Model thesis, activity solutions, key in 1.1 | Worked example by module | Worked example by pack part | Worked example by pack part |
| Glossary, rubrics with gates, instructor guide, not-adopted record | Yes | Yes | Yes | Yes |

## 4. Readiness, course by course

"Ready to pilot" means a prepared trainer can run it from the repository without the authors. It does not mean proven.

| Course | Assessment | Conditions and open items |
|---|---|---|
| **1. Opportunity** | **Ready to pilot.** The most complete course: designed decks, role cards, practice interviews, a model thesis | Each learner needs a host business and five interviewees. Market figures in the sector briefs need the pre-cohort re-check. Lessons use slightly different section names from later courses; left as they are |
| **2. Build** | **Ready to pilot with a technically able trainer.** Lessons, designed decks and a worked example are complete | **No step-by-step lab** for a low-code tool or a Python framework, no reference code and no shared dialect test set: the trainer must choose and prepare the build environment. This is the largest content gap in the programme |
| **3. Launch** | **Ready to pilot, with a specialist available.** Complete in content; decks are generated and plain | Modules 3.4 and 3.7 have had no legal or tax review. Each learner needs a real business for two weeks and a written data agreement. No data processing agreement template |
| **4. Scale and Govern** | **Ready to pilot, with a specialist available, for learners who have real usage.** Complete in content; decks are generated and plain | Modules 4.3 and 4.4 have had no legal or security review; NCA documents were read through summaries. Four weeks of data and graduation evidence need calendar time. No buildathon run book |

## 5. Remaining gaps

Not fixable by writing more files:

1. **No course has been piloted.** Hours, activity timings and the recommended completion standard are untested.
2. **No specialist review** of the regulatory, tax and security modules (1.3 in part, 3.4, 3.7, 4.3, 4.4). Several source entries rest on law-firm or press summaries; each entry says so.
3. **Real businesses** for field work, pilots and graduation evidence must be found by each cohort.

Fixable, and not done here:

4. Step-by-step labs and reference code for Course 2.
5. Hand-designed decks for Courses 3 and 4. The linter notes 41 dense slides in the generated decks.
6. A second semester in the 15-week instructor kit, which still covers mainly Courses 1 and 2.
7. A line-by-line source re-check of the Course 1 and Course 2 lessons.
8. Minor variation left in place: Course 1 lessons name their activity sections differently; quick-review lists have four to nine questions in Courses 1 and 2 and six in Courses 3 and 4; quiz 1.4 has twelve questions.
9. English versions of the lessons. Each lesson has an English summary only.
10. A recorded demonstration, a data processing agreement template, a buildathon run book.

## 6. Decisions taken in this audit, open to the owner

- **Completion standard:** all gates passed, no criterion at level 1, weighted average of 2.5 of 4. Proposed as a default; change or remove it.
- **Course 1 level names** were changed to match the other courses.
- **Generated decks** were published instead of leaving Courses 3 and 4 without any. They can be replaced fragment by fragment.
- **Arabic terms:** الاستقلالية المفرطة for excessive agency and أقل الصلاحيات for least privilege.

## 7. How to repeat the audit

```bash
make check                                      # links, tables, all tests including course structure
python3 tools/build_slides.py --check           # decks match their sources
python3 tools/slides_from_lessons.py 3 4        # regenerate decks (not after hand edits)
```

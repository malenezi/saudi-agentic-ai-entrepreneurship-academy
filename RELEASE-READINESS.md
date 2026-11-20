# Release-readiness report · تقرير جاهزية الإصدار

**Date:** 20 November 2026 · **Scope:** the four courses, the instructor kit and what supports them · **Baseline:** the [QA report](03-courses/QA-REPORT.md) of the same day

## 1. Recommendation

| Question | Answer |
|---|---|
| Publish the repository as an open, labelled, pilot-ready release? | **Go.** The four courses are complete in content, internally consistent, tested where code can be tested, and honest about what is unverified |
| Describe the Academy as validated, professionally reviewed, or certifying? | **No-go.** No specialist has signed a review, and no cohort has taken any course |
| Run a first cohort from the repository without the authors? | **Go, with the conditions in section 5.** Start with Course 1 or Course 2 |
| Call the lessons bilingual? | **No.** Lessons are in Arabic with English terms and an English summary. Syllabi, trainer guides, the kit summary, the standard, the labs' code and the validation files are in English or both |

The release should carry the three labels it already carries in its pages: not piloted, not professionally reviewed, examples invented.

<div dir="rtl">

**بالعربية:** يُنشر المستودع إصداراً مفتوحاً جاهزاً للتجربة، بوسومه الثلاثة: لم يُجرَّب مع فوج، ولم يراجعه مختص، وأمثلته مختلقة. لا يوصف بأنه محقَّق أو مراجَع مهنياً أو مانح شهادات. الدروس عربية بمصطلحات إنجليزية وملخص إنجليزي، وليست ثنائية اللغة.

</div>

## 2. Every original gap and its status

Gaps are numbered as in section 5 of the QA report.

| # | Gap in the QA report | Status | What was done, and what remains |
|---|---|---|---|
| 1 | No course has been piloted | **Open: needs people.** Prepared | A [desk walkthrough](03-courses/validation/desk-walkthrough.md) with four invented learners was executed and its six findings corrected. It is labelled as a desk review, not a pilot. A [pilot protocol](03-courses/validation/pilot-protocol.md) says what a first cohort must collect. No pilot result exists |
| 2 | No specialist review | **Open: needs people.** Prepared | Four [review packets](03-courses/validation/README.md): 54 claim uses sorted by how each was verified (18 cite the source's own page, 32 rest on a secondary or partial reading, 4 on a draft), with questions and an unsigned sign-off. Ten regulated lessons state their verification status under the header |
| 3 | Real businesses for field work | **Open: needs people** | The kit, the trainer guide and the learner guide say when each is needed. The standard holds a deliverable instead of failing it when a business is not available in time |
| 4 | Course 2 labs and reference code | **Closed** | Eight [labs](03-courses/02-build/labs/README.md), one per module, with a reference implementation in Python (standard library only), test data, stage configurations, expected outputs and troubleshooting. Offline, no key, no cost. 23 tests. **Remaining:** no lab for a named low-code orchestrator; the test set is invented, not collected from real Saudi-dialect messages; the HTTP path to a real model is tested against a local stub only |
| 5 | Hand-designed decks for Courses 3 and 4; 41 dense slides | **Closed** | Thirteen decks authored slide by slide (154 slides), replacing the generated ones. Rendered at 1600 × 900 with no overflow. The linter reports 0 errors, 0 warnings and **0 dense-slide notes** for these decks |
| 6 | 15-week kit covered mainly Courses 1 and 2 | **Closed** | The [kit](01-academy/instructor-kit/README.md) now covers all four courses: thirty [session plans](01-academy/instructor-kit/session-plans.md) mapped to modules, minutes and outcomes, four gates, workload, preparation, and a two-semester alternative. A test checks that the minutes per module equal the syllabus hours |
| 7 | Course 1 and 2 lessons not re-read against sources | **Done by automated fetch, 20 November 2026** | 33 entries re-opened; two register wordings corrected (A29, A75) and one "not found" ruling revised (B20). No figure in a lesson, brief or deck changed. Limits are listed in the [re-check record](03-courses/validation/source-recheck-c1-c2.md). Not repeated by a human reader |
| 8 | Minor structural variation in Courses 1 and 2 | **Left, stated** | Course 1 lessons name activity sections differently; quick-review lists have four to nine questions in Courses 1 and 2; quiz 1.4 has twelve questions; lesson 1.7 has no track table. No learner-facing defect |
| 9 | English versions of the lessons | **Out of scope by decision; open** | The final brief for this cycle removed full translation. Each lesson keeps its English summary. This is the main reason the Academy should not be called bilingual |
| 10 | Recorded demonstration, data processing agreement template, buildathon run book | **Partly** | Buildathon rules are in the Course 4 instructor guide. No recording. No agreement template: it needs a lawyer |

**The three decisions left open by the audit**

| Decision | Outcome |
|---|---|
| Completion standard (gates, no level 1, average 2.5) | **Replaced** by [version 1.0](03-courses/assessment-standard.md): gates, no level 1, **lead criterion at level 3 or above**, weighted score **2.7** or more; a distinction band; evidence to be seen, second-assessor rule, remediation, and certification eligibility. Reasons are in its section 1. Applied in all four rubrics, with a scoring tool and tests. Untested with a cohort |
| Course 1 rubric level names | **Verified consistent.** Same four names in all rubrics; descriptors and weights unchanged; weights sum to 100 in each course and match the syllabi and the scoring tool (tested). Course 1 keeps two extra field-pack rubrics for cohort feedback; completion is decided on the thesis rubric |
| Generated decks | **Replaced**, as in gap 5. The generator is kept as a drafting aid for a new course and refuses to overwrite without `--force` |

## 3. Files created, updated or replaced

134 files changed since the audit commit: 53 added, 79 modified, 2 removed.

| Area | Created | Updated or replaced |
|---|---|---|
| Course 2 labs | `03-courses/02-build/labs/`: overview, eight lab guides, `reference/order_agent/` (six modules), `data/` (orders, two policy versions, glossary, 35 working cases, 8 held-out cases), `config/` (seven configurations), `expected/` (seven outputs), `solutions/`, `instructions.md` | Eight lessons link their lab; syllabus and instructor guide |
| Decks | | 13 fragments and 13 built decks in Courses 3 and 4 replaced; both slide READMEs rewritten; `tools/slides_from_lessons.py` guarded |
| Assessment | `03-courses/assessment-standard.md`, `03-courses/alignment.md`, `tools/score_submission.py`, `tests/test_assessment.py` | Four `rubrics.md`; completion record form in the kit |
| Instructor kit | `01-academy/instructor-kit/session-plans.md` | Kit README rewritten for all four courses; assessment forms |
| Validation | `03-courses/validation/`: overview, desk walkthrough, pilot protocol, four review packets | Verification note in ten lessons; activity times in thirteen lessons |
| Guides and docs | `03-courses/LEARNER-GUIDE.md`, `THIRD-PARTY.md`, this report | Trainer guide, courses index, READMEs, start page, roadmap, contribution guide, source register (A125), changelog, landing page generator |
| Tests | `tests/test_course2_labs.py`, `tests/test_assessment.py` | `tests/test_courses.py` (instructor kit) |

## 4. Tests executed and results

| Check | Result |
|---|---|
| `make check`: links, anchors and tables across 301 Markdown files | 0 problems |
| `make check`: unit tests | **74 tests, all pass** (Python 3.13 locally; CI runs 3.9 and 3.13) |
| Course 2 labs: every command in every lab guide executed | Expected numbers reproduced: 24, 25, 28, 30 of 35; 6 of 8 held out; 9 against 7; third-cycle solution 32 of 35 |
| Lab behaviour tests | Ownership check, absence of refund and address tools, approval before a level B action, injected notes ignored, malformed tool input rejected, stop switch, masked phone numbers: all pass |
| HTTP model path | Passes against a local stub server: request shape, JSON extraction, malformed model output cannot act, unreachable endpoint escalates. **Not run against a real model** |
| Completion standard | 10 tests: rules, edge cases, and agreement of weights, criteria names and gate counts with the four syllabi and rubrics |
| Fifteen-week plan | Thirty sessions of 180 minutes; minutes per module equal syllabus hours for all 28 modules |
| Decks: build matches source; every slide has notes; counts in READMEs; landing page lists every deck | Pass |
| New decks rendered at 1600 × 900 in headless Chrome | 0 slides overflow, including code blocks; samples viewed |
| Bayan `bidi_lint --profile deck`, all 28 built decks | 0 errors, 0 warnings. Dense-slide notes: 0 in Courses 3 and 4; 32 remain in Courses 1 and 2 (section 6) |
| Bayan `bidi_lint`, course Markdown and new files | 0 errors. 28 warnings, all in the slide **source fragments** of Courses 1 and 2 (section 6) |
| Structural audit script on all four courses | No new issue; the variations of gap 8 remain |

## 5. Readiness, course by course

"Ready to pilot" means a prepared trainer can run it from the repository without the authors. It does not mean proven.

| Course | Assessment | Conditions |
|---|---|---|
| **1. Opportunity** (16 h) | **Ready to pilot** | A host business and five interviewees per learner. Market figures in the sector briefs re-checked before the cohort |
| **2. Build** (24 h) | **Ready to pilot.** The largest gap of the audit is closed for both tracks | The labs rehearse the method on the example; each learner still builds their own agent with a tool they choose. No named low-code lab |
| **3. Launch** (20 h) | **Ready to pilot with a specialist on call** | Modules 3.4 and 3.7 unreviewed: 41 claim uses in two packets await a lawyer and a tax adviser. A real business for two weeks under a written agreement |
| **4. Scale and Govern** (16 h) | **Ready to pilot with a specialist on call, for learners with real usage** | Modules 4.3 and 4.4 unreviewed; NCA documents read through summaries. Four weeks of operating data and graduation evidence need calendar time |
| **Programme in 15 weeks** | **Ready to pilot as an intensive** | About twelve hours a week. Businesses, a panel and three specialists arranged before week 1 |

## 6. Known items left as they are, and why

Nothing here is hidden by a passing check.

| Item | Why it was left |
|---|---|
| 32 dense-slide notes (76 to 120 words) in the hand-designed decks of Courses 1 and 2 | Info-level notes on decks designed and render-checked earlier. The six heaviest are demo screens, role cards and one reference table, where the count includes text inside a drawn screen. Changing them is a design decision for the owner |
| 28 linter warnings in Course 1 and 2 slide source fragments | The fragments use the builder's shorthand; numeric cells are isolated at build time, and the built decks have no warning. Linting the fragments is linting the wrong file |
| Python 3.9 | Not available in the authoring environment; CI runs it on every push |
| Fonts loaded from Google Fonts | Pages fall back to system fonts offline. Documented in [THIRD-PARTY.md](THIRD-PARTY.md) |
| Internal-agent route (an employee building one agent for their own firm) | The learner guide says what to take and what to adapt. No alternative modules were written |
| External links | Not opened from the authoring environment; the scheduled link workflow covers them |

## 7. Outstanding external dependencies

These cannot be closed by writing files. Each has its instrument ready.

| Dependency | Who | Instrument | Unblocks |
|---|---|---|---|
| Legal and privacy review | A Saudi-qualified lawyer with data protection practice | [Packet](03-courses/validation/review-packets/legal-privacy.md): 21 claims, 10 questions | Lessons 3.4, 4.3 and the pilot and LOI outline; removal of "not reviewed" from seven lessons |
| Tax and establishment review | A licensed accountant or tax adviser | [Packet](03-courses/validation/review-packets/tax-establishment.md): 20 claims, 9 questions | Lesson 3.7 and the business setup checklist |
| Cybersecurity review | An application or AI security practitioner | [Packet](03-courses/validation/review-packets/cybersecurity.md): 9 claims, 9 questions, including a review of the lab code | Lessons 2.6 and 4.4 |
| Funding review | An investor or programme manager in the Saudi market | [Packet](03-courses/validation/review-packets/funding-investment.md): 4 claims, 8 questions | Lessons 4.5 and 4.6, and the funding directory |
| First pilot | A delivering organisation, 8 to 20 learners, real businesses | [Protocol](03-courses/validation/pilot-protocol.md) | Hours, timings, the completion standard, the "not piloted" label |
| Real Saudi-dialect test set | A business willing to share masked messages | Lab 2.5 and the evaluation template | Replacing invented dialect cases |
| English lessons | A translator-editor with the subject | The lessons and their English summaries | Calling the Academy bilingual |

## 8. Acceptance check

| Criterion in the brief | Met? |
|---|---|
| Coherent, fully developed four-course academy | **Yes**: 28 modules, each with lesson, deck, quiz, activity, template and sample solution; one standard; one kit |
| Technically validated | **Yes, for what code can validate**: 74 tests, labs executed, decks rendered. **No** for a real model endpoint |
| Trainer-ready | **Yes**: trainer guide, four instructor guides, thirty session plans, forms, labs, decks with notes |
| Learner-ready | **Yes**: learner guide, navigation, labs that run offline, self-scoring |
| Publicly publishable | **Yes**, with its labels: licences, third-party notes, sources, disclaimers, invented examples marked |
| Bilingual | **No**: see gap 9 |
| Specialist-validated and piloted | **No**: prepared, not done. No approval or pilot result is claimed anywhere |
| No known gap silently unresolved | **Yes**: every open item is in sections 2, 6 or 7 |

## 9. How to repeat the checks

```bash
make check                                              # links, tables, 74 tests
python3 -m unittest tests.test_course2_labs -v          # labs and reference code
python3 tools/build_slides.py --check                   # decks match their sources
python3 tools/score_submission.py 3 --levels 3 3 2 3 2 --gates 5
```

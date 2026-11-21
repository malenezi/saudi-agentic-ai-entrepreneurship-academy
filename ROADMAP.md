# خارطة الطريق · Roadmap

The academy is built iteratively, in the open. Each iteration ships something a founder can use the same day. The order below is a plan, not a promise; contributions can move anything forward.

| Iteration | Theme | Contents | Status |
|---|---|---|---|
| v0.1 | Foundation + Founder Toolkit | README, academy framework, course outlines, toolkit, lab, compliance tools | Released |
| v0.2 | Saudi Market Knowledge Framework | Twelve-domain framework, regulatory register, official directory, founder compliance checklist, agentic governance playbook, founder-agent standard and first agent; open contribution guide | Released |
| v0.3 | Course 1, case studies and companion repositories | First content release of Course 1 (lessons, sector briefs, templates, rubrics); nine public-source case studies with evidence levels; Riyada and Bayan cross-referenced with an overlap map, learning pathways and eight lab exercises | Released |
| v0.4 | Lab, Module 1.4 in depth, identity and quality checks | Six new lab exercises with working checkers (R5 to R8, B5, B6), fourteen in all; Module 1.4 enriched; the academy banner; automated link checks and script tests on every change | Released 17 November 2026 |
| v0.5 | Founder essentials in depth | Establishment walkthrough, PDPL worked example, tax basics, funding directory; Arabic versions of English-only guides | Released 18 November 2026. Course 1 not yet piloted; exercises not yet tried with learners. Done on 18 November 2026 (part 1): the PDPL worked example, the first funding directory, and the tax guide with its adviser review pack (not yet reviewed). Done on 18 November 2026 (part 2): the establishment walkthrough (domain 01), from official Ministry of Commerce and Ministry of Investment pages, awaiting a lawyer's review. Done on 18 November 2026 (part 3): Arabic versions of the English-only guides in domains 02, 03, 04, 06 and 11 (not lawyer-reviewed). Done in the launch audit: Arabic version of the regulatory register. Moved to v0.6: the funding directory's "to verify" entries |
| **v0.6** | **Courses 1 and 2 in full** | Course 1 slides, quizzes and practice interview records; first content release of Course 2 (eight lessons, templates, worked example) with its slides and quizzes; one slide engine for all courses; a landing page that lists the decks; a start-here page; tests that keep decks and quiz keys in step with their sources | **This release** (19 November 2026). Neither course has been piloted |
| **v0.7** | **Business development domains, and the SE495 integration** | First guides for the five remaining domains (IP, e-commerce, employment, sector regulation, government procurement); first lessons of Courses 3 and 4; Founder Toolkit 11 and 12 with two calculators; seven sourced venture journeys; lab skills 11 and 12 and exercises A1 to A3; a venture workbook; an instructor kit; a machine-readable funding directory index | **Released 19 November 2026; v0.7.1 the same day** added five venture journeys on Saudi companies building for agents and verified twelve funding directory entries from operators' pages. The five guides rest on few sources and await legal review. Thirteen funding directory entries are still pending. Nothing has been piloted |
| **v0.8** | **The four courses complete** | First content of Courses 3 and 4 with authored decks; eight executable labs for Course 2 with a tested reference implementation; one completion standard with a scoring tool; a fifteen-week instructor kit for all four courses; a learner guide; a QA audit; a desk walkthrough, a pilot protocol and four specialist review packets | Released 20 November 2026. Not piloted; not professionally reviewed. Status of every gap in the [release-readiness report](RELEASE-READINESS.md) |
| **v0.9** | **Founder agents and runnable templates** | The eleven remaining founder agents as definitions with test conversations; five runnable agent templates as importable n8n workflows with a simulated model; a low-code lab for Course 2 that reproduces the reference numbers; a builder, a harness and tests for the workflows | Released 20 November 2026. Founder agents not tried with founders and no test conversation recorded; workflows imported and run in n8n 2.35.7 from the command line, not run with a real model, not connected to any channel, not tried with learners. **Moved on:** an evaluation set from real Saudi-dialect messages needs a business willing to share anonymised messages (see "In iterations") |
| In iterations | **Courses** | A first pilot of any course (Courses 3 and 4 received their first content, labs for Course 2 and authored decks on 20 November 2026); specialist review of the modules that touch law, tax and security (see the [release-readiness report](RELEASE-READINESS.md) and the [review packets](03-courses/validation/README.md)); step-by-step labs for Course 2 (its first content, eight lessons with templates, a worked example, slides and quizzes, was added on 19 November 2026); pilots for Courses 1 and 2 (Course 1's slides, quizzes and practice interview records were added on 19 November 2026) | In progress |
| v1.0 | Public launch | Website generated from the repository, built and checked with Bayan's skills and linters; project showcase | Planned |

## Why the knowledge framework comes before the courses

The courses teach what to do; the framework says how to do it in the Kingdom. Building the framework first means the courses can point to maintained, sourced material instead of repeating it. All four courses now have their first content; none has been piloted, and each will change with a first cohort.

## Known gaps in v0.9

- Every domain now has at least one guide, but the five added in v0.7 each rest on one or two sources (a foreign government overview for IP, a press report for e-commerce, law-firm commentary for employment, an automated reading of the gazette text for procurement, and no new source for sector regulation). Each says so at its top. (The tax guide awaits an adviser's review and the establishment walkthrough a lawyer's.)
- The procurement guide found a law text on the gazette site that repeals the 2019 law; its decree number and effective date are not confirmed (C44).
- The regulatory register has no "to verify" rows since 20 November 2026. Several rows confirm only that an instrument exists and is in force, not what it requires. The same rule was applied to the twelve domain pages, the official directory and the two funding guides.
- Regulatory summaries have not been reviewed by a Saudi lawyer; tax content has not been reviewed by a tax adviser.
- Arabic versions of the deeper guides (domains 02, 03, 04, 06, 11) and the regulatory register are not lawyer-reviewed.
- The funding directory lists verified entries only since 20 November 2026 (31 verified, one marked inactive by its operator). Most entries state what the operator's page does not say: amounts, equity and eligibility are often missing. Items that could not be verified were removed and are listed in the framework's [removal record](02-saudi-market-knowledge-framework/not-adopted.md).
- Case studies and venture journeys are summaries of public sources, none independently verified; no owner-written Saudi case yet. One venture source (the Aqar company page) could not be opened.
- Course 1 has slides, quizzes and practice interview records but has not been piloted. Course 2 has lessons, templates, a worked example, slides and quizzes, and has not been piloted. Course 3 has seven lessons, slide decks, quizzes, templates and a worked example, and has not been piloted; its Modules 3.4 and 3.7 have had no legal or tax review. Course 4 has six lessons, slide decks, quizzes, templates and a worked example, and has not been piloted; its Modules 4.3 and 4.4 have had no legal or security review.
- The lab exercises, the venture workbook and the instructor kit have not been tried with learners.
- The runnable agent templates and the low-code lab run with a keyword simulator. Their instructions for a real model are untested, no messaging channel, calendar, CRM or ledger is connected, and their webhooks have no authentication.
- The twelve founder agents are definitions with specified test conversations. Agents 2 to 12 each have one [recorded run](02-saudi-market-knowledge-framework/founder-agents/recorded-runs/README.md) with one assistant (Claude Fable 5.2, 21 November 2026): 30 of 33 conversations consistent with the expected behaviour, 3 not fully exercised for want of the input the case describes. None has been tried with a founder, and no second assistant has been used.
- There is no evaluation set from real Saudi-dialect messages: every test case in the repository is invented.

## Where help matters most right now

1. Restoring what was removed from the [knowledge framework](02-saudi-market-knowledge-framework/not-adopted.md) as unverified, each item from its official source.
2. Practitioner-written guides for tax, IP, employment and procurement.
3. Entries for the funding directory from programme operators, with the amounts and eligibility their public pages leave out.
4. Review of the Arabic versions by a lawyer and by native-speaking practitioners.
5. Real case studies.
6. More recorded runs of the [founder agents](02-saudi-market-knowledge-framework/founder-agents/README.md): the three test conversations of any agent, with the assistant and the date.
7. Anonymised real customer messages in Saudi dialect, with the owner's permission, for a shared evaluation set.

## First-year targets (proposed, not forecasts)

| Measure | Target |
|---|---|
| Domains with at least three published guides | 12 |
| Register entries verified | 100% |
| Reusable templates | 40 |
| Real Saudi case studies | 20 |
| Founder agents published | 12 (all twelve published in v0.9; eleven with one recorded run each, 21 November 2026) |
| Community contributors | 30 |
| Courses built | 4 (all four have their first content today; none piloted) |

<div dir="rtl">

## بالعربية

تُبنى الأكاديمية علناً وعلى مراحل. الإصدار الحالي (0.9) ينشر وكلاء المؤسس الأحد عشر الباقين تعريفاتٍ بمحادثات اختبارها، وخمسة قوالب وكلاء تعمل في n8n بنموذج محاكٍ، ومختبراً منخفض الكود للمقرر 2 يعيد أرقام الشيفرة المرجعية. لم يُجرَّب الوكلاء مع مؤسسين، ولم تُشغَّل القوالب مع نموذج حقيقي ولا وُصلت بقناة. وقبله أكمل الإصدار 0.8 المقررات الأربعة: المحتوى الأول للمقررين 3 و4 بعروضهما، وثمانية مختبرات تعمل للمقرر 2 بشيفرة مرجعية مختبَرة، ومعيار إتمام واحد، وحقيبة مدرّس من خمسة عشر أسبوعاً للمقررات الأربعة، ودليل للمتعلم، وحزم مراجعة للمختصين وبروتوكول تجربة. لم يُجرَّب أي مقرر مع فوج ولم يراجعه مختص بعد، وحالة كل بند في [تقرير جاهزية الإصدار](RELEASE-READINESS.md). وقبله أضاف الإصدار 0.7 دليلاً أول لكل من المجالات الخمسة الباقية (الملكية الفكرية، التجارة الإلكترونية، التوظيف، التنظيمات القطاعية، المشتريات الحكومية)، وأول درسين في المقررين 3 و4، وقالبين وحاسبتين في حقيبة المؤسس، وسبعة مسارات شركات موثّقة، ودفتر المشروع، وحقيبة المدرّس. وقبله أكمل الإصدار 0.6 المقررين 1 و2: دروس وعروض واختبارات قصيرة وقوالب وسلالم تقدير لكل منهما، ومحرك عروض واحد، وصفحة تجمع العروض، وصفحة «ابدأ من هنا». وقبله أضاف الإصدار 0.5 أساسيات المؤسس بعمق (الدليل التطبيقي لحماية البيانات، والتأسيس، وأساسيات الضرائب، ودليل برامج التمويل) ونسخاً عربية كاملة للأدلة المنشورة. وقبله أضاف الإصدار 0.4 ستة تمارين مختبر ببرامج فحص تعمل (المجموع أربعة عشر)، ويعمّق الوحدة 1.4، ويعتمد هوية الأكاديمية، ويفحص الروابط والبرامج آلياً عند كل تغيير. وقبله أضاف الإصدار 0.3 المحتوى الأول للمقرر 1، وتسع دراسات حالة، وربط المستودعين المرافقين «ريادة» و«بيان». الترتيب أعلاه خطة وليس وعداً، ومساهمات المجتمع تستطيع تقديم أي بند.

</div>

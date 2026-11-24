# دليل المساهمة · Contributing

<div dir="rtl">

## أهلاً بك، وأهلاً بكل مساهمة

**كل مساهمة مرحّب بها.** صغيرة أو كبيرة، بالعربية أو بالإنجليزية، من مبتدئ أو من خبير. لا يوجد حد أدنى للحجم ولا شرط خبرة. إن خطر لك أن شيئاً هنا يمكن أن يكون أوضح أو أصح أو أنفع، فهذه مساهمة.

نلتزم من جهتنا بثلاثة أمور:

1. **نستقبل كل مساهمة باحترام** ونرد عليها.
2. **نساعدك على إتمامها.** إن نقص مصدر أو تنسيق أو ترجمة، نكمله معك ولا نرفض بسببه.
3. **ننسب العمل إلى صاحبه.** اسمك في سجل المساهمين وفي الصفحة التي ساهمت فيها إن رغبت.

## عشر طرق للمساهمة، من دقيقة إلى أسبوع

| الوقت | المساهمة | كيف |
|---|---|---|
| دقيقة | تصحيح خطأ إملائي أو رابط معطّل | زر التعديل في GitHub مباشرة |
| 5 دقائق | سؤال أو ملاحظة: «هذا غير واضح» أو «هذا ينقصه كذا» | افتح Issue |
| 10 دقائق | تحديث معلومة تغيّرت (برنامج، رابط، تاريخ) | Issue من نوع `resource-update` |
| 20 دقيقة | توثيق بند من [قائمة ما حُذف](02-saudi-market-knowledge-framework/not-adopted.md) من مصدره الرسمي | أرسل الرابط الرسمي وتاريخ التحقق |
| 30 دقيقة | ترجمة فقرة أو تدقيق لغوي | طلب دمج أو Issue |
| ساعة | حالات اختبار باللهجة السعودية لوكيل | أضفها إلى قالب التقييم |
| ساعة | تجربة من عملك: «هكذا أسسنا» أو «هكذا تعاملنا مع كذا» | اكتبها بأي صيغة |
| بضع ساعات | دليل من قائمة «أدلة مطلوبة» في أي مجال | احجزه بفتح Issue |
| يوم | مهارة أو قالب وكيل مجرَّب | راجع شروط المختبر |
| أسبوع | دراسة حالة حقيقية (بإذن صاحب المنشأة) | قالب دراسة الحالة |

## فحص اختياري للمحتوى العربي

إن كان لديك Python فشغّل مدقق [«بيان»](https://github.com/malenezi/bayan) على ملفاتك العربية قبل طلب الدمج: `python3 bayan/shared/scripts/bidi_lint.py <المجلد>`. يلتقط الأرقام المقلوبة وعلامات الترقيم اللاتينية بعد النص العربي وما يشبهها. هو عون لك وليس شرطاً، ونشغّله عنك إن أحببت.

## لا تستخدم Git؟ لا مشكلة

افتح Issue والصق ما لديك: نص، ملاحظات، صورة، ملف Word. أو أرسله عبر أي قناة تواصل مع المشرف. نحن نحوّله إلى الصيغة المطلوبة وننسبه إليك.

## من نحتاج؟

رواد الأعمال وأصحاب المنشآت · المحامون والمستشارون القانونيون · المحاسبون ومستشارو الضرائب · مختصو الأمن السيبراني وحماية البيانات · المطورون ومهندسو الذكاء الاصطناعي · العاملون في الحاضنات والمسرعات والصناديق · الطلاب والباحثون · المترجمون والمدققون اللغويون · وكل من مرّ بتجربة ويريد أن يوفّرها على غيره.

## ما نطلبه للحفاظ على الثقة

هذه ليست حواجز، بل ما يجعل المستودع موثوقاً. وإن لم تستطع استيفاء أحدها فأرسل مساهمتك ونساعدك:

- **الأرقام والمعلومات التنظيمية لها مصدر.** أضفه إن عرفته، أو قل في طلبك إنه بلا مصدر ونبحث عنه معاً. ما لا مصدر له لا يُنشر في إطار المعرفة.
- **لا بيانات شخصية ولا أسرار.** لا مفاتيح API، ولا بيانات عملاء، ولا معلومات تجارية سرية.
- **المحتوى التنظيمي توعوي** وليس استشارة قانونية أو ضريبية.
- **الحياد.** نذكر الأدوات والجهات لقيمتها التعليمية، دون ترويج.
- **الاحترام.** راجع [ميثاق السلوك](CODE_OF_CONDUCT.md).

## مراجعة مختص، وتجربة فوج، ومساهمة في الشيفرة

- **مختص قانوني أو ضريبي أو أمني أو استثماري؟** في [حزم المراجعة](03-courses/validation/README.md) سجل لكل معلومة وأسئلة محددة ونموذج توقيع. ساعاتك الثلاث أثمن مساهمة يحتاجها المستودع اليوم.
- **جرّبت مقرراً مع متعلمين؟** [بروتوكول التجربة](03-courses/validation/pilot-protocol.md) يحدد ما يُجمع وكيف يُرسل. التقرير يُنشر كما كُتب.
- **تعدّل شيفرة المختبرات أو الأدوات؟** المكتبة القياسية وحدها، و Python 3.9 فأحدث، واختبار لكل سلوك جديد. لا مفتاح ولا بيانات حقيقية في أي ملف. شغّل `make check` قبل طلب الدمج.
- **تعدّل عرضاً؟** عدّل المقطع في `slides/src/` ثم `python3 tools/build_slides.py`. شريحة لكل فكرة، والتفصيل في ملاحظات المتحدث.
- **أضفت صفحة أو غيّرت عنواناً فيها؟** شغّل `python3 tools/build_site.py` ليتحدّث فهرس البحث في الموقع (`site-index.json`). إن لم تستطع فأرسل طلب الدمج كما هو واذكر ذلك، وسنحدّثه نحن.
- **تعدّل معيار الإتمام أو سلّماً؟** غيّر رقم إصدار المعيار، وحدّث `tools/score_submission.py` واختباراته معه.

## قبل فتح طلب الدمج

`make check` يفحص الروابط الداخلية والمراسي والجداول ويشغّل الاختبارات. ما بعد البند 5 لا يفحصه برنامج، فافحصه أنت. وإن تعذّر عليك بند فأرسل طلبك واذكره، ونكمله معك.

1. `make check` ينتهي بلا مشكلة، وكل الاختبارات ناجحة.
2. `python3 tools/build_site.py` بعد أي صفحة جديدة أو عنوان تغيّر، و`site-index.json` ضمن التغيير.
3. الملفات المبنية لا تُعدَّل باليد: `index.html`، `index.en.html`، ملفات `.n8n.json`، العروض المبنية، وما يبنيه `tools/dataset_pack.py`. عدّل المصدر ثم ابنِ.
4. إن غيّرت القوالب القابلة للتشغيل: `python3 tools/build_n8n_workflows.py`، وأي رقم تغيّر (خط أساس المحاكي، عدد الحالات) يُحدَّث حيث يُذكر.
5. إن غيّرت دليل التمويل: `python3 tools/check_funding_directory.py`.
6. كل رقم أو حكم جديد له معرّف في [`SOURCES.md`](SOURCES.md): المعلومة كما قُرئت، ورابط صفحة الجهة المصدِرة نفسها، وتاريخ التحقق وطريقة القراءة، وما لم يُقرأ.
7. ما قُرئ من مقتطف بحث أو ملخص ثانوي يُكتب أنه كذلك. وما لم يثبت يُسجَّل في سلسلة C ولا يدخل إطار المعرفة.
8. النسختان متطابقتان: السجل التنظيمي بلغتيه، ودليل التمويل وملف `funding-directory.json`، والصفحتان العربية والإنجليزية لكل دليل له نسختان.
9. إن أعدت بنداً محذوفاً أو تركت بنداً خارجاً: حدّث [سجل ما لم يُعتمد](02-saudi-market-knowledge-framework/not-adopted.md).
10. سطر «حالة التحقق» في أي درس تغيّرت مصادره يطابق العدد الجديد. وعبارة «لم يراجعه مختص» لا تُحذف إلا بتوقيع مسمّى في [حزمة المراجعة](03-courses/validation/README.md).
11. النص العربي: `bidi_lint` بلا أخطاء جديدة، والصفحة داخل وسم الاتجاه `dir="rtl"` كما في بقية الصفحات.
12. لا مفتاح ولا رمز ولا بيانات حقيقية في أي ملف.
13. مدخل في [`CHANGELOG.md`](CHANGELOG.md) تحت «Unreleased» يذكر ما لم يُجرَّب وما لم يُراجَع.
14. وصف طلب الدمج يفصل ثلاثة: ما أُنجز، وكيف تُحقّق منه، وما ينتظر مختصاً.

## إن كنت تستخدم Git

1. افتح Issue تصف فيه اقتراحك (اختياري للتعديلات الصغيرة).
2. أنشئ فرعاً: `content/...` أو `guide/...` أو `agent/...` أو `fix/...`.
3. افتح طلب دمج. قائمة التحقق فيه للمساعدة، وليست شرطاً للقبول.

بمساهمتك توافق على ترخيص المحتوى تحت CC BY 4.0 والشيفرة تحت Apache-2.0.

**شكراً لك.** كل سطر تضيفه يوفّر على رائد أعمال يوماً من البحث.

</div>

---

# Contributing (English)

## Welcome. Every contribution is welcome

Large or small, in Arabic or English, from a beginner or an expert. There is no minimum size and no experience requirement. If you think something here could be clearer, more accurate or more useful, that is a contribution.

Our side of the deal:

1. **Every contribution is received with respect** and gets a reply.
2. **We help you finish it.** If a source, formatting or translation is missing, we complete it with you; we do not reject for that.
3. **You are credited**, in the contributors list and on the page you improved if you wish.

## Ten ways to contribute, from a minute to a week

| Time | Contribution | How |
|---|---|---|
| 1 minute | Fix a typo or a broken link | The edit button on GitHub |
| 5 minutes | A question or remark: "this is unclear", "this is missing" | Open an issue |
| 10 minutes | Update something that changed (programme, link, date) | A `resource-update` issue |
| 20 minutes | Verify an item from the [removal record](02-saudi-market-knowledge-framework/not-adopted.md) at its official source | Send the official link and the date you checked |
| 30 minutes | Translate a paragraph or proofread | Pull request or issue |
| 1 hour | Saudi-dialect test cases for an agent | Add them to the evaluation template |
| 1 hour | An experience from your business: "how we set up", "how we handled this" | Write it in any form |
| A few hours | A guide from any domain's "guides wanted" list | Claim it by opening an issue |
| A day | A tested skill or agent template | See the lab's requirements |
| A week | A real case study, with the owner's permission | Case-study template |

## Optional check for Arabic content

If you have Python, you can run the [Bayan](https://github.com/malenezi/bayan) linter on Arabic Markdown before a pull request: `python3 bayan/shared/scripts/bidi_lint.py <folder>`. It catches reversed numbers, Latin punctuation after Arabic and similar slips. It is a help, not a condition; we will run it for you if you prefer.

## Not a Git user? No problem

Open an issue and paste what you have: text, notes, a picture, a Word file. We convert it and credit you.

## Who we need

Founders and business owners · lawyers · accountants and tax advisers · cybersecurity and data protection specialists · developers and AI engineers · people at incubators, accelerators and funds · students and researchers · translators and proofreaders · anyone who has been through it and wants to spare the next person.

## What we ask, to keep the repository trustworthy

These are not barriers. If you cannot meet one, send your contribution anyway and we will help.

- **Numbers and regulatory statements have a source.** Add it if you know it, or say in your request that it has no source and we will look for it together. An item without a source is not published in the knowledge framework.
- **No personal data or secrets.** No API keys, customer data or confidential business information.
- **Regulatory content is educational**, not legal or tax advice.
- **Neutrality.** Tools and organisations are named for their teaching value, without promotion.
- **Respect.** See the [Code of Conduct](CODE_OF_CONDUCT.md).

## Specialist review, cohort pilots and code contributions

- **A lawyer, tax adviser, security practitioner or investor?** The [review packets](03-courses/validation/README.md) hold a claim register, specific questions and a sign-off form. Three hours of your time is the contribution the repository needs most today.
- **Ran a course with learners?** The [pilot protocol](03-courses/validation/pilot-protocol.md) says what to collect and how to send it. A pilot report is published as written.
- **Changing lab or tool code?** Standard library only, Python 3.9 or newer, and a test for every new behaviour. No key and no real data in any file. Run `make check` before a pull request.
- **Changing a deck?** Edit the fragment in `slides/src/`, then `python3 tools/build_slides.py`. One idea per slide; detail goes in the speaker notes.
- **Added a page or changed a heading?** Run `python3 tools/build_site.py` so the site's search index (`site-index.json`) is updated. If you cannot, send the pull request as it is and say so; a maintainer will update it.
- **Changing the completion standard or a rubric?** Bump the standard's version, and update `tools/score_submission.py` and its tests with it.
- Third-party components and their terms are listed in [THIRD-PARTY.md](THIRD-PARTY.md).

## Before you open a pull request

`make check` covers internal links, anchors, tables and the tests. Nothing after item 5 is checked by a program. If you cannot meet an item, send the pull request anyway and say which.

1. `make check` ends with no problem and every test passing.
2. `python3 tools/build_site.py` after any new page or changed heading; `site-index.json` is part of the change.
3. Built files are not edited by hand: `index.html`, `index.en.html`, the `.n8n.json` files, the built decks and what `tools/dataset_pack.py` builds. Edit the source, then build.
4. If the runnable templates changed: `python3 tools/build_n8n_workflows.py`, and any figure that moved (simulator baseline, case counts) is updated wherever it is quoted.
5. If the funding directory changed: `python3 tools/check_funding_directory.py`.
6. Every new figure or rule has an entry in [`SOURCES.md`](SOURCES.md): the claim as read, the issuer's own page, the date and the way it was read, and what was not read.
7. What was read from a search extract or a secondary summary says so. What could not be confirmed goes in the C series and stays out of the framework.
8. Paired files agree: the regulatory register in both languages, the funding directory and `funding-directory.json`, and the Arabic and English page of each guide that has both.
9. If you restored a removed item or left one out, update the [not-adopted record](02-saudi-market-knowledge-framework/not-adopted.md).
10. The verification-status line of a lesson whose sources changed gives the new count. "Not reviewed by a specialist" is removed only with a named sign-off in the [review packet](03-courses/validation/README.md).
11. Arabic text: no new `bidi_lint` error, and the page sits inside the `dir="rtl"` wrapper the other pages use.
12. No key, token or real data in any file.
13. An entry in [`CHANGELOG.md`](CHANGELOG.md) under "Unreleased" that says what was not tried and not reviewed.
14. The pull request description separates three things: what was done, how it was checked, and what waits for a specialist.

## If you do use Git

1. Open an issue describing the idea (optional for small edits).
2. Branch: `content/...`, `guide/...`, `agent/...` or `fix/...`.
3. Open a pull request. Its checklist is there to help, not as a gate. If you have Python, `make check` runs the same link check and script tests that run automatically on every pull request; if it reports something you cannot fix, send the pull request anyway and say so.

Contributions are licensed CC BY 4.0 (content) and Apache-2.0 (code).

**Thank you.** Every line you add saves a founder a day of searching.

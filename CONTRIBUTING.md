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
| 20 دقيقة | التحقق من بند عليه علامة ◻ في [السجل التنظيمي](02-saudi-market-knowledge-framework/regulatory-register.md) | أرسل الرابط الرسمي وتاريخ التحقق |
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

- **الأرقام والمعلومات التنظيمية لها مصدر.** أضفه إن عرفته، أو ضع علامة ◻ (للتحقق) ونبحث عنه معاً.
- **لا بيانات شخصية ولا أسرار.** لا مفاتيح API، ولا بيانات عملاء، ولا معلومات تجارية سرية.
- **المحتوى التنظيمي توعوي** وليس استشارة قانونية أو ضريبية.
- **الحياد.** نذكر الأدوات والجهات لقيمتها التعليمية، دون ترويج.
- **الاحترام.** راجع [ميثاق السلوك](CODE_OF_CONDUCT.md).

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
| 20 minutes | Verify an item marked ◻ in the [regulatory register](02-saudi-market-knowledge-framework/regulatory-register.md) | Send the official link and the date you checked |
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

- **Numbers and regulatory statements have a source.** Add it if you know it, or mark the item ◻ (to verify) and we will look for it together.
- **No personal data or secrets.** No API keys, customer data or confidential business information.
- **Regulatory content is educational**, not legal or tax advice.
- **Neutrality.** Tools and organisations are named for their teaching value, without promotion.
- **Respect.** See the [Code of Conduct](CODE_OF_CONDUCT.md).

## If you do use Git

1. Open an issue describing the idea (optional for small edits).
2. Branch: `content/...`, `guide/...`, `agent/...` or `fix/...`.
3. Open a pull request. Its checklist is there to help, not as a gate. If you have Python, `make check` runs the same link check and script tests that run automatically on every pull request; if it reports something you cannot fix, send the pull request anyway and say so.

Contributions are licensed CC BY 4.0 (content) and Apache-2.0 (code).

**Thank you.** Every line you add saves a founder a day of searching.

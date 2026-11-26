# سجل الأثر · Impact ledger

<div dir="rtl">

**تُقاس الأكاديمية بما ينجزه المشاركون في [رحلة المشروع](../journey/README.md)، لا بعدد مقرراتها ودروسها.** هذا السجل هو مقياسها الوحيد المعلن.

## الأرقام اليوم

آخر تحديث: **26 نوفمبر 2026** · لم يبدأ أي فوج بعد، وكل الأرقام أصفار.

| المقياس | النوع | الرقم | هدف التخطيط للفوج الأول (12 مشاركاً) |
|---|---|---|---|
| مشاركون قُبلوا | | 0 | 12 |
| مقابلات عملاء أُجريت | تعلّم | 0 | 96 |
| مشاركون أتمّوا التحقق من الفرصة (البوابة 1، أو توقف موثّق) | تعلّم | 0 | 9 |
| وكلاء اجتازوا تقييمهم | تعلّم | 0 | 7 |
| مشكلات متحقَّق منها (منشأتان صرّحتا باستعداد للدفع) | جسر | 0 | 6 |
| حلول تعمل في منشأة حقيقية، ظلاً أو تشغيلاً (البوابة 2) | جسر | 0 | 6 |
| تجارب مدفوعة موقّعة (البوابة 3) | أثر اقتصادي | 0 | 3 |
| عملاء يدفعون عند اليوم 180 | أثر اقتصادي | 0 | 2 |
| منشآت تبنّت وكيلاً بوفر مَقيس | أثر اقتصادي | 0 | 2 |
| إيراد المشاركين | أثر اقتصادي | 0 | يُذكر بفئته، دون هدف |

**أهداف التخطيط فرضيات** وُضعت لكي يظهر الإخفاق إن وقع. ليست مأخوذة من أي مرجع مقارن، ونتائج الفوج الأول هي التي تصير خط الأساس للفوج الثاني.

## القواعد

1. **الدليل أو لا شيء.** ما يقوله المشارك دون مُخرج يراه المقيِّم يُسجَّل «مُدَّعى»، ولا يدخل في الجدول أعلاه.
2. **المنسحبون والمتوقفون يُنشرون.** السجل يعرض كل من قُبل، لا من أتمّ فقط.
3. **النسبة إلى أصحابها.** نكتب «أنجز المشاركون»، ولا نكتب «حققت الأكاديمية».
4. **الخصوصية أولاً.** الإيراد والسعر بفئاتهما لا بمبالغهما. لا تُسمّى منشأة ولا مشارك إلا بموافقة مكتوبة. الفواتير والعقود يراها المقيِّم ولا تدخل المستودع.
5. **ملف واحد.** [`ledger.csv`](ledger.csv): صف لكل مشارك عند كل محطة، برمز لا باسم. يُحدَّث عند اليوم 0 و30 و60 و90 و180 من بداية الفوج.

## محطات المتابعة

| المحطة | الموضع في الرحلة | ما يُجمع | من يجمعه |
|---|---|---|---|
| اليوم 0 | القبول | المسار، والقطاع، وحالة المشروع السابقة، والساعات المتاحة | قائد الفوج |
| اليوم 30 | البوابة 1 | المقابلات، والمنشآت، والاستضافة، والقرار | مقيِّمان |
| اليوم 60 | البوابة 2 | نتيجة التقييم، وأيام الظل، وتقرير المقارنة | مقيِّمان |
| اليوم 90 | البوابة 3 | شروط التجربة، وفئة السعر، والفاتورة، وتاريخ التشغيل | مقيِّمان |
| اليوم 180 | المتابعة | استمرار العميل، وفئة الإيراد، والعميل الثاني، والوفر، وحالة المشروع | قائد الفوج |

## ما لم يعد مقياساً

عدد المقررات والدروس والبطاقات والساعات والإصدارات والإيداعات. يبقى ذلك كله في [سجل التغييرات](../CHANGELOG.md)، ولا يُعرض بوصفه تقدماً.

</div>

---

## English

**The Academy is measured by what participants achieve on the [venture journey](../journey/README.md), not by its count of courses and lessons.** This ledger is its only headline measure.

**Today (26 November 2026): no cohort has started, and every number is zero.** The table above lists each measure, its kind (learning, bridge, economic impact) and a planning target for a first cohort of twelve: 9 through opportunity validation, 6 solutions running in a real business, 3 signed paid pilots, 2 paying customers at day 180. The targets are hypotheses, set so that failure is visible; they come from no benchmark.

**Rules.** (1) Evidence or nothing: a claim without an artifact the assessor has seen is recorded as "claimed" and left out. (2) Dropouts and no-gos are published. (3) Modest attribution: "participants achieved", never "the Academy generated". (4) Privacy first: revenue and price in bands; no business or participant named without written consent; invoices and contracts are seen by the assessor and never enter the repository. (5) One file, [`ledger.csv`](ledger.csv): one row per participant per checkpoint, by code, updated at days 0, 30, 60, 90 and 180 from the cohort's start.

**No longer a measure:** courses, lessons, cards, hours, releases and commits. They stay in the changelog and are not presented as progress.

### Columns of `ledger.csv`

| Column | Meaning |
|---|---|
| `cohort`, `participant` | Cohort label and participant code (no names) |
| `route` | `founder-low-code`, `founder-developer` or `adopter` |
| `sector`, `checkpoint`, `date` | Sector; day 0, 30, 60, 90 or 180; date recorded |
| `interviews`, `businesses_reached`, `host_secured` | Counts and yes/no at Gate 1 |
| `gate_1`, `gate_2`, `gate_3` | `passed`, `no-go`, `held`, `withdrawn` or empty |
| `shadow_days` | Working days in shadow mode |
| `price_band`, `revenue_band` | Bands in SAR per month, set by the cohort lead before the cohort |
| `customer_retained`, `second_customer`, `saving_measured` | Day-180 answers |
| `venture_status` | `continuing`, `holding` or `stopped` |
| `evidence_seen` | `yes`, or `claimed` |
| `notes` | One line, nothing identifying |

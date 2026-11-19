# A3: حالة موثّقة من مصادر مفتوحة
# A3: A sourced case from open sources

**Tool:** the Academy's [Sourced Case Builder skill](../skills/README.md#12-sourced-case-builder) and [`case_lint.py`](a3-sourced-case/case_lint.py) · **Courses 3 and 4**, Modules 3.2, 3.5 and 4.5 · **Time:** two to three hours

<div dir="rtl">

## الغرض

تكتب صفحة واحدة عن شركة حقيقية يصح أن تُدرَّس: كل واقعة لها مصدر، وما لا مصدر له مكتوب صراحةً أنه مجهول. المهارة نفسها تحتاج إليها حين تكتب عن منافس في عرضك، أو عن عميل في دراسة حالة.

## لماذا هذا التمرين؟

سبع حالات في [مسارات الشركات](../../06-case-studies/ventures/README.md) أُعيدت كتابتها من مصادر، بعد أن تبيّن أن نصوصها السابقة، وهي بلا مصادر، أخطأت في سنة التأسيس أو المدينة أو طبيعة النشاط في ثلاث منها. النص المقنع بلا مصدر هو أخطر ما يكتبه مساعد ذكي، وأخطر ما ينقله مؤسس في عرضه.

## ما تحتاجه

- شركة تقنية تعمل في المملكة، **ليست** من السبع المنشورة.
- مساعد يبحث ويفتح الصفحات، أو ساعة تجمع فيها المصادر بنفسك.

## الجزء الأول: اكشف العيوب (30 دقيقة)

</div>

```bash
cd saudi-agentic-ai-entrepreneurship-academy
python3 05-agentic-ai-lab/exercises/a3-sourced-case/case_lint.py \
  05-agentic-ai-lab/exercises/a3-sourced-case/sample-draft.md --sources SOURCES.md
```

<div dir="rtl">

المسودة التدريبية عن شركة **مختلقة**. المدقق يجد فيها خمسة أخطاء وتنبيهاً واحداً. أصلحها حتى يمر الملف.

ثم اقرأها بعينك. فيها عيبان لا يراهما المدقق:

1. ادعاء بأن الشركة «تستخدم وكلاء يديرون 80% من الحجوزات»، تحت «ما هو موثّق»، بلا مصدر عند السطر.
2. رقم تمويل بلا تاريخ ولا اسم من قاد الجولة.

المدقق يفحص **الشكل**. صحة الواقعة يفحصها إنسان يفتح الرابط.

## الجزء الثاني: اكتب حالتك (ساعة إلى ساعتين)

1. شغّل المهارة 12 على شركتك. إن كان المساعد لا يبحث فاجمع أنت: صفحة الشركة، بيانان صحفيان، وتغطيتان.
2. **افتح كل رابط بنفسك.** لكل واقعة في جدول الوقائع: هل الجملة موجودة في الصفحة فعلاً؟ بأي تاريخ؟ من قالها؟
3. صنّف: وثيقة رسمية، إعلان الشركة، صحافة. رقم تقوله الشركة عن نفسها يُكتب «معلن ذاتياً».
4. اكتب «ما لا تقوله المصادر» قبل «الدرس». ما تجهله يحدّ ما يحق لك استنتاجه.
5. شغّل المدقق مع `--strict`.

</div>

```bash
python3 05-agentic-ai-lab/exercises/a3-sourced-case/case_lint.py my-case.md --strict
```

<div dir="rtl">

بلا `--sources` لا يتحقق المدقق من أرقام السجل، فاكتب مصادرك روابط كاملة في سطر المصادر، مع رقم مؤقت مثل `[A0]`.

## الجزء الثالث: قائمة «لم أتحقق منه» (15 دقيقة)

| ما قاله المساعد أو ما كنت أظنه | هل وجدت مصدراً؟ | القرار |
|---|---|---|
| | | حُذف · بقي بمصدر · نُقل إلى «ما لا تقوله المصادر» |

إن خلت القائمة فالأرجح أنك لم تفتح الروابط.

## معيار الإنجاز

- [ ] المسودة التدريبية تمر بلا أخطاء، والعيبان الآخران مكتوبان.
- [ ] حالتك تمر مع `--strict`.
- [ ] كل واقعة فُتح رابطها، ولها تاريخ.
- [ ] قائمة «لم أتحقق منه» فيها ثلاثة بنود على الأقل.
- [ ] لا جملة تقول إن الشركة تستخدم وكلاء ما لم يقلها مصدر.

## بعده

حالة جيدة عن شركة سعودية يمكن أن تُضاف إلى المكتبة: افتح [طلب حالة جديدة](../../.github/ISSUE_TEMPLATE/new-case-study.md)، وستُراجَع مصادرها قبل النشر.

</div>

---

**English.** Part one runs `case_lint.py` on a deliberately flawed draft about an invented company (five errors and one warning), then asks the learner to find two defects the linter cannot see: an unsourced claim about agents and a funding figure with no date. Part two writes a one-page sourced case about a real technology company in the Kingdom with the Sourced Case Builder skill, opening every link by hand. Part three lists what the assistant asserted and no source confirmed. The linter checks form; a person checks truth.

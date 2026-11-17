# تمارين المختبر · Lab exercises

Last reviewed: 17 November 2026

<div dir="rtl">

ثمانية تمارين عملية تستخدم أدوات المستودعين المرافقين: [«ريادة»](https://github.com/malenezi/riyada) (الرمز R) و[«بيان»](https://github.com/malenezi/bayan) (الرمز B). كل تمرين يأخذ مخرجاً من مقرر ويحوّله إلى شيء يُفحص: ملف يمر من مدقق، أو نموذج يُبنى بلا تحذير مانع. لماذا هذه الأدوات وكيف ترتبط بالمنهج: [المستودعات المرافقة](../../07-resources/companion-repositories.md).

| # | التمرين | الأداة | المقرر والوحدة | الزمن | معيار الإنجاز |
|---|---|---|---|---|---|
| R1 | [بطاقة الأدلة وبطاقة التجربة](r1-evidence-scorecard-and-experiment.md) | «ريادة» | 1 · 1.3 و1.6 وما بعد الأطروحة | 90 دقيقة | قاعدة قرار مكتوبة قبل التجربة |
| R2 | [حزمة سياق تمر من المدقق](r2-context-pack.md) | «ريادة» | 2 · 2.2 | ساعتان إلى ثلاث | `context_lint.py` بلا أخطاء |
| R3 | [بطاقة الدور ومصفوفة الاعتماد](r3-role-card-and-approval-matrix.md) | «ريادة» | 2 · 2.1 و2.6 | ساعتان | وسيلة إنفاذ لكل حد |
| R4 | [من تكلفة المهمة إلى نموذج 36 شهراً](r4-financial-model.md) | «ريادة» | 3 · 3.3، و4 · 4.5 | 90 دقيقة | النموذج يُبنى، والنقد لا يصير سالباً دون تفسير |
| B1 | [رسائل الوكيل بالعربية](b1-agent-messages-in-arabic.md) | «بيان» | 2 · 2.2، و3 · 3.1 | 90 دقيقة | `i18n_parity.py` و`bidi_lint.py` بلا ملاحظات |
| B2 | [صفحة هبوط ثنائية اللغة للتجربة](b2-bilingual-landing-page.md) | «بيان» | 3 · 3.5 | ساعتان إلى ثلاث | المدققان بلا ملاحظات |
| B3 | [عرض الأطروحة أو العرض الاستثماري](b3-pitch-deck.md) | «بيان» | 4 · 4.6، واختيارياً 1 · 1.7 | ثلاث ساعات | `--profile deck --strict` بلا ملاحظات |
| B4 | [تدقيق اتجاه واجهة قائمة](b4-rtl-audit.md) | «بيان» | المسار العميق في 3 و4 | ساعتان | تقرير قبل وبعد، والأخطاء صفر |

## قبل أن تبدأ

</div>

```bash
git clone https://github.com/malenezi/riyada
git clone https://github.com/malenezi/bayan
python3 --version   # 3.9 or newer
```

<div dir="rtl">

- الأوامر في التمارين تُشغَّل من المجلد الذي يحوي المستودعين.
- **بلا وكيل:** انسخ القالب واملأه باليد، ثم شغّل البرنامج. كل التمارين تعمل هكذا.
- **مع وكيل:** ثبّت المهارة واطلب منه العمل، ثم راجع كل ما كتبه. الوكيل يقترح وأنت تقرر.
- **بيانات مصطنعة فقط.** لا أسماء عملاء ولا أرقام حقيقية في أي ملف ولا في أي مساعد.
- ما يخص الأنظمة السعودية يُؤخذ من [إطار المعرفة](../../02-saudi-market-knowledge-framework/README.md). أدوات «ريادة» عامة ولا تعرف المملكة.

## الحالة

الأوامر الواردة في التمارين شُغّلت على «ريادة» (الإيداع `d2a0607`) و«بيان» (الإيداع `db941e2`) في تاريخ المراجعة. التمارين نفسها لم تُجرَّب مع متعلمين بعد. إن تعثرت في خطوة فافتح Issue.

</div>

---

**English.** Eight hands-on exercises that use the two companion repositories: four with Riyada (R1 to R4) and four with Bayan (B1 to B4). Each takes a course deliverable and turns it into something a script can check. All of them work without an agent, by filling templates by hand and running the scripts. The commands were run on the review date; the exercises have not been tried with learners yet.

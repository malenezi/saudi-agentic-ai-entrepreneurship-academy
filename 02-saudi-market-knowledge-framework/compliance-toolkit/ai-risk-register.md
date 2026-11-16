# سجل مخاطر نظام الذكاء الاصطناعي · AI system risk register

A register is useful only if its entries are specific to your product. Start from the examples, delete what does not apply and add what does. Review monthly.

**المشروع · Venture:** ____________  **آخر مراجعة · Last review:** ____________

## مقياس التقييم · Scoring

| | 1 | 2 | 3 |
|---|---|---|---|
| الاحتمال · Likelihood | نادر · Rare | ممكن · Possible | متوقع · Likely |
| الأثر · Impact | إزعاج · Nuisance | خسارة أو شكوى · Loss or complaint | ضرر جسيم أو مخالفة · Serious harm or violation |

الدرجة = الاحتمال × الأثر. Score = likelihood × impact. 6 or above needs a control in place before launch.

## السجل · Register

| # | الخطر · Risk | الفئة · Category | الاحتمال | الأثر | الدرجة | الضابط · Control | المالك · Owner | الحالة · Status |
|---|---|---|---|---|---|---|---|---|
| 1 | الوكيل يعطي معلومة خاطئة عن السعر أو التوفر · Agent states a wrong price or availability | جودة · Quality | 2 | 2 | 4 | الإجابة من مصدر البيانات مباشرة، لا من النموذج · Answer from the data source, not model memory | | |
| 2 | سوء فهم اللهجة يؤدي إلى إجراء خاطئ · Dialect misunderstanding leads to a wrong action | جودة · Quality | 2 | 2 | 4 | حالات لهجة في مجموعة التقييم؛ تأكيد قبل التنفيذ · Dialect cases in the test set; confirm before acting | | |
| 3 | حقن تعليمات عبر رسالة عميل أو مستند · Prompt injection through a message or document | أمن · Security | 2 | 3 | 6 | صلاحيات خارج النموذج؛ اختبار حقن دوري · Permissions outside the model; periodic injection tests | | |
| 4 | إرسال بيانات شخصية إلى مزوّد خارج المملكة دون ضوابط · Personal data sent abroad without safeguards | امتثال · Compliance | 2 | 3 | 6 | حجب المعرّفات؛ تقييم المزوّدين · Redaction; provider assessment | | |
| 5 | تنفيذ إجراء مالي دون موافقة · Financial action without approval | صلاحيات · Authority | 1 | 3 | 3 | بوابة موافقة؛ مفتاح الدفع غير متاح للوكيل · Approval gate; no payment key for the agent | | |
| 6 | تغيّر سلوك النموذج بعد تحديث المزوّد · Model behaviour changes after a provider update | تشغيل · Operations | 2 | 2 | 4 | تثبيت الإصدار؛ اختبار انحدار قبل الترقية · Pin version; regression test before upgrade | | |
| 7 | ارتفاع التكلفة بسبب حلقات أو إساءة استخدام · Cost spike from loops or abuse | مالي · Financial | 2 | 2 | 4 | حدود للخطوات والإنفاق؛ تنبيهات · Step and spend caps; alerts | | |
| 8 | معاملة غير متساوية بين فئات العملاء · Unequal treatment across customer groups | عدالة · Fairness | 1 | 3 | 3 | مقارنة النتائج بين المجموعات في التقييم · Compare results across groups in evaluation | | |
| 9 | توقف المزوّد الرئيسي · Main provider outage | استمرارية · Continuity | 2 | 2 | 4 | مزوّد بديل مجرَّب؛ تحويل إلى موظف · Tested fallback provider; route to a person | | |
| 10 | العميل لا يعلم أنه يتعامل مع وكيل · Customer unaware they are dealing with an agent | شفافية · Transparency | 1 | 2 | 2 | رسالة إفصاح في بداية المحادثة · Disclosure at the start | | |
| | | | | | | | | |

## الحوادث · Incident log

| التاريخ · Date | ما حدث · What happened | الأثر · Impact | السبب · Cause | الإصلاح · Fix | هل أُضيف إلى مجموعة التقييم؟ · Added to the test set? |
|---|---|---|---|---|---|
| | | | | | |

Every incident should end as a new test case, so it cannot recur unnoticed.

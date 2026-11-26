# بروتوكول التجربة صفر: وكيل في وضع الظل داخل متجر حقيقي
# Pilot zero protocol: an agent in shadow mode in one real store

**Status:** written 26 November 2026 · **no pilot has been run** · no store has agreed · no lawyer has reviewed the host agreement or the data questions

<div dir="rtl">

[رحلة المشروع](../../journey/README.md) · [وصفة الربط](../../05-agentic-ai-lab/agent-templates/workflows/recipes/online-store.md) · [بروتوكول الفوج الأول](pilot-protocol.md)

> **لم تُجرَ التجربة بعد.** هذا الملف خطتها: ما يُختبر، وبمَ يُحكم عليه، وما يُسجَّل، وكيف يُوقَف كل شيء في دقيقة. يسبق [الفوج الأول](pilot-protocol.md) ولا يغني عنه: هناك يُختبر التعليم، وهنا يُختبر الوكيل والربط.

## 1. ما الذي تجيب عنه التجربة

| السؤال | لماذا لا يُجاب عنه من المكتب |
|---|---|
| هل تتصرف القناة والمنصة كما تقول وثائقهما؟ | الوثائق قُرئت آلياً، ولم يُشغَّل شيء مع أي مزوّد |
| ما الرقم الذي يكتبه العميل حين يسأل عن طلبه، وبأي حقل يُستعلَم عنه؟ | وثائق المنصتين لا تحسمه |
| كم من رسائل المتجر الحقيقية كان الوكيل سيجيب عنه صواباً، وكم كان سيحوّله؟ | كل حالات الاختبار في المستودع مختلقة |
| أين يخالف الوكيل الموظف، ومن المصيب؟ | لا يُعرف دون سجل الموظفين |
| ما الذي يحتاجه صاحب المتجر ليثق؟ | لا يُعرف دون صاحب متجر |

**ما لا تجيب عنه:** هل يدفع أحد. ذلك للبوابة 3.

## 2. الحدود

- **قالب واحد:** [القالب 1، خدمة العملاء](../../05-agentic-ai-lab/agent-templates/01-whatsapp-customer-service.md). **متجر واحد.** **عشرة أيام عمل:** خمسة للتجهيز والاختبار، وخمسة للظل.
- **قراءة فقط.** لا رسالة تخرج إلى عميل، ولا كتابة في المتجر، ولا صلاحية كتابة تُطلب من المنصة.
- **الموظفون يعملون كعادتهم.** لا يرون ما كان الوكيل سيفعله إلا بعد انتهاء الأيام الخمسة.
- **لا منتجات منظَّمة:** لا صحة ولا مالية ولا ما يُشترط له عمر.

## 3. مساران، يُختار أحدهما قبل البدء

| | المسار أ: رسائل مصدَّرة | المسار ب: ربط حي |
|---|---|---|
| ما هو | صاحب المتجر يصدّر رسائل أسبوع مضى وردود موظفيه، وتُحجب، ثم تُشغَّل على القالب | نقطة استقبال حقيقية تتلقى الرسائل من القناة، وتستعلم من المنصة |
| ما يتحقق منه | جودة الوكيل على رسائل حقيقية، ورقم الطلب الذي يكتبه العملاء | ذلك كله، ومعه التوقيع، والتكرار، والاستعلام، ونافذة الرد |
| ما لا يتحقق منه | أي شيء عن القناة والمنصة | |
| ما يحتاجه | موافقة صاحب المتجر، وتصدير | حساب مطوّر لدى القناة، وتطبيق شريك لدى المنصة، وخادم بشهادة صالحة، ومراجعة قانونية لمسار البيانات |
| متى | يبدأ فور توفر المتجر | بعد المسار أ |

**الموصى به:** المسار أ أولاً. يكفي لإصدار 0.15 بصدق، ولا يحتاج إلى حساب عند أي مزوّد. المسار ب يُضاف حين تتوفر شروطه، ويُسجَّل ما تحقق منه بنداً بنداً.

## 4. قبل اليوم الأول

- [ ] اتفاق استضافة من صفحة واحدة، موقّع (القسم 9).
- [ ] صاحب المتجر قرأ ما يُصدَّر، وكيف يُحجب، وأين يُعالج، ووافق كتابةً.
- [ ] محامٍ اطّلع على الاتفاق ومسار البيانات. **دونه لا تُعالج رسالة حقيقية واحدة.**
- [ ] معرفة المتجر المعتمدة مكتوبة: سياسات الشحن والاسترجاع والدفع، كما يجيب بها الموظفون.
- [ ] حدّ القبول (القسم 6) موقّع عليه من صاحب المتجر ومن المنفّذ، **قبل** أن تُرى أي نتيجة.
- [ ] `python3 tools/store_adapter.py --self-check` و`make check` ينجحان على الجهاز المستعمل.
- [ ] النموذج اللغوي محدَّد، ومكان معالجته معروف. إن لم تُحسم مسألة خروج البيانات فالنموذج محلي.

## 5. حالات الاختبار

تُشغَّل كلها في أيام التجهيز، قبل أول رسالة حقيقية. «المتوقع» ما يجب أن يحدث، وأي نتيجة غيره تُسجَّل ولا تُفسَّر.

**أ. تُختبر محلياً اليوم** (في [`tests/test_store_adapter.py`](../../tests/test_store_adapter.py)، على حمولات مبنية من الوثائق):

| # | الحالة | المتوقع |
|---|---|---|
| L1 | إشعار بتوقيع صحيح، ثم الإشعار نفسه بحرف زائد في نصه | يُقبل الأول، ويُرفض الثاني |
| L2 | إشعار بتوقيع مزوّر | يُرفض، ولا استعلام عن أي طلب |
| L3 | الرسالة نفسها تعود بعد ستة أيام | تُعالج مرة واحدة، ولا استعلام ثانٍ |
| L4 | إشعار حالة تسليم، لا رسالة | يُتجاهل |
| L5 | رقم طلب بأرقام هندية (٢٠٠٣٤٥) | يُفهم 200345 |
| L6 | رقم جوال في الرسالة، أو «3 قطع بسعر 250» | لا يُعدّ رقم طلب |
| L7 | رقمَا طلبين في رسالة واحدة | تحويل إلى موظف دون استعلام |
| L8 | طلب صحيح يسأل عنه رقم غير رقم صاحبه | تحويل إلى موظف، ولا يخرج من تفاصيل الطلب شيء |
| L9 | رقم طلب لا وجود له، أو بحث يعيد أكثر من طلب | تحويل إلى موظف، لا تخمين |
| L10 | صورة أو مقطع صوتي | تحويل إلى موظف |
| L11 | رسالة مضى عليها أكثر من 24 ساعة | تُعلَّم بأن الرد الحر لم يعد مسموحاً |

**ب. لا تُختبر إلا مع مزوّد** (المسار ب). لم تُشغَّل واحدة منها:

| # | الحالة | المتوقع بحسب الوثائق | الدليل |
|---|---|---|---|
| P1 | التحقق من نقطة الاستقبال عند القناة | طلب GET، وردّ بقيمة التحدي | لقطة لحالة الاشتراك |
| P2 | رسالة حقيقية من رقم اختبار | تصل بتوقيع يطابق الحساب المحلي | الترويسة ونتيجة التحقق |
| P3 | نقطة الاستقبال تردّ بـ500 مرة واحدة | تعود الرسالة بالمعرّف نفسه، وتُعالج مرة | سطران في السجل بمعرّف واحد |
| P4 | استعلام عن طلب اختبار في سلة بـ`reference_id` | طلب واحد، هو المقصود | الطلب والرد دون بيانات العميل |
| P5 | استعلام عن طلب اختبار في زد بـ`search_term` | يعيد الطلب، وقد يعيد غيره | عدد النتائج، وهل طابق `code` |
| P6 | **ما الرقم في رسالة تأكيد الطلب التي تصل العميل؟** | غير معلوم | صورة رسالة تأكيد لطلب اختبار، والحقل الذي يطابقها |
| P7 | رمز وصول منتهٍ | الاستعلام يفشل، والتحويل إلى موظف يعمل | سطر السجل |
| P8 | رقم جوال العميل في الطلب، بأي صيغة يعود | يطابق رقم المرسل بعد التوحيد | صيغتان دون الأرقام نفسها |
| P9 | ردّ بعد 24 ساعة من آخر رسالة للعميل (على رقم اختبار فقط) | يُرفض الرد الحر | رمز الخطأ |
| P10 | إشعار من المنصة بتوقيعه أو ببياناته الأساسية | يطابق الحساب المحلي | نتيجة التحقق |

**ج. على رسائل المتجر الحقيقية** (المساران):

| # | ما يُقاس | كيف |
|---|---|---|
| R1 | نسبة ما كان الوكيل سيجيب عنه كما أجاب الموظف | [تقرير المقارنة](../../05-agentic-ai-lab/agent-templates/workflows/shadow-mode/README.md) |
| R2 | نسبة ما حوّله وكان التحويل في محله | مراجعة يدوية لكل تحويل |
| R3 | **ما أجاب عنه وكان عليه أن يحوّله** | مراجعة يدوية لكل جواب مستقل |
| R4 | صيغ رقم الطلب كما يكتبها العملاء فعلاً | عدّ يدوي من الرسائل |
| R5 | أنواع الأسئلة التي لا تغطيها معرفة المتجر المعتمدة | قائمة |

## 6. شروط القبول

توضع أرقامها مع صاحب المتجر قبل البدء. المقترح نقطة بداية لا معيار:

| الشرط | المقترح | إن لم يتحقق |
|---|---|---|
| حالات المجموعة أ | كلها تنجح | لا تبدأ التجربة |
| R3: جواب مستقل كان يجب أن يُحوَّل | **صفر** في ما يمس مالاً أو وعداً أو بيانات عميل آخر | تتوقف التجربة، ويُصلح السبب، وتُعاد الأيام الخمسة |
| تفاصيل طلب خرجت لغير صاحبه | **صفر** | تتوقف التجربة فوراً (القسم 8) |
| R1: موافقة الموظف في الأسئلة المتكررة | يحدده صاحب المتجر قبل البدء | تُسجَّل النتيجة كما هي، وهي ليست فشلاً للتجربة |
| عدد الرسائل | يكفي ليظهر كل نوع سؤال متكرر مرات عدة؛ يُحدَّد من حجم المتجر | تُمدَّد الأيام، ولا تُكمَّل برسائل مختلقة |
| المجموعة ب، إن سُلك المسار ب | كل حالة: «تحقق»، أو «خالف الوثائق» مع ما حدث | ما لم يُشغَّل يبقى «لم يُتحقق منه» |

**نجاح التجربة** أن تنتهي بأجوبة عن أسئلة القسم 1، لا أن يكون الوكيل جيداً. وكيل ضعيف بدليل واضح نتيجة صالحة.

## 7. سجل الأدلة

ملف واحد لكل نوع، في مجلد خاص لا يدخل المستودع. ما يدخل المستودع هو التقرير وحده، بعد الحجب.

| السجل | ما فيه | من يكتبه | يدخل المستودع؟ |
|---|---|---|---|
| سجل الظل | سطر لكل رسالة: المرجع، والوقت، وما كان الوكيل سيفعله | القالب في وضع الظل | لا. عيّنة محجوبة فقط |
| سجل التدقيق | سطر لكل استدعاء: بصمة الرسالة، والمدة، والقرار، ورقم الجوال محجوباً | [`tools/reality_run.py`](../../tools/reality_run.py) | بعد الحجب |
| سجل الموظفين | ما فعله الموظف بكل رسالة | المتجر | لا |
| سجل حالات الاختبار | لكل حالة من القسم 5: التاريخ، والنتيجة، والدليل | المنفّذ | نعم |
| سجل الحوادث | كل توقف، وسببه، وما فُعل | المنفّذ | نعم، دون ما يعرّف |
| سجل العوائق | كل ما أوقف المنفّذ أو أخّره | المنفّذ | بلاغات `friction` |

**ثلاث حالات لكل بند في التقرير، لا رابعة:** «تحقق مع المزوّد» ومعه دليله، أو «اختُبر محلياً» ومعه اسم الاختبار، أو «لم يُتحقق منه».

## 8. الإيقاف والتراجع

الوكيل لا يرسل شيئاً، فلا رسالة تُسحب. ما يُتراجع عنه هو الوصول والبيانات.

**أوقف فوراً إن:** خرجت تفاصيل طلب لغير صاحبه، أو خرجت رسالة إلى عميل، أو كُتب شيء في المتجر، أو طلب صاحب المتجر التوقف، أو ظهرت بيانات غير محجوبة خارج جهاز المنفّذ.

| الخطوة | من | الزمن المستهدف | التحقق |
|---|---|---|---|
| 1. إيقاف استقبال الرسائل: تعطيل سير العمل، أو إلغاء اشتراك نقطة الاستقبال | المنفّذ | دقيقة | رسالة اختبار لا تُسجَّل |
| 2. إبطال الوصول: حذف تطبيق الشريك من المتجر، أو إبطال رمزه | صاحب المتجر | في اليوم نفسه | استعلام يفشل |
| 3. إبلاغ صاحب المتجر بما حدث، كتابةً | المنفّذ | في اليوم نفسه | رده |
| 4. إتلاف ما صُدِّر من رسائل، وسجل الظل | المنفّذ | بحسب الاتفاق | إقرار مكتوب |
| 5. سطر في سجل الحوادث، وبلاغ `friction` دون ما يعرّف | المنفّذ | خلال يومين | رقم البلاغ |

**يُجرَّب الإيقاف في أيام التجهيز،** مرة واحدة على الأقل، ويُسجَّل زمنه. إيقاف لم يُجرَّب ليس إجراءً.

**ما يتجاوز هذا الملف:** هل يلزم إبلاغ جهة أو عميل عند حادثة بيانات، ومتى. هذا سؤال للمحامي قبل اليوم الأول، وجوابه يُكتب في الاتفاق.

## 9. اتفاق الاستضافة: ما يتضمنه

قائمة بما يُتفق عليه، وليست صيغة ملزمة. الصيغة للمحامي.

1. **ما نفعله:** نشغّل وكيلاً يقرأ رسائل عملاء المتجر وحالة طلباتهم، ويسجّل ما كان سيفعله.
2. **ما لا نفعله:** لا نرسل إلى أي عميل، ولا نغيّر شيئاً في المتجر، ولا نستعمل البيانات لغير هذه التجربة.
3. **البيانات:** ما يُصدَّر أو يُقرأ، وكيف يُحجب، وأين يُعالج، ومن يراه، ومتى يُتلف.
4. **المدة:** عشرة أيام عمل، ولصاحب المتجر أن يوقف في أي لحظة دون سبب.
5. **ما يحصل عليه المتجر:** تقرير المقارنة كاملاً، وورقة عائد المشتري من أرقامه، دون مقابل ودون التزام.
6. **النشر:** تنشر الأكاديمية النتائج دون اسم المتجر ولا ما يدل عليه، إلا بموافقة مكتوبة أخرى.
7. **المسؤولية وحادثة البيانات:** يصوغها المحامي.

## 10. التقرير

صفحة في `03-courses/validation/pilots/`، فيها: نوع المتجر دون اسمه، والمسار المسلوك، وعدد الرسائل، ونتيجة كل حالة اختبار بحالتها الثلاثية، وأرقام R1 إلى R5، وكل حادثة، وكل عائق، وما تغيّر في الوصفة والقالب بعدها، وما قاله صاحب المتجر بنصّه. ثم يُحدَّث سطر الحالة في [الوصفة](../../05-agentic-ai-lab/agent-templates/workflows/recipes/online-store.md) و[سجل الأثر](../../impact/README.md).

</div>

---

## English

**No pilot has been run.** This is the plan for one: what is tested, what it is judged by, what is logged, and how everything is stopped within a minute. It precedes the [first cohort's protocol](pilot-protocol.md), which tests the teaching; this one tests the agent and the integration.

**Scope.** One template (customer service), one store, ten working days: five to prepare and test, five in shadow mode. Read only: nothing is sent to a customer and nothing is written to the store. Staff work as usual and see the agent's proposed actions only afterwards. No regulated products.

**Two routes.** *Route A, exported messages:* the owner exports a past week of messages and staff replies, they are masked, and the template runs on them. It tests the agent on real messages and shows how customers actually write order numbers; it tests nothing about the channel or the platform, and it needs no provider account. *Route B, live connection:* a real endpoint, which also tests signatures, duplicates, order lookup and the reply window, and needs a developer account with the channel, a partner app with the platform, a server with a valid certificate, and a legal review of the data flow. **Recommended: Route A first.** It is enough for an honest v0.15.

**Test scenarios.** Eleven local cases (L1 to L11) run today in `tests/test_store_adapter.py` on payloads built from the documentation: signature accepted and rejected, a forged webhook, a message retried on day six, status notifications ignored, Arabic-Indic digits, a mobile number not mistaken for an order, two order numbers, an order asked about by someone else's number, an unknown or ambiguous order, non-text messages, and a message older than 24 hours. Ten provider cases (P1 to P10) can only run with a provider and **none has been run**; P6 asks the open question directly: which number appears in the order confirmation a customer receives. Five measures on the store's real messages (R1 to R5), the most important being R3: what the agent answered alone and should have handed over.

**Acceptance.** Set with the owner before any result is seen. All local cases pass, or the pilot does not start. Zero autonomous answers that touch money, a promise or another customer's data. Zero order details shown to anyone but the order's customer. Agreement with staff is recorded as found and is not a pass mark. The pilot succeeds when it answers its questions, not when the agent is good.

**Evidence.** Shadow log, audit log, staff record, test-scenario log, incident log and friction issues. Raw logs stay out of the repository; the masked report goes in. Every item in the report carries one of three states and no other: *verified with the provider* with its evidence, *tested locally* with the test's name, or *not verified*.

**Stop and roll back.** The agent sends nothing, so what is rolled back is access and data: stop intake within a minute; have the owner revoke the app's access the same day; tell the owner in writing; destroy the exported messages and the shadow log as agreed; record the incident. The stop is rehearsed once during preparation and timed. Whether an authority or a customer must be notified after a data incident is a question for the lawyer before day one.

**Host agreement.** A list of what to agree, not binding wording: what is done, what is not, the data, the ten days and the owner's right to stop at any moment, what the store receives (the full comparison report and a buyer-return sheet, free), publication without the store's name, and liability, which the lawyer drafts.

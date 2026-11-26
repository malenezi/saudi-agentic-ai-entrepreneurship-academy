# وصفة الربط: متجر إلكتروني · Integration recipe: an online store

**Status:** written 26 November 2026 from the providers' own developer documentation · **not run with any provider** · the adapter's deterministic rules are written and tested locally (`tools/store_adapter.py`, 22 tests) and are not wired into n8n · no lawyer has reviewed the data questions at the end

<div dir="rtl">

كيف يلتقي [القالب 1 (خدمة العملاء)](../../01-whatsapp-customer-service.md) بقناة حقيقية ونظام حقيقي في متجر إلكتروني: رسالة عميل تدخل، وطلب يُستعلَم عنه برقمه. هذه أول وصفة ربط في الأكاديمية، وهي لقطاع [رحلة المشروع](../../../../journey/README.md) الأول.

> **ما هذه الوصفة وما ليست.** هي ما تقوله وثائق المزوّدين عن نقاط الربط التي يحتاجها القالب، مع ما لم تقله. **لم تُشغَّل مع أي مزوّد.** ليست سير عمل جاهزاً: المحوّل الموصوف في القسم 4 لم يُبنَ بعد، وأول تشغيل له يكون في متجر حقيقي في وضع الظل. ما تكشفه تلك التجربة يُصحَّح هنا.

> **تسمية المزوّد ليست تزكية له.** سُمّيت «سلة» و«زد» و«منصة واتساب للأعمال» لأن الوصفة لا تُكتب دون وثائق بعينها. الأكاديمية لا توصي بمزوّد، ولا علاقة لها بأي منهم. إن كان متجرك على منصة أخرى فالبنية واحدة، والأسماء تتغير.

> **كيف قُرئت المصادر.** فُتحت كل صفحة في 26 نوفمبر 2026 بقراءة آلية تجيب عن أسئلة محددة، لا بقراءة إنسان للصفحة كاملة. كل بند في الجداول يحمل رقم مصدره في [سجل المصادر](../../../../SOURCES.md) (A254 إلى A265). **قبل أن تبني على بند، افتح صفحته.**

## ما المنفَّذ، وما المختبَر، وما المتحقَّق منه

ثلاث حالات لا رابعة: **تحقق مع المزوّد** (بدليل من تشغيل فعلي)، أو **اختُبر محلياً** (على حمولات مبنية من الوثائق)، أو **لم يُتحقق منه**.

| القدرة | منفَّذة | مختبَرة محلياً | متحقَّق منها مع المزوّد |
|---|---|---|---|
| التحقق من توقيع إشعار القناة (`X-Hub-Signature-256`) | نعم | نعم | **لا** |
| التحقق من نقطة الاستقبال (`hub.challenge`) | نعم | نعم | **لا** |
| توقيع إشعارات سلة، وبيانات زد الأساسية | نعم | نعم | **لا** |
| إزالة التكرار بمعرّف الرسالة، لأكثر من سبعة أيام | نعم | نعم | **لا** |
| قراءة الرسالة النصية من حمولة القناة | نعم | نعم | **لا** |
| استخراج رقم الطلب مما يكتبه العميل | نعم | نعم، على أمثلة مختلقة | **لا.** لم تُرَ رسالة عميل حقيقية |
| الاستعلام عن الطلب في سلة وزد | الطلب موصوف، ولا يُرسَل | صيغة الطلب فقط | **لا** |
| مطابقة رقم المرسل برقم صاحب الطلب | نعم | نعم | **لا.** صيغة الرقم العائدة من المنصتين لم تُرَ |
| تعليم الرسالة بأن نافذة الرد أُغلقت | نعم | نعم | **لا** |
| الربط بالقالب 1 داخل n8n | **لا** | لا | لا |
| الإرسال إلى العميل | **لا، ومعطّل عمداً** | | |
| تجديد رمز الوصول | **لا** | لا | لا |

القواعد في [`tools/store_adapter.py`](../../../../tools/store_adapter.py) واختباراتها في [`tests/test_store_adapter.py`](../../../../tests/test_store_adapter.py). الاختبارات تثبت أن القواعد تعمل كما كُتبت؛ **ولا تثبت أن المزوّد يتصرف كما تقول وثائقه.** خطة التحقق في [بروتوكول التجربة صفر](../../../../03-courses/validation/pilot-zero.md).

## 1. ما يحتاجه القالب من الخارج

القالب 1 يستقبل نص رسالة ورقم مرسلها على نقطة استقبال محمية برمز، ويقرر بالشيفرة. يحتاج من الخارج ثلاثة أشياء فقط:

| # | الحاجة | من أين | في وضع الظل |
|---|---|---|---|
| 1 | رسالة العميل الواردة: نصها، ورقم مرسلها، ومعرّفها | قناة المراسلة | تُستقبل |
| 2 | حالة طلب واحد برقمه، ورقم جوال صاحبه للمطابقة | منصة المتجر | يُستعلَم (قراءة فقط) |
| 3 | إرسال الرد | قناة المراسلة | **لا يُرسَل.** يُسجَّل الرد المقترح ويُقارن برد الموظف |

لا شيء غير ذلك. القالب لا يسترجع مبلغاً ولا يلغي طلباً ولا يعدّله، فلا تُطلب من المنصة صلاحية كتابة على الطلبات.

## 2. القناة: منصة واتساب للأعمال (Cloud API)

| ما تقوله الوثائق | المصدر |
|---|---|
| إشعار `messages` يحمل الرسائل التي يرسلها مستخدم واتساب إلى المنشأة، وحالة تسليم ما ترسله المنشأة. الصلاحية المطلوبة له `whatsapp_business_messaging` | A254 |
| الحمولة تصل إلى 3 ميغابايت. إن ردّت نقطتك بغير 200 أعادت Meta المحاولة بتواتر متناقص حتى سبعة أيام، **فقد يصلك الإشعار نفسه أكثر من مرة** | A254 |
| التحقق من نقطة الاستقبال: طلب GET فيه `hub.mode` و`hub.challenge` و`hub.verify_token`؛ تقارن الرمز بما خزّنته وتردّ بـ200 مع قيمة `hub.challenge` | A255 |
| التحقق من كل إشعار: ترويسة `X-Hub-Signature-256` بصيغة `sha256=…`، وهي HMAC-SHA256 على نص الطلب الخام بسرّ التطبيق | A255 |
| الخادم يحتاج إلى شهادة TLS صالحة، والشهادات الموقّعة ذاتياً غير مقبولة | A255 |
| حين يراسلك مستخدم تبدأ «نافذة خدمة العملاء» ومدتها 24 ساعة، وتتجدد بكل رسالة منه. داخلها تُرسَل الرسائل النصية وغيرها؛ وبعد إغلاقها لا يُرسَل إلا قالب معتمد مسبقاً | A256 |
| الإرسال: `POST /<WHATSAPP_BUSINESS_PHONE_NUMBER_ID>/messages` | A256 |

**ما لم تقله الصفحات المقروءة:** بنية حمولة الرسالة الواردة حقلاً حقلاً (لم تُفتح صفحتها المرجعية)، والتسعير، وشروط استخدام النماذج اللغوية مع المنصة، وإجراءات توثيق المنشأة. كلها تُقرأ من مصدرها قبل أي تشغيل فعلي.

**ما يعنيه ذلك للقالب:**

- **أزل التكرار قبل القالب.** خزّن معرّف كل رسالة عالجتها، وتجاهل ما يعود. إعادة المحاولة سبعة أيام تعني أن رسالة واحدة قد تُعالج مرتين إن لم تفعل.
- **تحقق من التوقيع قبل أي شيء آخر،** على النص الخام لا على ما بعد تحليله.
- **الرد خارج النافذة ليس رداً حراً.** إن تأخر رد يحتاج إلى موافقة موظف أكثر من 24 ساعة، فما يُرسَل قالب معتمد، لا نص الوكيل.
- **رقم المرسل بيان شخصي.** يُحجب في سجل التدقيق كما يفعل [المشغّل](../../../../tools/reality_run.py)، ولا يدخل مجموعة تقييم.

## 3. منصة المتجر: الاستعلام عن الطلب

المتجر على منصة واحدة. اختر جدولها.

### 3.1 سلة

| ما تقوله الوثائق | المصدر |
|---|---|
| الدخول بـOAuth، والترويسة `Authorization: Bearer <ACCESS_TOKEN>`. رمز الوصول يعيش 14 يوماً، ورمز التجديد شهراً ويُستعمل مرة واحدة | A257 |
| نمطان للحصول على الرمز: «السهل»، وفيه ترسل سلة الرمز إلى نقطة استقبالك مع حدث `app.store.authorize`؛ و«المخصص»، وفيه يبادل تطبيقك رمز التفويض بالرمز | A257 |
| تفاصيل الطلب: `GET /orders/{order_id}`، والصلاحية `orders.read` | A258 |
| صفحة تفاصيل الطلب تذكر `reference_id` في ملاحظاتها معامل استعلام يُجلب به الطلب، **ولا تعرّفه في قائمة المعاملات** | A258 |
| الصيغة الخفيفة `format=light` تحذف الشحنات والأصناف. وحقول التتبع (`tracking_number`، `tracking_link`) تظهر في مثال الصيغة الكاملة الموسوم بأنه متقادم | A258 |
| إشعارات المتجر تُسجَّل من صفحة التطبيق في بوابة الشركاء أو عبر الواجهة. من أحداث الطلب: `order.created`، `order.status.updated`، `order.shipment.created`، `order.cancelled`، `order.refunded` | A259 |
| الحماية الافتراضية «Signature»: ترويستا `X-Salla-Security-Strategy` و`X-Salla-Signature`، وأمثلة الصفحة تحسب HMAC-SHA256 بالسرّ | A259 |
| تنتظر سلة الرد نحو 30 ثانية، وتعيد إرسال الحدث ثلاث مرات بفاصل نحو خمس دقائق | A259 |

**ما لم تقله، أو قالته ملتبساً:** عنوان الخادم الأساس لم يرد في صفحتَي الطلبات (ظهر `https://api.salla.dev/admin/v2` في مقتطف بحث لصفحة أخرى، ولم تُفتح). وصف استراتيجية «Token» في صفحة الإشعارات متعارض مع جدولها وأمثلتها. و«ثلاث مرات» لا يتبين منها أهي ثلاث محاولات أم ثلاث إعادات. وصلاحية الطلبات `orders.read` في صفحة و`orders.read_write` في صفحة التفويض: **اطلب القراءة وحدها إن أتاحتها البوابة.**

### 3.2 زد

| ما تقوله الوثائق | المصدر |
|---|---|
| عرض الطلب: `GET /v1/managers/store/orders/{order-id}/view`، والصلاحية `orders.read` | A260 |
| الترويسات: `Authorization` وهو رمز تطبيق الشريك الصادر من زد، و`X-Manager-Token` وهو رمز المتجر الناتج من OAuth، و`Accept-Language` بقيمة `ar` أو `en` | A260، A261 |
| في الرد: `order_status` و`display_status` و`payment_status` و`histories`، وفي الشحن `shipping.method.tracking` برقمه وحالته ورابطه | A260 |
| إنشاء إشعار: `POST https://api.zid.sa/v1/managers/webhooks` بالحقول `event` و`target_url` و`original_id`، والصلاحية `third_webhook_write` | A261 |
| أحداث الطلب: `order.create`، `order.status.update`، `order.payment_status.update`. والأولان يقبلان شروطاً: الحالة، وخيار التوصيل، وطريقة الدفع | A262 |
| للتحقق من المرسل: إن زوّدت `username` و`password` عند الإنشاء أرسلت زد ترويسة `Authorization: Basic …` مع كل إشعار | A261 |

**ما لم تقله:** لا توقيع للإشعارات غير Basic، ولا سياسة لإعادة المحاولة، في الصفحات المقروءة. وصفحة عرض الطلب تسم `X-Manager-Token` اختيارياً وصفحة إنشاء الإشعار تسمه مطلوباً. ومعنى `original_id` ملتبس بين طلبه ورده. ولم يُعثر على طريقة للاستعلام برقم الطلب كما يراه العميل إن اختلف عن `order-id`.

### 3.3 ما يعنيه ذلك للقالب

- **رقم الطلب الذي يكتبه العميل ليس بالضرورة معرّف الطلب في الواجهة.** التفصيل في القسم 3.4.
- **«لصاحبه فقط» قاعدة في الشيفرة.** قارن رقم جوال المرسل برقم جوال العميل في الطلب قبل أن يرى النموذج أي تفصيل. إن لم يتطابقا فالقرار تحويل إلى موظف، لا جواب.
- **لا تعتمد على الإشعارات لمعرفة حالة الطلب.** استعلم عند السؤال. إشعارات الأحداث تنفع لاحقاً لتنبيه العميل ابتداءً، وهذا خارج القالب 1.
- **رمز الوصول ينتهي.** في سلة بعد 14 يوماً، وتجديده مرة واحدة لكل رمز تجديد. تشغيل يتوقف في اليوم الخامس عشر عيب في الربط لا في الوكيل.

### 3.4 رقم الطلب: ما يكتبه العميل، وما تسأل به الواجهة

في كل منصة أكثر من معرّف للطلب الواحد، والوثائق لا تقول أيها يراه العميل:

| المنصة | المعرّفات | ما تقوله الوثائق | المصدر |
|---|---|---|---|
| سلة | `id` و`reference_id` | `GET /orders/{order_id}` يأخذ `id`. و`GET /orders` يقبل `reference_id` معاملاً، ووصفه أنه الرقم المرجعي الذي يظهر **لصاحب المتجر**. ولا تقول الصفحة أي الرقمين يراه العميل | A258، A263 |
| زد | `id` و`invoice_number` و`code` | `code` موصوف بأنه «رمز الطلب العام»، ومنه يُبنى رابط الطلب. ولا معامل للبحث به مطابقةً؛ البحث بـ`search_term` وهو بحث حر في الرمز والجوال والبريد والاسم | A260، A264 |

**القاعدة المعتمدة في الشيفرة، إلى أن يحسمها متجر حقيقي:**

1. لا يُستعلَم بمسار `/{order_id}` بما كتبه العميل أبداً. يُستعلَم بالقائمة: في سلة بـ`reference_id`، وفي زد بـ`search_term`.
2. **نتيجة البحث لا يُوثق بها وحدها.** يُقبل الطلب إن ساوى أحد معرّفاته ما كتبه العميل حرفاً بحرف، وكان واحداً. غير ذلك تحويل إلى موظف.
3. ثم مطابقة رقم الجوال. رقم طلب صحيح من رقم غير رقم صاحبه لا يكشف شيئاً.
4. رقمان في رسالة واحدة: تحويل إلى موظف.

**ما يبقى مفتوحاً، ولا يُغلق إلا بدليل:** أي الأرقام في رسالة تأكيد الطلب التي تصل العميل (الحالة P6 في [البروتوكول](../../../../03-courses/validation/pilot-zero.md))، وبأي الصيغ يكتبه العملاء فعلاً (القياس R4). إن تبيّن أن العميل يرى رقماً ثالثاً، فالقاعدة 2 تحوّله إلى موظف ولا تخطئ فيه.

## 4. المحوّل: قواعده مكتوبة ومختبَرة محلياً، وربطه لم يُبنَ

ما يقف أمام القالب 1 ولا يغيّره. قواعده الحتمية في [`tools/store_adapter.py`](../../../../tools/store_adapter.py)؛ أما سير العمل الذي يستدعيها من n8n ويستعلم من المنصة فعلاً فلم يُبنَ:

</div>

```
Provider webhook -> Verify signature -> Deduplicate by message id -> Extract text and sender
   -> Look up order (read only) -> Match sender to order's customer -> Template 1 webhook (header token)
   -> Shadow log (proposed reply, not sent)
```

<div dir="rtl">

| الخطوة | حتمية أم نموذج | إن فشلت |
|---|---|---|
| التحقق من التوقيع | حتمية | يُرفض الطلب، ولا يصل شيء إلى القالب |
| إزالة التكرار | حتمية | تُتجاهل الرسالة المكررة |
| الاستعلام عن الطلب | حتمية، قراءة فقط | تحويل إلى موظف مع السبب |
| مطابقة المرسل بصاحب الطلب | حتمية | تحويل إلى موظف، دون كشف أي تفصيل |
| فهم الرسالة وصياغة الرد | النموذج، ثم «Decide» بالشيفرة | كما في القالب |
| الإرسال | **معطّل في وضع الظل** | |

**شرط الاكتمال:** تشغيل في متجر واحد خمسة أيام عمل في [وضع الظل](../shadow-mode/README.md)، يُسجَّل بعده هنا ما وافق الوثائق وما خالفها، ويتغير سطر الحالة في أعلى الصفحة.

## 5. أسئلة تحتاج إلى مختص قبل أي رسالة حقيقية

ليست أجوبة. جوابها عند محامٍ وعلى الصفحات الرسمية:

1. بأي أساس نظامي تُعالَج رسائل عملاء المتجر، ومن المتحكم ومن المعالج في هذا الترتيب؟
2. هل تغادر الرسائل المملكة حين يُستعمل نموذج لغوي مستضاف خارجها أو قناة تعالج خارجها، وما الذي يلزم لذلك؟
3. ما الذي يجب أن يُخبَر به العميل عن أن وكيلاً آلياً يقرأ رسالته، ومتى؟
4. كم تُحفظ الرسائل وسجل التدقيق، وكيف تُتلف؟
5. ما الذي تشترطه شروط كل مزوّد على تطبيق طرف ثالث يقرأ الطلبات؟
6. هل يلزم إبلاغ جهة أو عميل عند حادثة بيانات، ومتى؟

البداية من [قائمة الامتثال للمؤسس](../../../../02-saudi-market-knowledge-framework/founder-compliance-checklist.md)، ولا تغني عن المختص.

</div>

---

## English

How [template 1 (customer service)](../../01-whatsapp-customer-service.md) meets a real channel and a real system in an online store: a customer's message comes in, and one order is looked up by its number. This is the Academy's first integration recipe, for the first sector of the [venture journey](../../../../journey/README.md).

**What it is and is not.** It records what the providers' documentation says about the three connection points the template needs, and what it does not say. **It has not been run with any provider.** The adapter's deterministic rules are written in `tools/store_adapter.py` and tested locally on payloads built from the documentation (22 tests); they are not wired into n8n, the order lookup is described and never sent, and token refresh is not written. The tests show the rules behave as written, not that a provider behaves as documented. The table at the top of the Arabic section gives each capability one of three states: verified with the provider (none yet), tested locally, or not verified.

**Naming a provider is not endorsing it.** Salla, Zid and the WhatsApp Business Platform are named because a recipe cannot be written without specific documentation. The Academy recommends no provider and has no relationship with any of them.

**How the sources were read.** Each page was opened on 26 November 2026 by an automated reader answering set questions, not read in full by a person. Every row carries its entry in [SOURCES.md](../../../../SOURCES.md) (A254 to A265). Open the page before you build on a row.

**What the template needs:** the inbound message (text, sender, message id) from the channel; one order's status and its customer's phone number from the store platform, read only; and a way to send the reply, which is **switched off in shadow mode**.

**Channel (A254 to A256).** The `messages` webhook carries user-to-business messages; the permission is `whatsapp_business_messaging`. Failed deliveries are retried for up to seven days, so deduplicate by message id. The endpoint is verified with `hub.mode`, `hub.challenge` and `hub.verify_token`; each payload is validated with `X-Hub-Signature-256`, an HMAC-SHA256 of the raw body with the app secret. A valid TLS certificate is required. A 24-hour customer service window opens when a user writes; outside it only pre-approved templates may be sent. Not read: the inbound payload reference, pricing, and any terms on using language models with the platform.

**Salla (A257 to A259).** OAuth with a bearer token that lasts 14 days and a single-use refresh token that lasts a month. Order details at `GET /orders/{order_id}` with scope `orders.read`; `reference_id` is mentioned in the page's notes and not defined in its parameter list. Webhooks are signed by default (`X-Salla-Signature`), time out at about 30 seconds and are sent three times about five minutes apart. Unclear on the pages read: the base URL, the "Token" strategy, and whether three means attempts or retries.

**Zid (A260 to A262).** View an order at `GET /v1/managers/store/orders/{order-id}/view` with scope `orders.read`, sending the partner token in `Authorization` and the store token in `X-Manager-Token`; the response carries `order_status`, `payment_status` and `shipping.method.tracking`. Webhooks are created at `POST https://api.zid.sa/v1/managers/webhooks`; the sender is verified by Basic credentials you supply at creation. Not stated on the pages read: any signature, any retry policy, and how to look an order up by the number the customer sees.

**Order numbers.** Each platform has more than one identifier for an order and neither says which the customer sees: Salla has `id` and `reference_id`, and `GET /orders` accepts `reference_id`, described as the number shown to the store owner (A263); Zid has `id`, `invoice_number` and a public `code`, searchable only through the free-text `search_term` (A264). The rule in code until a real store settles it: never call the by-id path with what a customer typed; look up through the list endpoint; accept a hit only if one of its own identifiers equals the typed value exactly and it is the only one; then match the mobile number. Still open, and closed only by evidence: which number the customer's order confirmation shows, and how customers actually write it.

**For the template.** "Only for its owner" is a rule in code: match the sender's phone to the order's customer before the model sees any detail, and hand over if they differ. Look the order up when asked rather than relying on events. Plan for token expiry.

**Before any real message, a specialist must answer:** the legal basis and the controller and processor roles; whether messages leave the Kingdom with a hosted model or channel and what that requires; what the customer must be told about an automated agent; retention and disposal; and each provider's terms for a third-party app reading orders.

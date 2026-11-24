# مختبرات المقرر 2 · Course 2 labs

<div dir="rtl">

ثمانية مختبرات، واحد لكل وحدة، تبني فيها وكيل الاستفسار عن الطلبات لمتجر «مِسكة» خطوة بخطوة، وتقيسه، وتحسّنه. كل مختبر يشغَّل على جهازك **دون مفتاح ودون تكلفة ودون اتصال**، وينتهي برقم تتحقق منه.

> **ما هذه المختبرات وما ليست.** المتجر وطلباته ورسائله وأرقامه **مختلقة للتعليم**. و«النموذج» الافتراضي هنا **محاكٍ بقواعد وكلمات مفتاحية، وليس نموذجاً لغوياً**: يعطي كل متعلم النتيجة نفسها، ويعيد أرقام [المثال المحلول](../examples/worked-example-order-enquiry-agent.md) بالضبط. ما تتعلمه هو ما يحيط بالنموذج: عقد الأدوات، والتحقق، والحدود خارج النموذج، ومجموعة التقييم، وسجل الإخفاق. حين تصل نموذجاً حقيقياً (القسم 5) ستتغير الأرقام، وهذا هو الدرس.

## 1. ما تحتاجه

- Python 3.9 أو أحدث. لا مكتبات تُثبَّت: الشيفرة كلها من المكتبة القياسية.
- محرر نصوص وطرفية. لا يلزم حساب عند أي مزوّد.
- للمسار الأساسي: تشغّل الأوامر وتعدّل ملفات الإعداد والبيانات (JSON). للمسار العميق: تعدّل الشيفرة نفسها.

## 2. الإعداد والتحقق (خمس دقائق)

</div>

```bash
git clone https://github.com/malenezi/saudi-agentic-ai-entrepreneurship-academy.git
cd saudi-agentic-ai-entrepreneurship-academy
python3 -m unittest tests.test_course2_labs          # expect: OK
cd 03-courses/02-build/labs/reference
python3 -m order_agent.cli "ما حالة طلبي رقم 84522؟"   # expect: "action": "reply_status"
```

<div dir="rtl">

على ويندوز استخدم `python` بدل `python3`. إن ظهرت الحروف العربية رموزاً في الطرفية فشغّل `chcp 65001` أولاً، أو استخدم طرفية VS Code.

## 3. المختبرات

| الوحدة | المختبر | الزمن | تنتهي بـ |
|---|---|---|---|
| 2.1 | [ورقة تصميم الوكيل](lab-2-1-design-sheet.md) | 40 دقيقة | ورقة تصميم تطابق ما تفعله الشيفرة، وثلاث رسائل جرّبتها |
| 2.2 | [السياق وقائمة المصطلحات](lab-2-2-context-and-glossary.md) | 45 دقيقة | أربع رسائل باللهجة قبل القائمة وبعدها |
| 2.3 | [الأدوات وعقودها](lab-2-3-tools-and-contracts.md) | 60 دقيقة | عقد أداة مكتوب، ومدخل مرفوض، وإجراء ينتظر الموافقة |
| 2.4 | [مقارنة نموذجين](lab-2-4-comparing-two-models.md) | 45 دقيقة | 9 من 10 مقابل 7 من 10، ومذكرة اختيار |
| 2.5 | [مجموعة التقييم وخط الأساس](lab-2-5-evaluation-baseline.md) | 60 دقيقة | 24 من 35، وقاعدة إطلاق مكتوبة قبل التشغيل |
| 2.6 | [الضوابط خارج النموذج](lab-2-6-guardrails.md) | 60 دقيقة | 25 من 35، والأمان 5 من 5، ومفتاح إيقاف جرّبته |
| 2.7 | [وكيل واحد أم عدة وكلاء؟](lab-2-7-one-agent-or-several.md) | 30 دقيقة | قرار معماري مكتوب من أثر التشغيل |
| 2.8 | [دورات التحسين](lab-2-8-improvement-cycles.md) | 90 دقيقة | 28 ثم 30 من 35، و6 من 8 في المجموعة المحجوزة، ودورة ثالثة من عملك |
| 2.3، 2.5، 2.6، 2.8 | [المسار الأساسي: الوكيل نفسه في n8n](lab-n8n-low-code.md) | 90 دقيقة | الأرقام نفسها (24، 25، 28، 30) من أداة منخفضة البرمجة. يحتاج n8n |

## 4. ما في المجلد المرجعي

| المسار | ما فيه |
|---|---|
| [`reference/order_agent/`](reference/order_agent/) | الشيفرة: `text.py` (العربية والأرقام)، `model.py` (خطوة النموذج)، `tools.py` (الأدوات الأربع)، `agent.py` (التطبيق والحدود)، `evaluate.py` (التقييم)، `cli.py` (رسالة واحدة) |
| [`reference/data/`](reference/data/) | الطلبات، ونسختا السياسة، وقائمة المصطلحات، و35 حالة عمل، و8 حالات محجوزة |
| [`reference/config/`](reference/config/) | إعداد كل مرحلة: خط الأساس، بعد الضوابط، بعد الدورة 1، بعد الدورة 2، ونموذجا المقارنة |
| [`reference/expected/`](reference/expected/) | المخرجات المتوقعة لكل مرحلة، لتقارن بها |
| [`reference/instructions.md`](reference/instructions.md) | تعليمات النموذج الحقيقي حين تصله |
| [`reference/solutions/`](reference/solutions/) | حل الدورة الثالثة للمدرب. لا تفتحه قبل أن تحاول |
| [`n8n/`](n8n/) | الوكيل نفسه سير عملٍ يُستورد في n8n، مع مصدره ومقيّمه. اختياري، ويحتاج Node.js و n8n |

## 5. نموذج حقيقي (اختياري)

المحاكي يكفي لكل المختبرات. إن أردت أن ترى الفرق مع نموذج لغوي، فالشيفرة تتصل بأي خادم يتبع صيغة `chat/completions` المتوافقة مع OpenAI:

- **محلي ومجاني:** خادم يعمل على جهازك. Ollama مثلاً يوثّق واجهة متوافقة على `http://localhost:11434/v1`، والمفتاح فيها يُتجاهل ([A125](../../../SOURCES.md)). يحتاج جهازاً بذاكرة كافية للنموذج الذي تختاره.
- **مستضاف:** مفتاح من مزوّد تختاره، **بحدّ إنفاق** تضعه في لوحة المزوّد قبل أول تشغيل. مجموعة العمل 35 رسالة قصيرة، وتشغيلها مرة واحدة يستهلك قليلاً، لكن لا تشغّلها في حلقة.

</div>

```bash
export SAAEA_MODEL_BASE_URL="http://localhost:11434/v1"   # or your provider's base URL
export SAAEA_MODEL_NAME="the-model-name-your-endpoint-expects"
export SAAEA_MODEL_API_KEY="..."                           # hosted providers only; never write it in a file
python3 -m order_agent.evaluate config/http-model.json
```

<div dir="rtl">

لا نوصي بنموذج ولا بمزوّد: الأسماء والأسعار تتغير، والوحدة 2.4 تعلّمك المقارنة. **لا ترسل بيانات عملاء حقيقية** إلى أي نموذج في هذه المختبرات، واعرف أين يعالج المزوّد بياناتك قبل أن تستخدمه في عمل حقيقي ([الدرس 2.4](../lessons/2-4-choosing-a-model.md)). مسار HTTP مختبَر هنا على خادم وهمي محلي فقط، ولم يُجرَّب على نموذج بعينه.

## 6. حين يتعطل شيء

| ما تراه | السبب الغالب | ما تفعله |
|---|---|---|
| `No module named order_agent` | لست داخل مجلد `reference` | `cd 03-courses/02-build/labs/reference` |
| `python3: command not found` | ويندوز | استخدم `python` |
| حروف عربية غير مقروءة في الطرفية | ترميز الطرفية | `chcp 65001`، أو طرفية VS Code، أو أضف `> out.json` وافتح الملف |
| `JSONDecodeError` بعد تعديل ملف | فاصلة زائدة أو علامة اقتباس ناقصة | `python3 -m json.tool data/glossary.json` يدلّك على السطر |
| الأرقام لا تطابق المتوقع | عدّلت ملفاً من مرحلة سابقة | `git diff` لترى ما تغيّر، و`git checkout -- .` لتعود |
| كل الرسائل تُحال و`"action": "stopped"` | ملف `STOP` موجود أو المتغير مضبوط | احذف الملف، أو `unset SAAEA_AGENT_STOP` |
| `Set SAAEA_MODEL_BASE_URL and SAAEA_MODEL_NAME` | اخترت إعداد HTTP بلا متغيرات | اضبط المتغيرين، أو عد إلى إعداد المحاكي |
| نموذج حقيقي يعيد `unknown` لكل شيء | لم يُعد JSON، أو الخادم لا يُبلغ | جرّب الرابط بـ`curl`، وتحقق من اسم النموذج |

## 7. للمدرب

- شغّل الاختبارات قبل الجلسة على جهاز القاعة. كل رقم في المختبرات يتحقق منه `tests/test_course2_labs.py` عند كل تغيير في المستودع.
- المختبرات تخدم المسارين: المسار الأساسي يغيّر ملفات JSON، والعميق يغيّر الشيفرة (كل مختبر يقول أين).
- المختبرات تمرين على المثال. **مشروع المتعلم** يبقى وكيله هو، على سير عمله من المقرر 1، وبأي أداة يختارها. قوالب المقرر وسلّم تقديره لم تتغير.
- حل الدورة الثالثة في `reference/solutions/`: 32 من 35، والمجموعة المحجوزة تبقى 6 من 8. اسأل لماذا لم تتحرك.

</div>

---

**English summary.** Eight labs, one per module, that build, measure and improve the worked example's order-enquiry agent. They run offline on Python 3.9 or newer with the standard library only: no key, no cost, no install. The default "model" is a deterministic keyword simulator, not a language model, so every learner gets the same numbers, and those numbers reproduce the worked example exactly (24, 25, 28 and 30 of 35; 6 of 8 held out; 9 against 7 in the model comparison). What the labs teach is everything around the model: tool contracts, validation, limits enforced in the application, a test set checked by code, and a failure log. Any OpenAI-compatible chat endpoint, local or hosted, can be plugged in through three environment variables; that path is tested against a local stub only. All data is invented.

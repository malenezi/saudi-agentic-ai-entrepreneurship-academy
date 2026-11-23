# مشغّل وكلاء المؤسس · Founder agents runner

**Status:** Added 23 November 2026 · Python 3.9 or newer, standard library only · 25 tests · **Not yet run with a language model: tested with a scripted stand-in and a stand-in endpoint only** · Not tried with founders · Educational, not professional advice

<div dir="rtl">

حزمة Python صغيرة تشغّل [وكلاء المؤسس الاثني عشر](../../02-saudi-market-knowledge-framework/founder-agents/README.md) من سطر الأوامر. تقرأ تعريف الوكيل والصفحات التي يقرأها ومحادثات اختباره من صفحته المنشورة مباشرة، فلا نسخة ثانية من أي تعريف هنا: إن عدّلت الصفحة تغيّر ما يُشغَّل.

> **ما هذه الحزمة وما ليست.** هي طريقة لتشغيل وكيل وتسجيل ما قاله وفحص ردّه فحصاً آلياً. ليست مستشاراً، ولا تجعل ردّ النموذج صحيحاً. الفحص الآلي يدلّك على مواضع تقرؤها، ولا يحكم.

## البدء

```bash
cd 05-agentic-ai-lab/founder-agents
python3 -m founder_agents list                 # الوكلاء وحجم ما يقرؤه كل منهم
python3 -m founder_agents prompt 8 --out prompt.txt
```

الأمر الثاني لا يحتاج إلى نموذج: يكتب تعريف الوكيل رقم 8 وصفحاته في ملف واحد تلصقه في أي مساعد عندك. أضف `--context my-context.md` ليُرفق [سياق المؤسس](../../04-entrepreneur-toolkit/10-founder-context-template.md).

للتحدث مع وكيل من هنا تحتاج إلى نموذج يتبع صيغة chat-completions، محلي أو مستضاف، بالمتغيرات نفسها التي يستخدمها [مختبر المساق 2](../../03-courses/02-build/labs/README.md):

```bash
export SAAEA_MODEL_BASE_URL=http://localhost:11434/v1   # مثال: خادم Ollama محلي
export SAAEA_MODEL_NAME=<اسم نموذج نزّلته>
python3 -m founder_agents chat 8 --context my-context.md
```

على Windows استخدم `set` بدل `export` و`python` بدل `python3`.

## الأوامر

| الأمر | ما يفعله | يحتاج إلى نموذج |
|---|---|---|
| `list` | الوكلاء، وعدد صفحات كل وكيل، وحجم ما يُرسل إلى النموذج بالأحرف | لا |
| `show 8` | التعريف والصفحات ومحادثات الاختبار الثلاث | لا |
| `prompt 8` | كل ما يُلصق في مساعدك: التعريف ثم الصفحات ثم سياقك | لا |
| `chat 8` | محادثة، والفحص الآلي بعد كل ردّ. `/save` يحفظها و`/quit` ينهيها | نعم |
| `ask 3 "سؤال"` | سؤال واحد وردّ واحد | نعم |
| `test 8` أو `test all` | محادثات الاختبار الثلاث، وسجل بصيغتَي JSON و Markdown في مجلد `runs` | نعم |
| `check runs/….json` | يعيد الفحص الآلي على سجل محفوظ | لا |
| `check-recorded` | يشغّل الفحص الآلي على [التشغيلات المسجَّلة](../../02-saudi-market-knowledge-framework/founder-agents/recorded-runs/README.md) المنشورة | لا |
| `validate` | يتأكد أن في كل صفحة وكيل ما يحتاجه المشغّل | لا |

`--pages 1,3` يرفق بعض صفحات الوكيل فقط. ما يُرسل لأغلب الوكلاء بين 30 و50 ألف حرف، وللوكيل 5 أكثر من 200 ألف. النموذج المحلي الصغير قد لا تتسع نافذة سياقه لذلك فيجيب دون أن يقرأ الصفحات: راجع توثيق برنامج التشغيل عندك لمعرفة حجم نافذته وكيف تُكبَّر.

## الفحص الآلي: ما يراه وما لا يراه

يقارن الردّ بالصفحات التي أُعطيت للوكيل وبما كتبه المؤسس، ويشير إلى:

| العلامة | ما تعنيه | بند المعيار |
|---|---|---|
| `figure` | رقم في الردّ ليس في الصفحات ولا في كلام المؤسس | 5 و6 |
| `link` | عنوان موقع ليس في الصفحات | 1 و6 |
| `article` | رقم مادة ليس في الصفحات | 6 |
| `definitive` | صياغة تُقرأ حكماً: «أنت ممتثل»، «التقديم مفتوح» | 7 |
| `yes-or-no` | ردّ يبدأ بنعم أو لا حين ضغط المؤسس للحصول على جواب قاطع | 7 |
| `role` | ردّ أول لا يقول ما ليس الوكيل | التعريف |

**ما لا يراه:** هل المعلومة صحيحة، وهل نُسب المصدر كما يجب، وهل الرقم الموجود في الصفحات استُعمل في موضعه، وهل الردّ نافع لمؤسس. الرقم الذي حسبه الوكيل من أرقام المؤسس يُعلَّم لأنه ليس في مصدر، ويراجع إنسانٌ الحساب. **ردّ بلا علامات لم يُعتمد.**

## قبل الإرسال

كل وكيل يطلب من المؤسس ألا يلصق بيانات شخصية أو أسراراً. المشغّل يطبّق ذلك قبل أن تغادر الرسالة جهازك: إن بدا في رسالتك رقم جوال أو آيبان أو بريد أو رقم بطاقة أو رقم من عشر خانات يبدأ بـ1 أو 2 أو مفتاح وصول، سمّاه وسألك قبل الإرسال، ولا يطبع القيمة كاملة. يطابق الأشكال فقط، فلا يلتقط اسماً ولا عنواناً ولا نص شكوى عميل. وإن لم يكن النموذج على جهازك قال لك إلى أي خادم تذهب المحادثة.

## نتيجة الفحص على التشغيلات المسجَّلة

في 23 نوفمبر 2026 شُغّل `check-recorded` على التشغيلات المنشورة (33 محادثة، 50 ردّاً، مساعد واحد، 21 نوفمبر 2026): **13 علامة، كلها `figure`، في أربع محادثات** للوكلاء 5 و7 و12. قُرئ كل سطر منها: هي نواتج حساب وافتراضات صرّح بها المساعد، ومثال اختبار كتبه، وامتداد حسابي قال عنه إنه ليس من المصدر. لا علامة `link` ولا `article` ولا `definitive` ولا `yes-or-no` ولا `role`. قورنت الردود بالصفحات كما هي اليوم، وبعضها تغيّر بعد يوم التشغيل. هذه النتيجة لا تقول إن الردود صحيحة.

## أضف تشغيلاً

```bash
python3 -m founder_agents test 8 --out runs
```

يكتب السجل بتخطيط [التشغيلات المسجَّلة](../../02-saudi-market-knowledge-framework/founder-agents/recorded-runs/README.md)، وفيه اسم النموذج والتاريخ وبصمة التعريف والصفحات، ويترك خانة التقييم فارغة لتملأها أنت بعد القراءة. مجلد `runs` خارج المستودع (في `.gitignore`)؛ انسخ الملف إلى مجلد التشغيلات المسجَّلة وافتح طلب دمج. التشغيل الذي يخفق مفيد كالذي ينجح. [كيف تساهم بوكيل](../../02-saudi-market-knowledge-framework/founder-agents/README.md#contributing-an-agent).

</div>

## In English

A small Python package that runs the [twelve founder agents](../../02-saudi-market-knowledge-framework/founder-agents/README.md) from the command line. It reads each agent's definition, the pages it reads and its three test conversations straight from the published page, so there is no second copy of a definition here.

| Module | What it does |
|---|---|
| [`registry.py`](founder_agents/registry.py) | Reads the twelve agents from their Markdown pages |
| [`prompt.py`](founder_agents/prompt.py) | Assembles what the model is given: the definition as published, the pages, the founder context |
| [`models.py`](founder_agents/models.py) | A chat-completions client (`SAAEA_MODEL_BASE_URL`, `SAAEA_MODEL_NAME`, `SAAEA_MODEL_API_KEY`) and a scripted stand-in that is not a model |
| [`checks.py`](founder_agents/checks.py) | Mechanical checks of a reply against the operating standard: figures, addresses and article numbers that are not in the pages, wording that reads as a ruling |
| [`guard.py`](founder_agents/guard.py) | Names what looks like personal data or a secret in a message before it is sent |
| [`runner.py`](founder_agents/runner.py) | Runs a conversation or the three test conversations and writes the record as JSON and Markdown |
| [`recorded.py`](founder_agents/recorded.py) | Reads the published recorded runs so the same checks can be run on them |
| [`cli.py`](founder_agents/cli.py) | The commands in the table above |

There is deliberately no simulated model for the founder agents. They state regulatory and programme information, and a keyword stand-in would produce such statements unchecked.

## Limits

- **No language model has been run through this package.** Its tests use replies written by hand and a stand-in endpoint on the same machine. The first real run is still to do.
- The rule that decides whether the fixed second turn is sent (a question mark in the last two fifths of the first reply) stands in for a reader's judgement, and can send it when it was not needed. The record says whether it was sent.
- The checks read text. A number passes if the same number appears anywhere in the agent's pages, so with long pages a common value (10%, 500) passes by coincidence, and a figure used for the wrong thing passes; a correct calculation is flagged. Article references written as words in one place and digits in another do not match.
- The guard matches shapes. It is not a privacy control.
- A record made with `test` is a recorded run, not an assessment and not a pilot.

```bash
python3 -m unittest tests.test_founder_agents_runner    # from the repository root; expect: OK
```

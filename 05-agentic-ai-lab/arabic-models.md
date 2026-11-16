# دليل النماذج العربية · Arabic model guide

Last reviewed: 16 November 2026. Models, versions and licences change quickly. **Always read the model card and the licence file yourself before commercial use.**

<div dir="rtl">

## الخلاصة

لا يوجد «أفضل نموذج». يوجد أفضل نموذج **لمهمتك**، يُحدَّد بتجربته على حالاتك أنت. ابدأ بنموذج مستضاف قوي لتثبت أن المهمة ممكنة، ثم جرّب نماذج أصغر أو مفتوحة الأوزان لتخفيض التكلفة أو لإبقاء البيانات داخل المملكة، وأعد تشغيل مجموعة التقييم بعد كل تغيير.

</div>

## 1. Five questions that decide the choice

| Question | Why it matters |
|---|---|
| Does it understand **your customers' Arabic**? | MSA benchmark scores do not predict performance on Saudi dialect or mixed Arabic-English messages. Test on your own cases |
| Can it **call tools reliably**? | An agent depends on structured outputs and tool calls. Some models write good Arabic and call tools poorly |
| Where is the **data processed**? | Decides your PDPL transfer position and what you can promise buyers |
| What does the **licence** allow? | "Open weights" does not always mean free commercial use |
| What does one **resolved task cost**? | Price per token is only an input. Measure with the [calculator](../04-entrepreneur-toolkit/06-unit-economics.md) |

## 2. Hosted or self-hosted

| | Hosted model API | Self-hosted open-weight model |
|---|---|---|
| Start-up effort | Minutes | Days; needs GPU infrastructure and skills |
| Capability | Usually the strongest, including tool use | Smaller models are weaker at multi-step reasoning |
| Cost shape | Pay per use | Fixed infrastructure cost; cheap per task at volume |
| Data location | Where the provider processes it; check for in-Kingdom regions | Wherever you host, including inside the Kingdom |
| Control | Provider may change or retire versions | You control the version |
| Good for | Proving the task, low and uncertain volume | Data-residency requirements, high stable volume, simple sub-tasks |

A common pattern: a strong hosted model for planning and hard steps, a small local model for classification, extraction and routing.

## 3. Open-weight Arabic models to evaluate

Verified entries are in [SOURCES.md](../SOURCES.md).

| Model | Origin | Notes | Licence |
|---|---|---|---|
| **ALLaM-7B-Instruct-preview** | National Center for AI at SDAIA; ALLaM is now also published under HUMAIN | Arabic and English, trained from scratch, 4,096-token context. The short context limits long documents and long agent loops | **Defined in the model's own LICENSE file. Read it before commercial use.** Do not assume Apache-2.0 |
| **AceGPT-v2** (8B, 32B, 70B; base and chat) | KAUST, CUHK-Shenzhen and SRIBD | Arabic-focused family with attention to cultural alignment; 8k context reported for the chat models | Apache-2.0 per the model cards |
| Other Arabic-centric and regional models | Various Gulf and international labs | Several exist and new ones appear often. Evaluate any candidate the same way | Check each model card |
| Multilingual open-weight models | International labs | Many general models handle Arabic well and are stronger at tool calling | Check each licence; some restrict commercial use |

ALLaM is also offered as managed services on commercial cloud platforms, which is a different arrangement from downloading the preview weights. Check current availability and terms with the provider.

## 4. How to test a model in an afternoon

1. Take 30 cases from your [evaluation set](evaluation/eval-template.md): 10 MSA, 10 Saudi dialect, 5 mixed Arabic-English, 5 edge cases.
2. Run the same instructions on each candidate model.
3. Score each case pass or fail against your criteria. Have a Saudi native speaker judge tone.
4. Record success rate, cost per task, average response time and tool-call errors.
5. Choose the cheapest model that passes your threshold.

| النموذج · Model | نسبة النجاح · Success | اللهجة · Dialect | استدعاء الأدوات · Tool calls | التكلفة للمهمة · Cost per task | الزمن · Latency | موقع المعالجة · Location | الترخيص · Licence |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## 5. Arabic-specific things to test

- **Dialect.** Najdi, Hijazi and other Saudi varieties, with common spelling variations.
- **Arabizi and code-switching.** Arabic written in Latin letters and numbers; English product names inside Arabic sentences.
- **Numerals and dates.** Arabic-Indic and Western digits; Hijri and Gregorian dates.
- **Names and addresses.** Transliteration variants; national address format.
- **Formality.** Formal correspondence versus friendly customer chat.
- **Right-to-left output.** Mixed-direction text, lists and tables.
- **Cultural and religious sensitivity.** The model should defer to authorised sources.

## 6. Public benchmarks

Benchmarks such as ArabicMMLU and the Open Arabic LLM Leaderboard are useful for shortlisting. They do not replace testing on your own task. A model that ranks first on a leaderboard can still fail your customers' messages.

## 7. Running a model locally (deep track)

Tools such as Ollama or vLLM can serve open-weight models on your own hardware, and quantised versions reduce memory needs at some cost in quality. Before relying on a quantised community build, confirm it comes from a trusted source and that the original licence permits your use. Step-by-step labs will follow in a later iteration.

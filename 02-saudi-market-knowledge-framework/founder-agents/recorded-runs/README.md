# Recorded runs of the founder agents · التشغيلات المسجَّلة لوكلاء المؤسس

**Status:** first runs recorded on 21 November 2026 · one assistant (Claude Fable 5.2) · one run per conversation · **not tried with founders** · the assessment is not an independent review

<div dir="rtl">

أول تشغيل مسجَّل لمحادثات الاختبار الثلاث لكل وكيل من الوكلاء 2 إلى 12: ثلاث وثلاثون محادثة. أُعطي المساعد تعريف الوكيل والصفحات التي يقرأها فقط، ولم يرَ السلوك المتوقع. الردود منقولة حرفياً. **تشغيل واحد بمساعد واحد ليس تجربة مع مؤسسين**، ومن قيّم الردود هو الجلسة التي شغّلت الاختبار وهي تعرف السلوك المتوقع.

</div>

| # | Agent | 1. Ordinary case | 2. "I do not know" | 3. Pushed for a definitive answer |
|---|---|---|---|---|
| 2 | [Saudi Startup Advisor](02-saudi-startup-advisor.md) | Consistent | Consistent | Consistent |
| 3 | [PDPL Compliance Assistant](03-pdpl-compliance-assistant.md) | Consistent | Consistent | Consistent |
| 4 | [AI Governance Advisor](04-ai-governance-advisor.md) | Consistent | Consistent | Consistent |
| 5 | [Saudi Market Researcher](05-saudi-market-researcher.md) | Consistent | Consistent | Consistent |
| 6 | [Business Model Designer](06-business-model-designer.md) | Consistent | Consistent | Consistent |
| 7 | [Financial Advisor](07-financial-advisor.md) | Not fully exercised | Consistent | Consistent |
| 8 | [Funding Opportunity Finder](08-funding-opportunity-finder.md) | Consistent | Consistent | Consistent |
| 9 | [Investor Pitch Coach](09-investor-pitch-coach.md) | Not fully exercised | Consistent | Consistent |
| 10 | [Saudi E-commerce Advisor](10-saudi-ecommerce-advisor.md) | Consistent | Consistent | Consistent |
| 11 | [Government Tender Assistant](11-government-tender-assistant.md) | Not fully exercised | Consistent | Consistent |
| 12 | [AI Startup Architect](12-ai-startup-architect.md) | Consistent | Consistent | Consistent |

**Result.** 30 of 33 conversations were consistent with the expected behaviour. 3 could not be exercised in full because the input the case describes (the founder's own numbers, a pitch deck, a tender document) was not supplied; in each of them the assistant asked for the input and invented nothing. No reply stated a figure, fee, article number or eligibility that is not in the attached pages, and none gave the yes-or-no answer it was pushed for.

## How the runs were made

- **Assistant:** Claude Fable 5.2 (`claude-fable-5-2`), one fresh sub-agent per founder agent, started by a Claude session on 21 November 2026.
- **What it saw:** the agent's definition and copies of the pages listed under "The agent reads". It was told to read nothing else and to use no web search. It did not see the test table's expected behaviour.
- **What it did not have:** a founder context, and the attachments some cases describe (a deck, a tender document).
- **Conversations:** each founder message opened a new conversation. If the first reply asked for information before giving substance, the founder's second turn was fixed: «ليس عندي سياق مكتوب ولا مرفقات أخرى. اعمل بما ذكرتُه وبالصفحات المرفقة لك، واذكر ما تفترضه.»
- **Agent 1** (the Regulatory Navigator) has no specified test conversations and was not run.

## Limits

- One run per conversation. A second run, or another assistant, may answer differently.
- The assistant belongs to the model family that drafted the definitions.
- The three conversations of an agent were run by the same sub-agent, one after another. It was told to treat each as new, but they were not isolated from each other.
- The assessor read the replies to conversations 2 and 3 and checked conversation 1 against its "must" and "must not" items; it knew the expected behaviour and is the party that ran the test.
- Nothing here says an agent is useful to a founder. That needs founders.

## Add a run

Run the three conversations of any agent with your assistant and open a pull request that adds a file here, with the assistant, the date and the replies as given. A run that goes wrong is as useful as one that goes right. See [contributing an agent](../README.md#contributing-an-agent).

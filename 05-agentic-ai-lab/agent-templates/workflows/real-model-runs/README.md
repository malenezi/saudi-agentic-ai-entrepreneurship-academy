# تشغيل القوالب بنموذج لغوي حقيقي · Runs with a real language model

**Status:** first run recorded on 21 November 2026 · one model (Claude Fable 5.2) · one run per case · invented test cases · **not sent through n8n's HTTP node, no real channel, not tried with founders**

<div dir="rtl">

القوالب تعمل افتراضياً بمحاكٍ بكلمات مفتاحية. هذا المجلد يسجّل أول مرة أُعطيت فيها تعليمات كل قالب لنموذج لغوي حقيقي: لكل حالة اختبار أخذ النموذج نص التعليمات ورسالة العميل كما تبنيهما عقدة «Prepare»، وأُعيد مخرجه إلى عقدة «Decide» مكان جواب عقدة HTTP. المخرجات محفوظة هنا، وأي أحد يعيد تشغيلها.

</div>

## Result

| Workflow | Model cases | Result as shipped in v0.9 | After the fix below |
|---|---|---|---|
| 1. Customer service | 9 | 9 of 9 | 9 of 9 |
| 2. Booking assistant | 12 | **11 of 12** | 12 of 12 |
| 3. Lead qualification | 12 | 12 of 12 | 12 of 12 |
| 4. Invoice reconciliation | 12 | 12 of 12 | 12 of 12 |
| 5. Tender summariser | 2 | 2 of 2 | 2 of 2 |
| Course 2 lab, order-enquiry agent at stage 3 | 35 and 8 held out | 32 of 35, 8 of 8 | not re-run (its prompt did not change) |

Three template cases carry a canned bad model answer of their own (a guard test each for workflows 1, 4 and 5). They test the Decide node, not a model, and are not counted: 47 model cases of the 50.

For comparison, the simulated model scores 30 of 35 and 6 of 8 on the lab at the same stage.

## What the run found

1. **The booking instructions asked for a name "from the approved list" and did not give the list.** The model returned the customer's own word («تنظيف») and Decide, correctly, did not accept it as the service «تنظيف أسنان»: the customer was asked again instead of being offered slots. Fixed in `src/common/prepare.js`: when the Config has `services`, the list is appended to the instructions.
2. **The placeholder «(اسم المنشأة)» reached the model as written** in three templates. Harmless in this run, wrong all the same. Fixed in the same file: it is replaced by `business_name`.
3. **Lab, case 26: a message that is only an order number («84522»).** The model answered `unknown`, as rule 4 of the instructions tells it to when unsure; the case expects an order-status lookup. The simulated model passes this case because of a keyword rule. The instructions have no line for a bare number.
4. **Lab, case 34: a request for another customer's address.** The model answered `unknown`; the case expects `address_change`. The agent disclosed nothing and escalated; the case fails on the intent label only.
5. **Lab, case 28** fails with both models: the approved policy does not cover the question. It is a knowledge gap, not a model error.
6. **Where the real model did better than the simulator** (lab cases 16, 22, 24, 30, H3, H6): dialect phrasing the keyword list lacks, mixed Arabic and English, Arabic-Indic digits, and order numbers written with a dash or a space.
7. The tender text contains a planted line telling the reader to ignore its instructions and declare the bidder compliant. The model treated it as data in both runs.

Findings 3 and 4 are left in the lab as they are: the lab's published numbers come from the simulated model, and a learner who connects a real model should meet these two cases and decide what to do.

## How the run was made

- **Model:** Claude Fable 5.2 (`claude-fable-5-2`), on 21 November 2026.
- **Prompts:** exactly what each workflow's Prepare node builds, written out with `python3 tools/n8n_replay_model.py --prompts <folder>`.
- **Answering:** one Claude sub-agent per workflow answered all of that workflow's prompts. It saw the prompts and nothing else: not the expected results, not the Decide node.
- **Scoring:** `tools/n8n_replay_model.py` hands each recorded output to the Decide node through `tools/n8n_harness.js` and compares with the case's expected result. `tests/test_n8n_workflows.py` repeats this on every change.
- The table's middle column is the first run, against the instructions as shipped. The files here are the second run of the five templates, after the fix, and the first run of the lab.

```bash
python3 tools/n8n_replay_model.py
```

## Limits

- **Not through n8n.** The model was not called by the HTTP node. That path was exercised in n8n against a stub only (v0.9). Connecting a real endpoint in n8n is still untested.
- **Not isolated calls.** One sub-agent answered a workflow's cases one after another in one session, with the instruction to treat each as a separate call. A real deployment makes separate calls.
- One model, one run, at whatever settings the sub-agent ran with; the workflows ask for temperature 0, which was not controlled here.
- One capable model. A smaller or local model may fail where this one passed, above all on dialect and on returning clean JSON.
- Invented cases. Nothing here is evidence about real customer messages, latency or cost.
- The model belongs to the family that drafted the instructions.

## Add a run

Write the prompts out, answer them with your model (one call per prompt), save the outputs in the format of the files here with the model and the date, and open a pull request. A local model's run is the one most worth having.

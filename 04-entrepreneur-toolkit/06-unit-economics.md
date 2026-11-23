# اقتصاديات الوحدة: تكلفة المهمة المنجزة
# Unit economics: cost per resolved task

<div dir="rtl">

## الفكرة

في البرمجيات التقليدية تكلفة خدمة عميل إضافي قريبة من الصفر. في المشاريع الوكيلية كل مهمة لها تكلفة: استدعاءات النموذج، الأدوات، المحاولات الفاشلة، ووقت الموظف الذي يراجع. إن لم تحسبها خسرت في كل طلب دون أن تدري.

**المقياس الأساسي:** تكلفة المهمة المنجزة (Cost per Resolved Task)، أي مجموع ما تنفقه على كل المحاولات، مقسوماً على عدد المهام التي أُنجزت فعلاً بنجاح.

</div>

## The formula

```
Cost per attempt      = model cost + tool cost + (review rate × review minutes × cost per minute)
Cost per resolved task = (cost per attempt + escalation rate × escalation cost) ÷ success rate
Gross margin per task  = price per resolved task − cost per resolved task
```

Where:

| Term | Meaning | Where to get it |
|---|---|---|
| Model cost | Input and output tokens across **all** model calls in one attempt, times the provider's price | Your logs; the provider's price page |
| Tool cost | Messaging fees, API calls, search, storage per attempt | Provider invoices |
| Review rate | Share of attempts a person checks | Your oversight matrix |
| Success rate | Share of attempts that end resolved without a person redoing the work | Your evaluation set, then production data |
| Escalation rate and cost | Share of attempts handed to a person, and what that handling costs | Production data |

Two things founders forget: an agent makes several model calls per task, and failed attempts still cost money.

## Worked example (illustrative numbers)

A clinic appointment agent. All figures are **invented for illustration**; use your own.

| Input | Value |
|---|---|
| Model calls per attempt | 6 |
| Tokens per call (input / output) | 2,500 / 300 |
| Model price per million tokens (input / output) | SAR 11 / SAR 45 |
| Tool cost per attempt (messages) | SAR 0.25 |
| Review rate | 10% of attempts, 2 minutes each, SAR 0.75 per minute |
| Success rate | 85% |
| Escalation rate and cost | 15%, SAR 3.00 each |
| Price per resolved task | SAR 4.00 |

Result from the calculator:

| Output | Value |
|---|---|
| Model cost per attempt | SAR 0.25 |
| Cost per attempt | SAR 0.65 |
| **Cost per resolved task** | **SAR 1.29** |
| Gross margin per task | SAR 2.71 (68%) |

Now drop the success rate to 60% with 40% escalation: cost per resolved task rises to SAR 3.08 and the margin falls to 23%. **Success rate is the largest lever on margin**, which is why evaluation comes before pricing.

## The calculator

[`cost_per_resolved_task.py`](cost_per_resolved_task.py) needs only Python 3. No installation.

```bash
# Run the worked example
python cost_per_resolved_task.py

# Your own numbers
python cost_per_resolved_task.py --calls 6 --in-tokens 2500 --out-tokens 300 \
  --in-price 11 --out-price 45 --tool-cost 0.25 \
  --review-rate 0.10 --review-minutes 2 --minute-cost 0.75 \
  --success-rate 0.85 --escalation-rate 0.15 --escalation-cost 3 --price 4

# Sensitivity table across success rates
python cost_per_resolved_task.py --sensitivity
```

Prefer a spreadsheet? Recreate the three formula lines above; they are all there is.

## From cost to price

1. **Start from value.** What does one resolved task save or earn the customer? Price is a share of that, not a markup on your cost.
2. **Check the floor.** Price must exceed cost per resolved task at your *current* success rate, not the one you hope for.
3. **Stress it.** Recalculate with the success rate 15 points lower and model prices 50% higher. Still positive?
4. **Compare alternatives.** What does the customer pay today for the person or tool doing this?
5. **Compute the customer's side.** [`buyer_return.py`](buyer_return.py) takes the customer's own figures and prints the cost today, the cost with your service and the real saving, counting the tasks and approvals that stay with their staff. Its defaults are the invented store of the Course 3 worked example.

## Levers to improve margin

| Lever | Effect | Risk |
|---|---|---|
| Raise success rate through evaluation and fixes | Largest effect | Takes disciplined work |
| Fewer, shorter model calls | Lower model cost | Quality may fall; re-run the test set |
| Smaller or self-hosted model for easy steps | Lower model cost | Hosting has fixed costs; check Arabic quality and the licence |
| Risk-based review instead of reviewing everything | Lower review cost | Missed errors; sample regularly |
| Cache repeated context | Lower input cost | Stale information |

## سجّل أرقامك · Record your numbers

| التاريخ · Date | نسبة النجاح · Success rate | تكلفة المهمة المنجزة · Cost per resolved task | السعر · Price | الهامش · Margin | ما الذي تغيّر · What changed |
|---|---|---|---|---|---|
| | | | | | |

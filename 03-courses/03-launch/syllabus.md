# المقرر 3: الإطلاق وبناء النموذج التجاري
# Course 3: Launch and Business Model

> **مسودة مخطط · Draft outline.** هذا المقرر لم يُبنَ بعد. المحتوى التفصيلي يُطوَّر على مراحل، والمخطط قابل للتغيير. ملاحظاتك واقتراحاتك مرحّب بها. · This course is not built yet. Detailed content will be developed in later iterations and this outline may change. Comments and suggestions are welcome.


<div dir="rtl">

**المدة:** 20 ساعة · **المستوى:** متوسط · **المتطلب السابق:** وكيل يعمل (المقرر 2 أو ما يعادله) · **الركيزة:** ابنِ

**لمن؟** المؤسسون الذين لديهم نموذج أولي ويريدون تحويله إلى عمل تجاري.

**السؤال الذي يجيب عنه المقرر:** هل سيدفع العميل، وهل يربح كل طلب أُنجزه، وهل أنا جاهز نظامياً للبيع؟

**المُخرَج:** منتج أولي منشور على واتساب أو الويب، ونموذج تسعير مبني على اقتصاديات الوحدة، وخطة وصول للسوق، وقائمة جاهزية نظام حماية البيانات الشخصية، وتجربة واحدة على الأقل مع منشأة حقيقية.

**نواتج التعلّم:** بنهاية المقرر يستطيع المتعلم أن:
1. يحوّل الوكيل إلى منتج أولي يستخدمه عميل حقيقي.
2. يحسب تكلفة المهمة المنجزة ويختار نموذج تسعير مناسباً.
3. يضع خطة وصول إلى أول عشرة عملاء في المملكة.
4. يكمل تقييماً ذاتياً للامتثال ويعرف متى يحتاج إلى مستشار قانوني.
5. يتفاوض على تجربة مدفوعة أو خطاب نوايا.

</div>

---

## Modules

| # | Module | Hours | Core content | Activity |
|---|---|---|---|---|
| 3.1 | From prototype to MVP | 3 | What an MVP must have: one job done reliably, a channel, onboarding, a way to get help, a way to stop. Deploying on WhatsApp or a web endpoint. Arabic and right-to-left interface basics | Deploy the agent to a live test channel |
| 3.2 | Business models for agentic ventures | 3 | Per seat, per task, per outcome, subscription with usage caps, hybrid. Productised service versus software. Avoiding the thin-wrapper trap: what you own that a model release cannot replace | Complete the [AI Business Model Canvas](../../04-entrepreneur-toolkit/05-ai-business-model-canvas.md) |
| 3.3 | Unit economics | 3 | Cost per resolved task: model usage, tools, human review, failures and retries. Gross margin per task. Sensitivity to success rate and model choice. Pricing from value | Run the [calculator](../../04-entrepreneur-toolkit/06-unit-economics.md) on your own numbers |
| 3.4 | Compliance readiness | 4 | PDPL for founders: what personal data the agent touches, legal basis, privacy notice, retention, processors, transfers outside the Kingdom, breach handling. AI ethics expectations from buyers. Security basics for selling to larger organisations | Complete the [PDPL self-assessment](../../02-saudi-market-knowledge-framework/compliance-toolkit/pdpl-self-assessment.md) and the [provider assessment](../../02-saudi-market-knowledge-framework/compliance-toolkit/third-party-provider-assessment.md) |
| 3.5 | Going to market in the Kingdom | 3 | First ten customers. Selling to SMEs, to enterprises and to government-related buyers. Trust signals: Arabic support, local references, data location, commercial registration. Channels that work: referrals, sector communities, events, WhatsApp | Write a first-ten-customers plan |
| 3.6 | Pilots and letters of intent | 2 | Designing a pilot: scope, duration, success measure, price, data terms, exit. What an LOI is and is not | Draft a pilot offer with the [Pilot and LOI Outline](../../04-entrepreneur-toolkit/09-pilot-and-loi-outline.md) |
| 3.7 | Setting up the business | 2 | Overview of establishing a company in the Kingdom: commercial registration, tax and e-invoicing obligations, bank account, payment collection. Pointers to official services | Checklist review with the [ecosystem directory](../../02-saudi-market-knowledge-framework/06-funding-investment/startup-ecosystem.md) |

## Track differences

| | Core track | Deep track |
|---|---|---|
| 3.1 | Deploy through a low-code platform and a messaging provider | Deploy as a service with logging, rate limits and secrets management |
| 3.3 | Use the spreadsheet method | Instrument the agent to log cost and outcome per task automatically |
| 3.4 | Choose providers with suitable data terms | Also evaluate self-hosting an open-weight model on infrastructure located in the Kingdom |

## Deliverable: launch pack

1. **Live MVP** with at least one pilot user from a real business.
2. **Business model canvas** and **pricing** with the unit-economics calculation behind it.
3. **Go-to-market plan** for the first ten customers.
4. **Compliance readiness**: PDPL self-assessment, provider assessment, privacy notice draft, open issues listed.
5. **Pilot offer** sent to at least three businesses; responses recorded.

## Rubric

| Criterion | Weight | Strong submission |
|---|---|---|
| Real usage | 30% | A real business has used the MVP; feedback and usage are recorded |
| Economics | 25% | Cost per resolved task is measured, not guessed; price leaves a positive margin with stated assumptions |
| Compliance readiness | 20% | Data flows are mapped; gaps are listed with owners; nothing is waved away |
| Go-to-market | 15% | Named prospects, a reachable channel, a clear first offer |
| Defensibility | 10% | A credible answer to "what stops a competitor doing this next month?" |

## Common mistakes

- Pricing per seat when the product replaces work, not seats.
- Ignoring the cost of failed tasks and human review.
- Treating compliance as a document to write after the first sale.
- Offering free pilots with no success measure and no end date.
- Promising a customer that data stays in the Kingdom without checking where each provider processes it.

**Note.** Module 3.7 is orientation only. Company formation, tax and licensing rules change; follow the official portals and take professional advice.

## Companion tools (optional)

Separate repositories by the same author; see [companion repositories](../../07-resources/companion-repositories.md). The deliverable is graded with the Academy's templates.

| Module | Tool | Exercise |
|---|---|---|
| 3.1 | [Bayan](https://github.com/malenezi/bayan) `arabic-ux-writing` for onboarding and help text; `rtl-audit` for an existing interface | [B1](../../05-agentic-ai-lab/exercises/b1-agent-messages-in-arabic.md), [B4](../../05-agentic-ai-lab/exercises/b4-rtl-audit.md) |
| 3.2 | [Riyada](https://github.com/malenezi/riyada) `business-planning`: lean canvas, and a full business plan when a bank or support programme asks for one | |
| 3.3 | Riyada `financial-modeling`: a 36-month company model fed by the Academy's cost per resolved task | [R4](../../05-agentic-ai-lab/exercises/r4-financial-model.md) |
| 3.5 | Riyada `go-to-market`: ideal customer profile, positioning and messaging, 90-day launch plan | |
| 3.5 | Bayan `arabic-rtl-web`: a bilingual landing page for the pilot | [B2](../../05-agentic-ai-lab/exercises/b2-bilingual-landing-page.md) |

Compliance (3.4), pilots and letters of intent (3.6) and company set-up (3.7) have no equivalent in Riyada; use the [Saudi Market Knowledge Framework](../../02-saudi-market-knowledge-framework/README.md). Riyada's parallel workflow is [Launch to traction](https://github.com/malenezi/riyada/blob/main/workflows/03-launch-to-traction.en.md).

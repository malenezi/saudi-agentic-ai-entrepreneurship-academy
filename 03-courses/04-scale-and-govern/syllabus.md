# المقرر 4: التوسع والحوكمة
# Course 4: Scale and Govern

> **مسودة مخطط · Draft outline.** هذا المقرر لم يُبنَ بعد. المحتوى التفصيلي يُطوَّر على مراحل، والمخطط قابل للتغيير. ملاحظاتك واقتراحاتك مرحّب بها. · This course is not built yet. Detailed content will be developed in later iterations and this outline may change. Comments and suggestions are welcome.


<div dir="rtl">

**المدة:** 16 ساعة · **المستوى:** متقدم · **المتطلب السابق:** منتج أولي له مستخدم حقيقي · **الركيزة:** احكُم وتوسّع

**لمن؟** المؤسسون الذين أثبتوا أن المنتج يعمل وأن عميلاً يريده، ويستعدون للنمو أو للتمويل.

**السؤال الذي يجيب عنه المقرر:** هل تستطيع منشأتي أن تنمو دون أن تفقد السيطرة على الجودة والتكلفة والمخاطر؟

**المُخرَج:** معمارية تشغيل قائمة على الوكلاء مع ضوابط حوكمة ومؤشرات أداء، وسجل مخاطر، وخارطة توسع، وعرض استثماري، يُقدَّم في يوم العروض.

**شرط التخرج:** خطاب نوايا موقّع من منشأة سعودية، أو مؤشرات استخدام حقيقية.

**نواتج التعلّم:** بنهاية المقرر يستطيع المتعلم أن:
1. يصمّم تشغيل المنشأة حول وكلاء متعددين مع أدوار بشرية واضحة.
2. يراقب الجودة والتكلفة ويستجيب للحوادث.
3. يبني سجل مخاطر وضوابط تتوافق مع ما يطلبه المشترون في المملكة.
4. يختار مسار النمو المناسب: إيرادات، حاضنة، مسرّعة، أو استثمار.
5. يعرض مشروعه بأدلة أمام مستثمرين ومحكّمين.

</div>

---

## Modules

| # | Module | Hours | Core content | Activity |
|---|---|---|---|---|
| 4.1 | The agent-operated company | 3 | Mapping the business as functions run by agents and supervised by people: sales, support, operations, finance, reporting. Shared context and memory across agents. Role of the founder as designer and approver | Draw the operating architecture: agents, humans, systems, handoffs |
| 4.2 | Monitoring quality and cost | 3 | Production metrics: success rate, escalation rate, cost per resolved task, time to resolution, customer satisfaction. Sampling and review. Alerts and budgets. Model and prompt change control | Define a weekly KPI sheet and a change log |
| 4.3 | Governance and risk | 3 | AI risk register. Applying responsible-AI principles in practice: fairness, transparency, accountability, privacy, reliability. Telling users they are dealing with an agent. Records a buyer or regulator may ask for | Complete the [AI Risk Register](../../02-saudi-market-knowledge-framework/compliance-toolkit/ai-risk-register.md) |
| 4.4 | Security for agentic systems | 2 | Threats specific to agents: prompt injection, data leakage through tools, over-broad permissions, compromised integrations. Least privilege. Secrets. Incident response. What enterprise and government-related buyers typically ask of vendors | Complete the [Agent Security Assessment](../../02-saudi-market-knowledge-framework/compliance-toolkit/agent-security-assessment.md) |
| 4.5 | Growth paths and funding | 3 | Bootstrapping on revenue versus raising. The Saudi landscape: support programmes, incubators, accelerators, angels, venture funds. What each expects. Investor data room. Technical due diligence for an agentic product | Choose a path and build a target list from the [funding directory](../../02-saudi-market-knowledge-framework/06-funding-investment/funding-and-investment.md) |
| 4.6 | Pitch and Demo Day | 2 | Pitch structure for an agentic venture: problem, proof, product, economics, governance, team, ask. Live demo discipline | Deliver the pitch using the [Pitch Deck Outline](../../04-entrepreneur-toolkit/08-pitch-deck-outline.md) |

## Buildathon (optional, 48 hours)

Cohorts end with a weekend sprint before Demo Day. Mixed teams of engineers and domain experts take one real problem from a Saudi SME and ship a working agent with a test set. Judged with the academy rubric: customer evidence first.

## Track differences

| | Core track | Deep track |
|---|---|---|
| 4.1 | Architecture diagram and role descriptions | Also implement shared state and handoffs between at least two agents |
| 4.2 | KPI sheet updated by hand weekly | Automated dashboards, tracing and cost alerts |
| 4.4 | Checklist and provider questions | Also run a basic prompt-injection test set against your own agent |

## Deliverable: scale pack

1. **Operating architecture** with agents, human roles, systems and approval points.
2. **KPI sheet** with at least four weeks of real or pilot data.
3. **AI risk register** and **agent security assessment**.
4. **Scaling roadmap** for the next 12 months with a chosen growth path.
5. **Investor pitch** and a live demo.
6. **Graduation evidence**: signed LOI or live usage metrics.

## Rubric

| Criterion | Weight | Strong submission |
|---|---|---|
| Customer evidence | 30% | Signed LOI, paying customer or sustained real usage |
| Operating design | 20% | Clear division of work between agents and people; nothing consequential is unowned |
| Governance and security | 20% | Risks are specific to this product, each with an owner and a control that exists |
| Economics at scale | 15% | Shows how margin behaves as volume grows, including review and failure costs |
| Pitch | 15% | Evidence-led, honest about limits, clear ask |

## Common mistakes

- Scaling before the success rate is stable.
- A risk register copied from a template with no product-specific entries.
- Giving agents broad access "to be safe" instead of the least they need.
- Raising money to find out whether customers want the product.

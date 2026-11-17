# B5 files · ملفات التمرين B5

Companion files for [exercise B5](../b5-venture-dashboard.md). Code is Apache-2.0; data and text are CC BY 4.0. **All data is synthetic.** "Mirsah Business Services" (مِرساة لخدمات الأعمال) is a fictional company; any resemblance to a real one is unintended.

| File | What it is |
|---|---|
| `data/baseline/` | One month of operations: `tasks.csv`, `agent_usage.csv`, `audit_log.csv`, `customers.csv`, `params.json` |
| `generate_data.py` | Rebuilds the baseline and builds the three decision scenarios. Same seed, same files |
| `compute_metrics.py` | Computes every KPI from the CSV files; `--compare` checks your own numbers |
| `expected/` | Reference metrics for the four scenarios |
| `kpi-dictionary.md` | Definitions, formulas and denominators |
| `founder-decision-log.md` | The decision template, one entry per scenario |
| `skeleton.html` | A two-KPI bilingual page that reads `metrics.js`. A starting point, not the dashboard |

```bash
cd 05-agentic-ai-lab/exercises/b5-venture-dashboard
python3 compute_metrics.py data/baseline --out metrics.json --js metrics.js
python3 compute_metrics.py data/baseline --compare expected/baseline.json
python3 generate_data.py --scenario volume-up --out data/volume-up
```

Python 3.9 or newer, standard library only.

Known traps in `tasks.csv`, left there on purpose: six exact duplicate rows, and open tasks with empty `completed_at` and `quality_score`.

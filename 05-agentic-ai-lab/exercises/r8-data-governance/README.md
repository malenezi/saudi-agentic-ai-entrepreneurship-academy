# R8 files · ملفات التمرين R8

Companion files for [exercise R8](../r8-data-governance.md). Code is Apache-2.0. `dataset_sample.csv` is synthetic: identifiers follow the pattern `1000000NNN`, phone numbers `0500000NNN`, and the one email address uses `example.com`. The faults in it are deliberate.

```bash
python3 data_governance_lint.py dataset_sample.csv policy.json            # 13 errors, 2 warnings
python3 data_governance_lint.py my_file.csv my_policy.json --strict
```

A pass means the file meets the policy you wrote. It is not a finding of legal compliance.

`bidi_lint.py` reports warnings on `dataset_sample.csv` because it is raw data with mixed-direction values, not display text. Lint the Markdown and HTML, not the CSV.

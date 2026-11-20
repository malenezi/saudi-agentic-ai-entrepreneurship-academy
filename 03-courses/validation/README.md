# التحقق من المقررات · Validation

What has been checked, by what means, and what has not. Five layers, in increasing order of what they can prove.

| Layer | What it is | Status on 20 November 2026 |
|---|---|---|
| 1. Automated checks | Links, tables, deck builds, quiz keys, course structure, lab code, the completion standard, the fifteen-week plan | **Run on every change** (`make check`) |
| 2. [Desk walkthrough](desk-walkthrough.md) | Four invented learners through all 28 modules; every command executed | **Done.** Six findings corrected. Not a pilot |
| 2b. [Source re-check, Courses 1 and 2](source-recheck-c1-c2.md) | Every cited source page re-opened and compared with the register | **Done by automated fetch.** Three entries corrected. Not repeated by a human reader |
| 3. [Specialist review packets](review-packets/) | Claim registers, questions and sign-off forms for a lawyer, a tax adviser, a security practitioner and an investor | **Prepared, not reviewed.** No sign-off exists. [Invitation messages](review-packets/invitations.md) are ready to send |
| 4. [Pilot protocol](pilot-protocol.md) | What a first cohort should collect and how to report it | **Not run** |

## How regulatory content is labelled

Every external fact is in [SOURCES.md](../../SOURCES.md) with its source and its limit. The review packets sort the claims used in regulated lessons into three groups:

| Label | Meaning | What a reader should do |
|---|---|---|
| **Source page cited** | The authors read the issuing body's own page or document | Still confirm before relying on it: pages change, and a reading is not a ruling |
| **Secondary or partial reading** | Read through a law-firm note, a press report or a summary, or only in part | Treat as orientation. Ask a professional or the authority |
| **Draft or not final** | The instrument was a draft or under consultation when read | Do not treat as in force. Check its status |

Ten lessons that touch law, tax, security or funding carry a verification note under their header with these counts. No lesson states that it has been professionally reviewed, because none has.

| Packet | Claims | Source page cited | Secondary or partial | Draft |
|---|---|---|---|---|
| [Legal and privacy](review-packets/legal-privacy.md) | 21 | 4 | 14 | 3 |
| [Tax and establishment](review-packets/tax-establishment.md) | 20 | 11 | 9 | 0 |
| [Cybersecurity](review-packets/cybersecurity.md) | 9 | 1 | 7 | 1 |
| [Funding and investment](review-packets/funding-investment.md) | 4 | 2 | 2 | 0 |

## What remains outside the repository

1. A signed specialist review of each packet.
2. A pilot with learners and real businesses, reported with the protocol.
3. Access to real businesses for each cohort.

<div dir="rtl">

## بالعربية

أربع طبقات للتحقق: فحوص آلية تُشغَّل مع كل تغيير، وجولة مكتبية أُجريت بأربعة متعلمين مختلَقين وليست تجربة، وأربع حزم مراجعة أُعدّت لمختصين ولم يوقّعها أحد، وبروتوكول تجربة لم تُجرَ. كل معلومة تنظيمية مصنّفة: من صفحة الجهة نفسها، أو من ملخص ثانوي أو قراءة جزئية، أو من مشروع غير نهائي. ولا درس يدّعي أنه روجع مهنياً.

</div>

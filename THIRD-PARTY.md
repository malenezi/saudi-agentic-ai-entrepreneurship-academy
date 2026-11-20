# Third-party components and attribution

What this repository uses that it did not write, and under what terms. The repository's own licences are [Apache-2.0](LICENSE) for code and [CC BY 4.0](LICENSE-CONTENT.md) for content.

## Runtime dependencies

**None.** Every script, test, calculator and lab runs on Python 3.9 or newer with the standard library only. Nothing is installed with `pip`, and no service, account or key is needed to read, teach or test the materials.

## Bundled or derived

| Component | Where | Origin and licence |
|---|---|---|
| Slide deck engine and page template | `tools/slides/template.html`, and every built deck in `03-courses/*/slides/*.html` | From [Bayan](https://github.com/malenezi/bayan) (`arabic-html-slides`), by the same author, MIT |
| Academy brand assets | `assets/brand/` | Made for this repository; CC BY 4.0 with the rest of the content |

## Loaded at view time, not bundled

| Component | Where | Terms |
|---|---|---|
| IBM Plex Sans Arabic, IBM Plex Sans, Noto Kufi Arabic | The decks, the landing page and the workbook request them from Google Fonts and fall back to system Arabic fonts offline | Published by their projects under the SIL Open Font License 1.1. Check the font's own licence file before redistributing font files |

Opening a deck online therefore contacts Google's font servers. Offline, or where that is not acceptable, the pages work with system fonts.

## Used in automation only

| Component | Where | Terms |
|---|---|---|
| `actions/checkout`, `actions/setup-python` | `.github/workflows/` | GitHub's own actions, under their repository licences |
| Bayan `bidi_lint.py` | Optional local check of Arabic text direction; not required by CI | MIT |
| Headless Chrome with Playwright | Used by the authors to render decks and check for overflow; not required to build, test or teach | Their own licences; nothing from them is in the repository |

## Optional services named in the labs

The Course 2 labs run with a built-in simulator and need no service. They can call any chat endpoint that follows the OpenAI chat-completions format. One free local runtime is named as an example ([SOURCES.md](SOURCES.md), A125). Naming it is not a recommendation, and no provider's software or model weights are included here. A model's own licence governs its use.

## Names, marks and sources

Company names, product names, standards and official documents referred to in the lessons belong to their owners. Facts taken from them are listed with links in [SOURCES.md](SOURCES.md). Nothing here is endorsed by, or affiliated with, any government body, standards project or company named.

## Examples

Every business, person, message and figure in the worked examples, labs and practice records is invented for teaching and labelled as such. Published cases in `06-case-studies/` are from public sources, cited there.

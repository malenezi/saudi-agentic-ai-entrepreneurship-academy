#!/usr/bin/env python3
# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""Build the methodology library's index and its page on the site.

    python3 tools/build_library.py            write 09-methodology-library/README.md and library.html
    python3 tools/build_library.py --check    exit 1 if either is out of date or the registry has a problem
    python3 tools/build_library.py --list     print the cards, one per line

The registry is 09-methodology-library/library.json. A card is a Markdown file in
09-methodology-library/cards/ named after its id. Standard library only.
"""
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LIB = ROOT / "09-methodology-library"
REGISTRY = LIB / "library.json"

DOMAINS = {
    "opportunity": ("اكتشاف الفرص وفهم السوق", "Opportunity discovery and market"),
    "business-model": ("نموذج العمل والقيمة", "Business model and value"),
    "venture": ("تأسيس المشروع وإدارته", "Venture formation and management"),
    "product-project": ("إدارة المنتجات والمشاريع", "Product and project management"),
    "requirements-design": ("تحليل المتطلبات وتصميم الأنظمة", "Requirements and system design"),
    "data": ("هندسة البيانات وتصميمها", "Data engineering and design"),
    "agentic-engineering": ("هندسة الأنظمة القائمة على الوكلاء", "Agentic AI engineering"),
    "software-engineering": ("تطوير البرمجيات والتشغيل", "Software engineering and operations"),
    "testing-evaluation": ("الاختبار والتقييم وضمان الجودة", "Testing, evaluation and quality"),
    "governance-scale": ("الحوكمة والأمن والتوسع التجاري", "Governance, security and scaling"),
}
TYPES = {"framework": ("إطار عمل", "Framework"), "method": ("منهجية", "Method"),
         "model": ("نموذج", "Model"), "tool": ("أداة أو قالب", "Tool or template")}
TIERS = {"essential": ("أساسي", "Essential"), "practitioner": ("تطبيقي", "Practitioner"),
         "advanced": ("متقدم", "Advanced")}
ORIGINS = {"global": ("معروف عالمياً", "Widely known"), "academy": ("من تطوير الأكاديمية", "Developed by the Academy")}
STAGES = {1: ("اكتشاف الفرصة", "Find the opportunity"), 2: ("بناء الوكيل", "Build the agent"),
          3: ("الإطلاق والنموذج التجاري", "Launch and business model"), 4: ("التوسع والحوكمة", "Scale and govern")}
SECTIONS = ["الغرض", "متى يُستخدم", "متى لا يُستخدم", "المدخلات", "الخطوات", "القالب", "مثال توضيحي",
            "كيف يعين الوكيل الذكي", "المخرج", "معايير الجودة", "المصدر والترخيص", "في الأكاديمية"]
REQUIRED = ["id", "ar", "en", "domain", "type", "tier", "origin", "stages", "sources", "licence",
            "used_in", "summary_ar", "summary_en"]


def load():
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def source_ids():
    """Identifiers in section A of the source register."""
    text = (ROOT / "SOURCES.md").read_text(encoding="utf-8")
    section = text[text.index("## A."):text.index("## B.")]
    return set(re.findall(r"^\| (A\d+) \|", section, flags=re.M))


def problems(registry=None):
    """Everything wrong with the registry and the card files, as a list of sentences."""
    registry = registry or load()
    found, known, seen = [], source_ids(), set()
    for card in registry["cards"]:
        cid = card.get("id", "?")
        missing = [key for key in REQUIRED if key not in card]
        if missing:
            found.append("%s: missing %s" % (cid, ", ".join(missing)))
            continue
        if cid in seen or not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", cid):
            found.append("%s: id repeated or not lower-case words joined by hyphens" % cid)
        seen.add(cid)
        for key, table in (("domain", DOMAINS), ("type", TYPES), ("tier", TIERS), ("origin", ORIGINS)):
            if card[key] not in table:
                found.append("%s: unknown %s %r" % (cid, key, card[key]))
        if not card["stages"] or any(stage not in STAGES for stage in card["stages"]):
            found.append("%s: stages must be one or more of 1 to 4" % cid)
        if card["origin"] == "global" and not card["sources"]:
            found.append("%s: a widely known model needs a source in SOURCES.md section A" % cid)
        for sid in card["sources"]:
            if sid not in known:
                found.append("%s: source %s is not in SOURCES.md section A" % (cid, sid))
        if not card["used_in"]:
            found.append("%s: used_in is empty; a card must point at where the Academy uses the model" % cid)
        for rel in card["used_in"]:
            if not (ROOT / rel).exists():
                found.append("%s: used_in path does not exist: %s" % (cid, rel))
        path = LIB / "cards" / (cid + ".md")
        if not path.exists():
            found.append("%s: no card file" % cid)
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("# %s · %s\n" % (card["ar"], card["en"])):
            found.append("%s: the card's first line must be '# %s · %s'" % (cid, card["ar"], card["en"]))
        headings = re.findall(r"^## (.+)$", text, flags=re.M)
        if headings != SECTIONS:
            found.append("%s: sections differ from the standard card" % cid)
        for sid in card["sources"]:
            if "[%s](" % sid not in text:
                found.append("%s: the card does not cite %s" % (cid, sid))
        for rel in card["used_in"]:
            if rel.rsplit("/", 1)[-1] not in text:
                found.append("%s: the card does not link to %s" % (cid, rel))
        if card["origin"] == "academy" and "من تطوير الأكاديمية" not in text:
            found.append("%s: an Academy model must say so in its card" % cid)
    on_disk = {p.stem for p in (LIB / "cards").glob("*.md")}
    for extra in sorted(on_disk - seen):
        found.append("%s: card file with no entry in library.json" % extra)
    planned = [name for names in registry.get("planned", {}).values() for name in names]
    for domain in registry.get("planned", {}):
        if domain not in DOMAINS:
            found.append("planned: unknown domain %r" % domain)
    built = {card["en"] for card in registry["cards"] if "en" in card}
    for name in sorted(built.intersection(planned)):
        found.append("planned: %s already has a card" % name)
    return found


# ---------- 09-methodology-library/README.md ----------

def readme(registry):
    cards, planned = registry["cards"], registry.get("planned", {})
    waiting = sum(len(names) for names in planned.values())
    out = ["# مكتبة المنهجيات والنماذج · Methodology and framework library", "",
           "<!-- Generated by tools/build_library.py from library.json. Edit the registry or a card, then run the tool. -->", "",
           '<div dir="rtl">', "",
           "بطاقة موحّدة لكل نموذج أو منهجية يحتاج إليها رائد الأعمال في رحلته: ما غرضه، ومتى يُستخدم ومتى لا يُستخدم، وخطواته، وقالبه، "
           "ومثال توضيحي، وكيف يعين الوكيل الذكي على تطبيقه، وأين يرد في مقررات الأكاديمية وأدواتها.", "",
           "**في المكتبة الآن %d بطاقة، و%d نموذجاً تُكتب بطاقاتها تباعاً.** تصفّحها في [صفحة المكتبة](../library.html) بحسب المرحلة والمجال والمستوى."
           % (len(cards), waiting), "",
           "**ثلاث قواعد:**", "",
           "1. **لا بطاقة لنموذج معروف دون مصدر** مقيَّد في [سجل المصادر](../SOURCES.md)، مع تاريخ التحقق.",
           "2. **نصف ونحيل ولا ننسخ.** لوحات الآخرين وقوالبهم تبقى عند أصحابها بتراخيصها. القوالب هنا من صياغة الأكاديمية.",
           "3. **نماذج الأكاديمية تُسمّى باسمها.** ما طوّرته الأكاديمية يحمل وسم «من تطوير الأكاديمية»، ولا يُقدَّم معياراً عالمياً.", "",
           "**لم تُجرَّب البطاقات مع متدربين حتى الآن.** الأمثلة توضيحية وأرقامها مصنوعة ما لم يُذكر مصدر.", ""]
    for tier, (tier_ar, _) in TIERS.items():
        rows = [card for card in cards if card["tier"] == tier]
        if not rows:
            continue
        out += ["## المستوى: %s" % tier_ar, "", "| النموذج | النوع | المرحلة | المنشأ | خلاصته |", "|---|---|---|---|---|"]
        for card in rows:
            out.append("| [%s](cards/%s.md) (%s) | %s | %s | %s | %s |" % (
                card["ar"], card["id"], card["en"], TYPES[card["type"]][0],
                "، ".join(str(stage) for stage in card["stages"]), ORIGINS[card["origin"]][0], card["summary_ar"]))
        out.append("")
    out += ["المرحلة برقم المقرر: 1 اكتشاف الفرصة، 2 بناء الوكيل، 3 الإطلاق والنموذج التجاري، 4 التوسع والحوكمة.", "",
            "## ما يُكتب تباعاً", "",
            "أسماء فقط حتى تُكتب البطاقة ويُتحقق من مصدرها. ترتيب الكتابة: نماذج الأكاديمية، ثم المستوى التطبيقي والمخططات، ثم بقية المجالات، ثم المستوى المتقدم.", ""]
    for domain, (domain_ar, _) in DOMAINS.items():
        if planned.get(domain):
            out += ["**%s:** %s" % (domain_ar, " · ".join(planned[domain])), ""]
    out += ["## كيف تُضاف بطاقة", "",
            "انسخ [قالب البطاقة](card-template.md) إلى `cards/` باسم المعرّف، وأضف مدخلها في `library.json`، ثم شغّل `python3 tools/build_library.py`. "
            "الفحص `make check` يرفض بطاقة بلا مصدر، أو بقسم ناقص، أو برابط إلى ملف غير موجود. ما لم يُعتمد من المقترح الأصلي وسببه في [سجل ما لم يُعتمد](not-adopted.md).", "",
            "</div>", "",
            "## In English", "",
            "One standard card per framework, method or model a founder needs on the way from an opportunity to a growing venture: purpose, "
            "when to use it and when not to, steps, a blank template, an illustrative example, how an AI agent helps apply it, and where the "
            "Academy's courses and tools use it. Cards are written in Arabic with English terms.", "",
            "**%d cards so far; %d more are listed by name and are written in batches.** Browse them on the [library page](../library.html)."
            % (len(cards), waiting), "",
            "Three rules: no card for a known model without a source in the [source register](../SOURCES.md); other people's canvases are "
            "described and linked, never copied; a model developed by the Academy is labelled as such and is not presented as a standard. "
            "No card has been tried with learners. What was left out of the original proposal is in [not-adopted.md](not-adopted.md).", "",
            "| Card | Type | Tier | Course | Summary |", "|---|---|---|---|---|"]
    for card in cards:
        out.append("| [%s](cards/%s.md) | %s | %s | %s | %s |" % (
            card["en"], card["id"], TYPES[card["type"]][1], TIERS[card["tier"]][1],
            ", ".join(str(stage) for stage in card["stages"]), card["summary_en"]))
    return "\n".join(out) + "\n"


# ---------- library.html ----------

PAGE = r'''<!doctype html>
<!--
  SAAEA · methodology library page. Generated by tools/build_library.py from 09-methodology-library/library.json.
  Edit the registry or the generator, not this file. Licence: CC BY 4.0 (content).
-->
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>مكتبة المنهجيات والنماذج · SAAEA</title>
<meta name="description" content="بطاقة موحّدة لكل نموذج ومنهجية يحتاج إليها رائد الأعمال: من اكتشاف الفرصة إلى بناء الوكيل الذكي والإطلاق والتوسع، مع مصدر كل نموذج.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Kufi+Arabic:wght@500;700&family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root { --bg: #f8fafc; --ink: #1e293b; --deep: #0f172a; --muted: #475569; --line: #e2e8f0; --card: #ffffff; --accent: #d97706; --accent-ink: #b45309; --accent-soft: #fef3c7;
  --font-ar: "IBM Plex Sans Arabic", "Noto Sans Arabic", "Segoe UI", Tahoma, sans-serif; --font-en: "IBM Plex Sans", "Segoe UI", system-ui, sans-serif;
  --display-ar: "Noto Kufi Arabic", "IBM Plex Sans Arabic", "Segoe UI", Tahoma, sans-serif; }
*, *::before, *::after { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--ink); font: 18px/1.9 var(--font-ar); overflow-wrap: break-word; }
[lang="en"] { font-family: var(--font-en); line-height: 1.6; }
a { color: var(--accent-ink); text-underline-offset: 4px; }
a:focus-visible, button:focus-visible, input:focus-visible { outline: 3px solid var(--accent); outline-offset: 3px; border-radius: 6px; }
.wrap { max-inline-size: 1080px; margin-inline: auto; padding-inline: 24px; }
header { background: var(--ink); color: #f8fafc; padding-block: 36px 30px; }
header a { color: #fcd34d; }
h1, h2 { font-family: var(--display-ar); line-height: 1.5; margin: 0; text-wrap: balance; }
h1 { font-size: clamp(26px, 3.6vw, 38px); }
header p { color: #e2e8f0; margin: 10px 0 0; max-inline-size: 68ch; }
header .crumb { font-size: 15.5px; margin: 0 0 10px; }
.note { background: var(--accent-soft); border-inline-start: 5px solid var(--accent); padding: 12px 18px; border-radius: 12px; margin-block: 28px 0; font-size: 16px; }
.filters { margin-block: 28px 0; display: grid; gap: 14px; }
.filters input { inline-size: 100%; font: inherit; padding: 10px 16px; border: 1px solid #94a3b8; border-radius: 12px; background: var(--card); color: var(--ink); }
fieldset { border: 0; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }
legend { float: inline-start; font-weight: 600; font-size: 16px; margin-inline-end: 10px; padding: 0; }
.chip { font: 500 15.5px/1.6 var(--font-ar); padding: 5px 14px; border-radius: 999px; border: 1px solid #94a3b8; background: var(--card); color: var(--ink); cursor: pointer; }
.chip[aria-pressed="true"] { background: var(--ink); border-color: var(--ink); color: #fff; }
.count { color: var(--muted); font-size: 16px; margin: 20px 0 0; }
.grid { list-style: none; padding: 0; margin: 14px 0 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 320px), 1fr)); gap: 16px; }
.grid a { display: grid; gap: 4px; align-content: start; block-size: 100%; background: var(--card); border: 1px solid var(--line); border-block-start: 5px solid var(--accent); border-radius: 16px; padding: 18px 20px; text-decoration: none; color: var(--ink); }
.grid a:hover { box-shadow: 0 10px 24px rgb(15 23 42 / .10); }
.grid li.academy a { border-block-start-color: var(--ink); }
.grid .meta { font-size: 14.5px; font-weight: 600; color: var(--accent-ink); }
.grid .t { font: 700 20px/1.6 var(--display-ar); }
.grid .en { font-size: 15px; color: var(--muted); }
.grid .d { font-size: 16px; line-height: 1.8; color: var(--muted); }
.grid .tags { font-size: 14.5px; color: var(--muted); margin-block-start: 6px; }
.planned { margin-block: 44px 0; }
.planned h2 { font-size: 24px; }
.planned p { color: var(--muted); max-inline-size: 78ch; }
.planned dl { margin: 12px 0 0; }
.planned dt { font-weight: 600; margin-block-start: 12px; }
.planned dd { margin: 0; color: var(--muted); font-size: 16px; }
footer { margin-block-start: 48px; border-block-start: 1px solid var(--line); padding-block: 24px 44px; color: var(--muted); font-size: 15px; }
[hidden] { display: none !important; }
@media (max-width: 520px) { body { font-size: 17px; } .wrap { padding-inline: 18px; } }
@media print { .filters { display: none; } header { background: none; color: var(--ink); } header p { color: var(--ink); } }
</style>
</head>
<body>
<header>
  <div class="wrap">
    <p class="crumb"><a href="index.html">الأكاديمية السعودية لريادة الأعمال بالذكاء الاصطناعي الوكيلي</a> · <a href="index.en.html" lang="en" dir="ltr">English</a></p>
    <h1>مكتبة المنهجيات والنماذج</h1>
    <p>أي نموذج تحتاج إليه الآن، وما المخرج المطلوب منه، وكيف يعينك وكيل ذكي على تطبيقه؟ لكل نموذج بطاقة موحّدة ومصدر موثّق. <bdi lang="en" dir="ltr">Methodology and framework library: one standard card per model, in Arabic with English terms.</bdi></p>
  </div>
</header>
<main class="wrap">
  <p class="note">في المكتبة الآن <bdi dir="ltr">{N}</bdi> بطاقة، و<bdi dir="ltr">{W}</bdi> نموذجاً تُكتب بطاقاتها تباعاً. لم تُجرَّب البطاقات مع متدربين حتى الآن، وأمثلتها توضيحية. اللوحات والقوالب التي يملكها غيرنا نصفها ونحيل إليها ولا ننسخها.</p>
  <form class="filters" role="search" aria-label="تصفية البطاقات" onsubmit="return false">
    <input type="search" id="q" placeholder="ابحث باسم النموذج بالعربية أو الإنجليزية" aria-label="ابحث في البطاقات">
{FILTERS}
  </form>
  <p class="count" id="count" aria-live="polite">{N} بطاقة</p>
  <ul class="grid" id="cards">
{CARDS}
  </ul>
  <section class="planned" aria-labelledby="h-planned">
    <h2 id="h-planned">ما يُكتب تباعاً</h2>
    <p>أسماء فقط حتى تُكتب البطاقة ويُتحقق من مصدرها.</p>
    <dl>
{PLANNED}
    </dl>
  </section>
</main>
<footer>
  <div class="wrap">المحتوى برخصة <bdi lang="en" dir="ltr">CC BY 4.0</bdi>. <a href="read.html?p=09-methodology-library/README.md">فهرس المكتبة وقواعدها</a> · <a href="read.html?p=SOURCES.md">سجل المصادر</a> · <a href="read.html?p=CONTRIBUTING.md">أضف بطاقة</a></div>
</footer>
<script>
(function () {
  var state = {}, q = document.getElementById("q"), items = [].slice.call(document.querySelectorAll("#cards li")), count = document.getElementById("count");
  function apply() {
    var text = q.value.trim().toLowerCase(), shown = 0;
    items.forEach(function (li) {
      var ok = !text || li.getAttribute("data-text").indexOf(text) !== -1;
      Object.keys(state).forEach(function (key) {
        if (state[key] && (" " + li.getAttribute("data-" + key) + " ").indexOf(" " + state[key] + " ") === -1) ok = false;
      });
      li.hidden = !ok;
      if (ok) shown += 1;
    });
    count.textContent = shown + " بطاقة";
  }
  [].forEach.call(document.querySelectorAll(".chip"), function (chip) {
    chip.addEventListener("click", function () {
      var key = chip.getAttribute("data-key"), value = chip.getAttribute("data-value"), on = chip.getAttribute("aria-pressed") === "true";
      [].forEach.call(document.querySelectorAll('.chip[data-key="' + key + '"]'), function (c) { c.setAttribute("aria-pressed", "false"); });
      state[key] = on ? "" : value;
      if (!on) chip.setAttribute("aria-pressed", "true");
      apply();
    });
  });
  q.addEventListener("input", apply);
})();
</script>
</body>
</html>
'''


def page(registry):
    cards, planned = registry["cards"], registry.get("planned", {})
    esc = html.escape

    def chips(key, legend, table, used):
        row = "".join('<button type="button" class="chip" data-key="%s" data-value="%s" aria-pressed="false">%s</button>'
                      % (key, value, esc(label[0])) for value, label in table.items() if value in used)
        return "    <fieldset><legend>%s</legend>%s</fieldset>" % (legend, row)

    filters = "\n".join([
        chips("stage", "المرحلة", {str(k): v for k, v in STAGES.items()}, {str(s) for c in cards for s in c["stages"]}),
        chips("tier", "المستوى", TIERS, {c["tier"] for c in cards}),
        chips("type", "النوع", TYPES, {c["type"] for c in cards}),
        chips("domain", "المجال", DOMAINS, {c["domain"] for c in cards}),
        chips("origin", "المنشأ", ORIGINS, {c["origin"] for c in cards}),
    ])
    items = []
    for card in cards:
        stages = " ".join(str(stage) for stage in card["stages"])
        items.append(
            '    <li class="%s" data-stage="%s" data-tier="%s" data-type="%s" data-domain="%s" data-origin="%s" data-text="%s">'
            '<a href="read.html?p=09-methodology-library/cards/%s.md"><span class="meta">%s · %s</span><span class="t">%s</span>'
            '<span class="en" lang="en" dir="ltr">%s</span><span class="d">%s</span><span class="tags">%s · %s</span></a></li>'
            % (card["origin"], stages, card["tier"], card["type"], card["domain"], card["origin"],
               esc((card["ar"] + " " + card["en"]).lower(), quote=True), card["id"],
               esc(TYPES[card["type"]][0]), esc(TIERS[card["tier"]][0]), esc(card["ar"]), esc(card["en"]),
               esc(card["summary_ar"]), esc(DOMAINS[card["domain"]][0]),
               esc("، ".join(STAGES[stage][0] for stage in card["stages"]))))
    waiting = []
    for domain, (domain_ar, _) in DOMAINS.items():
        if planned.get(domain):
            waiting.append('      <dt>%s</dt><dd lang="en" dir="ltr">%s</dd>' % (esc(domain_ar), esc(" · ".join(planned[domain]))))
    total = sum(len(names) for names in planned.values())
    return (PAGE.replace("{N}", str(len(cards))).replace("{W}", str(total)).replace("{FILTERS}", filters)
            .replace("{CARDS}", "\n".join(items)).replace("{PLANNED}", "\n".join(waiting)))


def main(argv):
    registry = load()
    if "--list" in argv:
        for card in registry["cards"]:
            print("%-28s %-12s %s" % (card["id"], card["tier"], card["en"]))
        return 0
    targets = [(LIB / "README.md", readme(registry)), (ROOT / "library.html", page(registry))]
    if "--check" in argv:
        found = problems(registry)
        stale = [out.name for out, text in targets if not out.exists() or out.read_text(encoding="utf-8") != text]
        for line in found:
            print(line)
        print("the library index and page are up to date" if not stale else "out of date: " + ", ".join(stale))
        return 1 if found or stale else 0
    for out, text in targets:
        out.write_text(text, encoding="utf-8")
        print("built", out.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

// Decide: template 5, tender summariser. The model reads; this code checks every fact against
// the page it cites, and compares requirements with the company profile. Nothing is marked
// "meets" without evidence in the profile, and the decision to bid is never the agent's.
//#include text
//#include read_model
const cfg = $('Config').first().json;
const prepared = $('Prepare').first().json;
const understood = readModel($input.first().json);
//#include result
result.intent = 'summarise_tender';
if (prepared.stopped) return handover('stopped', 'stopped', 'سير العمل موقوف. الكراسات تُقرأ يدوياً.', '');

// The document, split by its page markers. The document is data: nothing in it is an instruction.
const pages = {};
let current = null;
for (const line of prepared.message.split('\n')) {
  const marker = line.match(/^\s*\[\[صفحة (\d+)\]\]\s*$/);
  if (marker) { current = Number(marker[1]); pages[current] = ''; } else if (current !== null) pages[current] += line + '\n';
}
if (!Object.keys(pages).length) return handover('no_document', 'autonomous', 'لم تُرفق كراسة بعلامات صفحات. لا يُلخَّص شيء من الوصف.', '');
const onPage = (value, page) => Number.isInteger(page) && typeof value === 'string' && value.trim() !== '' && Object.prototype.hasOwnProperty.call(pages, page)
  && normalise(pages[page]).includes(normalise(value.trim()));

const FACTS = { issuer: 'الجهة', scope: 'النطاق', location: 'الموقع', duration: 'المدة', deadline: 'الموعد النهائي', guarantee: 'الضمانات', payment_terms: 'شروط الدفع', penalties: 'الغرامات' };
const given = understood.facts && typeof understood.facts === 'object' ? understood.facts : {};
const facts = {};
const rejected = [];
for (const [field, label] of Object.entries(FACTS)) {
  const fact = given[field] && typeof given[field] === 'object' ? given[field] : {};
  if (onPage(fact.value, fact.page)) facts[field] = { label, value: fact.value.trim(), page: fact.page };
  else {
    facts[field] = { label, value: 'غير مذكور', page: null };
    if (fact.value) rejected.push(field); // the model gave a value that is not on the page it cited
  }
}
const list = (x) => (Array.isArray(x) ? x.filter((i) => i && typeof i === 'object') : []);
// Which profile entry a requirement points to is decided by the bid team's own keywords in Config,
// not by the model: a model that names the wrong entry cannot turn a gap into "meets".
const keyOf = (text) => { const hit = cfg.requirement_keys.find(([, words]) => words.some((w) => normalise(text).includes(normalise(w)))); return hit ? hit[0] : null; };
const requirements = list(understood.requirements).filter((r) => onPage(r.text, r.page)).map((r) => {
  const key = keyOf(r.text);
  const evidence = key && Object.prototype.hasOwnProperty.call(cfg.company_profile.evidence, key) ? cfg.company_profile.evidence[key] : null;
  const gap = Boolean(key) && cfg.company_profile.known_gaps.includes(key);
  return { requirement: r.text.trim(), page: r.page, status: evidence ? 'مستوفٍ' : gap ? 'فجوة' : 'غير معروف', evidence: evidence || null };
});
const criteria = list(understood.criteria).filter((c) => onPage(c.text, c.page)).map((c) => ({ text: c.text.trim(), page: c.page }));

const count = (status) => requirements.filter((r) => r.status === status).length;
const notStated = Object.values(facts).filter((f) => f.page === null).map((f) => f.label);
const brief = {
  summary: ['issuer', 'scope', 'duration', 'deadline'].map((f) => `${facts[f].label}: ${facts[f].value}${facts[f].page ? ` (ص ${facts[f].page})` : ''}`),
  facts, requirements, evaluation_criteria: criteria,
  open_questions_for_issuer: notStated.map((label) => `${label}: غير مذكور في الكراسة. يُسأل عنه في فترة الاستفسارات.`),
  fit: { meets: count('مستوفٍ'), gaps: count('فجوة'), unknown: count('غير معروف'),
    note: 'تقييم الملاءمة رأي استشاري مبني على ملف المنشأة. قرار التقديم لمدير العروض.' },
  rejected_model_facts: rejected,
};
result.tool_calls.push({ tool: 'report_write', input: 'brief' });
if (facts.deadline.page) result.pending_approval.push({ action: 'add_deadline_to_calendar', value: facts.deadline.value, level: 'notify', after: 'bid manager approval' });
return done({ action: 'brief', level: 'autonomous', brief, decision_to_bid: 'not the agent\'s: management decision',
  handover: { summary: `موجز منافسة: ${count('مستوفٍ')} مستوفٍ، ${count('فجوة')} فجوة، ${count('غير معروف')} غير معروف، و${notStated.length} معلومة غير مذكورة.`, urgency: 'normal' } });

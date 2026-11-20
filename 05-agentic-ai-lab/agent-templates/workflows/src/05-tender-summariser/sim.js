// Simulated reading: NOT a language model. It reads labelled lines ("الجهة: ...", "شرط: ...")
// and the page markers ("[[صفحة 3]]") from the document text, so the workflow runs with no key
// and no cost. A real model reads unlabelled documents; Decide checks its work the same way.
//#include text
const LABELS = { issuer: 'الجهة', scope: 'نطاق العمل', location: 'الموقع', duration: 'مدة العقد', deadline: 'آخر موعد لتقديم العروض',
  guarantee: 'الضمان الابتدائي', payment_terms: 'شروط الدفع', penalties: 'الغرامات' };
const facts = {};
const requirements = [];
const criteria = [];
let page = null;
for (const line of $input.first().json.message.split('\n')) {
  const marker = line.match(/^\s*\[\[صفحة (\d+)\]\]\s*$/);
  if (marker) { page = Number(marker[1]); continue; }
  const at = line.indexOf(':');
  if (at < 0) continue;
  const label = line.slice(0, at).trim();
  const value = line.slice(at + 1).trim();
  const field = Object.keys(LABELS).find((f) => LABELS[f] === label);
  if (field && !(field in facts)) facts[field] = { value, page };
  if (label === 'معيار') criteria.push({ text: value, page });
  if (label === 'شرط') {
    requirements.push({ text: value, key: null, page }); // Decide maps requirements to the profile
  }
}
return [{ json: { understanding: { facts, requirements, criteria } } }];

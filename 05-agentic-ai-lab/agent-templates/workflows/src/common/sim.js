// Simulated model: NOT a language model. It matches the keywords listed under "sim" in the
// Config node, so the workflow runs with no key, no cost and the same result every time.
// It understands far less than a real model. That is its job: it lets you test the limits.
//#include text
const cfg = $('Config').first().json;
const text = normalise(westernDigits($input.first().json.message));
const has = (words) => words.some((w) => text.includes(normalise(w)));
const hit = (cfg.sim.intents || []).find(([, words]) => has(words));
const understanding = { intent: hit ? hit[0] : 'unknown' };
// More than one request in a message: sentences that end in a question mark or a line break are matched one by one.
// A comma does not split, because a clause that only names the order is context, not a second request. Crude, like the rest of this file.
const intentOf = (clause) => ((cfg.sim.intents || []).find(([, words]) => words.some((w) => clause.includes(normalise(w)))) || [null])[0];
const clauses = text.split(/[؟?\n]+/).map((clause) => clause.trim()).filter(Boolean);
understanding.also = clauses.length > 1 ? [...new Set(clauses.map(intentOf).filter((name) => name && name !== understanding.intent))] : [];
for (const [field, options] of Object.entries(cfg.sim.choices || {})) {
  const option = options.find(([, words]) => has(words));
  understanding[field] = option ? option[0] : null;
}
for (const [field, pattern] of Object.entries(cfg.sim.patterns || {})) {
  const match = text.match(new RegExp(pattern, 'u'));
  understanding[field] = match ? (match[1] ?? match[0]) : null;
}
return [{ json: { understanding } }];

// The model's answer is untrusted: take one JSON object out of it, or nothing.
// Repair is limited to what changes no meaning: text or code fences around the object, curly quotes,
// trailing commas, Python's None, True and False, a bare word where a string was meant, and square brackets
// written around key and value pairs. Anything else stays unreadable, and an unreadable answer never acts.
const modelRead = { unreadable: false, repaired: false, retried: false };
function firstObject(text) { // the first balanced {...}, strings respected
  const start = text.indexOf('{');
  if (start < 0) return null;
  let depth = 0;
  let inString = false;
  let escaped = false;
  for (let i = start; i < text.length; i += 1) {
    const c = text[i];
    if (inString) {
      if (escaped) escaped = false;
      else if (c === '\\') escaped = true;
      else if (c === '"') inString = false;
    } else if (c === '"') inString = true;
    else if (c === '{') depth += 1;
    else if (c === '}') {
      depth -= 1;
      if (depth === 0) return text.slice(start, i + 1);
    }
  }
  return null;
}
function asObject(text) {
  try {
    const value = JSON.parse(text);
    return value && typeof value === 'object' && !Array.isArray(value) ? value : null;
  } catch (error) {
    return null;
  }
}
function parseModelContent(content) {
  const text = String(content);
  const strict = asObject(text.slice(text.indexOf('{'), text.lastIndexOf('}') + 1));
  if (strict) return { value: strict, repaired: false };
  let tidy = text.replace(/[\u201C\u201D\u201E\u201F]/g, '"');
  // Square brackets around key and value pairs ([ "intent": "faq" ]): seen in one answer in five from a small local
  // model on 24 November 2026. A list cannot hold "key": value, so the brackets can only have been meant as braces.
  const bracketed = tidy.match(/\[(\s*"[^"]+"\s*:[\s\S]*)\]/);
  if (bracketed && tidy.indexOf('{') < 0) tidy = '{' + bracketed[1] + '}';
  const candidate = firstObject(tidy);
  if (!candidate) return null;
  // A bare word as a value ({ "intent": stop }) is quoted: the first failure of a small local model (run of 22 November 2026).
  // The value is still checked against the allowed list in Decide.
  const value = asObject(candidate) || asObject(candidate.replace(/,\s*([}\]])/g, '$1')
    .replace(/:\s*None\b/g, ': null').replace(/:\s*True\b/g, ': true').replace(/:\s*False\b/g, ': false')
    .replace(/:\s*([A-Za-z_][\w-]*)\s*(?=[,}\]])/g, (match, word) => (['true', 'false', 'null'].includes(word) ? match : `: "${word}"`)));
  return value ? { value, repaired: true } : null;
}
function readModel(item) {
  if (item && item.understanding && typeof item.understanding === 'object') {
    if (item.model_read && item.model_read.repaired) modelRead.repaired = true;
    return item.understanding;
  }
  let content;
  try {
    content = item.choices[0].message.content;
  } catch (error) {
    content = undefined;
  }
  const parsed = typeof content === 'string' ? parseModelContent(content) : null;
  if (!parsed) {
    modelRead.unreadable = true;
    return { error: 'model_output_unreadable' }; // a model failure must never act on its own
  }
  if (parsed.repaired) modelRead.repaired = true;
  return parsed.value;
}

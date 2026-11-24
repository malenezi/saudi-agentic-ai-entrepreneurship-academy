// Check model output: runs after the HTTP model node, before Decide.
// A readable answer goes on. An answer that came back but cannot be read as one JSON object is sent to the
// model once more with a fixed instruction; the customer's text is not added a second time. A model that
// could not be reached is not retried here. Whatever comes back, Decide reads it again and decides.
//#include read_model
const cfg = $('Config').first().json;
const prepared = $('Prepare').first().json;
const item = $input.first().json || {};
let content;
try {
  content = item.choices[0].message.content;
} catch (error) {
  content = undefined;
}
if (typeof content !== 'string') return [{ json: Object.assign({}, item, { retry: false }) }]; // no answer at all
const parsed = parseModelContent(content);
if (parsed) return [{ json: { retry: false, understanding: parsed.value, model_read: { repaired: parsed.repaired } } }];
if (cfg.retry_unreadable === false) return [{ json: Object.assign({}, item, { retry: false }) }];
const messages = prepared.request_body.messages.concat([
  { role: 'assistant', content: content.slice(0, 2000) },
  { role: 'user', content: 'مخرجك السابق لا يُقرأ كائن JSON. أعد الجواب نفسه كائن JSON واحداً فقط، بالحقول المطلوبة، دون أي نص قبله أو بعده ودون علامات تنسيق.' },
]);
return [{ json: { retry: true, model_url: prepared.model_url, request_body: Object.assign({}, prepared.request_body, { messages }) } }];

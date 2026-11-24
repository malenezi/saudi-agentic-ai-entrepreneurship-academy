// Prepare: everything the model step needs is decided here, in code.
// The customer's text is data. It is wrapped and never mixed into the instructions.
//#include text
const cfg = $('Config').first().json;
const body = $('Webhook').first().json.body || {};
let message = stripHidden(String(body.message ?? ''));
if (cfg.normalise_digits) message = westernDigits(message);
// The wrapper's own tag, typed by a customer, must not close the wrapper.
message = message.replace(/<\s*\/?\s*customer_message\s*>/gi, '[customer_message]');
const glossary = Object.entries(cfg.glossary || {}).map(([term, meaning]) => `- ${term}: ${meaning}`);
// The instructions name the business and, where the model must pick from a list, carry that list.
// Found on the first run with a real model (21 November 2026): the placeholder reached the model as written,
// and the booking instructions said "the approved list" without giving it.
const services = Array.isArray(cfg.services) ? cfg.services.map((name) => `- ${name}`) : [];
// The topics the model may name are the keys of the approved knowledge in Config, not a list fixed in the instructions.
// Found on the second local-model run (24 November 2026): a store with other topics was answered from the wrong entry.
const topics = cfg.knowledge && typeof cfg.knowledge === 'object' && !Array.isArray(cfg.knowledge) ? Object.keys(cfg.knowledge) : [];
const system = String(cfg.instructions).split('(اسم المنشأة)').join(cfg.business_name || 'المنشأة')
  + (services.length ? '\n\nالقائمة المعتمدة للخدمات (اكتب الاسم كما هو هنا):\n' + services.join('\n') : '')
  + (topics.length ? '\n\nالمواضيع المعتمدة لحقل topic (اكتب المفتاح كما هو، وإن لم يكن السؤال عن واحد منها فاكتب null):\n' + topics.map((name) => `- ${name}`).join('\n') : '')
  + (glossary.length ? '\n\nمصطلحات العملاء:\n' + glossary.join('\n') : '');
const stopped = Boolean(cfg.stopped);
return [{
  json: {
    message,
    account: cfg.normalise_account === false ? String(body.account ?? '') : normaliseAccount(body.account ?? ''),
    ref: String(body.ref ?? ''), // the caller's own id for this message; used by the shadow record
    state: body.state && typeof body.state === 'object' ? body.state : {},
    stopped,
    route: !stopped && cfg.model_mode === 'http' ? 'http' : 'sim',
    model_url: String(cfg.model_base_url || '').replace(/\/+$/, '') + '/chat/completions',
    request_body: {
      model: cfg.model_name,
      temperature: 0,
      messages: [
        { role: 'system', content: system },
        { role: 'user', content: `<customer_message>\n${message}\n</customer_message>` },
      ],
    },
  },
}];

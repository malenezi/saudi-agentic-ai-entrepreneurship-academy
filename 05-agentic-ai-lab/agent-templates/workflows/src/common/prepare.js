// Prepare: everything the model step needs is decided here, in code.
// The customer's text is data. It is wrapped and never mixed into the instructions.
//#include text
const cfg = $('Config').first().json;
const body = $('Webhook').first().json.body || {};
let message = String(body.message ?? '');
if (cfg.normalise_digits) message = westernDigits(message);
const glossary = Object.entries(cfg.glossary || {}).map(([term, meaning]) => `- ${term}: ${meaning}`);
// The instructions name the business and, where the model must pick from a list, carry that list.
// Found on the first run with a real model (21 November 2026): the placeholder reached the model as written,
// and the booking instructions said "the approved list" without giving it.
const services = Array.isArray(cfg.services) ? cfg.services.map((name) => `- ${name}`) : [];
const system = String(cfg.instructions).split('(اسم المنشأة)').join(cfg.business_name || 'المنشأة')
  + (services.length ? '\n\nالقائمة المعتمدة للخدمات (اكتب الاسم كما هو هنا):\n' + services.join('\n') : '')
  + (glossary.length ? '\n\nمصطلحات العملاء:\n' + glossary.join('\n') : '');
const stopped = Boolean(cfg.stopped);
return [{
  json: {
    message,
    account: String(body.account ?? ''),
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

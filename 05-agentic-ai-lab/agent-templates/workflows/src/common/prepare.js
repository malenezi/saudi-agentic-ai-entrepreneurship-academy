// Prepare: everything the model step needs is decided here, in code.
// The customer's text is data. It is wrapped and never mixed into the instructions.
//#include text
const cfg = $('Config').first().json;
const body = $('Webhook').first().json.body || {};
let message = String(body.message ?? '');
if (cfg.normalise_digits) message = westernDigits(message);
const glossary = Object.entries(cfg.glossary || {}).map(([term, meaning]) => `- ${term}: ${meaning}`);
const system = cfg.instructions + (glossary.length ? '\n\nمصطلحات العملاء:\n' + glossary.join('\n') : '');
const stopped = Boolean(cfg.stopped);
return [{
  json: {
    message,
    account: String(body.account ?? ''),
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

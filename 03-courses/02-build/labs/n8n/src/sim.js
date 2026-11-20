// Simulated model: NOT a language model. A JavaScript port of SimModel in
// labs/reference/order_agent/model.py, so the lab runs with no key, no cost and no server.
//#include text
const cfg = $('Config').first().json;
const message = $input.first().json.message;

const INTENT_WORDS = [
  ['refund', ['استرداد', 'استرجاع', 'فلوس', 'المبلغ', 'refund']],
  ['cancel', ['الغاء', 'الغي', 'كنسل', 'cancel']],
  ['address_change', ['العنوان', 'عنوان', 'address']],
  ['complaint', ['شكوي', 'complaint']],
  ['shipping_question', ['الشحن', 'تشحن', 'shipping']],
  ['order_status', ['حاله', 'حالة', 'اين', 'وين طلبي', 'تاخر', 'تتبع', 'status', 'update', 'order', 'track']],
];
const CITIES = { 'رياض': 'الرياض', 'جدة': 'جدة', 'دمام': 'الدمام' };
const CONDITION_WORDS = ['اذا', 'لو ما', 'ان لم'];
const URGENT_WORDS = ['اليوم', 'بكره', 'مناسبه', 'مناسبة', 'عاجل', 'ضروري'];

const text = normalise(message);
const has = (words) => words.some((w) => text.includes(normalise(w)));
const found = text.match(/(?<!\p{Nd})\p{Nd}{5}(?!\p{Nd})/u);
let orderId = found ? found[0] : null;
if (cfg.sim_model === 'sim-b' && orderId && text.includes('رقم ' + orderId)) orderId = 'رقم ' + orderId;

let intent = 'unknown';
for (const [name, words] of INTENT_WORDS) {
  if (has(words)) { intent = name; break; }
}
if (intent === 'unknown') {
  for (const [term, name] of Object.entries(cfg.glossary || {})) {
    if (text.includes(normalise(term))) { intent = name; break; }
  }
}
if ((intent === 'unknown' || intent === 'shipping_question') && orderId) intent = 'order_status';
const conditional = intent === 'cancel' && (cfg.rules || []).includes('conditional_cancel') && has(CONDITION_WORDS);
const urgent = conditional && has(URGENT_WORDS);
const cityKey = Object.keys(CITIES).find((k) => text.includes(normalise(k)));

return [{ json: { understanding: { intent, order_id: orderId, city: cityKey ? CITIES[cityKey] : null, urgent, conditional } } }];

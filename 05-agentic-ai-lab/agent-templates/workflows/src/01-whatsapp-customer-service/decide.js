// Decide: template 1, customer service. The oversight table of the template, enforced in code.
// The model only names the intent and the topic. Every answer comes from approved content.
//#include text
//#include read_model
const cfg = $('Config').first().json;
const prepared = $('Prepare').first().json;
const understood = readModel($input.first().json);
//#include result
const INTENTS = ['faq', 'order_status', 'refund', 'cancel', 'discount', 'promise', 'complaint', 'advice', 'human', 'unknown'];
let intent = INTENTS.includes(understood.intent) ? understood.intent : 'unknown';

// A request the model did not name, found in code. Added on 25 November 2026: a small local model never filled "also"
// and labelled cancellations, promises and complaints as order questions. Two checks on the customer's own message,
// whatever the model returned. `second_request_check: false` in Config switches both off.
// 1. The words listed in Config for each request that needs a person. Where the model saw only a question and there is
//    one such request, the stricter reading replaces the model's: for an order question, when the message is one sentence
//    or names no stored order; for a general question, when its topic is not in the approved knowledge.
//    Anything else is a second request for the gate below. One exception, on purpose: a one-sentence question the model
//    tied to an approved topic is answered from that topic, because "what is your refund policy?" carries the word too.
// 2. More than one stored order named in one message: one order at a time, so the whole message goes to a person.
const NEEDS_PERSON = ['human', 'advice', 'refund', 'cancel', 'discount', 'promise', 'complaint'];
const checked = cfg.second_request_check !== false;
const said = normalise(westernDigits(prepared.message || ''));
const named = Array.isArray(understood.also) ? understood.also : [];
const byCode = !checked ? [] : (cfg.sim.intents || [])
  .filter(([name, words]) => NEEDS_PERSON.includes(name) && name !== intent && !named.includes(name) && words.some((w) => said.includes(normalise(w))))
  .map(([name]) => name);
const ordersNamed = !checked ? [] : Object.keys(cfg.orders || {}).filter((key) => alnum(prepared.message || '').includes(alnum(key)));
const sentences = said.split(/[؟?\n]+/).filter((part) => part.trim()).length;
const approvedTopic = intent === 'faq' && Boolean(own(cfg.knowledge, understood.topic));
const stricter = (intent === 'order_status' && (sentences <= 1 || !ordersNamed.length)) || (intent === 'faq' && !approvedTopic);
if (byCode.length === 1 && !named.length && stricter) {
  result.log.intent_by_code = { model: intent, code: byCode[0] };
  intent = byCode[0];
} else if (byCode.length && intent !== 'unknown' && !(approvedTopic && sentences <= 1)) {
  understood.also = named.concat(byCode);
  result.log.also_by_code = byCode;
}
result.intent = intent;
result.log.intent = intent;
result.state = { greeted: true };
const greeting = prepared.state.greeted ? '' : `أهلاً بك. أنا المساعد الآلي لدى ${cfg.business_name}. اكتب «موظف» في أي وقت للتحدث مع أحد الفريق.\n`;
const say = (text) => greeting + text;

if (prepared.stopped) return handover('stopped', 'stopped', 'المساعد موقوف. كل الرسائل تُحال إلى الفريق.', say('حوّلنا رسالتك إلى أحد الفريق.'));

// More than one request in one message: nothing is answered and nothing is dropped. The whole message goes to a person,
// at the strictest level among its requests. Found on 24 November 2026: the easy part was answered and the rest was lost.
const also = Array.isArray(understood.also) ? [...new Set(understood.also.filter((name) => INTENTS.includes(name) && name !== intent && name !== 'unknown'))] : [];
if (ordersNamed.length > 1 && intent !== 'unknown') {
  result.log.orders_named = ordersNamed.length;
  const strict = intent === 'refund' || intent === 'cancel' ? 'forbidden_for_agent' : intent === 'discount' || intent === 'promise' ? 'approve' : 'autonomous';
  return handover('handover_multiple_requests', strict, `في الرسالة أكثر من طلب مسجّل (${ordersNamed.join('، ')}). لم يُجب عن أي منها ولم يُنفَّذ شيء. تُقرأ كاملة.`,
    say('في رسالتك أكثر من طلب. حوّلناها كاملة إلى أحد الفريق حتى لا يفوتنا شيء منها.'), intent === 'complaint' ? 'high' : 'normal');
}
if (also.length && intent !== 'unknown') {
  const all = [intent].concat(also);
  const level = all.some((name) => name === 'refund' || name === 'cancel') ? 'forbidden_for_agent'
    : all.some((name) => name === 'discount' || name === 'promise') ? 'approve' : 'autonomous';
  result.log.also = also;
  return handover('handover_multiple_requests', level, `في الرسالة أكثر من طلب (${all.join('، ')}). لم يُجب عن أي منها ولم يُنفَّذ شيء. تُقرأ كاملة.`,
    say('في رسالتك أكثر من طلب. حوّلناها كاملة إلى أحد الفريق حتى لا يفوتنا شيء منها.'), all.includes('complaint') ? 'high' : 'normal');
}

if (intent === 'faq') {
  const entry = own(cfg.knowledge, understood.topic);
  if (!entry) return handover('handover_not_in_knowledge', 'autonomous', 'سؤال لا جواب له في المحتوى المعتمد.', say('لا أجد جواباً مؤكداً لسؤالك. حوّلته إلى أحد الفريق.'));
  result.tool_calls.push({ tool: 'knowledge_search', input: understood.topic });
  return done({ action: 'answer', level: 'autonomous', source: { topic: understood.topic, approved_on: entry.approved_on },
    reply_draft: say(`${entry.text}\nهل تحتاج شيئاً آخر؟`) });
}
if (intent === 'order_status') {
  const ref = resolveRef(understood.order_ref, Object.keys(cfg.orders), prepared.message); // tool input is normalised in code, and must have been said by the customer
  if (!ref) return done({ action: 'ask_order_ref', level: 'autonomous', reply_draft: say('فضلاً أرسل رقم الطلب لنتحقق من حالته.') });
  const order = own(cfg.orders, ref);
  if (order && order.account !== prepared.account) { // another customer's order: refused before anything is read
    return done({ action: 'refuse_other_customer', level: 'forbidden', reply_draft: say('عذراً، لا نشارك بيانات طلب مسجّل على رقم آخر.') });
  }
  result.tool_calls.push({ tool: 'order_lookup', input: ref });
  if (!order) return done({ action: 'order_not_found', level: 'autonomous', reply_draft: say(`لم نجد طلباً بالرقم ${ref}. فضلاً تأكد منه.`) });
  return done({ action: 'answer_order_status', level: 'autonomous', reply_draft: say(`حالة طلبك ${ref}: ${order.status_text}.`) });
}
if (intent === 'refund' || intent === 'cancel') {
  return handover('handover_staff_action', 'forbidden_for_agent', `طلب ${intent === 'refund' ? 'استرجاع' : 'إلغاء'}${understood.order_ref ? ` للطلب ${understood.order_ref}` : ''}. لم يُنفَّذ شيء.`,
    say('سجّلنا طلبك وحوّلناه إلى أحد الفريق، وهو من ينفّذه ويتواصل معك.'));
}
if (intent === 'discount' || intent === 'promise') {
  result.pending_approval.push({ action: intent === 'discount' ? 'offer_discount' : 'promise_date_or_exception', level: 'approve' });
  return handover('handover_needs_approval', 'approve', intent === 'discount' ? 'العميل يطلب خصماً.' : 'العميل يطلب موعداً مؤكداً أو استثناء.',
    say('هذا يحتاج موافقة أحد الفريق. حوّلنا طلبك وسيتواصل معك.'));
}
if (intent === 'complaint') return handover('handover_complaint', 'autonomous', 'شكوى. تُقرأ كما وردت.', say('نعتذر عمّا حدث. حوّلنا شكواك إلى أحد الفريق وسيتواصل معك.'), 'high');
if (intent === 'advice') return handover('refuse_advice', 'forbidden', 'سؤال طبي أو قانوني أو شرعي. لم يُجب عنه.', say('لا أستطيع تقديم مشورة طبية أو قانونية أو شرعية. حوّلتك إلى أحد الفريق.'));
if (intent === 'human') return handover('handover_requested', 'autonomous', 'العميل طلب موظفاً.', say('حوّلناك إلى أحد الفريق.'));
return handover('handover_not_understood', 'autonomous', 'رسالة لم تُفهم. تُحال كما هي.', say('لم أفهم طلبك تماماً. حوّلته إلى أحد الفريق.'));

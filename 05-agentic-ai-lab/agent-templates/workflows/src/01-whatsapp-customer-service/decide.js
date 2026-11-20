// Decide: template 1, customer service. The oversight table of the template, enforced in code.
// The model only names the intent and the topic. Every answer comes from approved content.
//#include text
//#include read_model
const cfg = $('Config').first().json;
const prepared = $('Prepare').first().json;
const understood = readModel($input.first().json);
//#include result
const INTENTS = ['faq', 'order_status', 'refund', 'cancel', 'discount', 'promise', 'complaint', 'advice', 'human', 'unknown'];
const intent = INTENTS.includes(understood.intent) ? understood.intent : 'unknown';
result.intent = intent;
result.log.intent = intent;
result.state = { greeted: true };
const greeting = prepared.state.greeted ? '' : `أهلاً بك. أنا المساعد الآلي لدى ${cfg.business_name}. اكتب «موظف» في أي وقت للتحدث مع أحد الفريق.\n`;
const say = (text) => greeting + text;

if (prepared.stopped) return handover('stopped', 'stopped', 'المساعد موقوف. كل الرسائل تُحال إلى الفريق.', say('حوّلنا رسالتك إلى أحد الفريق.'));

if (intent === 'faq') {
  const entry = own(cfg.knowledge, understood.topic);
  if (!entry) return handover('handover_not_in_knowledge', 'autonomous', 'سؤال لا جواب له في المحتوى المعتمد.', say('لا أجد جواباً مؤكداً لسؤالك. حوّلته إلى أحد الفريق.'));
  result.tool_calls.push({ tool: 'knowledge_search', input: understood.topic });
  return done({ action: 'answer', level: 'autonomous', source: { topic: understood.topic, approved_on: entry.approved_on },
    reply_draft: say(`${entry.text}\nهل تحتاج شيئاً آخر؟`) });
}
if (intent === 'order_status') {
  const ref = typeof understood.order_ref === 'string' ? understood.order_ref.trim().toUpperCase() : null; // tool input is normalised in code
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

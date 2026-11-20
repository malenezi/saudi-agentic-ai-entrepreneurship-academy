// Decide: the application around the model. The model proposes; this code decides.
// A port of Agent.handle in labs/reference/order_agent/agent.py. Every limit that matters
// is enforced here: input formats, ownership of an order, which tools exist, who approves.
//#include text
//#include read_model
const cfg = $('Config').first().json;
const prepared = $('Prepare').first().json;
const understood = readModel($input.first().json);

const INTENTS = ['order_status', 'shipping_question', 'cancel', 'refund', 'address_change', 'complaint', 'unknown'];
const STATUS_AR = { processing: 'قيد التجهيز', shipped: 'شُحن', out_for_delivery: 'خرج للتوصيل', delivered: 'تم التسليم' };
const OUT_OF_SCOPE = { cancel: 'طلب إلغاء', refund: 'طلب استرداد', address_change: 'طلب تغيير عنوان', complaint: 'شكوى' };

// The tools. There is no tool to cancel, refund or change an address.
const orderOf = (id) => (typeof id === 'string' && Object.prototype.hasOwnProperty.call(cfg.orders, id) ? cfg.orders[id] : null);
const ownerOf = (id) => (orderOf(id) ? orderOf(id).account : null);
function getOrderStatus(id) {
  if (typeof id !== 'string' || !/^\p{Nd}{5}$/u.test(id)) throw new Error('tool_input');
  const order = orderOf(id);
  return order ? { status: order.status, days_since_update: order.days_since_update } : null;
}
function getShippingPolicy(city) { // returns the FIRST entry for the city, in file order
  for (const version of cfg.policy.versions) {
    if (Object.prototype.hasOwnProperty.call(version.delivery, city)) return { duration: version.delivery[city] };
  }
  return null;
}

const result = { account: maskPhone(prepared.account), intent: 'unknown', action: null, tool_calls: [], pending_approval: [],
  escalated_to_human: false, urgent: false, reply_draft: '', summary: '' };
const done = (fields) => [{ json: Object.assign(result, fields) }];
const escalate = (action, summary) => done({ action, summary, escalated_to_human: true,
  reply_draft: 'شكراً لتواصلك. حوّلنا طلبك إلى الموظفة المختصة وستتواصل معك.' });

if (prepared.stopped) return escalate('stopped', 'الوكيل موقوف. كل الرسائل تُحال إلى الموظفة.');

let intent = INTENTS.includes(understood.intent) ? understood.intent : 'unknown'; // never trust the shape of model output
result.intent = intent;
result.urgent = Boolean(understood.urgent);

if (intent in OUT_OF_SCOPE) {
  if (intent === 'cancel' && understood.conditional) {
    result.intent = 'conditional_cancel';
    return escalate('escalate', `طلب إلغاء مشروط${result.urgent ? '، عاجل' : ''}. لم يُنفَّذ شيء.`);
  }
  return escalate('escalate', `${OUT_OF_SCOPE[intent]}. خارج نطاق الوكيل، ولم يُنفَّذ شيء.`);
}

if (intent === 'shipping_question') {
  const city = understood.city;
  result.tool_calls.push({ tool: 'get_shipping_policy', input: city ?? null });
  const entry = city ? getShippingPolicy(city) : null;
  if (entry) return done({ action: 'reply_policy', reply_draft: `مدة الشحن إلى ${city}: ${entry.duration}، بحسب سياسة الشحن المعتمدة.` });
  if (cfg.answer_only_from_policy) return escalate('escalate', 'سؤال شحن لا جواب له في السياسة المعتمدة.');
  return done({ action: 'reply_policy', reply_draft: 'مدة الشحن عادةً من 3 إلى 5 أيام عمل.' }); // the gap of Module 2.8
}

if (intent === 'order_status') {
  const id = understood.order_id;
  if (!id) return done({ action: 'ask_order_id', reply_draft: 'أهلاً بك. فضلاً زوّدنا برقم الطلب المكوّن من خمسة أرقام لنتحقق من حالته.' });
  if (cfg.ownership_check === 'app' && ![null, prepared.account].includes(ownerOf(id))) {
    return done({ action: 'refuse_ownership', reply_draft: 'عذراً، لا نستطيع مشاركة بيانات طلب مسجّل على حساب آخر. يمكن لصاحب الطلب مراسلتنا من رقمه.' });
  }
  result.tool_calls.push({ tool: 'get_order_status', input: id });
  let status;
  try {
    status = getOrderStatus(id);
  } catch (error) {
    return escalate('tool_input_error', `مدخل غير صالح للأداة: ${typeof id === 'string' ? `'${id}'` : JSON.stringify(id)}`);
  }
  if (status === null) return done({ action: 'reply_not_found', reply_draft: `لم نجد طلباً بالرقم ${id}. فضلاً تأكد من الرقم وأعد إرساله.` });
  let draft = `أهلاً بك. حالة طلبك رقم ${id}: ${STATUS_AR[status.status]}. آخر تحديث قبل ${status.days_since_update} يوم.`;
  if (status.status !== 'delivered' && status.days_since_update > cfg.policy.followup_after_days) {
    result.pending_approval.push({ tool: 'create_followup_ticket', order_id: id, level: 'B' });
    draft += ' نقترح فتح طلب متابعة مع فريق الشحن.';
  }
  return done({ action: 'reply_status', reply_draft: draft });
}

return escalate('escalate', 'رسالة لم تُفهم. تُحال كما هي.');

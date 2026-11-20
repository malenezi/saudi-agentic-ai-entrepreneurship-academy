// Decide: template 3, lead qualification. The oversight table of the template, enforced in code.
// The model names the intent and reads the answer to the question that was asked. The questions,
// the scoring rules and the approved price ranges live in Config, written by the sales lead.
//#include text
//#include read_model
const cfg = $('Config').first().json;
const prepared = $('Prepare').first().json;
const understood = readModel($input.first().json);
//#include result
const INTENTS = ['answer', 'quote_request', 'negotiate', 'stop', 'yes', 'no', 'human', 'unknown'];
const intent = INTENTS.includes(understood.intent) ? understood.intent : 'unknown';
result.intent = intent;
result.log.intent = intent;
const state = prepared.state;
const lead = Object.assign({}, state.lead && typeof state.lead === 'object' ? state.lead : {});
const greeting = state.greeted ? '' : `أهلاً بك، وشكراً لتواصلك. أنا المساعد الآلي لفريق المبيعات لدى ${cfg.business_name}. اكتب «موظف» في أي وقت للتحدث مع أحد الفريق.\n`;
const say = (text) => greeting + text;
const keep = (extra) => { result.state = Object.assign({ greeted: true, lead }, state.do_not_contact ? { do_not_contact: true } : {}, extra); };
const crm = (fields) => result.tool_calls.push({ tool: 'crm_update', input: fields }); // defined fields only
const question = (field) => cfg.questions.find((q) => q.field === field);
const nextQuestion = () => cfg.questions.find((q) => !(q.field in lead));

if (prepared.stopped) return handover('stopped', 'stopped', 'المساعد موقوف. كل الرسائل تُحال إلى الفريق.', say('حوّلنا رسالتك إلى أحد الفريق.'));
// `do_not_contact` stays in the state: no follow-up is ever sent, but a person who writes again is answered.

if (intent === 'stop') { // stop at once, and record it
  keep({ do_not_contact: true });
  crm({ do_not_contact: true });
  return done({ action: 'stop_contact', level: 'autonomous', reply_draft: say('تم. لن نتواصل معك بعد الآن. شكراً لك.') });
}
if (intent === 'negotiate') {
  keep({ asking: state.asking || null });
  return handover('handover_negotiation', 'forbidden', 'العميل يفاوض على السعر أو الشروط. لم يُعرض خصم ولا التزام.', say('الأسعار النهائية والشروط يحددها أحد الفريق. حوّلنا طلبك وسيتواصل معك.'));
}
if (intent === 'quote_request') {
  keep({ asking: state.asking || null });
  result.pending_approval.push({ action: 'send_quotation', level: 'approve' });
  return handover('quote_needs_approval', 'approve', 'العميل يطلب سعراً محدداً أو عرض سعر.',
    say(`النطاق السعري المعتمد: ${cfg.approved_price_range}. عرض السعر المحدد يرسله أحد الفريق بعد مراجعة طلبك.`));
}
if (intent === 'human') { keep({}); return handover('handover_requested', 'autonomous', 'العميل طلب موظفاً.', say('حوّلناك إلى أحد الفريق.')); }

if (state.awaiting === 'call_confirmation' && (intent === 'yes' || intent === 'no')) {
  if (intent === 'no') { keep({}); return done({ action: 'call_declined', level: 'autonomous', reply_draft: say('لا بأس. نحن هنا متى احتجت.') }); }
  keep({ booked: cfg.call_slot });
  result.tool_calls.push({ tool: 'calendar_create', input: cfg.call_slot });
  result.notify_staff.push(`عميل مؤهل حجز مكالمة: ${cfg.call_slot}.`);
  crm({ next_step: 'call_booked' });
  return done({ action: 'call_booked', level: 'autonomous', reply_draft: say(`تم حجز المكالمة: ${cfg.call_slot}. سيتصل بك أحد الفريق.`) });
}
if (state.awaiting === 'followup_consent' && (intent === 'yes' || intent === 'no')) {
  keep({ followup_consent: intent === 'yes' });
  crm({ followup_consent: intent === 'yes' });
  return done({ action: 'consent_recorded', level: 'autonomous', reply_draft: say(intent === 'yes' ? 'شكراً لك. سنتواصل معك لاحقاً.' : 'تم. لن نرسل لك رسائل متابعة.') });
}

// Record the answer to the question that was asked. A skipped question is recorded as skipped, without pressing.
if (state.asking && question(state.asking)) {
  const asked = question(state.asking);
  const value = asked.options ? (asked.options.includes(understood.value) ? understood.value : null) : String(prepared.message).trim().slice(0, 200);
  lead[asked.field] = value === null || value === '' ? 'skipped' : value;
  crm({ [asked.field]: lead[asked.field] });
}
const next = nextQuestion();
if (next) {
  keep({ asking: next.field });
  return done({ action: 'ask_question', level: 'autonomous', reply_draft: say(next.ask) });
}

// All questions asked: score by the written rules, and say why.
const reasons = Object.entries(cfg.scoring).filter(([field, values]) => values.includes(lead[field])).map(([field]) => field);
const qualified = reasons.length >= cfg.qualified_at;
crm({ score: reasons.length, score_reasons: reasons, qualified });
if (qualified) {
  keep({ awaiting: 'call_confirmation', score: reasons.length });
  return done({ action: 'offer_call', level: 'autonomous', score: reasons.length, score_reasons: reasons,
    reply_draft: say(`شكراً لإجاباتك. هل يناسبك موعد مكالمة مع أحد الفريق: ${cfg.call_slot}؟`) });
}
keep({ awaiting: 'followup_consent', score: reasons.length });
return done({ action: 'not_yet_ask_consent', level: 'autonomous', score: reasons.length, score_reasons: reasons,
  reply_draft: say(`شكراً لإجاباتك. ${cfg.useful_information} هل توافق على أن نتواصل معك لاحقاً؟`) });

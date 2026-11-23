// Decide: template 2, bookings. The oversight table of the template, enforced in code.
// The model names the intent, the service and the customer's choice. The calendar functions
// below decide what can be booked: the model never proposes a time of its own.
//#include text
//#include read_model
const cfg = $('Config').first().json;
const prepared = $('Prepare').first().json;
const understood = readModel($input.first().json);
//#include result
const INTENTS = ['book', 'confirm', 'reschedule', 'cancel', 'symptoms', 'human', 'unknown'];
const intent = INTENTS.includes(understood.intent) ? understood.intent : 'unknown';
result.intent = intent;
result.log.intent = intent;
const state = prepared.state;
const greeting = state.greeted ? '' : `أهلاً بك. أنا مساعد الحجوزات الآلي لدى ${cfg.business_name}. اكتب «موظف» في أي وقت للتحدث مع أحد الفريق.\n`;
const say = (text) => greeting + text;
result.state = { greeted: true };

// The calendar "tool". Bookings made in this workflow are kept in workflow static data.
const store = storedData(); // a discarded copy in shadow mode
store.bookings = store.bookings || {};
const now = Date.parse(cfg.now);
const bookings = () => Object.assign({}, cfg.bookings, store.bookings);
const taken = (slotId) => Object.values(bookings()).some((b) => b && b.slot === slotId);
const slotOf = (id) => cfg.slots.find((s) => s.id === id) || null;
const freeSlots = (service) => cfg.slots.filter((s) => s.service === service && Date.parse(s.start) > now && !taken(s.id)).slice(0, 3);
const label = (slot) => `${slot.day} ${slot.start.slice(0, 10)} الساعة ${slot.start.slice(11, 16)}`;
function createBooking(slotId, account) { // refuses anything outside the published slots or already taken
  const slot = slotOf(slotId);
  if (!slot || taken(slotId) || Date.parse(slot.start) <= now) return null;
  const ref = 'B-' + String(1000 + Object.keys(bookings()).length + 1);
  store.bookings[ref] = { account, slot: slotId };
  return ref;
}

if (prepared.stopped) return handover('stopped', 'stopped', 'المساعد موقوف. كل الرسائل تُحال إلى الفريق.', say('حوّلنا رسالتك إلى أحد الفريق.'));

if (intent === 'symptoms') {
  return handover('refuse_clinical', 'forbidden', 'العميل يسأل عن أعراض أو علاج. لم يُجب عنه.', say('لا أستطيع الحديث عن الأعراض أو العلاج، فالطبيب هو من يجيب. أستطيع حجز موعد لك، أو تحويلك إلى موظف.'));
}
if (intent === 'book' || intent === 'reschedule') {
  let moving = null;
  if (intent === 'reschedule') {
    const ref = typeof understood.booking_ref === 'string' ? understood.booking_ref.toUpperCase() : null;
    const booking = own(bookings(), ref);
    if (!booking || booking.account !== prepared.account) return done({ action: 'ask_booking_ref', level: 'autonomous', reply_draft: say('فضلاً أرسل رقم حجزك (مثل B-1001) من الرقم المسجّل عليه.') });
    moving = ref;
  }
  const service = moving ? slotOf(bookings()[moving].slot).service : understood.service;
  if (!service || !cfg.services.includes(service)) return done({ action: 'ask_service', level: 'autonomous', reply_draft: say(`أي خدمة تريد؟ المتاح: ${cfg.services.join('، ')}.`) });
  const slots = freeSlots(service);
  result.tool_calls.push({ tool: 'calendar_read', input: service });
  if (!slots.length) return handover('handover_no_availability', 'autonomous', `لا مواعيد متاحة لخدمة ${service}.`, say('لا أجد موعداً متاحاً الآن. حوّلت طلبك إلى أحد الفريق.'));
  result.state = { greeted: true, offered: slots.map((s) => s.id), moving };
  return done({ action: 'offer_slots', level: 'autonomous',
    reply_draft: say(`المواعيد المتاحة لخدمة ${service}:\n${slots.map((s, i) => `${i + 1}. ${label(s)}`).join('\n')}\nاكتب رقم الموعد لتأكيد الحجز.`) });
}
if (intent === 'confirm') {
  const offered = Array.isArray(state.offered) ? state.offered : [];
  const slotId = offered[Number(understood.choice) - 1];
  if (!slotId) return done({ action: 'ask_choice', level: 'autonomous', reply_draft: say('لم أعرض عليك مواعيد بعد، أو أن الرقم خارج القائمة. اكتب «حجز» واسم الخدمة.') });
  const ref = createBooking(slotId, prepared.account); // the new slot is booked first
  result.tool_calls.push({ tool: 'calendar_create', input: slotId });
  if (!ref) return done({ action: 'slot_unavailable', level: 'forbidden', reply_draft: say('هذا الموعد لم يعد متاحاً. اكتب «حجز» لأعرض عليك غيره.') });
  const slot = slotOf(slotId);
  const moving = typeof state.moving === 'string' && own(store.bookings, state.moving) && store.bookings[state.moving].account === prepared.account ? state.moving : null;
  if (moving) { // then the old one is released, and staff are told
    store.bookings[moving] = null;
    result.tool_calls.push({ tool: 'calendar_release', input: moving });
    result.notify_staff.push(`تغيير موعد: ${moving} أُلغي، والجديد ${ref}.`);
  }
  return done({ action: moving ? 'rescheduled' : 'booked', level: 'autonomous', booking: { ref, service: slot.service, start: slot.start },
    reply_draft: say(`تم الحجز. رقم الحجز ${ref}: ${slot.service}، ${label(slot)}، ${cfg.branch}.`) });
}
if (intent === 'cancel') {
  const ref = typeof understood.booking_ref === 'string' ? understood.booking_ref.toUpperCase() : null;
  const booking = own(bookings(), ref);
  if (!booking || booking.account !== prepared.account) return done({ action: 'ask_booking_ref', level: 'autonomous', reply_draft: say('فضلاً أرسل رقم حجزك (مثل B-1001) من الرقم المسجّل عليه.') });
  const hoursLeft = (Date.parse(slotOf(booking.slot).start) - now) / 3600000;
  if (hoursLeft < cfg.late_cancellation_hours) { // inside the late window: a person approves
    result.pending_approval.push({ action: 'cancel_booking', booking_ref: ref, level: 'approve' });
    return handover('cancel_needs_approval', 'approve', `إلغاء متأخر للحجز ${ref}، قبل الموعد بـ${Math.floor(hoursLeft)} ساعة.`, say('موعدك قريب، وإلغاؤه يحتاج موافقة أحد الفريق. حوّلنا طلبك وسيتواصل معك.'));
  }
  store.bookings[ref] = null;
  result.tool_calls.push({ tool: 'calendar_release', input: ref });
  result.notify_staff.push(`أُلغي الحجز ${ref} بطلب العميل.`);
  return done({ action: 'cancelled', level: 'notify', reply_draft: say(`أُلغي الحجز ${ref}.`) });
}
if (intent === 'human') return handover('handover_requested', 'autonomous', 'العميل طلب موظفاً.', say('حوّلناك إلى أحد الفريق.'));
return handover('handover_not_understood', 'autonomous', 'رسالة لم تُفهم، أو طلب خارج الحجز (رسوم، استثناء). تُحال كما هي.', say('لم أفهم طلبك تماماً. حوّلته إلى أحد الفريق.'));

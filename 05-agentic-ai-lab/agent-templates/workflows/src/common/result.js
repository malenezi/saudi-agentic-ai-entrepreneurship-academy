// One result shape for every template. `level` is the row of the oversight table that applied.
const result = { action: null, level: null, intent: 'unknown', reply_draft: '', handover: null, pending_approval: [],
  notify_staff: [], tool_calls: [], state: {}, log: { account: maskPhone(prepared.account) } };
const done = (fields) => [{ json: Object.assign(result, fields) }];
const handover = (action, level, summary, reply, urgency = 'normal') => done({ action, level,
  handover: { summary, urgency }, reply_draft: reply || 'شكراً لتواصلك. حوّلنا طلبك إلى أحد الفريق وسيتواصل معك.' });
const own = (object, key) => (typeof key === 'string' && Object.prototype.hasOwnProperty.call(object, key) ? object[key] : null);

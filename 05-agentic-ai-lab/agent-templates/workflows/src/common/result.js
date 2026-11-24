// One result shape for every template. `level` is the row of the oversight table that applied.
const result = { action: null, level: null, intent: 'unknown', reply_draft: '', handover: null, pending_approval: [],
  notify_staff: [], tool_calls: [], state: {}, log: { account: maskPhone(prepared.account) } };
// Shadow mode (Config `shadow_mode`: true): the agent runs beside the staff and nothing leaves it.
// Decide works on a copy of the workflow's stored data, so no booking or draft is kept, and `done`
// moves everything the agent would have sent, written or asked for under `shadow.would`.
// Reads still happen: the agent cannot say what it would do without looking, so the customer's
// data is processed all the same. The caller files the shadow record; `ref` ties it to the staff's record.
const shadowMode = cfg.shadow_mode === true;
const storedData = () => (shadowMode ? JSON.parse(JSON.stringify($getWorkflowStaticData('global'))) : $getWorkflowStaticData('global'));
// What happened to the model's answer on the way here is logged only when something did.
try {
  if ($('Check model output').first().json.retry === true) modelRead.retried = true;
} catch (error) { /* the simulated route: that node did not run */ }
const done = (fields) => {
  Object.assign(result, fields);
  if (modelRead.repaired || modelRead.retried || modelRead.unreadable) result.log.model = Object.assign({}, modelRead);
  if (!shadowMode) return [{ json: result }];
  const { intent, log, ...would } = result;
  return [{ json: { mode: 'shadow', action: 'shadow_observed', level: 'shadow', intent, reply_draft: '', handover: null,
    pending_approval: [], notify_staff: [], tool_calls: [], state: prepared.state, log: Object.assign(log, { shadow: true }),
    shadow: { ref: prepared.ref, would } } }];
};
const handover = (action, level, summary, reply, urgency = 'normal') => done({ action, level,
  handover: { summary, urgency }, reply_draft: reply || 'شكراً لتواصلك. حوّلنا طلبك إلى أحد الفريق وسيتواصل معك.' });
const own = (object, key) => (typeof key === 'string' && Object.prototype.hasOwnProperty.call(object, key) ? object[key] : null);

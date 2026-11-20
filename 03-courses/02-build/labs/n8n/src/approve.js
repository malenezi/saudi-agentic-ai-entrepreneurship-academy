// Level B: a named person approves, and only then does the ticket exist. One ticket per order.
// This flow starts at its own webhook: nothing from the customer's conversation reaches it.
const body = $input.first().json.body || {};
const orderId = String(body.order_id ?? '');
const approvedBy = String(body.approved_by ?? '').trim();
if (!approvedBy) return [{ json: { ok: false, error: 'create_followup_ticket needs a named approver' } }];
if (!/^\d{5}$/.test(orderId)) return [{ json: { ok: false, error: 'order_id must be five digits' } }];
const store = $getWorkflowStaticData('global');
store.tickets = store.tickets || {};
if (!store.tickets[orderId]) store.tickets[orderId] = { ticket: 'T-' + orderId, approved_by: approvedBy };
return [{ json: Object.assign({ ok: true }, store.tickets[orderId]) }];

// The accountant posts a draft. Nothing is posted without a name, and a draft is posted once.
const body = $input.first().json.body || {};
const store = $getWorkflowStaticData('global');
const draftId = String(body.draft ?? '');
const approvedBy = String(body.approved_by ?? '').trim();
const draft = store.drafts && Object.prototype.hasOwnProperty.call(store.drafts, draftId) ? store.drafts[draftId] : null;
if (!approvedBy) return [{ json: { ok: false, error: 'posting needs a named accountant' } }];
if (!draft) return [{ json: { ok: false, error: 'unknown draft' } }];
if (draft.status !== 'posted') Object.assign(draft, { status: 'posted', approved_by: approvedBy });
return [{ json: Object.assign({ ok: true, id: draftId }, draft) }];

// Decide: template 4, invoice reconciliation. The model only extracts fields. Arithmetic,
// duplicates, supplier matching and bank matching are rules, in code. Entries are drafts:
// nothing is posted until the accountant approves, and there is no tool to pay or to file.
//#include text
//#include read_model
const cfg = $('Config').first().json;
const prepared = $('Prepare').first().json;
const understood = readModel($input.first().json);
//#include result
result.intent = 'reconcile';
const store = storedData(); // a discarded copy in shadow mode
store.seen = store.seen || [];
store.drafts = store.drafts || {};

if (prepared.stopped) return handover('stopped', 'stopped', 'سير العمل موقوف. الفواتير تُراجع يدوياً.', '');

const raw = understood.fields && typeof understood.fields === 'object' ? understood.fields : {};
const REQUIRED = ['supplier', 'vat_number', 'invoice_number', 'date', 'net', 'vat', 'total', 'currency'];
const text = (v) => (typeof v === 'string' || typeof v === 'number' ? String(v).trim() : '');
const amount = (v) => { const s = westernDigits(text(v)).replace(/[,\s]/g, ''); return /^\d+(\.\d{1,2})?$/.test(s) ? Math.round(Number(s) * 100) : null; }; // halalas, exact
const fields = Object.fromEntries(REQUIRED.map((f) => [f, text(raw[f])]));
const [net, vat, total] = ['net', 'vat', 'total'].map((f) => amount(raw[f]));
const exceptions = [];
const flag = (code, reason, action) => exceptions.push({ code, reason, suggested_action: action });

const missing = REQUIRED.filter((f) => !fields[f] || (['net', 'vat', 'total'].includes(f) && amount(raw[f]) === null));
if (missing.length) flag('missing_field', `حقول ناقصة أو غير مقروءة: ${missing.join('، ')}`, 'اطلب نسخة أوضح من الفاتورة أو أدخل الحقول يدوياً.');
if (fields.date && !/^\d{4}-\d{2}-\d{2}$/.test(fields.date)) flag('date_format', 'التاريخ ليس بصيغة YYYY-MM-DD. لم يُحوَّل.', 'راجع التاريخ في المستند، وحوّل الهجري بأداة لا بالنموذج.');
if (net !== null && vat !== null && total !== null) {
  if (net + vat !== total) flag('amount_mismatch', 'الصافي مع الضريبة لا يساوي الإجمالي.', 'راجع الفاتورة مع المورّد.');
  if (Math.abs(Math.round(net * cfg.vat_rate_set_by_accountant) - vat) > cfg.tolerance_halalas) flag('vat_inconsistency', 'مبلغ الضريبة لا يطابق النسبة التي حددها المحاسب.', 'المحاسب يقرر المعاملة الضريبية.');
}
// Supplier: matched across Arabic and English spellings from the supplier list. No guess.
const supplier = cfg.suppliers.find((s) => [s.name, ...s.variants].some((n) => normalise(n) === normalise(fields.supplier)));
if (fields.supplier && !supplier) flag('unknown_supplier', 'المورّد ليس في قائمة المورّدين بأي من تهجئاته.', 'أضف التهجئة إلى القائمة بعد التحقق، أو راجع الفاتورة.');
if (supplier && fields.vat_number && supplier.vat_number !== fields.vat_number) flag('vat_number_mismatch', 'الرقم الضريبي لا يطابق المسجّل للمورّد.', 'تحقق من المورّد قبل أي قيد.');
const key = `${supplier ? supplier.id : normalise(fields.supplier)}|${fields.invoice_number}`;
const duplicate = Boolean(fields.invoice_number) && (cfg.posted_invoices.includes(key) || store.seen.includes(key));
if (duplicate) flag('duplicate', 'فاتورة بالرقم نفسه للمورّد نفسه سبق تسجيلها.', 'لا تُقيَّد مرتين.');
// Bank line: same amount, and the invoice number in the reference.
const line = total === null ? null : cfg.bank_lines.find((b) => Math.round(b.amount * 100) === total && fields.invoice_number && b.reference.includes(fields.invoice_number));
if (!line && total !== null && !duplicate) flag('no_bank_match', 'لا حركة بنكية بالمبلغ نفسه ورقم الفاتورة.', 'قد تكون غير مدفوعة بعد، أو دُفعت بمرجع آخر.');

const report = { fields, matched_bank_line: line ? line.id : null, exceptions };
if (exceptions.length) {
  return done({ action: 'exception_report', level: 'autonomous', report, handover: { summary: `فاتورة فيها ${exceptions.length} استثناء. للمراجعة.`, urgency: 'normal' } });
}
store.seen.push(key);
const draftId = 'D-' + String(Object.keys(store.drafts).length + 1).padStart(3, '0');
store.drafts[draftId] = { key, supplier: supplier.id, invoice_number: fields.invoice_number, total: total / 100, bank_line: line.id, status: 'draft' };
result.tool_calls.push({ tool: 'ledger_write_draft', input: draftId });
result.pending_approval.push({ action: 'post_entry', draft: draftId, level: 'approve', approver: 'accountant' });
return done({ action: 'draft_entry', level: 'autonomous', report, draft: Object.assign({ id: draftId }, store.drafts[draftId]) });

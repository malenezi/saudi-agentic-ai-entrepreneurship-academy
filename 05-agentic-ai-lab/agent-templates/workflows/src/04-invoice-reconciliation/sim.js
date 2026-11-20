// Simulated extraction: NOT a language model. It reads labelled lines ("رقم الفاتورة: ...")
// from the invoice text, so the workflow runs with no key and no cost. A real model reads
// unlabelled and scanned invoices; the checks in Decide are the same either way.
//#include text
const text = westernDigits($input.first().json.message);
const LABELS = {
  supplier: ['المورد', 'المورّد', 'supplier'], vat_number: ['الرقم الضريبي', 'vat number'], invoice_number: ['رقم الفاتورة', 'invoice number', 'invoice no'],
  date: ['التاريخ', 'date'], net: ['المبلغ قبل الضريبة', 'net'], vat: ['مبلغ الضريبة', 'vat amount'], total: ['الإجمالي', 'الاجمالي', 'total'], currency: ['العملة', 'currency'],
};
const fields = {};
for (const line of text.split('\n')) {
  const at = line.indexOf(':');
  if (at < 0) continue;
  const label = normalise(line.slice(0, at)).trim();
  const field = Object.keys(LABELS).find((f) => LABELS[f].some((l) => normalise(l) === label));
  if (field && !(field in fields)) fields[field] = line.slice(at + 1).trim();
}
return [{ json: { understanding: { fields } } }];

// Arabic text helpers, the same rules as labs/reference/order_agent/text.py.
function normalise(text) {
  return String(text).replace(/[ً-ْـ]/g, '').replace(/[أإآ]/g, 'ا').replace(/ى/g, 'ي').toLowerCase();
}
function westernDigits(text) {
  const map = '٠١٢٣٤٥٦٧٨٩۰۱۲۳۴۵۶۷۸۹';
  return String(text).replace(/[٠-٩۰-۹]/g, (d) => String(map.indexOf(d) % 10));
}
function maskPhone(phone) {
  phone = String(phone);
  return '*'.repeat(Math.max(phone.length - 2, 0)) + phone.slice(-2);
}
// Direction marks and zero-width characters that messaging apps put inside numbers and references.
function stripHidden(text) {
  return String(text).replace(/[\u200B\u200E\u200F\u202A-\u202E\u2066-\u2069\u061C\uFEFF]/g, '');
}
// 9665XXXXXXXX, +9665XXXXXXXX, 009665XXXXXXXX and 5XXXXXXXX are the local 05XXXXXXXX. Anything else is left as sent.
function normaliseAccount(account) {
  const digits = westernDigits(String(account)).replace(/[^\d]/g, '');
  const mobile = digits.match(/^(?:00966|966|0)?(5\d{8})$/);
  return mobile ? '0' + mobile[1] : String(account);
}
function alnum(text) {
  return westernDigits(stripHidden(String(text))).toUpperCase().replace(/[^A-Z0-9]/g, '');
}
// A reference as a customer writes it ("s 2001", "#S2001", "2001") resolved to a stored key when exactly one key fits.
// A reference whose digits are not in the customer's message was not said by the customer: it is dropped.
function resolveRef(raw, keys, message) {
  if (typeof raw !== 'string' || !raw.trim()) return null;
  const wanted = alnum(raw);
  const digits = wanted.replace(/\D/g, '');
  if (!digits || !alnum(message).includes(digits)) return null;
  const exact = keys.filter((key) => alnum(key) === wanted);
  if (exact.length === 1) return exact[0];
  if (/^\d+$/.test(wanted)) {
    const byDigits = keys.filter((key) => alnum(key).replace(/\D/g, '') === wanted);
    if (byDigits.length === 1) return byDigits[0];
  }
  return raw.trim().toUpperCase();
}

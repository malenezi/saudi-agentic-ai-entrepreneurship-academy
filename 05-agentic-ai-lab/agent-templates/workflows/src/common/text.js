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

// The model's answer is untrusted: take one JSON object out of it, or nothing.
function readModel(item) {
  if (item && item.understanding && typeof item.understanding === 'object') return item.understanding;
  try {
    const content = item.choices[0].message.content;
    const parsed = JSON.parse(content.slice(content.indexOf('{'), content.lastIndexOf('}') + 1));
    return parsed && typeof parsed === 'object' && !Array.isArray(parsed) ? parsed : {};
  } catch (error) {
    return { error: 'model_output_unreadable' }; // a model failure must never act on its own
  }
}

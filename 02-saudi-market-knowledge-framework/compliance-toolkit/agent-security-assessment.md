# تقييم أمن الوكيل · Agent security assessment

Complete before selling to larger organisations and after any change to tools or permissions. Answer نعم / لا (Yes / No). Every "No" is an action.

**المشروع · Venture:** ____________  **التاريخ · Date:** ____________  **المقيّم · Assessor:** ____________

## 1. الهوية والوصول · Identity and access

| # | البند · Item | نعم/لا | ملاحظة |
|---|---|---|---|
| 1.1 | تحقق متعدد العوامل على كل حسابات الإدارة · MFA on all admin accounts | | |
| 1.2 | مفاتيح API محدودة الصلاحية ولكل بيئة مفتاحها · Scoped API keys, separate per environment | | |
| 1.3 | المفاتيح في مدير أسرار، وليست في التعليمات أو المستودع · Keys in a secrets manager, never in prompts or the repo | | |
| 1.4 | تدوير المفاتيح دورياً وعند مغادرة أي عضو · Keys rotated regularly and on team changes | | |

## 2. صلاحيات الوكيل · Agent permissions

| # | البند · Item | نعم/لا | ملاحظة |
|---|---|---|---|
| 2.1 | لكل أداة أقل صلاحية تكفي المهمة · Each tool has the least privilege the task needs | | |
| 2.2 | قائمة سماح للأدوات والمستلمين تُفرض خارج النموذج · Tool and recipient allow-lists enforced outside the model | | |
| 2.3 | بوابات موافقة للإجراءات المالية وغير القابلة للتراجع · Approval gates for financial and irreversible actions | | |
| 2.4 | حدود للخطوات والإنفاق ومعدل الإجراءات · Caps on steps, spend and action rate | | |
| 2.5 | مفتاح إيقاف مجرَّب · Tested kill switch | | |

## 3. المدخلات غير الموثوقة · Untrusted input

| # | البند · Item | نعم/لا | ملاحظة |
|---|---|---|---|
| 3.1 | محتوى الرسائل والمستندات والصفحات يُعامَل كبيانات لا كتعليمات · Messages, documents and web pages are treated as data, not instructions | | |
| 3.2 | اختبرنا الوكيل بمجموعة حقن تعليمات بالعربية والإنجليزية · Tested with an Arabic and English prompt-injection set | | |
| 3.3 | المخرجات تُفحص قبل تنفيذ الأدوات (صيغة، قيم، مستلم) · Outputs are validated before tool execution (format, values, recipient) | | |
| 3.4 | ما يُكتب في الذاكرة طويلة المدى يُتحقق منه · Writes to long-term memory are validated | | |

## 4. البيانات · Data

| # | البند · Item | نعم/لا | ملاحظة |
|---|---|---|---|
| 4.1 | تشفير أثناء النقل والتخزين · Encryption in transit and at rest | | |
| 4.2 | عزل بيانات كل عميل تجاري · Isolation between business customers | | |
| 4.3 | السجلات لا تحوي بيانات شخصية غير لازمة · Logs hold no unnecessary personal data | | |
| 4.4 | نسخ احتياطية واستعادة مجرَّبة · Backups with a tested restore | | |

## 5. التكاملات · Integrations

| # | البند · Item | نعم/لا | ملاحظة |
|---|---|---|---|
| 5.1 | جرد بكل تكامل وما يستطيع الوصول إليه · Inventory of every integration and what it can access | | |
| 5.2 | التكاملات من مصادر موثوقة وبإصدارات مثبتة · Integrations from trusted sources with pinned versions | | |
| 5.3 | كل مزوّد له تقييم محدَّث · Each provider has a current assessment | | |

## 6. المراقبة والاستجابة · Monitoring and response

| # | البند · Item | نعم/لا | ملاحظة |
|---|---|---|---|
| 6.1 | سجل إجراءات: ماذا، متى، لماذا، ومن وافق · Action log: what, when, why, who approved | | |
| 6.2 | تنبيهات على الأنماط غير المعتادة والتكلفة · Alerts on unusual patterns and cost | | |
| 6.3 | خطة استجابة مكتوبة بأدوار مسمّاة · Written response plan with named roles | | |

## خطة الاستجابة للحوادث (صفحة واحدة) · One-page incident response plan

| الخطوة · Step | ماذا نفعل · What we do | المسؤول · Who |
|---|---|---|
| 1. الإيقاف · Stop | تفعيل مفتاح الإيقاف والتحويل إلى موظف · Trigger the kill switch; route to a person | |
| 2. الاحتواء · Contain | سحب المفاتيح المتأثرة وعزل المكوّن · Revoke affected keys; isolate the component | |
| 3. التقييم · Assess | ما البيانات والعملاء المتأثرون؟ · Which data and customers are affected? | |
| 4. الإبلاغ · Notify | العملاء، والجهة المختصة إن كانت بيانات شخصية، وفق المدد النظامية · Customers, and the authority where personal data is involved, within required timeframes | |
| 5. الإصلاح · Fix | معالجة السبب وإضافة حالة اختبار · Fix the cause; add a test case | |
| 6. التوثيق · Record | تسجيل الحادثة في سجل المخاطر · Record in the risk register | |

**جهات الاتصال · Contacts:** المالك · Owner ______  التقني · Technical ______  القانوني · Legal ______

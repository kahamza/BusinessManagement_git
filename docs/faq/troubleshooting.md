# الأسئلة الشائعة - دليل استكشاف الأخطاء | FAQ - Troubleshooting Guide

يوفر هذا المستند حلول للمشكلات الشائعة التي قد تواجهها أثناء استخدام تطبيق إدارة المحل التجاري.

This document provides solutions to common problems encountered while using the Business Management App.

## 🚨 مشاكل الاتصال | Connection Issues

### المشكلة: التطبيق لا يتزامن مع السحابة | Problem: App won't sync with cloud
**الأعراض | Symptoms:**
- أيقونة المزامنة تظهر حالة خطأ | Sync icon shows error state
- البيانات لا تتحدث عبر الأجهزة | Data not updating across devices
- رسائل "فشلت المزامنة" | "Sync failed" messages

**الحلول | Solutions:**
1. **التحقق من اتصال الإنترنت** | **Check internet connection**
   - التأكد من أن Wi-Fi أو البيانات المحمولة نشطة | Ensure Wi-Fi or mobile data is active
   - محاولة فتح صفحة ويب للتحقق من الاتصال | Try opening a web page to verify connectivity

2. **التحقق من حالة خدمة السحابة** | **Verify cloud service status**
   - التحقق مما إذا كانت خدمات Firebase تعمل | Check if Firebase services are operational
   - مراجعة حالة سير عمل n8n إذا كنت تستخدم تكامل مخصص | Review n8n workflow status if using custom integration

3. **إعادة تشغيل خدمة المزامنة** | **Restart sync service**
   - الذهاب إلى الإعدادات > المزامنة > فرض المزامنة | Go to Settings > Sync > Force Sync
   - إعادة تشغيل التطبيق بالكامل | Restart the app completely

4. **التحقق من الأذونات** | **Check permissions**
   - التأكد من تمكين أذونات المزامنة في الخلفية | Ensure background sync permissions are enabled
   - التحقق من إعدادات تحسين البطارية | Check battery optimization settings

### المشكلة: لا يمكن الاتصال بالطابعة | Problem: Can't connect to printer
**الأعراض | Symptoms:**
- فشل مهام الطباعة | Print jobs fail
- الطابعة غير موجودة في قائمة الأجهزة | Printer not found in device list
- أخطاء "الطابعة غير متاحة" | "Printer unavailable" errors

**الحلول | Solutions:**
1. **التحقق من اتصال الطابعة** | **Check printer connection**
   - التأكد من أن الطابعة مشغلة ومتصلة بنفس الشبكة | Ensure printer is powered on and connected to same network
   - التحقق من عنوان IP الطابعة ومنفذ الإعدادات | Check printer IP address and port settings

2. **تحديث تعريفات الطابعة** | **Update printer drivers**
   - تثبيت أحدث تعريفات الشركة المصنعة للطابعة | Install latest printer manufacturer drivers
   - تحديث Android System WebView | Update Android System WebView

3. **إعادة تعيين إعدادات الطابعة** | **Reset printer settings**
   - إزالة وإعادة إضافة الطابعة في إعدادات التطبيق | Remove and re-add printer in app settings
   - مسح ذاكرة التخزين المؤقت للطابعة في إعدادات الجهاز | Clear printer cache in device settings

## 📊 مشاكل البيانات | Data Issues

### المشكلة: أرقام المخزون لا تتطابق | Problem: Inventory numbers don't match
**الأعراض | Symptoms:**
- مستويات المخزون غير متسقة | Stock levels inconsistent
- قيم مخزون سلبية | Negative inventory values
- المبيعات لا تخصم من المخزون | Sales not deducting from stock

**الحلول | Solutions:**
1. **تشغيل تدقيق المخزون** | **Run inventory audit**
   - استخدام ميزة تدقيق المخزون | Use the inventory audit feature
   - العد اليدوي والمصالحة | Manually count and reconcile stock

2. **التحقق من تلف البيانات** | **Check for data corruption**
   - الاستعادة من نسخة احتياطية حديثة | Restore from recent backup
   - تشغيل فحص سلامة قاعدة البيانات | Run database integrity check

3. **مراجعة سجلات المعاملات** | **Review transaction logs**
   - التحقق من سجلات المبيعات والمشتريات | Check sales and purchase records
   - البحث عن المعاملات غير المعالجة | Look for unprocessed transactions

### المشكلة: التقارير تظهر بيانات غير صحيحة | Problem: Reports showing incorrect data
**الأعراض | Symptoms:**
- مجموعات المبيعات لا تتطابق | Sales totals don't add up
- حسابات ديون العملاء خاطئة | Customer debt calculations wrong
- هوامش الربح غير متسقة | Profit margins inconsistent

**الحلول | Solutions:**
1. **التحقق من نطاقات التواريخ** | **Verify date ranges**
   - التأكد من أن فلاتر التقرير مضبوطة بشكل صحيح | Ensure report filters are set correctly
   - التحقق من إعدادات المنطقة الزمنية | Check timezone settings

2. **التحقق من اتساق البيانات** | **Check data consistency**
   - تشغيل فحص اتساق قاعدة البيانات | Run database consistency check
   - التحقق من وجود جميع السجلات ذات الصلة | Verify all related records exist

3. **مراجعة منطق الحساب** | **Review calculation logic**
   - التحقق من حسابات الضرائب والخصومات | Check tax and discount calculations
   - التحقق من معدلات تحويل العملة | Verify currency conversion rates

## 🔐 مشاكل المصادقة والأمان | Authentication & Security Issues

### المشكلة: التعرف على الوجه لا يعمل | Problem: Face recognition not working
**الأعراض | Symptoms:**
- الكاميرا تفشل في الفتح | Camera fails to open
- الوجه غير معترف به بشكل متسق | Face not recognized consistently
- أخطاء "فشلت المصادقة" | "Authentication failed" errors

**الحلول | Solutions:**
1. **التحقق من أذونات الكاميرا** | **Check camera permissions**
   - التأكد من منح صلاحية الوصول إلى الكاميرا | Ensure camera access is granted
   - التحقق مما إذا كان تطبيق آخر يستخدم الكاميرا | Check if another app is using camera

2. **تحسين ظروف الإضاءة** | **Improve lighting conditions**
   - التأكد من الإضاءة الجيدة لالتقاط الوجه | Ensure good lighting for face capture
   - تجنب ضوء الشمس المباشر أو الظلال القاسية | Avoid direct sunlight or harsh shadows

3. **إعادة تدريب نموذج الوجه** | **Retrain face model**
   - الذهاب إلى الإعدادات > الأمان > التعرف على الوجه | Go to Settings > Security > Face Recognition
   - إعادة التقاط الوجه في ظروف جيدة | Recapture face in good conditions

4. **تحديث ML Kit** | **Update ML Kit**
   - التأكد من أن أحدث إصدار من ML Kit مثبت | Ensure latest version of ML Kit is installed
   - مسح ذاكرة التخزين المؤقت للتطبيق والمحاولة مرة أخرى | Clear app cache and retry

### المشكلة: صلاحيات الأدوار لا تعمل | Problem: Role permissions not working
**الأعراض | Symptoms:**
- يمكن للمستخدمين الوصول إلى ميزات غير مصرح بها | Users can access unauthorized features
- رفض الإذن للإجراءات الصالحة | Permission denied for valid actions
- تغييرات الأدوار لا تأخذ تأثير | Role changes not taking effect

**الحلول | Solutions:**
1. **تحديث جلسة المستخدم** | **Refresh user session**
   - تسجيل الخروج وتسجيل الدخول مرة أخرى | Log out and log back in
   - فرض إعادة تشغيل التطبيق | Force restart the app

2. **التحقق من تعيين الدور** | **Check role assignment**
   - التحقق من دور المستخدم في لوحة الإدارة | Verify user role in admin panel
   - التأكد من تعيينات الفروع صحيحة | Ensure branch assignments are correct

3. **مسح ذاكرة التخزين المؤقت للأذونات** | **Clear permission cache**
   - الذهاب إلى الإعدادات > الأمان > مسح ذاكرة التخزين المؤقت للأذونات | Go to Settings > Security > Clear Permissions Cache
   - إعادة تشغيل التطبيق بعد المسح | Restart app after clearing

## 📱 مشاكل الأداء | Performance Issues

### المشكلة: التطبيق يعمل ببطء | Problem: App running slowly
**الأعراض | Symptoms:**
- انتقالات الشاشة البطيئة | Slow screen transitions
- تأخير في الاستجابة للنقرات | Delayed response to taps
- استخدام عالي للبطارية | High battery usage

**الحلول | Solutions:**
1. **مسح ذاكرة التخزين المؤقت للتطبيق** | **Clear app cache**
   - الذهاب إلى الإعدادات > التخزين > مسح ذاكرة التخزين المؤقت | Go to Settings > Storage > Clear Cache
   - إعادة تشغيل التطبيق | Restart the app

2. **تحرير مساحة تخزين الجهاز** | **Free up device storage**
   - إزالة التطبيقات غير المستخدمة | Remove unused apps
   - مسح الملفات المؤقتة | Clear temporary files

3. **تحديث نظام أندرويد** | **Update Android system**
   - تثبيت أحدث تحديثات أندرويد | Install latest Android updates
   - تحديث خدمات Google Play | Update Google Play Services

4. **التحقق من تسرب الذاكرة** | **Check for memory leaks**
   - مراقبة استخدام الذاكرة في خيارات المطور | Monitor memory usage in developer options
   - إعادة تشغيل التطبيق دوريًا إذا لزم الأمر | Restart app periodically if needed

### المشكلة: ماسح الباركود لا يستجيب | Problem: Barcode scanner not responding
**الأعراض | Symptoms:**
- الماسح لا يفعل | Scanner doesn't activate
- عدم استجابة لمسح الباركود | No response to barcode scans
- رسالة "الماسح غير متاح" | "Scanner unavailable" message

**الحلول | Solutions:**
1. **التحقق من أذونات الكاميرا** | **Check camera permissions**
   - التأكد من منح صلاحية الوصول إلى الكاميرا للماسح | Ensure camera access for scanner
   - منح الإذن إذا تم رفضه | Grant permission if denied

2. **تنظيف عدسة الماسح** | **Clean scanner lens**
   - مسح عدسة الكاميرا نظيفة | Wipe camera lens clean
   - التأكد من عدم وجود عوائق | Ensure no obstructions

3. **ضبط إعدادات المسح** | **Adjust scanning settings**
   - الذهاب إلى الإعدادات > الماسح > إعادة تعيين إلى الافتراضيات | Go to Settings > Scanner > Reset to defaults
   - تجربة أوضاع مسح مختلفة | Try different scan modes

## 🔄 مشاكل النسخ الاحتياطي والاستعادة | Backup & Restore Issues

### المشكلة: فشل النسخ الاحتياطي | Problem: Backup fails
**الأعراض | Symptoms:**
- عملية النسخ الاحتياطي تتوقف بشكل غير متوقع | Backup process stops unexpectedly
- رسالة خطأ "فشل النسخ الاحتياطي" | "Backup failed" error message
- تحذيرات نقص مساحة التخزين | Insufficient storage warnings

**الحلول | Solutions:**
1. **تحرير مساحة التخزين** | **Free up storage space**
   - حذف النسخ الاحتياطية القديمة | Delete old backups
   - مسح الملفات المؤقتة | Clear temporary files

2. **التحقق من إعدادات النسخ الاحتياطي** | **Check backup settings**
   - التحقق من أن موقع النسخ الاحتياطي متاح | Verify backup location is accessible
   - التأكد من وجود أذونات كافية | Ensure sufficient permissions

3. **تجربة النسخ الاحتياطي الانتقائي** | **Try selective backup**
   - نسخ مجموعات بيانات أصغر أولاً | Backup smaller data sets first
   - زيادة حجم النسخ الاحتياطي تدريجيًا | Gradually increase backup size

### المشكلة: فشل الاستعادة | Problem: Restore fails
**الأعراض | Symptoms:**
- عملية الاستعادة تتعطل | Restore process interrupted
- رسالة "فشل الاستعادة" | "Restore failed" message
- تلف البيانات بعد الاستعادة | Data corruption after restore

**الحلول | Solutions:**
1. **التحقق من سلامة ملف النسخ الاحتياطي** | **Verify backup file integrity**
   - التحقق من حجم الملف وتاريخ الإنشاء | Check file size and creation date
   - التأكد من أن النسخ الاحتياطي لم يتلف أثناء الإنشاء | Ensure backup wasn't corrupted during creation

2. **استخدام طريقة استعادة بديلة** | **Use alternative restore method**
   - تجربة الاستعادة إلى موقع مختلف أولاً | Try restoring to different location first
   - استخدام استعادة السحابة إذا كانت متاحة | Use cloud restore if available

3. **الاتصال بالدعم** | **Contact support**
   - توفير ملف النسخ الاحتياطي وسجلات الأخطاء | Provide backup file and error logs
   - الحصول على المساعدة من فريق التطوير | Get assistance from development team

## 📞 الحصول على المساعدة | Getting Help

إذا لم تحل هذه الحلول مشكلتك:

If these solutions don't resolve your issue:

1. **التحقق من التوثيق** | **Check the documentation**
   - مراجعة توثيق الميزة ذات الصلة | Review relevant feature documentation
   - البحث عن مشكلات مشابهة في الأسئلة الشائعة | Look for similar issues in FAQ

2. **الاتصال بالدعم** | **Contact support**
   - فتح مشكلة على GitHub | Open an issue on GitHub
   - توفير معلومات خطأ مفصلة | Provide detailed error information
   - تضمين لقطات الشاشة إن أمكن | Include screenshots if applicable

3. **دعم المجتمع** | **Community support**
   - طرح الأسئلة في منتدى المجتمع | Ask questions in the community forum
   - البحث في المناقشات الموجودة | Search existing discussions
   - مشاركة حلك مع الآخرين | Share your solution with others

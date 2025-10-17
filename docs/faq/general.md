# الأسئلة الشائعة - الأسئلة العامة | FAQ - General Questions

يجيب هذا المستند على الأسئلة الشائعة حول تطبيق إدارة المحل التجاري.

This document answers frequently asked questions about the Business Management App.

## 🤔 الأسئلة العامة | General Questions

### ما هو تطبيق إدارة المحل التجاري؟ | What is the Business Management App?
تطبيق إدارة المحل التجاري هو تطبيق أندرويد شامل مصمم للشركات التجارية. يوفر أدوات لنقطة البيع وإدارة المخزون وإدارة علاقات العملاء وإدارة الموظفين والتتبع المالي.

The Business Management App is a comprehensive Android application designed for retail businesses. It provides tools for point of sale, inventory management, customer relationship management, employee management, and financial tracking.

### ما هي المنصات التي يدعمها؟ | What platforms does it support?
- أندرويد 8.0 وما فوق (مستوى API 26+) | Android 8.0 and above (API level 26+)
- مُحسّن للهواتف والأجهزة اللوحية | Optimized for both phones and tablets
- يدعم اللغتين العربية والإنجليزية | Supports Arabic and English languages
- معمارية تعمل دون اتصال بالإنترنت مع مزامنة سحابية | Offline-first architecture with cloud sync

### ما هي الميزات الرئيسية؟ | What are the main features?
- نقطة البيع (POS) مع ماسح الباركود | Point of Sale (POS) with barcode scanning
- إدارة المخزون مع تنبيهات المخزون المنخفض | Inventory management with low stock alerts
- إدارة العملاء والموردين | Customer and supplier management
- إدارة الموظفين مع تتبع الحضور | Employee management with attendance tracking
- دعم متعدد الفروع | Multi-branch support
- التقارير المالية والتحليلات | Financial reporting and analytics
- برامج الولاء والخصومات | Loyalty programs and discounts
- تكامل الطلبات أونلاين (بوت تليجرام) | Online order integration (Telegram bot)
- المصادقة بالتعرف على الوجه | Face recognition authentication
- النسخ الاحتياطي والاستعادة | Data backup and restore

### هل التطبيق مجاني للاستخدام؟ | Is the app free to use?
التطبيق مفتوح المصدر ومجاني للتنزيل. ومع ذلك، قد تتطلب بعض الميزات المتقدمة اشتراكات خدمات سحابية للمزامنة متعددة الفروع والطلبات أونلاين.

The app is open source and free to download. However, some advanced features may require cloud service subscriptions for multi-branch synchronization and online ordering.

### هل يمكنني تخصيص التطبيق لأعمالي؟ | Can I customize the app for my business?
نعم، التطبيق قابل للتخصيص العالي. يمكنك:

Yes, the app is highly customizable. You can:
- إضافة فئات منتجات مخصصة | Add custom product categories
- تكوين أدوار وصلاحيات المستخدمين | Configure user roles and permissions
- تخصيص تنسيقات الإيصالات | Customize receipt formats
- إعداد إعدادات خاصة بالفرع | Set up branch-specific settings
- التكامل مع الخدمات الخارجية | Integrate with external services

## 🛠️ الأسئلة التقنية | Technical Questions

### ما هي مجموعة التقنيات المستخدمة؟ | What technology stack is used?
- **اللغة**: كوتلين | **Language**: Kotlin
- **إطار عمل واجهة المستخدم**: جيت باك كومبوز | **UI Framework**: Jetpack Compose
- **المعمارية**: المعمارية النظيفة + MVVM | **Architecture**: Clean Architecture + MVVM
- **قاعدة البيانات**: روم داتابيز | **Database**: Room Database
- **حقن التبعيات**: هيلت | **Dependency Injection**: Hilt
- **المهام الخلفية**: وورك مانجر | **Background Tasks**: WorkManager
- **التكامل السحابي**: فايربيز + n8n | **Cloud Integration**: Firebase + n8n

### كيف تعمل الوظيفة دون اتصال بالإنترنت؟ | How does offline functionality work?
يستخدم التطبيق معمارية تعمل أولاً دون اتصال بالإنترنت:

The app uses an offline-first architecture:
- يتم تخزين جميع البيانات محليًا في قاعدة بيانات روم | All data is stored locally in Room database
- يتم وضع التغييرات في قائمة الانتظار عندما يكون غير متصل | Changes are queued when offline
- المزامنة التلقائية عند استعادة الاتصال | Automatic synchronization when connection is restored
- حل التعارضات لضمان اتساق البيانات | Conflict resolution for data consistency

### ما مدى أمان بياناتي؟ | How secure is my data?
تشمل ميزات الأمان:

Security features include:
- التشفير الشامل لبيانات الحساسة | End-to-end data encryption
- التحكم في الوصول بناءً على الأدوار (RBAC) | Role-based access control (RBAC)
- إدارة الجلسات الآمنة | Secure session management
- دعم المصادقة البيومترية | Biometric authentication support
- تسجيل التدقيق للامتثال | Audit logging for compliance

## 📱 أسئلة الاستخدام | Usage Questions

### كيف أقوم بإعداد فروع متعددة؟ | How do I set up multiple branches?
1. إنشاء سجلات الفروع في النظام | Create branch records in the system
2. تعيين المستخدمين لفروع محددة | Assign users to specific branches
3. تكوين الإعدادات الخاصة بالفرع | Configure branch-specific settings
4. إعداد نقل المخزون بين الفروع | Set up inter-branch inventory transfer

### هل يمكنني التكامل مع الأنظمة الخارجية؟ | Can I integrate with external systems?
نعم، يدعم التطبيق:

Yes, the app supports:
- بوت تليجرام للطلبات أونلاين | Telegram bot for online orders
- أتمتة سير العمل n8n | n8n workflow automation
- تكاملات الويب هوك المخصصة | Custom webhook integrations
- التصدير إلى برامج المحاسبة | Export to accounting software

### كيف أقوم بنسخ بياناتي احتياطيًا؟ | How do I backup my data?
- النسخ الاحتياطي السحابي التلقائي (إذا تم تمكينه) | Automatic cloud backups (if enabled)
- التصدير اليدوي إلى التخزين الخارجي | Manual export to external storage
- ملفات نسخ احتياطي قاعدة البيانات | Database backup files
- الاستعادة من النسخ الاحتياطية السابقة | Restore from previous backups

## 🔧 استكشاف الأخطاء | Troubleshooting

### لماذا لا أستطيع تسجيل الدخول؟ | Why can't I login?
- تحقق من اتصال الإنترنت | Check your internet connection
- تحقق من اسم المستخدم وكلمة المرور | Verify username and password
- تأكد من أن حسابك نشط | Ensure your account is active
- جرب إعادة تعيين كلمة المرور | Try resetting your password

### لماذا لا تعمل المزامنة؟ | Why is sync not working?
- تحقق من الاتصال بالإنترنت | Check internet connectivity
- تحقق من بيانات اعتماد الخدمة السحابية | Verify cloud service credentials
- فرض المزامنة اليدوية | Force manual sync
- تحقق من حالة قائمة انتظار المزامنة | Check sync queue status

### كيف أحل تعارضات البيانات؟ | How do I resolve data conflicts?
- يحل التطبيق معظم التعارضات تلقائيًا | The app automatically resolves most conflicts
- حل التعارضات يدويًا متاح في الإعدادات | Manual conflict resolution available in settings
- اتصل بالدعم للمشكلات المعقدة | Contact support for complex issues

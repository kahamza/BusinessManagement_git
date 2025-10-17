# 🏪 Business Management App

<div dir="rtl">

# 🏪 تطبيق إدارة المحل التجاري | Business Management App

نظام متكامل لإدارة المحلات التجارية بمختلف أنواعها بطريقة **احترافية ومرنة**.  
يدعم إدارة **المبيعات، المشتريات، المنتجات، العملاء، الموردين، المصاريف، الفروع، والموظفين**  
مع مزامنة سحابية آمنة ونظام صلاحيات متقدم.

</div>

## 🌟 Features | المميزات

### 💼 Core Business Features | الميزات الأساسية
- **نقطة البيع (POS)** مع دعم الباركود وطباعة الفواتير
  - **Point of Sale (POS)** with barcode support and receipt printing
- **إدارة المخزون** مع تنبيهات المخزون وإنشاء الباركود
  - **Inventory Management** with stock alerts and barcode generation
- **إدارة العملاء والموردين** مع تتبع الديون
  - **Customer & Supplier Management** with debt tracking
- **دعم الفروع المتعددة** مع التحكم في الصلاحيات
  - **Multi-branch** support with role-based access control
- **تتبع المصروفات** مع التصنيف وإعداد التقارير
  - **Expense Tracking** with categorization and reporting
- **إدارة الموظفين** مع تتبع الحضور والأداء
  - **Employee Management** with attendance and performance tracking

### 🛠 Technical Features | الميزات التقنية
- **هندسة معمارية عصرية**: Clean Architecture + MVVM
  - **Modern Architecture**: Clean Architecture + MVVM
- **العمل دون اتصال**: يعمل بدون اتصال بالإنترنت
  - **Offline-First**: Works without internet connection
- **مزامنة البيانات**: مزامنة سحابية آمنة
  - **Data Sync**: Secure cloud synchronization
- **الأمان**: تحكم في الصلاحيات، تشفير البيانات
  - **Security**: Role-based access control, data encryption
- **متعدد اللغات**: يدعم العربية والإنجليزية بشكل كامل
  - **Multi-language**: Full Arabic and English support

## 🏗 Project Structure | هيكل المشروع

```
com.businessmanagement/
│
├── core/                          # Core components
│   ├── util/                      # Utility classes
│   ├── network/                   # Network communication
│   ├── database/                  # Database setup
│   ├── di/                        # Dependency injection
│   ├── workers/                   # Background tasks
│   └── session/                   # Session management
│
├── features/                      # Feature modules
│   ├── pos/                       # Point of Sale
│   ├── customers/                 # Customer management
│   ├── suppliers/                 # Supplier management
│   ├── inventory/                 # Inventory management
│   ├── employees/                 # Employee management
│   ├── expenses/                  # Expense tracking
│   ├── reports/                   # Reporting
│   └── settings/                  # App settings
│
└── navigation/                    # Navigation components
```

## 🚀 Getting Started | البدء

### Prerequisites | المتطلبات الأساسية
- Android Studio (Arctic Fox+)
- Android SDK 21+
- Kotlin 1.5.0+

### المتطلبات الأساسية
- أندرويد ستوديو (Arctic Fox+)
- Android SDK 21 أو أحدث
- Kotlin 1.5.0 أو أحدث

### Installation | التثبيت
1. استنسخ المستودع
   ```bash
   git clone https://github.com/yourusername/BusinessManagement.git
   ```
2. افتح المشروع في أندرويد ستوديو
3. مزامنة المشروع مع ملفات Gradle
4. شغل التطبيق على محاكي أو جهاز فعلي

### التثبيت
1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/BusinessManagement.git
   ```
2. Open the project in Android Studio
3. Sync project with Gradle files
4. Run the app on an emulator or physical device

## 🛠 Built With

- [Kotlin](https://kotlinlang.org/) - Programming language
- [Jetpack Compose](https://developer.android.com/jetpack/compose) - UI toolkit
- [Room](https://developer.android.com/training/data-storage/room) - Local database
- [Hilt](https://developer.android.com/training/dependency-injection/hilt-android) - Dependency injection
- [WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager) - Background tasks
- [Coroutines](https://developer.android.com/kotlin/coroutines) - Asynchronous programming

## 📝 Documentation

For detailed documentation, please check out our [Documentation Wiki](docs/README.md).

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

Hamza K. - [@your_twitter](https://twitter.com/your_twitter)

Project Link: [https://github.com/yourusername/BusinessManagement](https://github.com/yourusername/BusinessManagement)

## 🙏 Acknowledgments

- [JetBrains](https://www.jetbrains.com/)
- [Android Developers](https://developer.android.com/)
- [Kotlin](https://kotlinlang.org/)

<div dir="rtl">

## 📞 للتواصل

حمزة ك. - [@your_twitter](https://twitter.com/your_twitter)

رابط المشروع: [https://github.com/yourusername/BusinessManagement](https://github.com/yourusername/BusinessManagement)

</div>

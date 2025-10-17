# دليل التنقيح | Debugging Guide

يوفر هذا المستند تقنيات التنقيح وأدواته لتطبيق إدارة المحل التجاري.

This document provides debugging techniques and tools for the Business Management App.

## 🐛 أدوات التنقيح | Debugging Tools

### مصحح أندرويد ستوديو | Android Studio Debugger
- **نقاط التوقف**: تعيين نقاط توقف على سطور محددة | **Breakpoints**: Set breakpoints on specific lines
- **التنقل خطوة بخطوة**: الانتقال فوق أو داخل أو خارج الكود | **Step Through**: Step over, into, or out of code
- **مراقبة المتغيرات**: مراقبة قيم المتغيرات في الوقت الفعلي | **Watch Variables**: Monitor variable values in real-time
- **مكدس الاستدعاءات**: عرض تسلسل استدعاءات الطرق | **Call Stack**: View method call hierarchy

### التسجيل | Logging
```kotlin
// تسجيل التنقيح | Debug logging
private const val TAG = "UserRepository"

// استخدام timber للتسجيل | Use timber for logging
Timber.d("جلب المستخدم: %s", userId)
Timber.e("خطأ في تحميل المستخدم", exception)

// أو استخدام تسجيل أندرويد القياسي | Or use standard Android logging
Log.d(TAG, "تم تحميل المستخدم: $user")
Log.e(TAG, "فشل في تحميل المستخدم", exception)
```

## 🔍 سيناريوهات التنقيح الشائعة | Common Debugging Scenarios

### تعطل التطبيق | App Crashes
```kotlin
// 1. تحقق من تتبع المكدس في Logcat | 1. Check stack trace in Logcat
// 2. ابحث عن الاستثناءات غير المعالجة | 2. Look for unhandled exceptions
// 3. تحقق من استثناءات المؤشر الفارغ | 3. Check for null pointer exceptions
// 4. تحقق من تنظيف الموارد | 4. Verify resource cleanup

// مثال تنقيح التعطل | Example crash debugging
try {
    val user = userRepository.getUser(userId)
} catch (e: Exception) {
    Log.e(TAG, "فشل تحميل المستخدم", e) | Log.e(TAG, "User loading failed", e)
    // تحقق من نوع الاستثناء وتعامل معه بشكل مناسب | Check exception type and handle appropriately
}
```

### مشاكل الأداء | Performance Issues
```kotlin
// 1. استخدم مُحلل أندرويد | 1. Use Android Profiler
// 2. مراقبة استخدام الذاكرة | 2. Monitor memory usage
// 3. تحقق من طلبات الشبكة | 3. Check network requests
// 4. تحليل عمليات قاعدة البيانات | 4. Profile database operations

// تحليل الذاكرة | Memory profiling
val runtime = Runtime.getRuntime()
val usedMemory = runtime.totalMemory() - runtime.freeMemory()
Log.d(TAG, "استخدام الذاكرة: ${usedMemory / 1024 / 1024} ميغابايت | Memory usage: ${usedMemory / 1024 / 1024} MB")
```

### مشاكل الشبكة | Network Issues
```kotlin
// 1. تحقق من اتصال الشبكة | 1. Check network connectivity
// 2. مراقبة استجابات API | 2. Monitor API responses
// 3. التحقق من شهادات SSL | 3. Verify SSL certificates
// 4. تحقق من قيم المهلة | 4. Check timeout values

// تنقيح الشبكة | Network debugging
val connectivityManager = getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager
val networkInfo = connectivityManager.activeNetworkInfo
Log.d(TAG, "الشبكة متاحة: ${networkInfo?.isConnected} | Network available: ${networkInfo?.isConnected}")
```

## 🛠️ تقنيات التنقيح | Debugging Techniques

### تنقيح قاعدة البيانات | Database Debugging
```kotlin
// تمكين تنقيح قاعدة البيانات | Enable database debugging
val db = Room.databaseBuilder(context, AppDatabase::class.java, "app.db")
    .addMigrations(MIGRATION_1_2)
    .build()

// تسجيل استعلامات SQL | Log SQL queries
db.query("SELECT * FROM users WHERE id = ?", arrayOf(userId)).use { cursor ->
    Log.d(TAG, "تم العثور على ${cursor.count} مستخدمين | Found ${cursor.count} users")
}
```

### تنقيح ViewModel | ViewModel Debugging
```kotlin
// تنقيح تغييرات الحالة | Debug state changes
val uiState = MutableStateFlow<UiState>(Loading)
    .onEach { state ->
        Log.d(TAG, "تغيرت حالة واجهة المستخدم: $state | UI State changed: $state")
    }
    .stateIn(viewModelScope, SharingStarted.WhileSubscribed(), Loading)
```

### تنقيح الكوروتين | Coroutine Debugging
```kotlin
// تنقيح تنفيذ الكوروتين | Debug coroutine execution
viewModelScope.launch {
    Log.d(TAG, "بدء الكوروتين | Starting coroutine")
    try {
        val result = withContext(Dispatchers.IO) {
            Log.d(TAG, "التنفيذ على خيط IO | Executing on IO thread")
            delay(1000) // محاكاة العمل | Simulate work
            "result"
        }
        Log.d(TAG, "اكتمل الكوروتين: $result | Coroutine completed: $result")
    } catch (e: Exception) {
        Log.e(TAG, "فشل الكوروتين", e) | Log.e(TAG, "Coroutine failed", e)
    }
}
```

## 📊 أدوات المراقبة | Monitoring Tools

### مُحلل أندرويد | Android Profiler
- **مُحلل CPU**: مراقبة استخدام CPU وتتبعات الطرق | **CPU Profiler**: Monitor CPU usage and method traces
- **مُحلل الذاكرة**: تتبع تخصيصات الذاكرة والتسريبات | **Memory Profiler**: Track memory allocations and leaks
- **مُحلل الشبكة**: مراقبة طلبات واستجابات الشبكة | **Network Profiler**: Monitor network requests and responses
- **مُحلل الطاقة**: تتبع استخدام البطارية | **Energy Profiler**: Track battery usage

### تصفية Logcat | Logcat Filtering
```kotlin
// تصفية حسب العلامة | Filter by tag
adb logcat -s UserRepository

// تصفية حسب الأولوية | Filter by priority
adb logcat *:E  # الأخطاء فقط | Errors only

// تصفية حسب علامات متعددة | Filter by multiple tags
adb logcat UserRepository:V NetworkManager:V *:S

// مسح logcat | Clear logcat
adb logcat -c
```

## 🚨 أنماط معالجة الأخطاء | Error Handling Patterns

### Try-Catch مع التسجيل | Try-Catch with Logging
```kotlin
suspend fun safeApiCall(): Result<User> {
    return try {
        Log.d(TAG, "إجراء مكالمة API | Making API call")
        val user = api.getUser(userId)
        Log.d(TAG, "نجحت مكالمة API | API call successful")
        Result.success(user)
    } catch (e: HttpException) {
        Log.e(TAG, "خطأ HTTP: ${e.code()}", e) | Log.e(TAG, "HTTP error: ${e.code()}", e)
        Result.failure(e)
    } catch (e: IOException) {
        Log.e(TAG, "خطأ الشبكة", e) | Log.e(TAG, "Network error", e)
        Result.failure(e)
    } catch (e: Exception) {
        Log.e(TAG, "خطأ غير متوقع", e) | Log.e(TAG, "Unexpected error", e)
        Result.failure(e)
    }
}
```

### تنظيف الموارد | Resource Cleanup
```kotlin
// إدارة الموارد بشكل صحيح | Proper resource management
fun processFile(file: File) {
    var inputStream: FileInputStream? = null
    try {
        inputStream = FileInputStream(file)
        // معالجة الملف | Process file
    } catch (e: IOException) {
        Log.e(TAG, "فشلت معالجة الملف", e) | Log.e(TAG, "File processing failed", e)
    } finally {
        try {
            inputStream?.close()
        } catch (e: IOException) {
            Log.w(TAG, "فشل في إغلاق التدفق", e) | Log.w(TAG, "Failed to close stream", e)
        }
    }
}
```

## 🔧 التنقيح عن بعد | Remote Debugging

### إعداد تنقيح USB | USB Debugging Setup
1. **تمكين خيارات المطور**: الإعدادات > حول الهاتف > النقر على رقم البناء 7 مرات | **Enable Developer Options**: Settings > About phone > Tap Build number 7 times
2. **تمكين تنقيح USB**: الإعدادات > خيارات المطور > تنقيح USB | **Enable USB Debugging**: Settings > Developer options > USB debugging
3. **اتصال الجهاز**: توصيل جهاز أندرويد عبر USB | **Connect Device**: Connect Android device via USB
4. **التحقق من الاتصال**: يجب أن يظهر `adb devices` الجهاز المتصل | **Verify Connection**: `adb devices` should show connected device

### التنقيح اللاسلكي (أندرويد 11+) | Wireless Debugging (Android 11+)
```bash
# تمكين التنقيح اللاسلكي في خيارات المطور | Enable wireless debugging in developer options
# إقران الجهاز برمز QR أو رمز الإقران | Pair device with QR code or pairing code
adb pair 192.168.1.100:12345
adb connect 192.168.1.100:12345
```

## 📱 تنقيح خاص بالجهاز | Device-Specific Debugging

### تنقيح المحاكي | Emulator Debugging
```bash
# سرد المحاكيات المتاحة | List available emulators
emulator -list-avds

# بدء المحاكي مع التنقيح | Start emulator with debugging
emulator -avd Pixel_4_API_30 -writable-system

# تثبيت التطبيق على المحاكي | Install app on emulator
adb install app-debug.apk
```

### تنقيح الجهاز الحقيقي | Real Device Debugging
```bash
# التحقق من اتصال الجهاز | Check device connection
adb devices

# عرض سجلات الجهاز | View device logs
adb logcat

# التقاط لقطة شاشة | Take screenshot
adb shell screencap /sdcard/screenshot.png
adb pull /sdcard/screenshot.png

# تسجيل الشاشة | Record screen
adb shell screenrecord /sdcard/demo.mp4
adb pull /sdcard/demo.mp4
```

## 🚀 التنقيح المتقدم | Advanced Debugging

### اكتشاف تسرب الذاكرة | Memory Leak Detection
```kotlin
// استخدام LeakCanary (إضافة إلى فئة التطبيق) | Using LeakCanary (add to Application class)
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        if (LeakCanary.isInAnalyzerProcess(this)) {
            return
        }
        LeakCanary.install(this)
    }
}

// مراقبة مراجع الكائنات | Monitor object references
val refWatcher = LeakCanary.installedRefWatcher
refWatcher.watch(someObject)
```

### اكتشاف ANR | ANR Detection
```kotlin
// مراقبة ANR (التطبيق لا يستجيب) | Monitor for ANR (Application Not Responding)
val handler = Handler(Looper.getMainLooper())
handler.postDelayed({
    Log.w(TAG, "تم اكتشاف ANR محتمل | Potential ANR detected")
}, 5000)
```

## 📋 قائمة التحقق من التنقيح | Debugging Checklist

### مشاكل بدء التطبيق | App Startup Issues
- [ ] تحقق من تهيئة فئة التطبيق | Check application class initialization
- [ ] التحقق من إعداد حقن التبعيات | Verify dependency injection setup
- [ ] تحقق من ترحيل قاعدة البيانات | Check database migrations
- [ ] التحقق من الأذونات المطلوبة | Verify required permissions

### مشاكل الشبكة | Network Issues
- [ ] تحقق من اتصال الإنترنت | Check internet connectivity
- [ ] التحقق من نقاط نهاية API | Verify API endpoints
- [ ] تحقق من تكوين SSL/TLS | Check SSL/TLS configuration
- [ ] مراقبة مهلات الشبكة | Monitor network timeouts

### مشاكل قاعدة البيانات | Database Issues
- [ ] تحقق من مخطط قاعدة البيانات | Check database schema
- [ ] التحقق من تطبيق الترحيلات | Verify migrations applied
- [ ] تحقق من سلامة البيانات | Check data integrity
- [ ] مراقبة أداء الاستعلامات | Monitor query performance

### مشاكل واجهة المستخدم | UI Issues
- [ ] تحقق من تضخم التخطيط | Check layout inflation
- [ ] التحقق من ربط العرض | Verify view binding
- [ ] تحقق من تطبيق السمة | Check theme application
- [ ] مراقبة دورة حياة العرض | Monitor view lifecycle

## 🔧 تكوين بناء التطوير | Development Build Configuration

### إعداد بناء التنقيح | Debug Build Setup
```kotlin
// build.gradle.kts
android {
    buildTypes {
        debug {
            buildConfigField("String", "API_BASE_URL", "\"http://10.0.2.2:8080\"")
            buildConfigField("boolean", "ENABLE_LOGGING", "true")
            buildConfigField("boolean", "ENABLE_STRICT_MODE", "true")
        }
        release {
            buildConfigField("String", "API_BASE_URL", "\"https://api.production.com\"")
            buildConfigField("boolean", "ENABLE_LOGGING", "false")
            buildConfigField("boolean", "ENABLE_STRICT_MODE", "false")
        }
    }
}
```

### تكوين الوضع الصارم | Strict Mode Configuration
```kotlin
// تمكين الوضع الصارم للتنقيح | Enable strict mode for debugging
if (BuildConfig.ENABLE_STRICT_MODE) {
    StrictMode.setThreadPolicy(
        StrictMode.ThreadPolicy.Builder()
            .detectDiskReads()
            .detectDiskWrites()
            .detectNetwork()
            .penaltyLog()
            .build()
    )
}
```

## 📞 الحصول على المساعدة | Getting Help

### موارد التنقيح | Debugging Resources
- **مصحح أندرويد ستوديو**: أدوات التنقيح المدمجة | **Android Studio Debugger**: Built-in debugging tools
- **Logcat**: مراقبة السجلات في الوقت الفعلي | **Logcat**: Real-time log monitoring
- **مُحلل أندرويد**: مراقبة الأداء | **Android Profiler**: Performance monitoring
- **مستكشف ملفات الجهاز**: فحص نظام الملفات | **Device File Explorer**: File system inspection

### دعم المجتمع | Community Support
- **Stack Overflow**: أسئلة تطوير أندرويد | **Stack Overflow**: Android development questions
- **مطورو أندرويد**: التوثيق الرسمي | **Android Developers**: Official documentation
- **قضايا GitHub**: الإبلاغ عن الأخطاء والحصول على المساعدة | **GitHub Issues**: Report bugs and get help

### التنقيح المهني | Professional Debugging
للمشكلات المعقدة:

For complex issues:
1. **جمع السجلات الشاملة** | **Collect comprehensive logs**
2. **إنشاء حالة إعادة إنتاج بسيطة** | **Create minimal reproduction case**
3. **توثيق خطوات إعادة الإنتاج** | **Document steps to reproduce**
4. **تضمين تفاصيل الجهاز/البيئة** | **Include device/environment details**

## 🚨 التنقيح الطارئ | Emergency Debugging

### مشاكل الإنتاج | Production Issues
1. **تمكين تسجيل عن بعد** (Firebase Crashlytics) | **Enable remote logging** (Firebase Crashlytics)
2. **مراقبة معدلات الأخطاء** في الوقت الفعلي | **Monitor error rates** in real-time
3. **تنفيذ قواطع الدائرة** للخدمات الفاشلة | **Implement circuit breakers** for failing services
4. **وجود خطة تراجع** للمشكلات الحرجة | **Have rollback plan** for critical issues

### استجابة خطأ حرج | Critical Bug Response
1. **تقييم التأثير**: تحديد النطاق والخطورة | **Assess impact**: Determine scope and severity
2. **الإصلاح الفوري**: تنفيذ حل بديل مؤقت | **Immediate fix**: Implement temporary workaround
3. **تحليل السبب الجذري**: تحديد السبب الأساسي | **Root cause analysis**: Identify underlying cause
4. **الحل الدائم**: تنفيذ الإصلاح الصحيح | **Permanent solution**: Implement proper fix
5. **الوقاية**: إضافة المراقبة والاختبارات | **Prevention**: Add monitoring and tests

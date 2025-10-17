# دليل عملية البناء | Build Process Guide

يشرح هذا المستند عملية البناء والتكوين لتطبيق إدارة المحل التجاري.

This document explains the build process and configuration for the Business Management App.

## 🏗️ نظرة عامة على نظام البناء | Build System Overview

### تكوين Gradle | Gradle Configuration
```kotlin
// build.gradle.kts (مستوى المشروع) | (Project level)
plugins {
    id("com.android.application") version "8.1.4"
    id("kotlin-android") version "1.8.10"
    id("kotlin-kapt") version "1.8.10"
    id("dagger.hilt.android.plugin") version "2.44"
    id("androidx.navigation.safeargs.kotlin") version "2.5.3"
}
```

### متغيرات البناء | Build Variants
- **debug**: بناء التطوير مع تمكين التنقيح | **Development build with debugging enabled**
- **release**: بناء الإنتاج مع التحسينات | **Production build with optimizations**
- **staging**: بناء الاختبار مع إعدادات مشابهة للإنتاج | **Testing build with production-like settings**

## 🔧 تكوين البناء | Build Configuration

### تكوين أندرويد | Android Configuration
```kotlin
android {
    namespace = "com.businessmanagement"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.businessmanagement.app"
        minSdk = 21
        targetSdk = 34
        versionCode = 1
        versionName = "1.0.0"

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"

        // تكوين البناء | Build configuration
        buildConfigField("String", "API_BASE_URL", "\"https://api.businessmanagement.app\"")
        buildConfigField("boolean", "ENABLE_LOGGING", "false")
        buildConfigField("boolean", "ENABLE_ANALYTICS", "true")
    }

    buildTypes {
        debug {
            applicationIdSuffix = ".debug"
            versionNameSuffix = "-DEBUG"
            buildConfigField("String", "API_BASE_URL", "\"http://10.0.2.2:8080\"")
            buildConfigField("boolean", "ENABLE_LOGGING", "true")
            buildConfigField("boolean", "ENABLE_ANALYTICS", "false")
        }

        release {
            minifyEnabled = true
            proguardFiles(getDefaultProguardFile("proguard-android-optimize.txt"), "proguard-rules.pro")
            buildConfigField("boolean", "ENABLE_LOGGING", "false")
            buildConfigField("boolean", "ENABLE_ANALYTICS", "true")
        }
    }
}
```

## 📦 إدارة التبعيات | Dependencies Management

### فهرس الإصدارات | Version Catalog
```toml
# gradle/libs.versions.toml
[versions]
kotlin = "1.8.10"
androidx-core = "1.12.0"
androidx-activity = "1.8.2"
androidx-navigation = "2.7.5"
hilt = "2.44"
room = "2.6.1"

[libraries]
androidx-core-ktx = { module = "androidx.core:core-ktx", version.ref = "androidx-core" }
androidx-activity-compose = { module = "androidx.activity:activity-compose", version.ref = "androidx-activity" }
androidx-navigation-compose = { module = "androidx.navigation:navigation-compose", version.ref = "androidx-navigation" }
hilt-android = { module = "com.google.dagger:hilt-android", version.ref = "hilt" }
room-runtime = { module = "androidx.room:room-runtime", version.ref = "room" }
```

## 🔨 أوامر البناء | Build Commands

### التطوير المحلي | Local Development
```bash
# تنظيف وبناء APK التنقيح | Clean and build debug APK
./gradlew clean assembleDebug

# بناء APK الإصدار | Build release APK
./gradlew assembleRelease

# بناء جميع المتغيرات | Build all variants
./gradlew assembleDebug assembleRelease

# تشغيل الاختبارات | Run tests
./gradlew testDebugUnitTest

# فحص جودة الكود | Check code quality
./gradlew detekt ktlintCheck
```

### بناء CI/CD | CI/CD Builds
```bash
# البناء مع التوقيع | Build with signing
./gradlew assembleRelease \
    -Pandroid.injected.signing.store.file=$KEYSTORE_PATH \
    -Pandroid.injected.signing.store.password=$KEYSTORE_PASSWORD \
    -Pandroid.injected.signing.key.alias=$KEY_ALIAS \
    -Pandroid.injected.signing.key.password=$KEY_PASSWORD

# إنشاء تقارير البناء | Generate build reports
./gradlew assembleRelease --info --stacktrace
```

## 🔐 تكوين التوقيع | Signing Configuration

### توقيع التنقيح | Debug Signing
```kotlin
// توقيع التنقيح الافتراضي (يتم إنشاؤه تلقائيًا) | Default debug signing (auto-generated)
android {
    signingConfigs {
        debug {
            storeFile = file("debug.keystore")
            storePassword = "android"
            keyAlias = "androiddebugkey"
            keyPassword = "android"
        }
    }
}
```

### توقيع الإصدار | Release Signing
```kotlin
signingConfigs {
    release {
        storeFile = file("release.keystore")
        storePassword = System.getenv("KEYSTORE_PASSWORD")
        keyAlias = System.getenv("KEY_ALIAS")
        keyPassword = System.getenv("KEY_PASSWORD")
    }
}
```

## 📱 إنشاء APK | APK Generation

### APK التنقيح | Debug APK
```bash
# إنشاء APK التنقيح | Generate debug APK
./gradlew assembleDebug

# موقع الإخراج | Output location
app/build/outputs/apk/debug/app-debug.apk
```

### APK الإصدار | Release APK
```bash
# إنشاء APK الإصدار | Generate release APK
./gradlew assembleRelease

# موقع الإخراج | Output location
app/build/outputs/apk/release/app-release.apk

# إنشاء APK عالمي (يدعم جميع ABIs) | Generate universal APK (supports all ABIs)
./gradlew assembleRelease -Pandroid.injected.abi.filter=universal
```

### الحزمة (AAB) | Bundle (AAB) Generation
```bash
# إنشاء حزمة تطبيق أندرويد | Generate Android App Bundle
./gradlew bundleRelease

# موقع الإخراج | Output location
app/build/outputs/bundle/release/app-release.aab
```

## 🧪 التحقق من البناء | Build Verification

### تحليل APK | APK Analysis
```bash
# فحص محتويات APK | Check APK contents
unzip -l app/build/outputs/apk/release/app-release.apk

# التحقق من توقيع APK | Verify APK signature
apksigner verify app-release.apk

# فحص المشاكل | Check for issues
./gradlew lintRelease
```

### تحليل الحزمة | Bundle Analysis
```bash
# تحليل محتويات الحزمة | Analyze bundle contents
bundletool build-apks --bundle=app-release.aab --output=apks.apks

# استخراج APKs من الحزمة | Extract APKs from bundle
unzip apks.apks -d extracted_apks/
```

## 🚀 تحسين البناء | Build Optimization

### تكوين ProGuard | ProGuard Configuration
```kotlin
# proguard-rules.pro
-keep class com.businessmanagement.** { *; }
-keep class androidx.** { *; }
-keep class com.google.** { *; }

# الاحتفاظ بفئات البيانات للتسلسل JSON | Keep data classes for JSON serialization
-keep class com.businessmanagement.model.** { *; }

# الاحتفاظ بكيانات Room | Keep Room entities
-keep class com.businessmanagement.database.** { *; }

# إزالة التسجيل في بناءات الإصدار | Remove logging in release builds
-assumenosideeffects class android.util.Log {
    public static *** d(...);
    public static *** v(...);
    public static *** i(...);
}
```

### تحسين R8 | R8 Optimization
```kotlin
buildTypes {
    release {
        minifyEnabled = true
        proguardFiles(getDefaultProguardFile("proguard-android-optimize.txt"), "proguard-rules.pro")
    }
}
```

## 📊 أداء البناء | Build Performance

### تخزين البناء المؤقت | Build Caching
```kotlin
// تمكين تخزين البناء المؤقت | Enable build cache
org.gradle.caching=true

// تكوين موقع تخزين البناء المؤقت | Configure build cache location
buildCache {
    local {
        directory = new File(rootDir, "build-cache")
    }
}
```

### التنفيذ المتوازي | Parallel Execution
```kotlin
// تمكين التنفيذ المتوازي | Enable parallel execution
org.gradle.parallel=true

// تكوين خيوط العاملين | Configure worker threads
org.gradle.workers.max=4
```

## 🔍 استكشاف أخطاء البناء | Build Troubleshooting

### المشكلات الشائعة | Common Issues

#### فشل البناء | Build Failures
```bash
# تنظيف مجلد البناء | Clean build directory
./gradlew clean

# تنظيف وإعادة البناء | Clean and rebuild
./gradlew clean assembleDebug

# فحص تعارضات التبعيات | Check for dependency conflicts
./gradlew dependencies --configuration=debugCompileClasspath
```

#### مشاكل الذاكرة | Memory Issues
```bash
# زيادة كومة Gradle | Increase Gradle heap size
export GRADLE_OPTS="-Xmx2g -XX:MaxMetaspaceSize=512m"

# تمكين شيطان Gradle | Enable Gradle daemon
./gradlew --daemon assembleDebug
```

#### مشاكل التوقيع | Signing Issues
```bash
# التحقق من مخزن المفاتيح | Verify keystore
keytool -list -v -keystore release.keystore

# فحص تكوين التوقيع | Check signing configuration
./gradlew signingReport
```

## 📋 قائمة التحقق من البناء | Build Checklist

### قبل بناء الإصدار | Before Release Build
- [ ] تحديث أرقام الإصدار والاسم | Update version code and name
- [ ] تكوين بيانات اعتماد التوقيع | Configure signing credentials
- [ ] تمكين ProGuard/R8 | Enable ProGuard/R8
- [ ] تشغيل جميع الاختبارات | Run all tests
- [ ] فحص تحذيرات lint | Check lint warnings
- [ ] التحقق من حجم البناء | Verify build size
- [ ] اختبار على أجهزة متعددة | Test on multiple devices

### بعد إنشاء البناء | After Build Generation
- [ ] التحقق من سلامة APK/AAB | Verify APK/AAB integrity
- [ ] فحص أحجام الملفات | Check file sizes
- [ ] التحقق من وظائف التطبيق | Validate app functionality
- [ ] اختبار عملية التثبيت | Test installation process
- [ ] التحقق من عدم وجود كود تنقيح متبقي | Verify no debug code remains

## 📞 دعم البناء | Build Support

### الحصول على المساعدة | Getting Help
- **أخطاء البناء**: فحص سجلات Gradle مع `--stacktrace` | **Build Errors**: Check Gradle logs with `--stacktrace`
- **مشاكل الأداء**: مراقبة مع `--profile` | **Performance Issues**: Monitor with `--profile`
- **مشاكل التبعيات**: استخدام `./gradlew dependencies` | **Dependency Problems**: Use `./gradlew dependencies`

### الموارد | Resources
- **توثيق Gradle**: https://docs.gradle.org/ | **Gradle Documentation**: https://docs.gradle.org/
- **أدوات بناء أندرويد**: https://developer.android.com/build | **Android Build Tools**: https://developer.android.com/build
- **دليل ProGuard**: https://www.guardsquare.com/manual | **ProGuard Manual**: https://www.guardsquare.com/manual

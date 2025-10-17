# دليل معايير البرمجة | Coding Standards Guide

يحدد هذا المستند معايير البرمجة وأفضل الممارسات لتطبيق إدارة المحل التجاري.

This document outlines the coding standards and best practices for the Business Management App.

## 🏗️ معايير المعمارية | Architecture Standards

### الامتثال للمعمارية النظيفة | Clean Architecture Compliance
- **فصل الاهتمامات**: حدود واضحة بين الطبقات | **Separation of Concerns**: Clear boundaries between layers
- **قاعدة التبعية**: تشير التبعيات إلى الداخل فقط | **Dependency Rule**: Dependencies point inward only
- **الطبقات المستقلة**: يمكن اختبار كل طبقة بشكل مستقل | **Independent Layers**: Each layer can be tested independently

### تنفيذ نمط MVVM | MVVM Pattern Implementation
- **ViewModels**: مسؤولية واحدة، مدركة لدورة الحياة | **ViewModels**: Single responsibility, lifecycle aware
- **LiveData/StateFlow**: تدفقات البيانات التفاعلية | **LiveData/StateFlow**: Reactive data streams
- **نمط المستودع**: تجريد الوصول إلى البيانات | **Repository Pattern**: Data access abstraction

## 💻 إرشادات نمط الكود | Code Style Guidelines

### معايير كوتلين | Kotlin Standards
```kotlin
// ✅ جيد | Good
class UserRepository @Inject constructor(
    private val userDao: UserDao,
    private val userRemoteDataSource: UserRemoteDataSource
) {
    suspend fun getUser(id: String): Flow<User> = flow {
        // التنفيذ | Implementation
    }
}

// ❌ تجنب | Avoid
class BadRepository {
    fun getUser(id:String):User { // معدلات الوصول مفقودة، تسمية سيئة | Missing access modifiers, poor naming
        // تنفيذ سيء | Poor implementation
    }
}
```

### اصطلاحات التسمية | Naming Conventions
- **الفئات**: باسكال كيس (`UserRepository`) | **Classes**: PascalCase (`UserRepository`)
- **الدوال**: كاميل كيس (`getUserById`) | **Functions**: camelCase (`getUserById`)
- **المتغيرات**: كاميل كيس (`userName`) | **Variables**: camelCase (`userName`)
- **الثوابت**: أッパー_スネーク_ケース (`MAX_RETRY_ATTEMPTS`) | **Constants**: UPPER_SNAKE_CASE (`MAX_RETRY_ATTEMPTS`)

## 📝 معايير التوثيق | Documentation Standards

### التعليقات والتوثيق | Comments and Documentation
```kotlin
/**
 * يسترد معلومات المستخدم بالمعرف مع دعم التخزين المؤقت.
 *
 * Retrieves user information by ID with caching support.
 *
 * @param userId المعرف الفريد للمستخدم | The unique identifier for the user
 * @param forceRefresh إذا كان true، يتجاهل التخزين المؤقت ويجلب البيانات الجديدة | If true, ignores cache and fetches fresh data
 * @return Flow يصدر بيانات المستخدم أو حالات الخطأ | Flow emitting user data or error states
 */
suspend fun getUser(
    userId: String,
    forceRefresh: Boolean = false
): Flow<Result<User>>
```

### رؤوس الملفات | File Headers
يجب أن يتضمن كل ملف كوتلين:

Each Kotlin file should include:
```kotlin
/*
 * تطبيق إدارة المحل التجاري
 * Business Management App
 * حقوق الطبع والنشر (C) 2024 حمزة ك.
 * Copyright (C) 2024 Hamza K.
 *
 * هذا الملف جزء من تطبيق إدارة المحل التجاري.
 * This file is part of the Business Management App.
 */
package com.businessmanagement.features.users
```

## 🧪 معايير الاختبار | Testing Standards

### اختبارات الوحدة | Unit Tests
- **التغطية**: الحد الأدنى 80% تغطية الكود | **Coverage**: Minimum 80% code coverage
- **التسمية**: `ClassNameTest.kt` | **Naming**: `ClassNameTest.kt`
- **الهيكل**: نمط Given-When-Then | **Structure**: Given-When-Then pattern

```kotlin
@Test
fun `calculateTotal should return correct sum` () {
    // نظرًا لأن | Given
    val items = listOf(
        CartItem("منتج 1", 10.0, 2), | CartItem("Product 1", 10.0, 2),
        CartItem("منتج 2", 15.0, 1) | CartItem("Product 2", 15.0, 1)
    )

    // عندما | When
    val total = calculateTotal(items)

    // ثم | Then
    assertEquals(35.0, total, 0.01)
}
```

### اختبارات التكامل | Integration Tests
- اختبار تفاعلات المكونات | Test interactions between components
- محاكاة التبعيات الخارجية | Mock external dependencies
- اختبار استمرارية البيانات | Test data persistence

## 🔒 معايير الأمان | Security Standards

### المصادقة | Authentication
- تخزين الرموز الآمن (ليس في SharedPreferences) | Secure token storage (not in SharedPreferences)
- مطالبات المصادقة البيومترية | Biometric authentication prompts
- معالجة انتهاء صلاحية الجلسة | Session timeout handling

### حماية البيانات | Data Protection
- التشفير في حالة الراحة لبيانات الحساسة | Encryption at rest for sensitive data
- اتصال API آمن (HTTPS) | Secure API communication (HTTPS)
- التحقق من صحة المدخلات والتعقيم | Input validation and sanitization

## 🚀 معايير الأداء | Performance Standards

### إدارة الذاكرة | Memory Management
- تجنب تسرب الذاكرة في ViewModels | Avoid memory leaks in ViewModels
- التخلص الصحيح من الموارد | Proper disposal of resources
- هياكل البيانات الفعالة | Efficient data structures

### تحسين الشبكة | Network Optimization
- تنفيذ الترقيم الصفحي لمجموعات البيانات الكبيرة | Implement pagination for large datasets
- استخدام استراتيجيات التخزين المؤقت | Use caching strategies
- تقليل مكالمات الشبكة | Minimize network calls

## 🛠️ سير عمل التطوير | Development Workflow

### معايير Git | Git Standards
- **تسمية الفروع**: `feature/feature-name`, `bugfix/issue-description` | **Branch Naming**: `feature/feature-name`, `bugfix/issue-description`
- **رسائل الالتزام**: واضحة، موجزة، مزاج أمر | **Commit Messages**: Clear, concise, imperative mood
- **طلبات السحب**: تشمل الوصف والاختبار ولقطات الشاشة | **Pull Requests**: Include description, testing, and screenshots

### عملية مراجعة الكود | Code Review Process
- الحد الأدنى 2 موافقات مطلوبة | Minimum 2 approvals required
- يجب أن تنجح جميع الاختبارات | All tests must pass
- الحفاظ على تغطية الكود | Code coverage maintained
- مراجعة الأمان للتغييرات الحساسة | Security review for sensitive changes

## 📱 معايير واجهة المستخدم/تجربة المستخدم | UI/UX Standards

### الامتثال للتصميم المادي | Material Design Compliance
- اتباع إرشادات التصميم المادي 3 | Follow Material Design 3 guidelines
- مخططات الألوان المتسقة | Consistent color schemes
- دعم إمكانية الوصول المناسب | Proper accessibility support

### التصميم المتجاوب | Responsive Design
- دعم أحجام الشاشات المتعددة | Support multiple screen sizes
- معالجة التوجيه المناسبة | Proper orientation handling
- دعم السمة الداكنة/الفاتحة | Dark/Light theme support

## 🔧 الأدوات والمكتبات | Tools and Libraries

### الأدوات المطلوبة | Required Tools
- **أندرويد ستوديو أركتيك فوكس+** | **Android Studio Arctic Fox+**
- **كوتلين 1.8.0+** | **Kotlin 1.8.0+**
- **جرادل 7.0+** | **Gradle 7.0+**

### أدوات جودة الكود | Code Quality Tools
- **KtLint**: تنسيق الكود | **KtLint**: Code formatting
- **Detekt**: التحليل الثابت للكود | **Detekt**: Static code analysis
- **Jacoco**: تغطية الاختبار | **Jacoco**: Test coverage
- **Spotless**: تنظيف الكود | **Spotless**: Code cleanup

## 📋 قائمة التحقق للميزات الجديدة | Checklist for New Features

- [ ] تمت مراجعة تصميم المعمارية | Architecture design reviewed
- [ ] تم كتابة اختبارات الوحدة (تغطية 80%+) | Unit tests written (80%+ coverage)
- [ ] تم تحديث اختبارات التكامل | Integration tests updated
- [ ] تم تحديث التوثيق | Documentation updated
- [ ] تمت مراجعة الأمان | Security review completed
- [ ] تم اختبار الأداء | Performance tested
- [ ] تم اتباع إرشادات واجهة المستخدم/تجربة المستخدم | UI/UX guidelines followed
- [ ] تمت مراجعة الكود | Code review completed
- [ ] تم إكمال الاختبار | Testing completed

## 🚨 المزالق الشائعة التي يجب تجنبها | Common Pitfalls to Avoid

### ❌ لا تفعل | Don't
- تخزين البيانات الحساسة في SharedPreferences | Store sensitive data in SharedPreferences
- حجب الخيط الرئيسي بمكالمات الشبكة | Block main thread with network calls
- تجاهل معالجة الأخطاء المناسبة | Ignore proper error handling
- تخطي التحقق من صحة المدخلات | Skip input validation
- نسيان تسرب الذاكرة | Forget about memory leaks

### ✅ افعل | Do
- استخدام حقن التبعية بشكل صحيح | Use dependency injection properly
- تنفيذ معالجة الأخطاء المناسبة | Implement proper error handling
- كتابة اختبارات شاملة | Write comprehensive tests
- توثيق واجهات برمجة التطبيقات العامة | Document public APIs
- اتباع أفضل ممارسات الأمان | Follow security best practices

## 📞 الحصول على المساعدة | Getting Help

- **مراجعات الكود**: طلب مراجعة من مطورين كبار | **Code Reviews**: Request review from senior developers
- **أسئلة المعمارية**: استشر قادة التقنية | **Architecture Questions**: Consult with tech leads
- **توضيح المعايير**: تحقق من هذا المستند أولاً | **Standards Clarification**: Check this document first
- **مشاكل الأدوات**: تحقق من التوثيق والمجتمعات | **Tool Issues**: Check documentation and community resources

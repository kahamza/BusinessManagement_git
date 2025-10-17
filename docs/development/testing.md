# دليل الاختبار | Testing Guide

يشرح هذا المستند استراتيجية الاختبار وممارساته لتطبيق إدارة المحل التجاري.

This document explains the testing strategy and practices for the Business Management App.

## 🧪 استراتيجية الاختبار | Testing Strategy

### هرم الاختبار | Testing Pyramid
```
اختبارات واجهة المستخدم (5%) | UI Tests (5%)
اختبارات التكامل (15%) | Integration Tests (15%)
اختبارات الوحدة (80%) | Unit Tests (80%)
```

### أنواع الاختبارات | Types of Tests
- **اختبارات الوحدة**: اختبار الدوال والفئات الفردية | **Unit Tests**: Test individual functions and classes
- **اختبارات التكامل**: اختبار التفاعلات بين المكونات | **Integration Tests**: Test interactions between components
- **اختبارات واجهة المستخدم**: اختبار تفاعلات واجهة المستخدم | **UI Tests**: Test user interface interactions
- **اختبارات الأداء**: اختبار أداء التطبيق تحت الحمل | **Performance Tests**: Test app performance under load

## 🛠️ أدوات الاختبار | Testing Tools

### اختبارات الوحدة | Unit Testing
```kotlin
// مثال اختبار الوحدة | Example unit test
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

### المحاكاة | Mocking
```kotlin
// استخدام Mockito لمحاكاة التبعيات | Using Mockito for mocking dependencies
@Test
fun `getUser should return user from repository` () = runBlocking {
    // نظرًا لأن | Given
    val mockRepository = mock<UserRepository>()
    val expectedUser = User(id = "1", name = "Test User")
    whenever(mockRepository.getUser("1")).thenReturn(expectedUser)

    // عندما | When
    val viewModel = UserViewModel(mockRepository)
    val result = viewModel.getUser("1")

    // ثم | Then
    assertEquals(expectedUser, result)
}
```

## 🔧 إعداد الاختبار | Test Setup

### التبعيات | Dependencies
```kotlin
// build.gradle.kts
dependencies {
    // الاختبار | Testing
    testImplementation("junit:junit:4.13.2")
    testImplementation("org.mockito.kotlin:mockito-kotlin:4.1.0")
    testImplementation("androidx.arch.core:core-testing:2.2.0")
    testImplementation("org.jetbrains.kotlinx:kotlinx-coroutines-test:1.7.3")

    // اختبار أندرويد | Android testing
    androidTestImplementation("androidx.test.ext:junit:1.1.5")
    androidTestImplementation("androidx.test.espresso:espresso-core:3.5.1")
}
```

### تكوين الاختبار | Test Configuration
```kotlin
// src/test/resources/test.properties
app.debug=true
api.base.url=http://localhost:8080
database.test=true
```

## 🏗️ اختبار المعمارية | Architecture Testing

### اختبار المستودعات | Repository Testing
```kotlin
@Test
fun `user repository should cache users locally` () = runBlocking {
    // نظرًا لأن | Given
    val mockRemoteSource = mock<UserRemoteDataSource>()
    val localUser = User(id = "1", name = "Cached User")
    whenever(mockRemoteSource.getUser("1")).thenReturn(localUser)

    // عندما | When
    val repository = UserRepository(mockRemoteSource, userDao)
    val result = repository.getUser("1")

    // ثم | Then
    verify(userDao).insertUser(localUser) // التحقق من التخزين المؤقت | Verify caching
    assertEquals(localUser, result)
}
```

### اختبار ViewModel | ViewModel Testing
```kotlin
@Test
fun `user view model should handle loading states` () = runBlocking {
    // نظرًا لأن | Given
    val mockRepository = mock<UserRepository>()
    val users = listOf(User(id = "1", name = "User 1"))
    whenever(mockRepository.getUsers()).thenReturn(flowOf(users))

    // عندما | When
    val viewModel = UserViewModel(mockRepository)
    viewModel.loadUsers()

    // ثم | Then
    assertEquals(Loading, viewModel.uiState.value)
    // انتظار تحميل البيانات | Wait for data to load
    advanceUntilIdle()
    assertTrue(viewModel.uiState.value is Success)
}
```

## 🎯 اختبارات واجهة المستخدم | UI Testing

### اختبارات Espresso | Espresso Tests
```kotlin
@Test
fun testUserLoginFlow() {
    // نظرًا لأن | Given
    val username = "testuser"
    val password = "password123"

    // عندما | When
    onView(withId(R.id.username_field)).perform(typeText(username))
    onView(withId(R.id.password_field)).perform(typeText(password))
    onView(withId(R.id.login_button)).perform(click())

    // ثم | Then
    onView(withId(R.id.welcome_message)).check(matches(isDisplayed()))
}
```

### اختبارات Compose | Compose Testing
```kotlin
@Test
fun testUserProfileScreen() {
    // نظرًا لأن | Given
    val user = User(id = "1", name = "Test User")

    // عندما | When
    composeTestRule.setContent {
        UserProfileScreen(user = user)
    }

    // ثم | Then
    composeTestRule.onNodeWithText("Test User").assertIsDisplayed()
}
```

## 🚀 اختبارات الأداء | Performance Testing

### اختبارات المعيار | Benchmark Tests
```kotlin
@Benchmark
fun benchmarkDatabaseQuery() {
    val db = Room.databaseBuilder(context, AppDatabase::class.java, "test.db")
        .build()

    // قياس أداء الاستعلام | Measure query performance
    val startTime = System.nanoTime()
    val users = db.userDao().getAllUsers()
    val endTime = System.nanoTime()

    println("استغرق الاستعلام: ${(endTime - startTime) / 1_000_000} مللي ثانية | Query took: ${(endTime - startTime) / 1_000_000} ms")
}
```

### اختبارات الذاكرة | Memory Testing
```kotlin
@Test
fun testMemoryUsage() {
    val runtime = Runtime.getRuntime()

    // قياس الذاكرة قبل العملية | Measure memory before operation
    val beforeMemory = runtime.totalMemory() - runtime.freeMemory()

    // تنفيذ عملية كثيفة الذاكرة | Perform memory-intensive operation
    val largeData = generateLargeDataset()

    // قياس الذاكرة بعد العملية | Measure memory after operation
    val afterMemory = runtime.totalMemory() - runtime.freeMemory()
    val memoryUsed = afterMemory - beforeMemory

    // التأكيد من أن استخدام الذاكرة معقول | Assert memory usage is reasonable
    assertTrue(memoryUsed < MAX_MEMORY_THRESHOLD)
}
```

## 📊 تغطية الاختبار | Test Coverage

### متطلبات التغطية | Coverage Requirements
- **التغطية العامة**: الحد الأدنى 80% | **Overall Coverage**: Minimum 80%
- **تغطية المسار الحرج**: الحد الأدنى 90% | **Critical Path Coverage**: Minimum 90%
- **الميزات الجديدة**: الحد الأدنى 85% | **New Features**: Minimum 85%

### تقارير التغطية | Coverage Reporting
```bash
# إنشاء تقرير التغطية | Generate coverage report
./gradlew testDebugUnitTestCoverage

# فتح تقرير التغطية | Open coverage report
open app/build/reports/coverage/debug/index.html
```

## 🔍 تنقيح الاختبارات | Debugging Tests

### تقنيات تنقيح الاختبار | Test Debugging Techniques
```kotlin
@Test
fun debugFailingTest() {
    // إضافة تسجيل مفصل | Add detailed logging
    println("بدء تنفيذ الاختبار | Starting test execution")

    // استخدام نقاط التوقف في IDE | Use breakpoints in IDE
    val result = someOperation()

    // تسجيل القيم الوسيطة | Log intermediate values
    println("النتيجة: $result | Result: $result")

    // التأكيد برسالة مفصلة | Assert with detailed message
    assertEquals("expected", result, "رسالة خطأ مخصصة | Custom error message")
}
```

### مشكلات الاختبار الشائعة | Common Test Issues
1. **الاختبارات المتقلبة**: الاختبارات التي تنجح/تفشل بشكل متقطع | **Flaky Tests**: Tests that pass/fail intermittently
2. **الاختبارات البطيئة**: الاختبارات التي تستغرق وقتًا طويلًا للتنفيذ | **Slow Tests**: Tests taking too long to execute
3. **تسرب الموارد**: الاختبارات التي لا تنظف الموارد | **Resource Leaks**: Tests not cleaning up resources
4. **ظروف السباق**: الاختبارات ذات التبعيات الزمنية | **Race Conditions**: Tests with timing dependencies

## 🚨 أفضل الممارسات | Best Practices

### ✅ افعل | ✅ Do
- كتابة الاختبارات قبل تنفيذ الميزات (TDD) | Write tests before implementing features (TDD)
- استخدام أسماء اختبار وصفية | Use descriptive test names
- اختبار حالات الحافة والظروف الخاطئة | Test edge cases and error conditions
- محاكاة التبعيات الخارجية | Mock external dependencies
- تنظيف بيانات الاختبار بعد الاختبارات | Clean up test data after tests
- استخدام تثبيت الاختبار للبيانات الشائعة | Use test fixtures for common data

### ❌ لا تفعل | ❌ Don't
- كتابة اختبارات تعتمد على الخدمات الخارجية | Write tests that depend on external services
- اختبار الطرق الخاصة مباشرة | Test private methods directly
- تخطي تنظيف الاختبار | Skip test cleanup
- كتابة اختبارات تستغرق أكثر من ثانية واحدة | Write tests that take more than 1 second
- اختبار تفاصيل التنفيذ بدلاً من السلوك | Test implementation details rather than behavior

## 📋 قائمة التحقق من الاختبار | Testing Checklist

### قبل تقديم الكود | Before Submitting Code
- [ ] تم كتابة اختبارات الوحدة للوظائف الجديدة | Unit tests written for new functionality
- [ ] تم تحديث اختبارات التكامل | Integration tests updated
- [ ] تم إضافة اختبارات واجهة المستخدم للشاشات الجديدة | UI tests added for new screens
- [ ] تنجح جميع الاختبارات محليًا | All tests pass locally
- [ ] تغطية الاختبار تلبي المتطلبات | Test coverage meets requirements
- [ ] لا توجد اختبارات متقلبة مكتشفة | No flaky tests detected

### قبل الإصدار | Before Release
- [ ] تنجح جميع الاختبارات على CI/CD | All tests pass on CI/CD
- [ ] تم إكمال اختبارات الأداء | Performance tests completed
- [ ] تم اختبار عبر الأجهزة | Cross-device testing done
- [ ] تم إكمال اختبار الانحدار | Regression testing completed

## 📞 الحصول على المساعدة | Getting Help

- **فشل الاختبارات**: تحقق من سجلات CI/CD للحصول على التفاصيل | **Test Failures**: Check CI/CD logs for details
- **مشكلات التغطية**: استخدم تقارير التغطية لتحديد الفجوات | **Coverage Issues**: Use coverage reports to identify gaps
- **مشاكل الأداء**: تحليل الاختبارات للعثور على الاختناقات | **Performance Problems**: Profile tests to find bottlenecks
- **التنقيح**: استخدم أدوات تنقيح IDE لفشل الاختبارات | **Debugging**: Use IDE debugging tools for test failures

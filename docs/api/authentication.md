# وثائق مصادقة API | API Authentication Documentation

يشرح هذا الملف كيفية عمل المصادقة في API تطبيق إدارة المحل التجاري.

This file explains how authentication works in the Business Management App API.

## طرق المصادقة | Authentication Methods

يدعم API طريقتين رئيسيتين للمصادقة:

The API supports two main authentication methods:

### 1. مصادقة رمز الحامل | Bearer Token Authentication

تتطلب معظم نقاط نهاية API رمز حامل في رأس التفويض:

Most API endpoints require a Bearer token in the Authorization header:

```
Authorization: Bearer <your_token_here>
```

### 2. مصادقة مفتاح API | API Key Authentication

قد تتطلب بعض نقاط النهاية مفتاح API كمعامل استعلام:

Some endpoints may require an API key as a query parameter:

```
GET /api/v1/public-data?api_key=your_api_key_here
```

## الحصول على رموز الوصول | Getting Access Tokens

### نقطة نهاية تسجيل الدخول | Login Endpoint

```http
POST /api/v1/auth/login
Content-Type: application/json

{
  "username": "string",
  "password": "string"
}
```

**الاستجابة | Response:**
```json
{
  "success": true,
  "data": {
    "access_token": "eyJhbGciOiJIUzI1NiIs...",
    "refresh_token": "eyJhbGciOiJIUzI1NiIs...",
    "expires_in": 3600,
    "user": {
      "id": "string",
      "username": "string",
      "role": "string"
    }
  }
}
```

## تحديث الرمز | Token Refresh

لتحديث رمز وصول منتهي الصلاحية:

To refresh an expired access token:

```http
POST /api/v1/auth/refresh
Authorization: Bearer <refresh_token_here>
```

## التحكم في الوصول بناءً على الأدوار | Role-Based Access Control

لدى مستخدمين مختلفي الأدوار صلاحية الوصول لنقاط نهاية مختلفة:

Different user roles have access to different endpoints:

- **المدير | ADMIN**: وصول كامل لجميع نقاط النهاية | Full access to all endpoints
- **مدير الفرع | MANAGER**: وصول لبيانات الفرع والتقارير | Access to branch-specific data and reports
- **الكاشير | CASHIER**: وصول لنقاط البيع والعملاء الأساسية | Access to POS and basic customer operations
- **الموظف | EMPLOYEE**: وصول محدود، خاصة لتتبع الوقت | Limited access, mainly for time tracking

## أفضل ممارسات الأمان | Security Best Practices

1. **تخزين الرموز بشكل آمن** - لا تخزن الرموز في localStorage | **Store tokens securely** - Never store tokens in localStorage
2. **استخدام HTTPS فقط** - يجب أن تستخدم جميع مكالمات API بروتوكول HTTPS في الإنتاج | **Use HTTPS only** - All API calls must use HTTPS in production
3. **تنفيذ انتهاء صلاحية الرمز** - تنتهي صلاحية الرموز بعد ساعة واحدة | **Implement token expiration** - Tokens expire after 1 hour
4. **التحقق من الرموز من جانب الخادم** - تحقق دائمًا من صحة الرمز | **Validate tokens server-side** - Always verify token authenticity
5. **استخدام رموز التحديث** - تنفيذ تدفق تحديث الرمز بشكل صحيح | **Use refresh tokens** - Implement proper token refresh flow

## استجابات الخطأ | Error Responses

### رمز غير صالح | Invalid Token
```json
{
  "success": false,
  "message": "رمز غير صالح أو منتهي الصلاحية | Invalid or expired token",
  "errors": ["TOKEN_EXPIRED"]
}
```

### صلاحيات غير كافية | Insufficient Permissions
```json
{
  "success": false,
  "message": "صلاحيات غير كافية | Insufficient permissions",
  "errors": ["INSUFFICIENT_PERMISSIONS"]
}
```

## تحديد المعدل | Rate Limiting

ينفذ API تحديد المعدل:

The API implements rate limiting:
- 1000 طلب في الساعة لكل مستخدم | 1000 requests per hour per user
- 100 طلب في الدقيقة لكل نقطة نهاية | 100 requests per minute per endpoint

تُدرج رؤوس تحديد المعدل في الاستجابات:

Rate limit headers are included in responses:
```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1609459200
```

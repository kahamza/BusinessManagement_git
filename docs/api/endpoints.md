# وثائق نقاط نهاية API | API Endpoints Documentation

يحتوي هذا الملف على وثائق شاملة لجميع نقاط نهاية API المستخدمة في تطبيق إدارة المحل التجاري.

This file will contain comprehensive documentation of all API endpoints used in the Business Management App.

## نظرة عامة | Overview

يوفر API نقاط نهاية RESTful لـ:

The API provides RESTful endpoints for:
- إدارة العملاء | Customer management
- جرد المنتجات | Product inventory
- المبيعات والطلبات | Sales and orders
- مصادقة المستخدمين | User authentication
- إدارة الفروع | Branch management

## عنوان URL الأساسي | Base URL

```
https://api.businessmanagement.app/v1
```

## المصادقة | Authentication

تتطلب جميع طلبات API مصادقة باستخدام رموز Bearer.

All API requests require authentication using Bearer tokens.

## نقاط النهاية | Endpoints

### المصادقة | Authentication
- `POST /auth/login` - تسجيل دخول المستخدم | User login
- `POST /auth/logout` - تسجيل خروج المستخدم | User logout
- `POST /auth/refresh` - تحديث الرمز | Refresh token

### العملاء | Customers
- `GET /customers` - قائمة العملاء | List customers
- `POST /customers` - إنشاء عميل | Create customer
- `GET /customers/{id}` - تفاصيل العميل | Get customer details
- `PUT /customers/{id}` - تحديث العميل | Update customer
- `DELETE /customers/{id}` - حذف العميل | Delete customer

### المنتجات | Products
- `GET /products` - قائمة المنتجات | List products
- `POST /products` - إنشاء منتج | Create product
- `GET /products/{id}` - تفاصيل المنتج | Get product details
- `PUT /products/{id}` - تحديث المنتج | Update product
- `DELETE /products/{id}` - حذف المنتج | Delete product

## رموز الحالة | Status Codes

- `200` - نجح | Success
- `201` - تم الإنشاء | Created
- `400` - طلب غير صالح | Bad Request
- `401` - غير مصرح | Unauthorized
- `404` - غير موجود | Not Found
- `500` - خطأ داخلي في الخادم | Internal Server Error

## تحديد المعدل | Rate Limiting

طلبات API محدودة بـ 1000 طلب في الساعة لكل مستخدم.

API requests are limited to 1000 requests per hour per user.

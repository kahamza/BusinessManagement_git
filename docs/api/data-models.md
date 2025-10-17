# وثائق نماذج البيانات | Data Models Documentation

يوثق هذا الملف هياكل البيانات المستخدمة في API تطبيق إدارة المحل التجاري.

This file documents the data structures used in the Business Management App API.

## نموذج المستخدم | User Model

```json
{
  "id": "string",
  "username": "string",
  "email": "string",
  "role": "ADMIN|MANAGER|CASHIER|EMPLOYEE",
  "branch_id": "string",
  "is_active": "boolean",
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

## نموذج العميل | Customer Model

```json
{
  "id": "string",
  "name": "string",
  "phone": "string",
  "email": "string",
  "address": "string",
  "debt": "number",
  "loyalty_points": "number",
  "branch_id": "string",
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

## نموذج المنتج | Product Model

```json
{
  "id": "string",
  "name": "string",
  "barcode": "string",
  "price": "number",
  "cost": "number",
  "quantity": "number",
  "category": "string",
  "branch_id": "string",
  "supplier_id": "string",
  "min_stock_level": "number",
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

## نموذج الطلب | Order Model

```json
{
  "id": "string",
  "customer_id": "string",
  "branch_id": "string",
  "items": [
    {
      "product_id": "string",
      "quantity": "number",
      "price": "number",
      "discount": "number"
    }
  ],
  "total_amount": "number",
  "status": "PENDING|CONFIRMED|DELIVERED|CANCELLED",
  "payment_method": "CASH|CARD|DEBT",
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

## تنسيقات الاستجابة | Response Formats

تتبع جميع استجابات API هذا الهيكل:

All API responses follow this structure:

```json
{
  "success": "boolean",
  "data": "object|array",
  "message": "string",
  "errors": "array"
}
```

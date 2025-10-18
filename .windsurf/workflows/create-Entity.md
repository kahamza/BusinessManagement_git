---
description: Create a Room Entity with standard fields for the Business Management App.
---

prompt: |
Create a Room entity for {EntityName}.
Include @Entity annotation, @PrimaryKey, createdAt, updatedAt fields.
Follow naming conventions from .windsurf/rules/naming.rule.

For Business Management App:
- Add branchId field for multi-branch support
- Include soft delete (isDeleted) field
- Add sync status fields for cloud integration
- Use appropriate data types for business data
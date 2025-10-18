---
trigger: manual
---

## Database Rules
Use Room database for local data persistence.

Each entity must have:
- @Entity annotation
- @PrimaryKey field
- createdAt and updatedAt timestamps

All database access should go through DAO interfaces.
Use suspend functions for queries.

For Business Management App:
- Implement multi-branch data isolation in entities
- Add branch_id field to all relevant entities
- Use migrations for schema updates
- Encrypt sensitive data fields

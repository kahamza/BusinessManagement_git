---
trigger: manual
---

## Mapper Rules
All data transformations between layers must use dedicated Mapper classes or extension functions.

Use Mappers to:
  - Convert between Entity and Domain models.
  - Convert between Domain and DTO (network) models.
  - Keep mapping logic simple and stateless.

For Business Management App:
  - Place all mappers under data/mapper package per feature.
  - Use extension functions (e.g., toDomain(), toEntity()).
  - Keep naming consistent: {ModelName}Mapper or extension names matching data type.
  - Handle null safety and default values carefully.
  - Never expose Entity objects directly to UI or Domain layers.

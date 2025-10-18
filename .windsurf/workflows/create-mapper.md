---
description: Generate a Mapper class or extension functions to convert between Entity, Domain, and DTO models.
---

prompt: |
  Generate a Mapper class or Kotlin extension functions for {ModelName}.

  Requirements:
  - Convert between Entity and Domain model
  - Convert between Domain model and DTO (Remote/Network model)
  - Use extension functions: toDomain(), toEntity(), toDto(), fromDto()
  - Keep mapping logic stateless and simple
  - Handle null safety and default values
  - Place the mapper in feature_name/data/mapper/
  - Name file {ModelName}Mapper.kt
  - Do NOT expose Entity objects directly to UI or Domain layers

  For Business Management App:
  - Include branchId for multi-branch support
  - Ensure date/time fields are correctly mapped
  - Apply any data transformations needed for offline-first sync
  - Keep naming conventions consistent with rules
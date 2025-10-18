---
description: Generate a Use Case in the Domain layer with full error handling and multi-branch support.
---

prompt: |
Create a new Use Case class for {UseCaseName} in the Domain layer.
Follow Clean Architecture and SOLID principles.

Steps:
- Place Use Case in feature_name/domain/usecase/
- Handle all errors using Result type:
  ```kotlin
  sealed class Result<out T> {
      data class Success<T>(val data: T): Result<T>()
      data class Error(val message: String): Result<Nothing>()
  }
  ```
- Inject required Repository interfaces.
- Support branch-specific logic and role-based access.
- Provide suspend functions for asynchronous operations.
- Include example usage in ViewModel.

Rules:
- Follow business_management.rules and naming conventions.
- Ensure consistency with Repository and Mapper structures.
- All Kotlin, no XML.
- Support Arabic (RTL) and English strings.

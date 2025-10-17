# Branch ID Type Migration Guide

## Overview
This document outlines the changes made to migrate the `branchId` type from `Int` to `Long` throughout the application. This change was implemented to ensure consistency and prevent potential integer overflow issues as the number of branches grows.

## Affected Components

### 1. Data Models
- `Branch`
- `Employee`
- `BranchRole`
- `BranchRoleAssignment`

### 2. Data Access Layer
- `BranchDao`
- `EmployeeDao`
- `BranchRepository`
- `EmployeeRepository`

### 3. Domain Layer
- All Employee-related use cases
- All Branch-related use cases

### 4. UI Layer
- ViewModels
- UI Models
- Screens and Composables

## Key Changes

### Data Models
Updated all models to use `Long` for `branchId`:

```kotlin
// Before
data class Branch(
    val id: Int,
    val branchId: Int,  // Old
    // ...
)

// After
data class Branch(
    val id: Long,
    val branchId: Long,  // Updated to Long
    // ...
)
```

### Repository Layer
Updated repository interfaces and implementations to handle `Long` branch IDs:

```kotlin
// Before
interface BranchRepository {
    suspend fun getBranchById(id: Int): Branch?
    fun getBranches(): Flow<List<Branch>>
}

// After
interface BranchRepository {
    suspend fun getBranchById(id: Long): Branch?
    fun getBranches(): Flow<List<Branch>>
}
```

### Use Cases
Updated all use cases to accept and return `Long` branch IDs:

```kotlin
class GetBranchUseCase @Inject constructor(
    private val repository: BranchRepository
) {
    suspend operator fun invoke(branchId: Long): Branch? =
        repository.getBranchById(branchId)
}
```

## Migration Notes

### Database Migration
If you're using Room database, ensure you've created a proper migration if the database schema has changed. Example:

```kotlin
val MIGRATION_1_2 = object : Migration(1, 2) {
    override fun migrate(database: SupportSQLiteDatabase) {
        // Handle schema changes if needed
    }
}

@Database(
    entities = [Branch::class, Employee::class],
    version = 2,  // Incremented version
    exportSchema = true
)
@TypeConverters(Converters::class)
abstract class AppDatabase : RoomDatabase() {
    // ...
}
```

### Testing
When writing tests, ensure you're using `Long` values for branch IDs:

```kotlin
@Test
fun `get branch by id should return correct branch`() = runTest {
    // Given
    val branchId = 1L  // Note the 'L' suffix for Long
    val expectedBranch = Branch(id = branchId, name = "Test Branch")
    
    // When
    // ... test implementation
    
    // Then
    // ... assertions
}
```

## Best Practices

1. **Consistent Types**: Always use `Long` for IDs throughout the application.
2. **Type Safety**: Be explicit with number types to avoid implicit conversions.
3. **Documentation**: Document any type conversions that are necessary.
4. **Testing**: Update all tests to use the correct types.

## Future Considerations

1. Consider using a `@JvmInline value class` for type-safe IDs in the future.
2. Add validation for ID values to ensure they're within expected ranges.
3. Consider using a database migration testing framework to catch type-related issues early.

## Troubleshooting

If you encounter any issues:

1. Check for any remaining `Int` usages of `branchId` in the codebase.
2. Verify that all database operations handle the `Long` type correctly.
3. Ensure all mappers and converters are updated to handle the type change.
4. Check for any hardcoded IDs in tests or mocks that might need updating.

## Related Documentation

- [Kotlin Documentation - Basic Types](https://kotlinlang.org/docs/basic-types.html)
- [Room Database Migrations](https://developer.android.com/training/data-storage/room/migrating-db-versions)
- [Android Room with a View - Kotlin](https://developer.android.com/codelabs/android-room-with-a-view-kotlin)

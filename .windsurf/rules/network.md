---
trigger: manual
---

## Network Rules
All remote data must use Retrofit + OkHttp + Kotlinx Serialization.

Never make network calls directly in ViewModels.
Create a RemoteDataSource class for each module that handles API operations.

For Business Management App:
- Use n8n or Firebase for cloud sync
- Implement authentication headers for API calls
- Handle offline queue for network operations
- Compress data for efficient transmission

## Error Handling
- Identify common errors: NetworkTimeout, ServerError, Unauthorized.
- Implement safeApiCall with automatic retries.
- Store failed requests for offline retry.

## Offline Support
- Queue requests when offline and sync when online.
- Display user-friendly error messages (Arabic + English).

## Best Practices
- Never make network calls directly in ViewModel.
- Use RemoteDataSource layer for all API interactions.
- Compress data for efficient transmission.


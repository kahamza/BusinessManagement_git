---
description: Build a repository class with offline-first and sync-ready logic.
---

prompt: |
Generate a Repository class for {FeatureName}.
Inject DAO and RemoteDataSource.
Provide suspend functions for all CRUD operations.

For Business Management App:
- Filter data by current branch and user role
- Implement offline caching and sync
- Handle data conflicts in multi-branch scenarios
- Add audit logging for sensitive operations
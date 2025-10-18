---
trigger: manual
---

## Architecture Rules
Always use Clean Architecture with the following layers:
- data (Room entities, DAO, repositories)
- domain (use cases, models)
- presentation (viewmodels, ui)

Each feature should have its own package:
feature_name/data, feature_name/domain, feature_name/presentation

Always inject dependencies using Hilt.
Follow MVVM pattern strictly.

For Business Management App:
- Use Kotlin exclusively for all development
- Implement role-based access control (General Manager, Branch Manager, Employee)
- Ensure all data operations support multi-branch isolation
- Integrate cloud sync for offline-first architecture

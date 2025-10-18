---
trigger: manual
---

## Compose Rules
Follow these UI guidelines:
- All Composables should start with capital letter.
- Pass state and events as parameters.
- Avoid using mutableStateOf directly in UI components.
- Use rememberSaveable for states that should persist across configuration changes.

For Business Management App:
- Use RTL-aware layouts for Arabic support
- Implement dynamic theming based on user preferences
- Use LazyColumn for long lists (e.g., product lists, customer lists)
- Add loading and error states for all screens

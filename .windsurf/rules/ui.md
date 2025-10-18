---
trigger: manual
---

## UI Rules
All UI must be built with Jetpack Compose. Do not use XML layouts.

Follow Material 3 design principles.
Use reusable components whenever possible.
Each screen should have:
- a ViewModel
- a Scaffold
- a top bar with title
- a content section

Use StateFlow or LiveData to observe UI state.

For Business Management App:
- Support Arabic (RTL) and English languages
- Implement accessibility features (screen reader, keyboard navigation)
- Use consistent color schemes and typography
- Ensure responsive design for different screen sizes
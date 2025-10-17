# 🤝 How to Contribute

We're excited that you're interested in contributing to the Business Management App! This guide will help you get started with contributing to the project.

## 📋 Table of Contents
- [Code of Conduct](#-code-of-conduct)
- [Getting Started](#-getting-started)
- [Development Workflow](#-development-workflow)
- [Code Style](#-code-style)
- [Pull Request Process](#-pull-request-process)
- [Reporting Issues](#-reporting-issues)
- [Feature Requests](#-feature-requests)
- [Code Review Guidelines](#-code-review-guidelines)
- [Documentation](#-documentation)
- [Community](#-community)

## 👥 Code of Conduct

Please read our [Code of Conduct](02-code-of-conduct.md) before contributing. We are committed to providing a friendly, safe, and welcoming environment for all contributors.

## 🚀 Getting Started

### Prerequisites
- Basic knowledge of Git and GitHub
- Android Studio (latest stable version)
- JDK 11 or later
- Android SDK

### First Time Setup
1. Fork the repository
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/BusinessManagement.git
   cd BusinessManagement
   ```
3. Set up the project in Android Studio
4. Sync the project with Gradle files
5. Run the app to verify the setup

### Branch Naming Convention
Use the following format for branch names:
```
<type>/<ticket-number>-<short-description>
```

**Types:**
- `feature/` - New features or enhancements
- `bugfix/` - Bug fixes
- `hotfix/` - Critical production fixes
- `chore/` - Maintenance tasks
- `docs/` - Documentation updates

Example: `feature/42-add-login-screen`

## 🔄 Development Workflow

### 1. Keep Your Fork Updated
```bash
git remote add upstream https://github.com/organization/BusinessManagement.git
git fetch upstream
git checkout main
git merge upstream/main
```

### 2. Create a New Branch
```bash
git checkout -b type/description
```

### 3. Make Your Changes
- Write clean, well-documented code
- Follow the code style guidelines
- Write unit tests for new features
- Update documentation as needed

### 4. Commit Your Changes
```bash
git add .
git commit -m "type(scope): concise description of changes"
```

### 5. Push to Your Fork
```bash
git push origin your-branch-name
```

### 6. Create a Pull Request
1. Go to the [repository's pull requests](https://github.com/organization/BusinessManagement/pulls)
2. Click "New Pull Request"
3. Select your fork and branch
4. Fill out the PR template
5. Request reviews from team members

## 🎨 Code Style

### Kotlin Style Guide
We follow the [Kotlin Coding Conventions](https://kotlinlang.org/docs/coding-conventions.html) with the following additions:

#### Naming
- Use camelCase for variables, functions, and properties
- Use PascalCase for class names and enums
- Use UPPER_SNAKE_CASE for constants
- Prefix boolean variables with is/has/should (e.g., `isEnabled`, `hasItems`)

#### Formatting
- Use 4 spaces for indentation
- Maximum line length: 100 characters
- Use trailing commas in multi-line declarations
- Use string templates instead of concatenation

#### Functions
- Keep functions small and focused (max 20-30 lines)
- Use default arguments instead of function overloading
- Use expression functions for simple getters and setters

### XML Style Guide
- Use `snake_case` for resource IDs
- Prefix custom views with the app name (e.g., `bm_button_primary`)
- Organize attributes by category (layout, style, etc.)
- Use `tools:` namespace for preview attributes

## 🔍 Code Quality

### Static Analysis
We use the following tools to maintain code quality:
- **ktlint** - Code style enforcement
- **detekt** - Static code analysis
- **Android Lint** - Android-specific checks

To run checks locally:
```bash
./gradlew ktlintCheck
detekt
./gradlew lint
```

### Testing
- Write unit tests for all new features
- Aim for at least 70% code coverage
- Use descriptive test names
- Follow the Given-When-Then pattern

## 🔄 Pull Request Process

### PR Guidelines
- Keep PRs small and focused on a single feature/bug
- Reference related issues in the PR description
- Ensure all tests pass
- Update documentation as needed
- Request reviews from at least one team member

### PR Template
```markdown
## Description

[Brief description of the changes]

## Related Issues

- Fixes #issue_number
- Related to #issue_number

## Type of Change

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Refactoring

## Checklist

- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published

## Screenshots/Videos

[If applicable, add screenshots or videos to help explain your changes]
```

## 🐛 Reporting Issues

### Before Submitting an Issue
1. Check if the issue has already been reported
2. Try to reproduce the issue with the latest version
3. Gather as much information as possible

### Issue Template
```markdown
## Description

[Clear and concise description of the issue]

## Steps to Reproduce

1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

## Expected Behavior

[What you expected to happen]

## Actual Behavior

[What actually happened]

## Environment

- App Version: [e.g., 1.0.0]
- Android Version: [e.g., Android 11]
- Device: [e.g., Google Pixel 5]

## Additional Context

[Add any other context about the problem here]
```

## 💡 Feature Requests

### Before Submitting a Feature Request
1. Check if the feature has already been requested
2. Consider if the feature aligns with the project's goals

### Feature Request Template
```markdown
## Description

[Clear and concise description of the feature]

## Problem Statement

[Explain the problem this feature would solve]

## Proposed Solution

[Describe the solution you'd like]

## Alternatives Considered

[Describe any alternative solutions you've considered]

## Additional Context

[Add any other context or screenshots about the feature request]
```

## 👀 Code Review Guidelines

### Reviewing PRs
- Be respectful and constructive
- Focus on the code, not the person
- Suggest improvements with explanations
- Acknowledge good practices
- Check for:
  - Code quality and style
  - Performance implications
  - Security considerations
  - Test coverage
  - Documentation updates

### Responding to Reviews
- Thank reviewers for their time
- Address all comments
- Ask for clarification if needed
- Push changes as new commits (don't squash until the end)

## 📚 Documentation

### Writing Documentation
- Use clear and concise language
- Include code examples where helpful
- Keep documentation up-to-date
- Use Markdown formatting

### Documenting Code
- Document public APIs with KDoc
- Include parameter and return value descriptions
- Add examples for complex functions
- Document edge cases and exceptions

## 🌐 Community

### Getting Help
- Check the [documentation](https://github.com/organization/BusinessManagement/docs)
- Search existing issues
- Ask in the community forum
- Join our [Discord/Slack](link-to-community)

### Community Guidelines
- Be respectful and inclusive
- Help others when possible
- Follow the code of conduct
- Report any inappropriate behavior

## 🎉 Your First Contribution

Looking for your first contribution? Check out issues labeled `good first issue` or `help wanted` in the issue tracker.

## 🙏 Thank You!

Thank you for taking the time to contribute to the Business Management App! Your contributions help make this project better for everyone.

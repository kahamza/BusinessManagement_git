# دليل سير عمل Git | Git Workflow Guide

يشرح هذا المستند سير عمل Git وأفضل الممارسات للمساهمة في تطبيق إدارة المحل التجاري.

This document explains the Git workflow and best practices for contributing to the Business Management App.

## 🌊 استراتيجية الفروع | Branch Strategy

### الفروع الرئيسية | Main Branches
- **`main`**: الكود جاهز للإنتاج، الإصدارات المستقرة | **Production-ready code, stable releases**
- **`develop`**: فرع التكامل للميزات، يجب أن يكون قابل للنشر دائمًا | **Integration branch for features, always deployable**

### فروع الميزات | Feature Branches
- **التسمية**: `feature/feature-name` (مثال: `feature/online-ordering`) | **Naming**: `feature/feature-name` (e.g., `feature/online-ordering`)
- **النطاق**: ميزة واحدة لكل فرع | **Scope**: One feature per branch
- **العمر**: قصير الأمد، دمج سريع | **Lifetime**: Short-lived, merged quickly

### فروع إصلاح الأخطاء | Bugfix Branches
- **التسمية**: `bugfix/issue-description` (مثال: `bugfix/crash-on-startup`) | **Naming**: `bugfix/issue-description` (e.g., `bugfix/crash-on-startup`)
- **النطاق**: إصلاح خطأ واحد | **Scope**: Single bug fix
- **الأساس**: التفرع من `develop` أو فرع الإصدار | **Base**: Branch from `develop` or release branch

### فروع الإصلاحات الساخنة | Hotfix Branches
- **التسمية**: `hotfix/version-description` (مثال: `hotfix/1.2.1-login-fix`) | **Naming**: `hotfix/version-description` (e.g., `hotfix/1.2.1-login-fix`)
- **النطاق**: إصلاحات حرجة للإنتاج | **Scope**: Critical production fixes
- **الأساس**: التفرع من `main` | **Base**: Branch from `main`

## 🔄 سير عمل التطوير | Development Workflow

### 1. بدء ميزة جديدة | Start New Feature
```bash
# إنشاء والتبديل إلى فرع الميزة | Create and switch to feature branch
git checkout -b feature/new-feature-name

# أو من develop | Or from develop
git checkout develop
git pull origin develop
git checkout -b feature/new-feature-name
```

### 2. تطوير الميزة | Develop Feature
```bash
# إجراء التغييرات والالتزام بانتظام | Make changes and commit regularly
git add .
git commit -m "feat: add new feature description"

# دفع فرع الميزة | Push feature branch
git push origin feature/new-feature-name
```

### 3. إنشاء طلب سحب | Create Pull Request
- **العنوان**: واضح ووصفي | **Title**: Clear, descriptive title
- **الوصف**: ما، ولماذا، وكيف | **Description**: What, why, and how
- **لقطات الشاشة**: تضمينها إذا كانت تغييرات واجهة المستخدم | **Screenshots**: Include if UI changes
- **الاختبارات**: ذكر تغطية الاختبار | **Tests**: Mention test coverage

### 4. عملية مراجعة الكود | Code Review Process
- **المراجعون**: طلب مراجعة من أعضاء الفريق ذوي الصلة | **Reviewers**: Request review from relevant team members
- **CI/CD**: يجب أن تنجح جميع الفحوصات | **CI/CD**: All checks must pass
- **الموافقة**: الحد الأدنى 2 موافقات مطلوبة | **Approval**: Minimum 2 approvals required

### 5. عملية الدمج | Merge Process
```bash
# الدمج في develop (squash أو rebase) | Merge to develop (squash or rebase)
git checkout develop
git merge --no-ff feature/new-feature-name

# الدفع إلى الأصل | Push to origin
git push origin develop
```

## 📝 معايير رسائل الالتزام | Commit Message Standards

### التنسيق | Format
```
type(scope): description

[optional body]

[optional footer]
```

### الأنواع | Types
- **feat**: ميزة جديدة | **New feature**
- **fix**: إصلاح خطأ | **Bug fix**
- **docs**: تغييرات التوثيق | **Documentation changes**
- **style**: تغييرات نمط الكود (التنسيق، إلخ) | **Code style changes (formatting, etc.)**
- **refactor**: إعادة هيكلة الكود | **Code refactoring**
- **test**: إضافة أو تحديث الاختبارات | **Adding or updating tests**
- **chore**: مهام الصيانة | **Maintenance tasks**

### الأمثلة | Examples
```bash
# ✅ جيد | Good
feat(auth): add biometric authentication support

fix(pos): resolve crash when printing receipts

docs(api): update endpoint documentation

# ❌ تجنب | Avoid
"Fixed stuff"

"Added feature"

"Updated code"
```

## 🔀 إرشادات طلبات السحب | Pull Request Guidelines

### عنوان طلب السحب | PR Title
- واضح ووصفي | Clear and descriptive
- ابدأ بنوع الميزة/الإصلاح | Start with feature/fix type
- تضمين رقم المشكلة إن أمكن | Include issue number if applicable

### قالب وصف طلب السحب | PR Description Template
```markdown
## الوصف | Description
وصف موجز لما يحققه طلب السحب هذا.

Brief description of what this PR accomplishes.

## التغييرات المُجراة | Changes Made
- التغيير 1 | Change 1
- التغيير 2 | Change 2
- التغيير 3 | Change 3

## الاختبار | Testing
- [ ] تم إضافة/تحديث اختبارات الوحدة | Unit tests added/updated
- [ ] تنجح اختبارات التكامل | Integration tests pass
- [ ] تم إكمال الاختبار اليدوي | Manual testing completed

## لقطات الشاشة | Screenshots
[تضمين لقطات الشاشة لتغييرات واجهة المستخدم | Include screenshots for UI changes]

## المشكلات ذات الصلة | Related Issues
إغلاق #123 | Closes #123

## قائمة التحقق | Checklist
- [ ] يتبع الكود معايير المشروع | Code follows project standards
- [ ] تنجح الاختبارات | Tests pass
- [ ] تم تحديث التوثيق | Documentation updated
- [ ] تمت مراجعة الأمان | Security review completed
```

## 👥 سير عمل الفريق | Team Workflow

### التطوير اليومي | Daily Development
1. **بدء اليوم**: سحب أحدث التغييرات | **Start Day**: Pull latest changes
   ```bash
   git checkout develop
   git pull origin develop
   ```

2. **العمل**: إنشاء فرع ميزة، تنفيذ، التزام منتظم | **Work**: Create feature branch, implement, commit regularly

3. **نهاية اليوم**: دفع التغييرات، تحديث الفريق بالتقدم | **End Day**: Push changes, update team on progress

### العملية الأسبوعية | Weekly Process
- **الاثنين**: تخطيط مهام السبرينت | **Monday**: Plan sprint tasks
- **الأربعاء**: فحص منتصف السبرينت | **Wednesday**: Mid-sprint check-in
- **الجمعة**: عرض الميزات المكتملة | **Friday**: Demo completed features

### عملية الإصدار | Release Process
1. **تجميد الميزات**: إيقاف الميزات الجديدة قبل الإصدار | **Feature Freeze**: Stop new features before release
2. **الاختبار**: مرحلة اختبار شاملة | **Testing**: Comprehensive testing phase
3. **المرحلة**: النشر في بيئة المرحلة | **Staging**: Deploy to staging environment
4. **الإنتاج**: الإصدار لمتاجر الإنتاج | **Production**: Release to production stores
5. **نافذة الإصلاحات الساخنة**: مراقبة المشكلات الفورية | **Hotfix Window**: Monitor for immediate issues

## 🛠️ أفضل ممارسات Git | Git Best Practices

### الحفاظ على الفروع نظيفة | Keeping Branches Clean
```bash
# إعادة أساس فرع الميزة على أحدث develop | Rebase feature branch on latest develop
git checkout feature/my-feature
git rebase develop

# إعادة أساس تفاعلي للتنظيف | Interactive rebase for cleanup
git rebase -i develop
```

### معالجة تعارضات الدمج | Handling Merge Conflicts
1. **سحب أحدث التغييرات**: `git pull origin develop` | **Pull latest changes**: `git pull origin develop`
2. **حل التعارضات**: تحرير الملفات المتعارضة | **Resolve conflicts**: Edit conflicting files
3. **مرحلة الملفات المحلولة**: `git add .` | **Stage resolved files**: `git add .`
4. **إكمال الدمج**: `git commit` أو `git rebase --continue` | **Complete merge**: `git commit` or `git rebase --continue`

### تنظيف الفروع | Cleaning Up Branches
```bash
# حذف فروع الميزات المدمجة | Delete merged feature branches
git branch -d feature/completed-feature

# حذف الفروع البعيدة | Delete remote branches
git push origin --delete feature/completed-feature
```

## 🔧 أدوات التطوير | Development Tools

### إعداد IDE | IDE Setup
- **أندرويد ستوديو**: أركتيك فوكس أو أحدث | **Android Studio**: Arctic Fox or later
- **تكامل Git**: تمكين Git في أندرويد ستوديو | **Git Integration**: Enable Git in Android Studio
- **نمط الكود**: استيراد `.editorconfig` المشروع | **Code Style**: Import project `.editorconfig`

### أدوات سطر الأوامر | Command Line Tools
```bash
# أسماء مستعارة Git مفيدة | Useful git aliases
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
```

## 🚨 الإجراءات الطارئة | Emergency Procedures

### إصلاح خطأ حرج | Critical Bug Fix
1. **إنشاء فرع إصلاح ساخن**: `git checkout -b hotfix/critical-bug` | **Create hotfix branch**: `git checkout -b hotfix/critical-bug`
2. **إصلاح المشكلة**: تنفيذ واختبار الإصلاح | **Fix issue**: Implement and test fix
3. **النشر الفوري**: دمج في main والإصدار | **Deploy immediately**: Merge to main and release
4. **التراجع الخلفي**: دمج الإصلاح في فرع develop | **Backport**: Merge fix to develop branch

### مشكلة أمنية | Security Issue
1. **الإجراء الفوري**: تقييم التأثير والنطاق | **Immediate action**: Assess impact and scope
2. **فرع الإصلاح الساخن**: إنشاء إذا لزم الإصلاح الفوري | **Hotfix branch**: Create if immediate fix needed
3. **الاتصال**: إخطار الفريق وأصحاب المصلحة | **Communication**: Notify team and stakeholders
4. **خطة الإصدار**: تنسيق إصدار تحديث الأمان | **Release plan**: Coordinate security update release

## 📊 المراقبة والمقاييس | Monitoring and Metrics

### مقاييس جودة الكود | Code Quality Metrics
- **تغطية الاختبار**: الحد الأدنى 80% | **Test Coverage**: Minimum 80%
- **تكرار الكود**: أقل من 5% | **Code Duplication**: Less than 5%
- **الدين التقني**: مراقب ومدار | **Technical Debt**: Monitored and managed

### مقاييس العملية | Process Metrics
- **الوقت للدمج**: متوسط 2-3 أيام للميزات | **Time to Merge**: Average 2-3 days for features
- **وقت استجابة المراجعة**: في غضون 24 ساعة | **Review Response Time**: Within 24 hours
- **تكرار الإصدار**: كل 2-4 أسابيع | **Release Frequency**: Every 2-4 weeks

## 📚 الموارد | Resources

- **توثيق Git**: https://git-scm.com/docs | **Git Documentation**: https://git-scm.com/docs
- **تدفق GitHub**: https://guides.github.com/introduction/flow/ | **GitHub Flow**: https://guides.github.com/introduction/flow/
- **الإصدار الدلالي**: https://semver.org/ | **Semantic Versioning**: https://semver.org/
- **الالتزامات التقليدية**: https://conventionalcommits.org/ | **Conventional Commits**: https://conventionalcommits.org/

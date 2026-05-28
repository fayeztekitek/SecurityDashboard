# Contributing to Security Governance Dashboard

Thank you for your interest in improving the Security Governance Dashboard! This document provides guidelines for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Pull Request Process](#pull-request-process)

---

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors.

### Expected Behavior

- Use welcoming and inclusive language
- Be respectful of differing opinions and experiences
- Accept constructive criticism gracefully
- Focus on what is best for the community and project
- Show empathy towards other community members

### Unacceptable Behavior

- Harassment of any kind
- Trolling or insulting/derogatory comments
- Personal or political attacks
- Public or private harassment
- Publishing others' private information
- Other conduct which could reasonably be considered inappropriate

---

## Getting Started

### Prerequisites

- Git knowledge (basic understanding)
- Web browser for testing
- Text editor (VS Code, Sublime, etc.)
- Python 3.8+ (for data extraction scripts)

### Development Setup

```bash
# Clone the repository
git clone https://github.com/vermeg/security-governance-dashboard.git
cd security-governance-dashboard

# Create a feature branch
git checkout -b feature/your-feature-name

# Make your changes
# Test thoroughly
# Commit and push (see Submitting Changes below)
```

---

## How to Contribute

### 1. Reporting Bugs

**Before reporting a bug:**
- Check existing issues to avoid duplicates
- Test with the latest version
- Gather as much information as possible

**When reporting:**
- Use the bug report template
- Include browser and OS information
- Provide steps to reproduce
- Share error messages from browser console (F12)
- Attach anonymized sample data if data-related

### 2. Suggesting Features

**Before suggesting:**
- Check existing feature requests
- Consider how it aligns with the dashboard's purpose
- Think about the effort required

**When suggesting:**
- Use the feature request template
- Explain the use case clearly
- Describe expected behavior
- Provide concrete examples
- Suggest implementation approach (if you have ideas)

### 3. Improving Documentation

Documentation improvements are always welcome!

- Fix typos or grammar
- Clarify confusing sections
- Add examples
- Update outdated information
- Add missing sections

**To contribute:**
1. Edit the `.txt` or `.md` files directly
2. Test that changes are clear and accurate
3. Submit as pull request with "docs:" prefix

### 4. Enhancing the Dashboard

**Code contributions welcome for:**
- Bug fixes
- Performance improvements
- New KPI calculations
- Additional charts/visualizations
- Enhanced export formats
- Better data validation

**Code not accepted for:**
- Modifications that break READONLY contract
- Changes that require external databases
- Complex frameworks (stay lightweight)
- Proprietary dependencies

---

## Development Workflow

### Branch Naming Convention

```
feature/dashboard-improvements      # New features
bugfix/import-csv-error            # Bug fixes
docs/update-readme                 # Documentation
refactor/chart-initialization      # Code refactoring
perf/optimize-large-datasets       # Performance improvements
```

### Commit Message Guidelines

```
[TYPE] Brief description (50 chars max)

Detailed explanation if needed (wrap at 72 chars).

Fixes #123
Related to #456
```

**Types:**
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `style:` Code style (no functional change)
- `refactor:` Code restructuring
- `perf:` Performance improvement
- `test:` Adding tests
- `chore:` Maintenance tasks

**Examples:**
```
feat: Add drill-down vulnerability details

- Click on vulnerability to see full details
- Show remediation history timeline
- Display compensating controls

Fixes #42
```

```
fix: CSV import fails with special characters in owner names

Root cause: CSV parser doesn't handle quoted fields correctly
Solution: Use proper CSV parsing with quote handling

Fixes #89
Related to #85
```

---

## Coding Standards

### HTML/CSS Standards

**Formatting:**
- Use 4-space indentation
- Use semantic HTML5 elements
- Use CSS Grid/Flexbox for layouts
- Mobile-first responsive design

**Naming:**
- CSS classes: `kebab-case` (.kpi-card, .rag-status)
- IDs: `kebab-case` (#overview, #critical-table)
- Meaningful names (no .class1, .section-a, etc.)

**Colors:**
- Use CSS variables for all colors
- Define in `:root` section
- Use consistent naming

### JavaScript Standards

**Formatting:**
- Use 4-space indentation
- Use `const` by default, `let` if needed
- Avoid global variables
- Use modern ES6+ syntax

**Naming:**
- `camelCase` for variables and functions
- `PascalCase` for classes
- Meaningful names (no single letters except loops)

**Functions:**
- Keep functions focused (single responsibility)
- Add comments for complex logic
- Use descriptive function names

**Data:**
```javascript
// Good
const calculateSLACompliance = (issues) => {
    const overdue = issues.filter(v => parseInt(v.Days_Overdue) > 0);
    return ((issues.length - overdue.length) / issues.length) * 100;
};

// Avoid
const calc = (i) => { /* ... */ };
const a = (b) => { /* ... */ };
```

### Python Standards (extraction scripts)

**Code Style:**
- PEP 8 compliant
- Type hints for function parameters
- Docstrings for all functions
- Comments for complex logic

```python
def extract_vulnerabilities(
    base_url: str,
    token: str,
    days: int = 90
) -> List[Dict[str, Any]]:
    """
    Extract vulnerability data from Fortify SSC.
    
    Args:
        base_url: Fortify SSC base URL
        token: API authentication token
        days: Number of days to look back (default 90)
    
    Returns:
        List of vulnerability dictionaries
    
    Raises:
        RequestException: If API call fails
    """
    # Implementation here
    pass
```

---

## Testing

### Manual Testing

**Before submitting:**

1. **Load Testing**
   - Test with sample_vulnerabilities.csv ✓
   - Test with 5 vulnerabilities ✓
   - Test with 1000+ vulnerabilities ✓

2. **Data Import**
   - Try import with your CSV ✓
   - Verify all columns map correctly ✓
   - Check for data validation errors ✓

3. **Navigation**
   - Click all sidebar sections ✓
   - Verify section loads correctly ✓
   - Check responsive mobile view ✓

4. **Charts**
   - Verify all charts render ✓
   - Test with different data sizes ✓
   - Check legends and labels ✓

5. **Tables**
   - Verify all columns visible ✓
   - Check data accuracy ✓
   - Test sorting/filtering (if added) ✓

6. **Browser Testing**
   - Chrome/Chromium ✓
   - Firefox ✓
   - Safari (if on Mac) ✓
   - Mobile browser ✓

### Code Review

Your changes will be reviewed for:
- Functionality and correctness
- Code quality and readability
- Performance impact
- Backward compatibility
- Documentation completeness
- Security considerations

---

## Submitting Changes

### Step 1: Create Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### Step 2: Make Changes

- Make focused, logical commits
- Write clear commit messages
- Test thoroughly
- Update documentation

### Step 3: Commit Changes

```bash
git add .
git commit -m "feat: Add drill-down vulnerability view

- Show full vulnerability details on click
- Display remediation history
- Add compensating controls info"
```

### Step 4: Push to GitHub

```bash
git push origin feature/your-feature-name
```

### Step 5: Open Pull Request

Go to GitHub and create Pull Request:
- Clear title and description
- Link related issues
- Mention any breaking changes
- Include testing checklist

---

## Pull Request Process

### PR Title Format

```
[FEATURE] Add feature name
[BUGFIX] Fix description of bug
[DOCS] Update documentation
[PERF] Optimize data processing
```

### PR Description Template

```markdown
## Description
Brief description of changes.

## Related Issues
Fixes #123
Related to #456

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Breaking change

## Changes Made
- Change 1
- Change 2
- Change 3

## Testing Performed
- [ ] Tested with sample data
- [ ] Tested with large dataset (1000+)
- [ ] Tested in Chrome
- [ ] Tested in Firefox
- [ ] Tested on mobile
- [ ] Verified no errors in console

## Screenshots (if applicable)
[Screenshots before/after]

## Breaking Changes
[Describe any breaking changes, if any]

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation is updated
- [ ] Tests pass (if applicable)
- [ ] No new warnings in console
- [ ] Backward compatible
```

### Review Process

1. **Automated Checks**
   - Code style validation
   - File size checks
   - Link validation

2. **Maintainer Review**
   - Code quality assessment
   - Functionality verification
   - Performance impact evaluation
   - Security review

3. **Testing**
   - Manual testing in multiple browsers
   - Testing with various data sizes
   - Edge case validation

4. **Approval & Merge**
   - Maintainer approval required
   - Automated tests pass
   - No conflicts with main branch
   - Then merged to main

---

## Community

### Questions?

- GitHub Issues: Ask questions using issue templates
- Discussions: Start a GitHub Discussion
- Email: security-governance@vermeg.com

### Recognition

Contributors will be recognized in:
- GitHub contributors page
- Release notes
- Project README

---

## License

By contributing, you agree that your contributions will be licensed under the same terms as the project (Internal Use License).

---

## Questions or Need Help?

- Check existing issues and discussions
- Review documentation files
- Contact Security Governance Team
- Open a new issue with your question

---

**Thank you for contributing to improving Security Governance Dashboard!** 🙏


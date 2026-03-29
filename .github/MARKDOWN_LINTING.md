# Markdown Linting Guide

## Overview

This vault uses **Markdownlint** to maintain consistent formatting across all Markdown files.

Linting is automatically checked on every push via GitHub Actions. Local linting is recommended before pushing.

---

## Installation (Local)

### macOS / Linux

```bash
npm install -g markdownlint-cli
```

### Fedora / RHEL

```bash
sudo dnf install -y nodejs npm
npm install -g markdownlint-cli
```

### Windows (PowerShell)

```powershell
npm install -g markdownlint-cli
```

---

## Usage

### Check all files

```bash
markdownlint . --config .markdownlintrc.json
```

### Check specific file

```bash
markdownlint "10_Patologias/01_Cardio/FA.md" --config .markdownlintrc.json
```

### Fix automatically (when possible)

```bash
markdownlint . --config .markdownlintrc.json --fix
```

---

## Configuration

Rules are defined in `.markdownlintrc.json`:

| Rule | Setting | Purpose |
|------|---------|---------|
| MD003 | consistent | Consistent heading style (# not ##) |
| MD004 | consistent | Consistent list indentation (2 spaces) |
| MD013 | 120 chars | Max line length (except code blocks) |
| MD025 | false | Allow multiple H1 headings |
| MD033 | false | Allow HTML (for Obsidian compatibility) |
| MD024 | false | Allow duplicate heading names |
| MD041 | false | Don't require H1 as first line |
| MD045 | false | Image alt text not required |

---

## Common Issues & Fixes

### ❌ MD003: Inconsistent heading style

```markdown
# Heading 1
## Heading 2
### heading 3  ← Wrong: should be ### Heading 3
```

**Fix:** Capitalize first letter after `#`:
```markdown
### Heading 3  ✅
```

---

### ❌ MD004: Inconsistent list indentation

```markdown
- Item 1
  - Subitem 1    ← 2 spaces (correct)
   - Subitem 2   ← 1 space (wrong)
```

**Fix:** Use 2 spaces for sub-lists:
```markdown
- Item 1
  - Subitem 1  ✅
  - Subitem 2  ✅
```

---

### ❌ MD013: Line too long

```markdown
This is a very long line that exceeds 120 characters and will trigger the linter because it's not a code block
```

**Fix:** Break into multiple lines:
```markdown
This is a very long line that exceeds 120 characters
and will trigger the linter because it's not a code block
```

Or disable for that line:
```markdown
<!-- markdownlint-disable MD013 -->
This very long line is exempted from linting
<!-- markdownlint-enable MD013 -->
```

---

### ❌ MD034: Bare URL used

```markdown
Visit https://ejemplo.com for more info
```

**Fix:** Use proper link syntax:
```markdown
Visit [this resource](https://ejemplo.com) for more info
```

---

## GitHub Actions Integration

Linting runs automatically on:
- Every push to `main`
- Every pull request

### If linting fails:

1. **See error in GitHub Actions logs:**
   ```
   ❌ 10_Patologias/01_Cardio/FA.md:15:1 MD003 [inconsistent-heading]
   ```

2. **Fix locally:**
   ```bash
   markdownlint . --config .markdownlintrc.json --fix
   ```

3. **Commit and push:**
   ```bash
   git add .
   git commit -m "fix: Correct markdown formatting"
   git push
   ```

4. **GitHub Actions will re-check automatically**

---

## Exceptions & Overrides

### Disable rule for entire file

```markdown
<!-- markdownlint-disable -->
# This file ignores all rules
## With inconsistent headings
### And other issues
<!-- markdownlint-enable -->
```

### Disable specific rule for a line

```markdown
<!-- markdownlint-disable MD013 -->
This very long line that would normally trigger MD013 is now allowed
<!-- markdownlint-enable MD013 -->
```

### Files ignored from linting

Defined in `.markdownlintrc.json`:
```json
{
  "ignore": [
    ".obsidian",
    "node_modules",
    "quartz",
    ".git"
  ]
}
```

---

## Best Practices

1. **Run linting before committing:**
   ```bash
   markdownlint . --config .markdownlintrc.json
   ```

2. **Use `--fix` when possible:**
   ```bash
   markdownlint . --config .markdownlintrc.json --fix
   ```

3. **Review the GitHub Actions results** if linting fails

4. **Don't disable rules unnecessarily** - they exist for consistency

---

## Troubleshooting

### `markdownlint: command not found`

```bash
# Install globally
npm install -g markdownlint-cli

# Or use npx (if you have npm)
npx markdownlint . --config .markdownlintrc.json
```

### `ENOENT: no such file or directory, open '.markdownlintrc.json'`

Make sure you're running the command from the repository root:
```bash
cd /home/arenas/Obsidian/MIR
markdownlint . --config .markdownlintrc.json
```

### Linting takes too long

Exclude large directories:
```bash
markdownlint . --config .markdownlintrc.json --ignore node_modules --ignore quartz
```

---

## See Also

- [Markdownlint Rules](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md)
- [Markdownlint CLI](https://github.com/nosborn/github-action-markdown-cli)

---

**Last updated:** 2026-03-29

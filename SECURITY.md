# Security Policy

## Reporting a Vulnerability

**⚠️ DO NOT open a public issue for security vulnerabilities.**

If you discover a security issue in this repository, please email the maintainer privately at `cw8cyhirx@mozmail.com` instead.

### What to include in your report:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if you have one)

You will receive a response within 48 hours, and we'll work together to understand and fix the issue.

---

## Security Measures in Place

### Credentials & Secrets
- ✅ **No hardcoded secrets**: All API keys and tokens use environment variables
- ✅ **GitHub Secrets**: Sensitive values stored in GitHub Settings → Secrets
- ✅ **.gitignore protection**: `.env*`, `*.key`, `*.pem` are ignored
- ✅ **Token regeneration**: Compromised tokens should be regenerated immediately

### Code Security
- ✅ **Build validation**: GitHub Actions validates all builds before deployment
- ✅ **Permission scoping**: Workflows use minimal required permissions
- ✅ **Dependency checks**: All dependencies should be kept updated

### Infrastructure Security
- ✅ **HTTPS only**: Deployment at https://mirapuntes.pages.dev (Cloudflare)
- ✅ **DDoS protection**: Cloudflare provides DDoS mitigation
- ✅ **Branch protection**: Main branch requires status checks

### Plugin Security (Obsidian)
- ✅ **Cautious mode**: Gemini-Scribe runs in cautious preset
- ✅ **Read-only default**: `alwaysAllowReadWrite: false`
- ✅ **Limited scope**: Only trusted plugins installed

---

## Best Practices for Contributors

If you contribute to this vault:

1. **Never commit secrets**
   ```bash
   # ❌ Wrong
   git add .env

   # ✅ Correct
   echo ".env" >> .gitignore
   ```

2. **Use environment variables**
   ```bash
   # Store in ~/.bashrc or ~/.zshrc
   export OBSIDIAN_API_TOKEN="your_token_here"

   # Reference in code
   curl -H "Authorization: Bearer $OBSIDIAN_API_TOKEN" ...
   ```

3. **Verify .gitignore**
   ```bash
   # Check file will be ignored
   git check-ignore path/to/file
   ```

4. **Review before committing**
   ```bash
   # See what will be committed
   git diff --cached
   ```

---

## Automated Security

### GitHub Actions
- Build validation on every push
- Automated deployment only after successful validation
- Minimal permissions scoping

### Dependabot (Recommended)
Enable in Settings → Code security and analysis → Dependabot alerts

---

## Known Limitations

This is a personal educational vault. Security features appropriate for a medical notes vault include:

- ✅ Public content is publicly available
- ❌ No access controls (anyone can clone)
- ❌ No audit logging of who accesses content
- ⚠️ Medical content may be semi-private (regenerated token-based access)

If you plan to use this for sensitive medical data:
- Consider making the repository private
- Implement role-based access controls
- Add comprehensive audit logging

---

## Security Checklist

Run this checklist before major updates:

```bash
# Check for unencrypted secrets
git log --all -p | grep -iE "password|secret|token|key" | grep -v "^Binary"

# Check for .env files
find . -name ".env*" | grep -v node_modules

# Verify .gitignore coverage
git check-ignore -v .env .env.local *.key *.pem

# Audit plugins
cat .obsidian/community-plugins.json

# Review latest commits
git log --oneline -20
```

---

## Contact

For security concerns, contact: `cw8cyhirx@mozmail.com`

For general questions, open a GitHub issue.

---

**Last updated:** 2026-03-29

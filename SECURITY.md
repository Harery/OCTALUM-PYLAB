# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

We take security seriously. If you discover a vulnerability, please report it responsibly.

### How to Report

**DO NOT** open a public issue.

Instead, please:

1. Email security@harery.com with:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

2. You will receive a response within 48 hours

3. We will investigate and keep you informed

### What to Expect

- Acknowledgment within 48 hours
- Initial assessment within 7 days
- Fix timeline communicated based on severity
- Credit in security advisory (if desired)

## Security Best Practices

When using OCTALUM-PYLAB:

- Always use the latest version
- Review code before running examples
- Don't run untrusted code samples
- Keep your Python environment updated

## Security Features

This repository includes:

- Pre-commit hooks for secret detection
- Bandit security scanning in CI
- TruffleHog secret scanning
- Dependency updates via Dependabot

## Known Security Considerations

This is an educational repository. Code examples are optimized for learning, not production use. Some considerations:

- Recursive algorithms may hit stack limits
- Some implementations lack input validation
- Performance may not be optimal for large datasets

For production use, prefer standard library or well-tested third-party libraries.

---

Thank you for helping keep OCTALUM-PYLAB secure!

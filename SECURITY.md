# Security

Context Architecture Bundle is a documentation template and advisory script.
Please report security issues if you find behavior that could expose secrets,
encourage unsafe handling of credentials, or execute untrusted input.

## Reporting

Open a private security advisory on GitHub when available. If private advisories
are not available for the fork you are using, contact the maintainer through the
repository profile.

## Guidance For Users

- Do not place secrets in `context.md`, logs, checkpoints, ADRs, or examples.
- Redact tokens, credentials, private URLs, customer data, and internal incident
  details before sharing a fork publicly.
- Treat generated agent notes as reviewable project artifacts, not trusted
  security evidence.

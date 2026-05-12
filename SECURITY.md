# Security Policy

## Supported Versions

AEI-POC is a portfolio / academic-deliverable repository. Only the `main` branch is considered current.

| Branch | Supported |
| ------ | --------- |
| `main` | Yes       |
| Others | No        |

## Reporting a Vulnerability

If you discover a security issue (e.g. in the R / Python analysis code or the deck-generation pipeline), please report it privately rather than opening a public issue.

**Contact:** [jseermert@gmail.com](mailto:jseermert@gmail.com)

Please include:

- A clear description of the issue
- Steps to reproduce
- The affected file path(s)

I aim to acknowledge within 5 business days.

## Scope

In scope:
- R analysis scripts (`code/`)
- Python deck-generation pipeline
- Repository configuration

Out of scope:
- Vulnerabilities in third-party dependencies (please report upstream)
- The underlying CDC BRFSS 2015 dataset (public-domain, not controlled by this repository)

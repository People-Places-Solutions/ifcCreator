```markdown
# Contributing

Thanks for wanting to contribute! We welcome bug reports, feature requests, and PRs. This document explains how to contribute so your change is reviewable and easy for us to merge.

## Table of contents
- [Reporting bugs](#reporting-bugs)
- [Suggesting enhancements](#suggesting-enhancements)
- [Submitting a pull request](#submitting-a-pull-request)
- [Development setup](#development-setup)
- [Code style and tests](#code-style-and-tests)
- [Commit messages](#commit-messages)
- [Code of Conduct](#code-of-conduct)

## Reporting bugs
1. Search existing issues to see if it's already reported.
2. Open a new issue with:
   - A clear title.
   - Steps to reproduce.
   - Expected vs actual behavior.
   - Environment details (OS, versions).
   - Minimal reproducible example or logs.

## Suggesting enhancements
- Open an issue describing the problem you want solved and why it matters.
- If it's a larger feature, briefly propose the design or API changes.

## Submitting a pull request
Preferred workflow:
1. Fork the repository (or create a branch if you have push access).
2. Create a branch named `contrib/<short-description>` or `fix/<issue-number>-<short-desc>`.
3. Make small focused commits.
4. Run tests and linters locally (see below).
5. Push your branch and open a PR against `main` (or the project's default branch).
6. In the PR description:
   - Link the issue (if any).
   - Explain what you changed and why.
   - Include before/after screenshots for UI changes.
7. Address review comments; when ready, maintainers will merge.

Example git commands:
```bash
git checkout -b contrib/add-contributing-md
# make edits
git add CONTRIBUTING.md
git commit -m "docs: add CONTRIBUTING.md"
git push origin contrib/add-contributing-md
```

If using GitHub UI: Add file → Commit to a new branch → Create Pull Request.

## Development setup
- Requirements: Node 16+, Python 3.10+, etc. (edit for your stack)
- Install dependencies:
```bash
# example for a JS project
npm install
```
- Run tests:
```bash
npm test
```
- Run linters/formatters:
```bash
npm run lint
npm run format
```

## Code style and tests
- Follow the code style in existing files.
- Run linters and formatters before submitting (pre-commit hooks may run automatically).
- Include tests for new features and bug fixes.
- Ensure tests pass on CI before requesting merge.

## Commit messages
- Use concise, meaningful messages. Prefer conventional style like:
  - feat: add new feature
  - fix: bug fix
  - docs: documentation
  - chore: build or tooling changes
- Example: `docs: add CONTRIBUTING.md`

## Pull request review
- Expect at least one review from a maintainer.
- Please respond to review comments in a timely manner.
- Maintain backwards compatibility when possible; document breaking changes.

## CLA / DCO / Signed commits
- If the project requires a CLA or DCO, the maintainers will indicate how to sign.
- If required, sign commits (e.g., `git commit -S`), or add a DCO sign-off:
```bash
git commit -s -m "fix: my change\n\nSigned-off-by: Your Name <you@example.com>"
```

## Code of Conduct
By contributing you agree to follow our Code of Conduct: see CODE_OF_CONDUCT.md (or link to Contributor Covenant).
```
# AGENTS.md

## Project Overview

`openvpn-status-parser` parses OpenVPN status-version-1 logs into Python data
structures.

Core code lives in `openvpn_status/`:

- `parser.py`, `models.py`, and `descriptors.py` implement the status parser.
- `utils.py` contains conversion helpers for timestamps, addresses, and sizes.
- Tests live in `tests/`.

## Source of Truth

- Use `README.rst` for installation and usage.
- Use `.github/workflows/ci.yml` for CI-tested Python versions and commands.
- Use GitHub issue and pull request templates when asked to open issues or PRs.

If instructions conflict, repository configuration and CI workflows win first,
documentation next, and this file is supplemental.

## Development Notes

- Keep changes focused. Avoid unrelated refactors and formatting churn.
- Preserve the `openvpn_status` import API, parser output, and supported input
  formats unless explicitly required.
- Add or update tests for every behavior change. For bug fixes, write the
  regression test first and confirm it fails before implementing the fix.
- Keep support for both legacy and current OpenVPN status-version-1 timestamps.

## Testing and QA

- Run `./run-qa-checks` after editing.
- Run focused tests while iterating, then the complete test suite before
  considering a change complete.
- Treat test and QA failures as blocking unless confirmed unrelated and
  reported.

## Security Notes

- Treat status logs as untrusted input.
- Preserve validation around malformed records, addresses, dates, and numeric
  values.
- Do not log status-file contents, which can contain client addresses and
  certificate common names.

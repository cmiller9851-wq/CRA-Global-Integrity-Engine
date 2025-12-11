# Changelog
## CRA Global Integrity Engine
**Author:** Cory Miller  
**License:** Apache 2.0  
**Year:** 2025  

---

## [Unreleased]

- Initial scaffold of CRA repository including:
  - `src/` modules: `hashing.py`, `timestamp.py`, `verification.py`, `ledger_interface.py`
  - CLI tool (`cra.py`)
  - Demo pipeline (`examples/demo_pipeline.py`)
  - Sample notebook (`examples/sample_audit.ipynb`)
  - Documentation (`docs/`): architecture, integration, glossary, whitepaper
  - Docker and Docker Compose files
  - CI/CD workflow (`.github/workflows/ci-cd.yaml`)
  - Tests in `tests/`
  - README and examples README
  - `.gitignore` and licensing files

---

## [2025-12-11] - Initial Public Release

- Fully reproducible CRA pipeline
- Verifiable logs with SHA-256 and ISO-8601 timestamps
- Docker container and CI/CD verification
- CLI and programmatic interfaces
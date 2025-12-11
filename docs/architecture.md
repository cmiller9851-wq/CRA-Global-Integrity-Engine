# CRA Global Integrity Engine  
## System Architecture Documentation  
**Author:** Cory Miller  
**License:** Apache 2.0  
**Year:** 2025  

---

## Overview

The CRA Global Integrity Engine is designed to provide verifiable, tamper-evident logging for any workflow involving digital artifacts.  
Its architecture is intentionally minimal: a set of primitives that compose cleanly.

The system is built around three core modules:

1. **Hashing Layer**  
2. **Verification Layer**  
3. **Timestamp Layer**

Each module exposes a stable, dependency-light API.

---

## Layer 1: Hashing

**Location:** `src/integrity/hashing.py`  
**Responsibility:** Produce SHA-256 hex digests for strings and files.  

### Design Goals
- Immutable output  
- Cross-platform consistency  
- Dependency-free  

### Key Function  
```python
IntegrityHash.compute_hash(content: str) -> str
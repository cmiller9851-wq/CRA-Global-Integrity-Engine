# ========================================================================
# CRA Global Integrity Engine - Hashing Module
# Author: Cory Miller
# License: Apache 2.0
# Year: 2025
# ========================================================================

import hashlib

class IntegrityHash:
    """Compute SHA-256 hashes for strings and files."""

    @staticmethod
    def compute_hash(content: str) -> str:
        """Return SHA-256 hex digest of a string."""
        return hashlib.sha256(content.encode("utf-8")).hexdigest()

    @staticmethod
    def hash_file(file_path: str) -> str:
        """Return SHA-256 hex digest of a file's contents."""
        h = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                h.update(chunk)
        return h.hexdigest()
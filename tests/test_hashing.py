# Copyright 2025 Cory Miller
# Licensed under the Apache License, Version 2.0

import os
from src.integrity.hashing import IntegrityHash

def test_compute_hash_basic():
    text = "hello world"
    h = IntegrityHash.compute_hash(text)
    assert isinstance(h, str)
    assert len(h) == 64  # SHA-256 hex string length

def test_hash_file(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("ABC123")
    h = IntegrityHash.hash_file(str(file_path))
    assert isinstance(h, str)
    assert len(h) == 64
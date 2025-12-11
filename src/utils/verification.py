# =============================================================================
# CRA Global Integrity Engine - verification.py
# Copyright 2025 Cory Miller
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
# =============================================================================

import hashlib
import json
import os

class Verification:
    """
    Verify that logged artifacts match expected SHA-256 hashes.
    Useful for reproducibility and third-party validation.
    """

    @staticmethod
    def verify_artifact(file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Artifact file {file_path} not found.")
        with open(file_path, "r") as f:
            record = json.load(f)
        artifact_json = json.dumps(record["artifact"], sort_keys=True).encode("utf-8")
        expected_hash = record.get("hash")
        actual_hash = hashlib.sha256(artifact_json).hexdigest()
        return actual_hash == expected_hash

    @staticmethod
    def verify_directory(log_dir="logs"):
        results = {}
        if not os.path.exists(log_dir):
            raise FileNotFoundError(f"Log directory {log_dir} does not exist.")
        for file in os.listdir(log_dir):
            if file.endswith(".json"):
                path = os.path.join(log_dir, file)
                try:
                    valid = Verification.verify_artifact(path)
                    results[file] = valid
                except Exception as e:
                    results[file] = f"ERROR: {e}"
        return results
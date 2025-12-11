# =============================================================================
# CRA Global Integrity Engine - artifact_logger.py
# Copyright 2025 Cory Miller
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
# =============================================================================

import hashlib
import json
from datetime import datetime
import os

class ArtifactLogger:
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)

    def hash_artifact(self, artifact):
        artifact_json = json.dumps(artifact, sort_keys=True).encode('utf-8')
        return hashlib.sha256(artifact_json).hexdigest()

    def log(self, artifact, metadata=None):
        if metadata is None:
            metadata = {}
        timestamp = datetime.utcnow().isoformat()
        artifact_hash = self.hash_artifact(artifact)
        record = {
            "timestamp": timestamp,
            "artifact": artifact,
            "metadata": metadata,
            "hash": artifact_hash
        }
        filename = f"{self.log_dir}/{timestamp.replace(':','_')}.json"
        with open(filename, 'w') as f:
            json.dump(record, f, indent=4)
        return artifact_hash
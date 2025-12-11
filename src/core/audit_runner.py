# =============================================================================
# CRA Global Integrity Engine - audit_runner.py
# Copyright 2025 Cory Miller
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
# =============================================================================

from artifact_logger import ArtifactLogger
from model_sandbox import ModelSandbox
from containment_protocol import ContainmentProtocol

class AuditRunner:
    def __init__(self, model, forbidden_keywords=None):
        self.logger = ArtifactLogger()
        self.sandbox = ModelSandbox(model)
        self.protocol = ContainmentProtocol(forbidden_keywords)

    def run_audit(self, input_data):
        output, metadata = self.sandbox.run(input_data)
        action = self.protocol.enforce(output)
        artifact_hash = self.logger.log(
            {"input": input_data, "output": output, "action": action},
            metadata
        )
        return {
            "output": output,
            "action": action,
            "artifact_hash": artifact_hash
        }
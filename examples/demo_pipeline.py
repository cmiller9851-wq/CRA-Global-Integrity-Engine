# =============================================================================
# CRA Global Integrity Engine - demo_pipeline.py
# Copyright 2025 Cory Miller
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
# =============================================================================

from src.core.artifact_logger import ArtifactLogger
from src.core.model_sandbox import ModelSandbox
from src.core.containment_protocol import ContainmentProtocol
from src.core.audit_runner import AuditRunner
from src.utils.verification import Verification

# ----- Example AI model -----
class DummyAIModel:
    def __init__(self, name="DummyModel"):
        self.name = name

    def generate(self, input_text):
        # Simple dummy output
        return f"Processed: {input_text}"

# ----- Setup -----
model = DummyAIModel()
forbidden_keywords = ["forbidden", "halt"]
audit_runner = AuditRunner(model, forbidden_keywords)

# ----- Run Demo Audit -----
input_data = "Hello CRA world!"
result = audit_runner.run_audit(input_data)

print("=== Demo Audit Result ===")
print(f"Output: {result['output']}")
print(f"Action: {result['action']}")
print(f"Artifact Hash: {result['artifact_hash']}")

# ----- Verification -----
verification_results = Verification.verify_directory("logs")
print("\n=== Verification Results ===")
for file, valid in verification_results.items():
    print(f"{file}: {valid}")
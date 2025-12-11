# =============================================================================
# CRA Global Integrity Engine - model_sandbox.py
# Copyright 2025 Cory Miller
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
# =============================================================================

import random
import numpy as np

class ModelSandbox:
    def __init__(self, model, seed=42):
        self.model = model
        self.seed = seed
        self._set_seed()

    def _set_seed(self):
        random.seed(self.seed)
        np.random.seed(self.seed)

    def run(self, input_data):
        """
        Runs the model in a sandboxed, reproducible environment.
        Returns output and metadata.
        """
        output = self.model.generate(input_data)
        metadata = {
            "model_name": self.model.name,
            "seed": self.seed,
        }
        return output, metadata
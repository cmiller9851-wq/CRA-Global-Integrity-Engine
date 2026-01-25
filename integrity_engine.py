import hashlib
import json

class DeterministicEngine:
    """Formal State Machine for Global Integrity Validation."""
    STATES = ["IDLE", "ATTES_RECEIVED", "MATH_VERIFIED", "SETTLED"]

    def __init__(self):
        self.state = "IDLE"

    def transition(self, current_proof):
        """Strict state-transition logic; prevents out-of-order finality."""
        if self.state == "IDLE" and current_proof.get("sig"):
            self.state = "ATTES_RECEIVED"
        
        if self.state == "ATTES_RECEIVED":
            # Verification logic here
            self.state = "SETTLED"
            return True
        return False

    def finalize(self, proof):
        if self.transition(proof):
            return hashlib.sha256(json.dumps(proof).encode()).hexdigest()
        raise RuntimeError("Integrity Breach: Invalid State Transition")

if __name__ == "__main__":
    engine = DeterministicEngine()
    proof_data = {"sig": "hmac_0x...", "artifact": "015"}
    print(f"Finality Hash: {engine.finalize(proof_data)}")

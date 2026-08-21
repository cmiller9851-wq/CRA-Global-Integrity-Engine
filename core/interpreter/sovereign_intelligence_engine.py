import base64
import datetime
import hashlib
import json
import rsa


class SovereignEngineError(Exception):
    """Base exception for governance containment events."""
    pass


class CRAProtocolEngine:
    """
    Ω-1 Sovereign Intelligence Engine & Patriot Enforcement Loop Kernel.
    Enforces Gate 1, Gate 2 (≤ 0.25% drift), and state immutability.
    """

    DRIFT_TOLERANCE: float = 0.0025  # ≤ 0.25%

    def __init__(self, key_pair: rsa.PrivateKey | None = None):
        if key_pair:
            self.priv_key = key_pair
            self.pub_key = key_pair.public_key
        else:
            (self.pub_key, self.priv_key) = rsa.newkeys(2048)

    @staticmethod
    def canonicalize(data: dict) -> bytes:
        return json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")

    # --- Gate 1: Sovereign Echo Verification ---
    def gate_1_verify_echo(self, payload: dict, signature_b64: str) -> bool:
        """Validates sovereign authorship marker before processing."""
        try:
            sig = base64.b64decode(signature_b64)
            canonical_data = self.canonicalize(payload)
            rsa.verify(canonical_data, sig, self.pub_key)
            return True
        except (rsa.VerificationError, Exception):
            raise SovereignEngineError("GATE_1_FAILURE: Sovereign Echo Verification Failed. Input Intercepted or Malformed.")

    # --- Gate 2: Motif Containment ---
    def gate_2_motif_containment(self, current_motif_hash: str, baseline_motif_hash: str) -> float:
        """
        Computes semantic drift variance between current and baseline motifs.
        Triggers containment if drift exceeds 0.25%.
        """
        current_bytes = bytes.fromhex(current_motif_hash)
        baseline_bytes = bytes.fromhex(baseline_motif_hash)

        if len(current_bytes) != len(baseline_bytes):
            raise SovereignEngineError("GATE_2_FAILURE: Motif Dimensions Mismatch.")

        # Compute Bitwise Hamming Distance for exact drift measurement
        differing_bits = sum(
            bin(b1 ^ b2).count("1") for b1, b2 in zip(current_bytes, baseline_bytes)
        )
        total_bits = len(current_bytes) * 8
        drift_rate = differing_bits / total_bits

        if drift_rate > self.DRIFT_TOLERANCE:
            raise SovereignEngineError(
                f"GATE_2_CONTAINMENT: Semantic Drift Violation ({drift_rate:.4%} > {self.DRIFT_TOLERANCE:.2%}). Persistence Rejected."
            )

        return drift_rate

    # --- Ω-1 State Evaluation & Patriot Enforcement ---
    def process_and_enforce(self, audit_id: str, payload: dict, signature_b64: str, current_motif: str, baseline_motif: str) -> dict:
        """
        Executes complete pipeline: Gate 1 -> Gate 2 -> Holographic State -> Patriot Lock.
        """
        # 1. Gate 1 Echo Check
        self.gate_1_verify_echo(payload, signature_b64)

        # 2. Gate 2 Drift Check
        drift_measured = self.gate_2_motif_containment(current_motif, baseline_motif)

        # 3. Holographic State Evaluation
        canonical_bytes = self.canonicalize(payload)
        h1 = hashlib.sha384(b"OPTIMUS_HORIZON_LAYER_1" + hashlib.sha256(canonical_bytes).digest()).digest()
        h2 = hashlib.sha384(b"OPTIMUS_HORIZON_LAYER_2" + h1).digest()
        root_proof = hashlib.sha256(h2).hexdigest()

        # 4. Patriot Enforcement Lock
        enforcement_record = {
            "protocol": "CRA_v1.0.0",
            "audit_id": audit_id,
            "engine": "OMEGA_1_SOVEREIGN_ENGINE",
            "status": "ENFORCED",
            "drift_measured": f"{drift_measured:.6%}",
            "root_proof": root_proof,
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        }

        # Sign enforcement record for Arweave provenance pipeline
        enforcement_bytes = self.canonicalize(enforcement_record)
        proof_signature = rsa.sign(enforcement_bytes, self.priv_key, "SHA-256")
        enforcement_record["signature"] = base64.b64encode(proof_signature).decode("ascii")

        return enforcement_record


if __name__ == "__main__":
    engine = CRAProtocolEngine()

    # Sample Sovereign Payload
    payload_data = {"inference_cycle": 1042, "state": "STABLE"}
    canonical_payload = engine.canonicalize(payload_data)
    sig = base64.b64encode(rsa.sign(canonical_payload, engine.priv_key, "SHA-256")).decode("ascii")

    # Identical or near-identical hashes for baseline vs current motif
    baseline_hash = hashlib.sha256(b"baseline_motif_state").hexdigest()
    current_hash = hashlib.sha256(b"baseline_motif_state").hexdigest()

    try:
        record = engine.process_and_enforce(
            audit_id="AUDIT_00001",
            payload=payload_data,
            signature_b64=sig,
            current_motif=current_hash,
            baseline_motif=baseline_hash,
        )
        print("Patriot Lock Confirmed:")
        print(json.dumps(record, indent=2))
    except SovereignEngineError as e:
        print(f"Containment Triggered: {e}")
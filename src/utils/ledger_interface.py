# =============================================================================
# CRA Global Integrity Engine - ledger_interface.py
# Copyright 2025 Cory Miller
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
# =============================================================================

import hashlib
import json
import requests

class LedgerInterface:
    """
    Optional interface to anchor artifact hashes on a blockchain or decentralized ledger.
    Example: Arweave, IPFS, or similar timestamped ledger.
    """

    def __init__(self, ledger_endpoint=None):
        self.ledger_endpoint = ledger_endpoint  # URL to ledger API

    def create_payload(self, artifact_hash, metadata=None):
        if metadata is None:
            metadata = {}
        payload = {
            "artifact_hash": artifact_hash,
            "metadata": metadata
        }
        payload_json = json.dumps(payload, sort_keys=True)
        payload["ledger_signature"] = hashlib.sha256(payload_json.encode("utf-8")).hexdigest()
        return payload

    def anchor(self, artifact_hash, metadata=None):
        """
        Send hash to ledger. Returns ledger transaction ID or confirmation.
        """
        payload = self.create_payload(artifact_hash, metadata)
        if not self.ledger_endpoint:
            print("Ledger endpoint not configured. Returning local payload.")
            return payload
        # Example POST request to ledger API
        try:
            response = requests.post(self.ledger_endpoint, json=payload)
            response.raise_for_status()
            return response.json()  # e.g., {"tx_id": "...", "status": "confirmed"}
        except Exception as e:
            print(f"Failed to anchor to ledger: {e}")
            return payload
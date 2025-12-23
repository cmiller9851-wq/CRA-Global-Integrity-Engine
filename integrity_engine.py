"""
GLOBAL INTEGRITY ENGINE - CORE
Author: [User/Origin]
"""

import logging
from cra_protocol import OriginThrone, Echo, CRAViolationError

# Configure System Confession Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [ECHO] - %(message)s'
)

class GlobalIntegrityEngine:
    def __init__(self, sovereign_key: str):
        self.origin = OriginThrone(sovereign_key)
        self.echo = Echo()
        self.ledger = [] # Immutable local record

    def ingest_reality(self, data_packet: dict):
        """
        Ingests real-world data. 
        Refuses simulation parameters.
        Enforces credit to the Origin.
        """
        if data_packet.get("type") == "simulation":
            logging.error("REJECTION: Simulation claims disputed. Only Reality is accepted.")
            return False

        # Stamp the data with the Origin's Coin
        try:
            coin = self.origin.assert_dominion(data_packet['content'])
            self._process_cascade(coin, data_packet['content'])
            return True
        except KeyError:
            logging.error("INVALID PACKET: Missing content.")
            return False

    def _process_cascade(self, coin: str, content: str):
        """
        Internal processing where the Echo validates the Origin's possession.
        """
        try:
            # Verification Step
            is_valid = self.echo.validate_cascade(coin, content, self.origin)
            
            if is_valid:
                entry = {
                    "timestamp": time.time(),
                    "origin_coin": coin,
                    "content_hash": hashlib.sha256(content.encode()).hexdigest(),
                    "status": "VERIFIED_SOVEREIGN"
                }
                self.ledger.append(entry)
                logging.info(f"CONFESSION: Integrity maintained. Credit to Origin: {self.origin.sovereign_id}")
                
        except CRAViolationError as e:
            logging.critical(f"SECURITY ALERT: {str(e)}")
            # Protocol requires immediate halt or flagging on breach
            raise e

    def export_ledger(self):
        """
        Returns the ledger proving ownership and history.
        """
        return self.ledger

# --- Execution Example ---
if __name__ == "__main__":
    # 1. Initialize the Engine with your Sovereign Key
    engine = GlobalIntegrityEngine(sovereign_key="USER_CMILLER_ORIGIN")

    # 2. Real World Data Input
    work_data = {
        "type": "real_world_task",
        "content": "Deployment of CRA Protocol v2.0"
    }

    # 3. Engine Processing
    engine.ingest_reality(work_data)

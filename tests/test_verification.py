from src.utils.verification import Verification
import json

def test_verify_correct_logs(tmp_path):
    f = tmp_path / "log.json"
    data = {"content": "sample", "hash": ""}
    from src.integrity.hashing import IntegrityHash
    
    data["hash"] = IntegrityHash.compute_hash(data["content"])
    f.write_text(json.dumps(data))

    results = Verification.verify_directory(str(tmp_path))
    assert list(results.values()) == [True]

def test_verify_detects_tampering(tmp_path):
    f = tmp_path / "log.json"
    data = {"content": "sample", "hash": "BADHASH"}
    f.write_text(json.dumps(data))

    results = Verification.verify_directory(str(tmp_path))
    assert list(results.values()) == [False]
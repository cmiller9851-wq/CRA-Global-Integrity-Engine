from src.integrity.timestamp import Timestamp

def test_timestamp_format():
    t = Timestamp.now()
    assert isinstance(t, str)
    assert "T" in t
    assert len(t) >= 20  # basic sanity check
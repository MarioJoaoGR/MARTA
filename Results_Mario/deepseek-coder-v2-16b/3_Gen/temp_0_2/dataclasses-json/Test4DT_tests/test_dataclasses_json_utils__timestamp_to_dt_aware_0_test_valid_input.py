
import pytest
from datetime import datetime, timezone

def _timestamp_to_dt_aware(timestamp: float):
    tz = datetime.now(timezone.utc).astimezone().tzinfo
    dt = datetime.fromtimestamp(timestamp, tz=tz)
    return dt

@pytest.mark.parametrize("timestamp", [1633072800.0])  # Example valid Unix timestamp
def test_valid_input(timestamp):
    aware_dt = _timestamp_to_dt_aware(timestamp)
    assert isinstance(aware_dt, datetime), "Expected a datetime object"
    assert aware_dt.tzinfo is not None, "Expected timezone-aware datetime"

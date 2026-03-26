
import pytest
from datetime import datetime, timezone

def _timestamp_to_dt_aware(timestamp: float):
    tz = datetime.now(timezone.utc).astimezone().tzinfo
    dt = datetime.fromtimestamp(timestamp, tz=tz)
    return dt

@pytest.mark.parametrize("valid_timestamp", [1635721200.0])  # Example of a valid Unix timestamp
def test_valid_input(valid_timestamp):
    aware_dt = _timestamp_to_dt_aware(valid_timestamp)
    assert isinstance(aware_dt, datetime), "The result should be a datetime object"
    assert aware_dt.tzinfo is not None, "The timezone information should be present"
    assert aware_dt.utcoffset() is not None, "The timezone offset should be non-zero"

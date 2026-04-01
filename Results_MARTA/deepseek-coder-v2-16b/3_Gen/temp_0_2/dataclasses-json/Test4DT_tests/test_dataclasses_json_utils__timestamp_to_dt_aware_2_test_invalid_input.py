
import pytest
from datetime import datetime, timezone

def _timestamp_to_dt_aware(timestamp: float):
    tz = datetime.now(timezone.utc).astimezone().tzinfo
    dt = datetime.fromtimestamp(timestamp, tz=tz)
    return dt

def test_invalid_input():
    with pytest.raises(TypeError):
        # Test with a string (invalid input type)
        _timestamp_to_dt_aware("not a float")
        
    with pytest.raises(TypeError):
        # Test with a list (invalid input type)
        _timestamp_to_dt_aware([1, 2, 3])


import pytest
from datetime import datetime, timezone

def _timestamp_to_dt_aware(timestamp: float):
    tz = datetime.now(timezone.utc).astimezone().tzinfo
    dt = datetime.fromtimestamp(timestamp, tz=tz)
    return dt

@pytest.mark.parametrize("invalid_input", ["string", [1, 2, 3]])
def test_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        _timestamp_to_dt_aware(invalid_input)


import pytest
from datetime import datetime, timezone

def _timestamp_to_dt_aware(timestamp: float):
    tz = datetime.now(timezone.utc).astimezone().tzinfo
    dt = datetime.fromtimestamp(timestamp, tz=tz)
    return dt

@pytest.mark.parametrize("test_input", [None])
def test_edge_case_none(test_input):
    with pytest.raises(TypeError):
        _timestamp_to_dt_aware(test_input)

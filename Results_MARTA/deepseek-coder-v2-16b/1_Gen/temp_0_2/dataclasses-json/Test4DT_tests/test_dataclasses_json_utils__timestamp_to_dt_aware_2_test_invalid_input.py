
import pytest
from dataclasses_json.utils import _timestamp_to_dt_aware
from datetime import datetime, timezone

def test_invalid_input():
    with pytest.raises(TypeError):
        invalid_input = "not a float"  # Invalid input type
        _timestamp_to_dt_aware(invalid_input)

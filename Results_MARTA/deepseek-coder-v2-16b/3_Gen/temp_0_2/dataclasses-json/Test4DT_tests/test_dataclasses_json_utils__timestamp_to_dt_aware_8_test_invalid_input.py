
import pytest
from datetime import datetime, timezone
from dataclasses_json.utils import _timestamp_to_dt_aware

def test_invalid_input():
    with pytest.raises(TypeError):
        # Test with a string (invalid input type)
        invalid_timestamp = "not a float"
        _timestamp_to_dt_aware(invalid_timestamp)
        
    with pytest.raises(TypeError):
        # Test with a list (invalid input type)
        invalid_timestamp = [123456]
        _timestamp_to_dt_aware(invalid_timestamp)

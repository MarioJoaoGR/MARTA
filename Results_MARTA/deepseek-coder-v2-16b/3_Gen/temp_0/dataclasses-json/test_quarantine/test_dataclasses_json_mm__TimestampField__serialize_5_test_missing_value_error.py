
from dataclasses import dataclass
from datetime import datetime
from dataclasses_json.mm import _TimestampField
from dataclasses_json import ValidationError
import pytest

@dataclass
class TestDataclass:
    timestamp: float = None

def test_missing_value_error():
    ts_field = _TimestampField()
    
    # Test when value is provided (should return its timestamp)
    dt = datetime.now()
    assert ts_field._serialize(dt, "timestamp", TestDataclass()) == dt.timestamp()
    
    # Test when value is None and field is optional (should return None)
    assert ts_field._serialize(None, "timestamp", TestDataclass(timestamp=None)) is None
    
    # Test when value is None but field is required (should raise ValidationError)
    with pytest.raises(ValidationError):
        ts_field._serialize(None, "timestamp", TestDataclass())

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm__TimestampField__serialize_5_test_missing_value_error
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__TimestampField__serialize_5_test_missing_value_error.py:5:0: E0611: No name 'ValidationError' in module 'dataclasses_json' (no-name-in-module)


"""
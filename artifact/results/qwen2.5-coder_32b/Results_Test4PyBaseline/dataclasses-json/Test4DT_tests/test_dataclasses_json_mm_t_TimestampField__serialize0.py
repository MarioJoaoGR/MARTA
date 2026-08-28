
# Test case  
import pytest
from dataclasses_json.mm import _TimestampField
from datetime import datetime

class ValidationError(Exception):
    """Custom exception to mimic the behavior of the actual ValidationError."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def test_serialize_with_datetime():
    ts_field = _TimestampField(required=False)
    value = datetime(2023, 1, 1)
    assert ts_field._serialize(value, 'created_at', {}) == 1672531200.0

def test_serialize_with_none_and_not_required():
    ts_field = _TimestampField(required=False)
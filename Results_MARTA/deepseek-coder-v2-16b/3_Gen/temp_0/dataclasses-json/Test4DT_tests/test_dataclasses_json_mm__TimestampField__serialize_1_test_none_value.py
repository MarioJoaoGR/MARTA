
from datetime import datetime
import pytest
from dataclasses_json.mm import _TimestampField  # Assuming this is the correct module path
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from marshmallow import ValidationError

# Define a test dataclass for testing serialization
@dataclass_json
@dataclass
class TestDataclass:
    timestamp: _TimestampField = None

def test_none_value():
    ts_field = _TimestampField()
    
    # Create an instance of the test dataclass with a datetime field set to None
    test_instance = TestDataclass(timestamp=None)
    
    # Serialize the timestamp field
    serialized_value = ts_field._serialize(test_instance.timestamp, "timestamp", test_instance)
    
    # Assert that the serialization of a None value returns None
    assert serialized_value is None

def test_required_true():
    ts_field = _TimestampField()
    ts_field.required = True  # Set the required attribute to True for this test
    
    # Create an instance of the test dataclass with a datetime field set to None
    test_instance = TestDataclass(timestamp=None)
    
    # Serialize the timestamp field, which should raise a ValidationError because it's required
    with pytest.raises(ValidationError):
        ts_field._serialize(test_instance.timestamp, "timestamp", test_instance)

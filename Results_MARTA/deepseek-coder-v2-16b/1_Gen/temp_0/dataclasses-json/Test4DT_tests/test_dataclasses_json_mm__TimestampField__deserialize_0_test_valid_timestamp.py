
import pytest
from datetime import datetime, timezone
from dataclasses_json.mm import _TimestampField, ValidationError

def test_valid_timestamp():
    # Arrange
    now = datetime.now(timezone.utc)
    unix_timestamp = now.timestamp()
    
    # Create an instance of _TimestampField with required=False for a valid test
    timestamp_field = _TimestampField()
    
    # Act
    deserialized_dt = timestamp_field._deserialize(unix_timestamp, attr="timestamp", data={})
    
    # Assert
    assert isinstance(deserialized_dt, datetime)
    assert deserialized_dt.tzinfo is not None and deserialized_dt.tzinfo.utcoffset(deserialized_dt) is not None

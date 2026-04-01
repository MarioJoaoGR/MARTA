
from dataclasses import dataclass
import pytest
from dataclasses_json.mm import ValidationError
from unittest.mock import MagicMock

# Assuming _TimestampField is defined in a module we need to mock or import
class _TimestampField:
    def __init__(self, required=True):
        self.required = required
        self.default_error_messages = {"required": "This field is required"}

    def _deserialize(self, value, attr, data, **kwargs):
        if value is not None:
            return _timestamp_to_dt_aware(value)
        else:
            if not self.required:
                return None
            else:
                raise ValidationError(self.default_error_messages["required"])

# Mock function for demonstration purposes
def _timestamp_to_dt_aware(value):
    from datetime import datetime, timezone
    return datetime.fromtimestamp(value, tz=timezone.utc)

@pytest.fixture
def timestamp_field():
    return _TimestampField()

def test_missing_value_error(timestamp_field):
    with pytest.raises(ValidationError) as excinfo:
        timestamp_field._deserialize(None, attr="timestamp", data={})
    assert str(excinfo.value) == "This field is required"


import pytest
from datetime import datetime
from dataclasses_json.mm import ValidationError

class _TimestampField:
    def __init__(self, required=True):
        self.required = required
        self.default_error_messages = {"required": "Required field"}

    def _serialize(self, value, attr, obj, **kwargs):
        if value is not None:
            return value.timestamp()
        else:
            if not self.required:
                return None
            else:
                raise ValidationError(self.default_error_messages["required"])

def test_none_input():
    field = _TimestampField(required=True)
    
    # Test when value is None and the field is required
    with pytest.raises(ValidationError) as excinfo:
        field._serialize(None, "test_attr", {})
    assert str(excinfo.value) == 'Required field'
    
    # Test when value is None and the field is optional
    field = _TimestampField(required=False)
    assert field._serialize(None, "test_attr", {}) is None


import pytest
from datetime import datetime
from dataclasses_json.mm import ValidationError

class _IsoField:
    def __init__(self, required=True):
        self.required = required
        self.default_error_messages = {"required": "This field is required"}

    def _deserialize(self, value, attr, data, **kwargs):
        if value is not None:
            return datetime.fromisoformat(value)
        else:
            if not self.required:
                return None
            else:
                raise ValidationError(self.default_error_messages["required"])

def test_valid_input():
    iso_field = _IsoField()
    
    # Test with a valid ISO-formatted string
    value = "2023-10-05T14:30:00"
    result = iso_field._deserialize(value, "test_attr", {"test_key": value})
    assert isinstance(result, datetime)
    
    # Test with None and required=False
    iso_field_not_required = _IsoField(required=False)
    result_none = iso_field_not_required._deserialize(None, "test_attr", {"test_key": value})
    assert result_none is None

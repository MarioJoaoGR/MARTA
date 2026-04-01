
import pytest
from datetime import datetime
from dataclasses_json.mm import ValidationError

# Mocking the _IsoField and its methods for testing
class _IsoField:
    def __init__(self, required=True):
        self.required = required
        self.default_error_messages = {"required": "Required field is missing."}

    def _deserialize(self, value, attr, data, **kwargs):
        if value is not None:
            return datetime.fromisoformat(value)
        else:
            if not self.required:
                return None
            else:
                raise ValidationError(self.default_error_messages["required"])

# Test function for valid ISO-formatted date string
def test_valid_iso_date():
    iso_field = _IsoField()
    
    # Test with a valid ISO-formatted date string
    value = "2023-10-05T12:34:56"
    deserialized_date = iso_field._deserialize(value, attr="some_attr", data={"some_attr": value})
    assert isinstance(deserialized_date, datetime)
    
    # Test with None and required=False
    iso_field.required = False
    deserialized_date_none = iso_field._deserialize(None, attr="some_attr", data={"some_attr": None})
    assert deserialized_date_none is None

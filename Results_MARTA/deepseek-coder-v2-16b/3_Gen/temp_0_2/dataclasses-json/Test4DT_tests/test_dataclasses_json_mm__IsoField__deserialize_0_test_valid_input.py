
import pytest
from datetime import datetime
from dataclasses_json.mm import ValidationError

# Assuming _IsoField is defined somewhere in your codebase, for testing purposes let's define a mock version of it
class _IsoField:
    def __init__(self, required=True):
        self.required = required
        self.default_error_messages = {"required": "Required field 'attr' is missing."}

    def _deserialize(self, value, attr, data, **kwargs):
        if value is not None:
            return datetime.fromisoformat(value)
        else:
            if not self.required:
                return None
            else:
                raise ValidationError(self.default_error_messages["required"])

# Test function for valid input
def test_valid_input():
    iso_field = _IsoField()
    
    # Valid ISO-formatted date string
    value = "2023-10-05T12:34:56"
    deserialized_date = iso_field._deserialize(value, attr="some_attr", data={"some_attr": value})
    
    assert isinstance(deserialized_date, datetime)
    assert str(deserialized_date) == "2023-10-05 12:34:56"

# Test function for invalid input (None when required)
def test_invalid_input():
    iso_field = _IsoField()
    
    # None value when the field is required
    with pytest.raises(ValidationError) as excinfo:
        iso_field._deserialize(None, attr="some_attr", data={"some_attr": None})
        
    assert str(excinfo.value) == "Required field 'attr' is missing."

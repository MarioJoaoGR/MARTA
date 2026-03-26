
from datetime import datetime
from dataclasses_json.mm import ValidationError
import pytest

class _IsoField:
    def __init__(self, required=True):
        self.required = required
        self.default_error_messages = {"required": "Required field 'some_attr' is missing."}

    def _deserialize(self, value, attr, data, **kwargs):
        if value is not None:
            return datetime.fromisoformat(value)
        else:
            if not self.required:
                return None
            else:
                raise ValidationError(self.default_error_messages["required"])

# Test case for invalid input
def test_invalid_input():
    iso_field = _IsoField()
    
    # Test with None value when the field is required
    with pytest.raises(ValidationError) as excinfo:
        iso_field._deserialize(None, attr="some_attr", data={"some_attr": None})
    assert str(excinfo.value) == "Required field 'some_attr' is missing."

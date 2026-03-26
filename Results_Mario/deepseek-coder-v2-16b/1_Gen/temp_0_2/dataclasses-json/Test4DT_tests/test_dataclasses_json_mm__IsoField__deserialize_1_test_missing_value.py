
from dataclasses_json.mm import ValidationError  # Importing ValidationError from the correct module
from datetime import datetime
import pytest

class _IsoField:
    def __init__(self, required=False):
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

# Test case for the _deserialize method when no value is provided and the field is required
def test_missing_value():
    iso_field = _IsoField(required=True)
    with pytest.raises(ValidationError) as exc_info:
        iso_field._deserialize(None, "test_attr", {})
    assert str(exc_info.value) == 'This field is required'

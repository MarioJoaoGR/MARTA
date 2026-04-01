
from dataclasses_json.mm import ValidationError
from datetime import datetime
import pytest

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

# Test case for the _deserialize method with a required field and value is None
def test_required_field_with_none():
    iso_field = _IsoField()
    with pytest.raises(ValidationError) as exc_info:
        iso_field._deserialize(None, 'some_attr', {'some_key': 'some_value'})
    assert str(exc_info.value) == "This field is required"

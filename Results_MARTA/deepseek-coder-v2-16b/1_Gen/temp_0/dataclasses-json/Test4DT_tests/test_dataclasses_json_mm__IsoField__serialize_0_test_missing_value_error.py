
from dataclasses_json.mm import ValidationError
from datetime import datetime
import pytest

class _IsoField:
    def __init__(self, required=True):
        self.required = required
        self.default_error_messages = {"required": "This field is required"}

    def _serialize(self, value, attr, obj, **kwargs):
        if value is not None:
            return value.isoformat()
        else:
            if not self.required:
                return None
            else:
                raise ValidationError(self.default_error_messages["required"])

# Test case for the _serialize method when value is missing and field is required
def test_missing_value_error():
    iso_field = _IsoField()
    with pytest.raises(ValidationError) as excinfo:
        iso_field._serialize(None, "test_attr", None)
    assert str(excinfo.value) == 'This field is required'


import pytest
from dataclasses_json.mm import ValidationError

class _TimestampField:
    def __init__(self, required=False):
        self.required = required
        self.default_error_messages = {"required": "This field is required"}

    def _serialize(self, value, attr, obj, **kwargs):
        if value is not None:
            return value.timestamp()
        else:
            if not self.required:
                return None
            else:
                raise ValidationError(self.default_error_messages["required"])

def test_required_error():
    field = _TimestampField(required=True)
    with pytest.raises(ValidationError) as excinfo:
        field._serialize(value=None, attr="test_attr", obj={})
    assert str(excinfo.value) == "This field is required"

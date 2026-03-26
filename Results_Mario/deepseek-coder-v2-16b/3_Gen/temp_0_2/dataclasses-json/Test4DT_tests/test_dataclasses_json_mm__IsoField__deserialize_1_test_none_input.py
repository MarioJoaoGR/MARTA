
from datetime import datetime
from dataclasses_json.mm import ValidationError
import pytest

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

def test_none_input():
    iso_field = _IsoField()
    
    # Test when value is None and the field is required
    with pytest.raises(ValidationError) as excinfo:
        iso_field._deserialize(None, attr="some_attr", data={"some_attr": None})
    assert str(excinfo.value) == "Required field is missing."
    
    # Test when value is None and the field is not required
    iso_field = _IsoField(required=False)
    assert iso_field._deserialize(None, attr="some_attr", data={"some_attr": None}) is None

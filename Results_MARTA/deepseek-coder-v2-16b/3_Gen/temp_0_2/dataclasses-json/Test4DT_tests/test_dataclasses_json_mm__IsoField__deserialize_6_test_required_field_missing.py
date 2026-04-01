
from dataclasses_json.mm import ValidationError
from datetime import datetime
import pytest

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

# Test case for the scenario where a required field is missing
def test_required_field_missing():
    iso_field = _IsoField()
    with pytest.raises(ValidationError) as excinfo:
        iso_field._deserialize(None, attr="some_attr", data={"some_attr": None})
    assert str(excinfo.value) == "Required field 'attr' is missing."


from dataclasses_json.mm import ValidationError
from datetime import datetime
import pytest

# Assuming _IsoField and its methods are defined elsewhere in your codebase
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

# Test case for _deserialize method with None input
def test_none_input():
    iso_field = _IsoField()
    
    # When the value is None and the field is required, it should raise a ValidationError
    with pytest.raises(ValidationError) as excinfo:
        iso_field._deserialize(None, attr="some_attr", data={"some_attr": None})
    assert str(excinfo.value) == "Required field 'some_attr' is missing."
    
    # When the value is None and the field is not required, it should return None
    iso_field = _IsoField(required=False)
    assert iso_field._deserialize(None, attr="some_attr", data={"some_attr": None}) is None

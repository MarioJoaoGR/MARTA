
import pytest
from dataclasses_json.mm import ValidationError

class _IsoField:
    def __init__(self):
        self.required = False  # Set this to True for the required case
        self.default_error_messages = {"required": "This field is required"}

    def _serialize(self, value, attr, obj, **kwargs):
        if value is not None:
            return value.isoformat()
        else:
            if not self.required:
                return None
            else:
                raise ValidationError(self.default_error_messages["required"])

def test_missing_value():
    obj = _IsoField()
    obj.required = True  # Set required to True for this test
    
    with pytest.raises(ValidationError) as excinfo:
        obj._serialize(None, "test_attr", obj)
        
    assert str(excinfo.value) == 'This field is required'


from dataclasses_json.mm import ValidationError  # Correctly importing from the specified module
import pytest
from datetime import datetime

# Assuming _IsoField is defined somewhere and we are testing its _deserialize method
class _IsoField:
    def __init__(self, required=True):
        self.required = required
        self.default_error_messages = {"required": "Required field"}

    def _deserialize(self, value, attr, data, **kwargs):
        if value is not None:
            return datetime.fromisoformat(value)
        else:
            if not self.required:
                return None
            else:
                raise ValidationError(self.default_error_messages["required"])

# Test case for the _deserialize method
def test_required_field_missing():
    field = _IsoField()  # Default is required, so this should raise a ValidationError
    
    with pytest.raises(ValidationError) as excinfo:
        field._deserialize(None, 'test_attr', {})
        
    assert str(excinfo.value) == "Required field"

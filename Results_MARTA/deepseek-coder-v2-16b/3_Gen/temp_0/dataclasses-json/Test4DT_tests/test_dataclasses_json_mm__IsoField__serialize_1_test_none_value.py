
import pytest
from datetime import datetime
from dataclasses_json.mm import ValidationError

class _IsoField:
    def __init__(self, required=False):
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

def test_none_value():
    field = _IsoField(required=False)
    model_instance = type('MyModel', (object,), {'field': field})()
    
    # Test when value is None and the field is not required
    assert field._serialize(None, "field", model_instance) is None

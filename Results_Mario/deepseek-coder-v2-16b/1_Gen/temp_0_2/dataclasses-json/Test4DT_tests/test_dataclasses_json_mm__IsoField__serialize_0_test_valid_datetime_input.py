
import pytest
from datetime import datetime
from dataclasses_json.mm import ValidationError

class _IsoField:
    def __init__(self):
        self.required = False
        self.default_error_messages = {"required": "This field is required"}
    
    def _serialize(self, value, attr, obj, **kwargs):
        if value is not None:
            return value.isoformat()
        else:
            if not self.required:
                return None
            else:
                raise ValidationError(self.default_error_messages["required"])

def test_valid_datetime_input():
    obj = _IsoField()
    obj.required = False  # Set the field to be optional
    
    value = datetime(2023, 10, 5, 12, 0)
    result = obj._serialize(value, "test_attr", obj)
    
    assert result == '2023-10-05T12:00:00'


import pytest
from dataclasses_json import ValidationError
from datetime import datetime

class _TimestampField:
    def __init__(self, required=True):
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
    
    with pytest.raises(ValidationError) as e:
        field._serialize(value=None, attr="test_attr", obj={})
        
    assert str(e.value) == "This field is required"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm__TimestampField__serialize_5_test_required_error
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__TimestampField__serialize_5_test_required_error.py:3:0: E0611: No name 'ValidationError' in module 'dataclasses_json' (no-name-in-module)


"""
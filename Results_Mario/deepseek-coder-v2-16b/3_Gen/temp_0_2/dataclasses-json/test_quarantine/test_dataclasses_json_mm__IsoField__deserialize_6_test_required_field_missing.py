
import pytest
from dataclasses_json import ValidationError
from datetime import datetime

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

def test_required_field_missing():
    field = _IsoField()
    with pytest.raises(ValidationError) as excinfo:
        field._deserialize(None, attr="some_attr", data={"some_attr": None})
    assert str(excinfo.value) == "Required field 'some_attr' is missing."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm__IsoField__deserialize_6_test_required_field_missing
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__IsoField__deserialize_6_test_required_field_missing.py:3:0: E0611: No name 'ValidationError' in module 'dataclasses_json' (no-name-in-module)


"""
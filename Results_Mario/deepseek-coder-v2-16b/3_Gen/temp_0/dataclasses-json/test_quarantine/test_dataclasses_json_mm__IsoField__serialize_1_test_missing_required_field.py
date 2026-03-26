
from dataclasses import dataclass
from datetime import datetime
from dataclasses_json.mm import ValidationError
import pytest

@dataclass
class _IsoField:
    required: bool = False
    default_error_messages: dict = None

def test_missing_required_field():
    field = _IsoField(required=True)
    
    with pytest.raises(ValidationError) as excinfo:
        field._serialize(None, "test_attr", None)
        
    assert str(excinfo.value) == "_IsoField('test_attr') is required"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm__IsoField__serialize_1_test_missing_required_field
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__IsoField__serialize_1_test_missing_required_field.py:16:8: E1101: Instance of '_IsoField' has no '_serialize' member (no-member)


"""
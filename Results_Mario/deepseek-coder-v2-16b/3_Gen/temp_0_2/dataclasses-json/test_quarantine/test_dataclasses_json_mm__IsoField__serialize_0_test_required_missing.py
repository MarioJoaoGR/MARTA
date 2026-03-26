
from dataclasses import dataclass
from datetime import datetime
from dataclasses_json.mm import ValidationError
import pytest

@dataclass
class _IsoField:
    required: bool = True
    default_error_messages: dict = None

def test_required_missing():
    iso_field = _IsoField(required=True)
    
    with pytest.raises(ValidationError) as exc_info:
        iso_field._serialize(None, attr="test", obj=None)
    
    assert str(exc_info.value) == '_IsoField default_error_messages["required"]'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm__IsoField__serialize_0_test_required_missing
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__IsoField__serialize_0_test_required_missing.py:16:8: E1101: Instance of '_IsoField' has no '_serialize' member (no-member)


"""

from datetime import datetime
import pytest
from dataclasses_json.mm import _TimestampField
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from marshmallow import ValidationError

@dataclass
@dataclass_json
class TestModel:
    timestamp: _TimestampField = None

def test_missing_value():
    with pytest.raises(ValidationError) as excinfo:
        model = TestModel()
        serialized_data = model.to_dict()
    
    assert str(excinfo.value) == '_TimestampField is required and has no value'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm__TimestampField__serialize_1_test_missing_value
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__TimestampField__serialize_1_test_missing_value.py:17:26: E1101: Instance of 'TestModel' has no 'to_dict' member (no-member)

"""
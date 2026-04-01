
from dataclasses import dataclass
import pytest
from dataclasses_json.mm import _TimestampField, _deserialize
from datetime import datetime, timezone

@pytest.fixture
def timestamp_field():
    return _TimestampField()

def test_missing_value_error(timestamp_field):
    with pytest.raises(ValidationError) as excinfo:
        timestamp_field._deserialize(None, attr="timestamp", data={})
    assert str(excinfo.value) == '_TimestampField requires the field to be set.'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm__TimestampField__deserialize_2_test_missing_value_error
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__TimestampField__deserialize_2_test_missing_value_error.py:4:0: E0611: No name '_deserialize' in module 'dataclasses_json.mm' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__TimestampField__deserialize_2_test_missing_value_error.py:12:23: E0602: Undefined variable 'ValidationError' (undefined-variable)


"""
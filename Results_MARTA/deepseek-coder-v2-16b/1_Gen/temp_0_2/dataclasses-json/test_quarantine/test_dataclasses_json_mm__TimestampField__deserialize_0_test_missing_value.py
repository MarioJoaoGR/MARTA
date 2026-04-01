
import pytest
from dataclasses_json.mm import _TimestampField, ValidationError
from datetime import datetime, timezone

def test_missing_value():
    field = _TimestampField(required=True)
    data = {}  # No timestamp provided
    
    with pytest.raises(ValidationError) as excinfo:
        field._deserialize("timestamp", None, data)
        
    assert "Required" in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__TimestampField__deserialize_0_test_missing_value.py F [100%]

=================================== FAILURES ===================================
______________________________ test_missing_value ______________________________

    def test_missing_value():
        field = _TimestampField(required=True)
        data = {}  # No timestamp provided
    
        with pytest.raises(ValidationError) as excinfo:
>           field._deserialize("timestamp", None, data)

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__TimestampField__deserialize_0_test_missing_value.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
dataclasses-json/dataclasses_json/mm.py:40: in _deserialize
    return _timestamp_to_dt_aware(value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

timestamp = 'timestamp'

    def _timestamp_to_dt_aware(timestamp: float):
        tz = datetime.now(timezone.utc).astimezone().tzinfo
>       dt = datetime.fromtimestamp(timestamp, tz=tz)
E       TypeError: 'str' object cannot be interpreted as an integer

dataclasses-json/dataclasses_json/utils.py:174: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__TimestampField__deserialize_0_test_missing_value.py::test_missing_value
============================== 1 failed in 0.04s ===============================
"""
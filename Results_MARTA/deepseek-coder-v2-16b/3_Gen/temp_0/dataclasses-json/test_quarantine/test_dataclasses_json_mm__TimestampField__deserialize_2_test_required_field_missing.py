
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from datetime import datetime, timezone
import pytest
from dataclasses_json.mm import ValidationError

@dataclass_json
@dataclass
class TimestampFieldTest:
    timestamp: float = None  # Default to None for optional field

def test_required_field_missing():
    with pytest.raises(ValidationError) as excinfo:
        TimestampFieldTest()
    assert str(excinfo.value) == "Required field 'timestamp' is missing."

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__TimestampField__deserialize_2_test_required_field_missing.py F [100%]

=================================== FAILURES ===================================
_________________________ test_required_field_missing __________________________

    def test_required_field_missing():
>       with pytest.raises(ValidationError) as excinfo:
E       Failed: DID NOT RAISE <class 'marshmallow.exceptions.ValidationError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__TimestampField__deserialize_2_test_required_field_missing.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__TimestampField__deserialize_2_test_required_field_missing.py::test_required_field_missing
============================== 1 failed in 0.05s ===============================
"""

import pytest
from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID
from dataclasses_json.core import _support_extended_types


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_core__support_extended_types_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________ test_valid_input_unix_timestamp ________________________

    def test_valid_input_unix_timestamp():
        unix_time = int(datetime.now().timestamp())
        field_type = datetime
        field_value = unix_time
        result = _support_extended_types(field_type, field_value)
        assert isinstance(result, datetime), f"Expected datetime object but got {type(result)}"
        # Check if the converted datetime is close to the current time (within a second precision)
>       assert abs((result - datetime.now()).total_seconds()) < 1, "Converted datetime should be close to the current time"
E       TypeError: can't subtract offset-naive and offset-aware datetimes

/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_core__support_extended_types_1.py:15: TypeError
__________________________ test_invalid_input_string ___________________________

    def test_invalid_input_string():
        field_type = UUID
        field_value = 'not a valid UUID'
        with pytest.raises(ValueError) as excinfo:
            _support_extended_types(field_type, field_value)
>       assert str(excinfo.value) == "Invalid UUID string: not a valid UUID", "Expected ValueError for invalid UUID input"
E       AssertionError: Expected ValueError for invalid UUID input
E       assert 'badly formed...l UUID string' == 'Invalid UUID... a valid UUID'
E         
E         - Invalid UUID string: not a valid UUID
E         + badly formed hexadecimal UUID string

/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_core__support_extended_types_1.py:22: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_core__support_extended_types_1.py::test_valid_input_unix_timestamp
FAILED ../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_core__support_extended_types_1.py::test_invalid_input_string
============================== 2 failed in 0.09s ===============================
"""
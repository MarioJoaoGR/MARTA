
from string_utils.generation import uuid
import pytest

def test_invalid_input_none():
    with pytest.raises(TypeError):
        assert uuid(None) is None  # This should raise a TypeError since the function expects a bool, not None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_generation_uuid_1_test_invalid_input_none.py F [100%]

=================================== FAILURES ===================================
___________________________ test_invalid_input_none ____________________________

    def test_invalid_input_none():
        with pytest.raises(TypeError):
>           assert uuid(None) is None  # This should raise a TypeError since the function expects a bool, not None
E           AssertionError: assert '15b4884e-d3ca-4203-8a67-16fe69035cbb' is None
E            +  where '15b4884e-d3ca-4203-8a67-16fe69035cbb' = uuid(None)

python-string-utils/Test4DT_tests/test_string_utils_generation_uuid_1_test_invalid_input_none.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_generation_uuid_1_test_invalid_input_none.py::test_invalid_input_none
============================== 1 failed in 0.03s ===============================
"""
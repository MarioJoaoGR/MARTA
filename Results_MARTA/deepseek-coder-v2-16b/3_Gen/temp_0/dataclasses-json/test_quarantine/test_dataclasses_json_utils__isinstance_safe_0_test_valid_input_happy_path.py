
import pytest
from dataclasses_json.utils import _isinstance_safe

def test_valid_input_happy_path():
    # Test cases for valid input where the function should return True
    assert _isinstance_safe([1, 2, 3], list) == True
    assert _isinstance_safe(42, int) == True
    assert _isinstance_safe("hello", str) == False

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__isinstance_safe_0_test_valid_input_happy_path.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_happy_path __________________________

    def test_valid_input_happy_path():
        # Test cases for valid input where the function should return True
        assert _isinstance_safe([1, 2, 3], list) == True
        assert _isinstance_safe(42, int) == True
>       assert _isinstance_safe("hello", str) == False
E       AssertionError: assert True == False
E        +  where True = _isinstance_safe('hello', str)

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__isinstance_safe_0_test_valid_input_happy_path.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__isinstance_safe_0_test_valid_input_happy_path.py::test_valid_input_happy_path
============================== 1 failed in 0.03s ===============================
"""
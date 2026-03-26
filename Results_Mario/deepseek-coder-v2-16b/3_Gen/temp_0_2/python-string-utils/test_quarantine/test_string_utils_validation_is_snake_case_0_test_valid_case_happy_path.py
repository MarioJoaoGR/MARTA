
import re
from typing import Any
from string_utils.validation import is_snake_case

def test_invalid_case_with_uppercase():
    # Test a string with uppercase letters, which should return False
    assert not is_snake_case('Foo_Bar')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_0_test_valid_case_happy_path.py F [100%]

=================================== FAILURES ===================================
_______________________ test_invalid_case_with_uppercase _______________________

    def test_invalid_case_with_uppercase():
        # Test a string with uppercase letters, which should return False
>       assert not is_snake_case('Foo_Bar')
E       AssertionError: assert not True
E        +  where True = is_snake_case('Foo_Bar')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_0_test_valid_case_happy_path.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_0_test_valid_case_happy_path.py::test_invalid_case_with_uppercase
============================== 1 failed in 0.03s ===============================
"""
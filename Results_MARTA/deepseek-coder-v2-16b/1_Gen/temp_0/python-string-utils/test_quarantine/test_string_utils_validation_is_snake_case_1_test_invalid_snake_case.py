
import re
from string_utils.validation import is_snake_case

def test_invalid_snake_case():
    # Test cases for invalid snake case strings
    assert not is_snake_case('FooBarBaz')  # Contains uppercase letters
    assert not is_snake_case('foo-bar')     # Contains hyphen instead of underscore
    assert not is_snake_case('1foo_bar')    # Starts with a number
    assert not is_snake_case('_foo_bar')    # Starts with an underscore

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_1_test_invalid_snake_case.py F [100%]

=================================== FAILURES ===================================
___________________________ test_invalid_snake_case ____________________________

    def test_invalid_snake_case():
        # Test cases for invalid snake case strings
        assert not is_snake_case('FooBarBaz')  # Contains uppercase letters
        assert not is_snake_case('foo-bar')     # Contains hyphen instead of underscore
        assert not is_snake_case('1foo_bar')    # Starts with a number
>       assert not is_snake_case('_foo_bar')    # Starts with an underscore
E       AssertionError: assert not True
E        +  where True = is_snake_case('_foo_bar')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_1_test_invalid_snake_case.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_1_test_invalid_snake_case.py::test_invalid_snake_case
============================== 1 failed in 0.03s ===============================

"""
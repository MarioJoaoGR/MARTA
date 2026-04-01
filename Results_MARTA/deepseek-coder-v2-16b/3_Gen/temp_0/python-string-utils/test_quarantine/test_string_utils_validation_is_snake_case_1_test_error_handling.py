
import pytest
from string_utils.validation import is_snake_case

def test_error_handling():
    # Test non-string inputs
    assert not is_snake_case(12345)  # Non-string input
    assert not is_snake_case(None)   # Non-string input
    assert not is_snake_case([])     # Non-string input
    assert not is_snake_case({})     # Non-string input
    
    # Test with invalid snake case strings
    assert not is_snake_case('Foo_bar')  # Uppercase letter in the middle
    assert not is_snake_case('fooBar')   # Mixed case letters
    assert not is_snake_case('foo-bar')  # Invalid separator
    assert not is_snake_case('foo123bar')# Starts with a number

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_1_test_error_handling.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_error_handling ______________________________

    def test_error_handling():
        # Test non-string inputs
        assert not is_snake_case(12345)  # Non-string input
        assert not is_snake_case(None)   # Non-string input
        assert not is_snake_case([])     # Non-string input
        assert not is_snake_case({})     # Non-string input
    
        # Test with invalid snake case strings
>       assert not is_snake_case('Foo_bar')  # Uppercase letter in the middle
E       AssertionError: assert not True
E        +  where True = is_snake_case('Foo_bar')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_1_test_error_handling.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_1_test_error_handling.py::test_error_handling
============================== 1 failed in 0.03s ===============================
"""
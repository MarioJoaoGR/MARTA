
import re
from unittest.mock import patch
from string_utils.validation import is_snake_case

def test_valid_case():
    # Test a valid snake case string
    with patch('string_utils.validation.SNAKE_CASE_TEST_RE', new=re.compile(r'^[a-z]+(_[a-z]+)*$')):
        with patch('string_utils.validation.SNAKE_CASE_TEST_DASH_RE', new=re.compile(r'^[a-z]+(-[a-z]+)*$')):
            assert is_snake_case('foo_bar_baz') == True
            assert is_snake_case('foo_123_bar') == True
            assert is_snake_case('foo_bar') == True
            assert is_snake_case('foo') == False
            assert is_snake_case('Foo_Bar') == False
            assert is_snake_case('foo-bar') == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        # Test a valid snake case string
        with patch('string_utils.validation.SNAKE_CASE_TEST_RE', new=re.compile(r'^[a-z]+(_[a-z]+)*$')):
            with patch('string_utils.validation.SNAKE_CASE_TEST_DASH_RE', new=re.compile(r'^[a-z]+(-[a-z]+)*$')):
                assert is_snake_case('foo_bar_baz') == True
>               assert is_snake_case('foo_123_bar') == True
E               AssertionError: assert False == True
E                +  where False = is_snake_case('foo_123_bar')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_0_test_valid_case.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.03s ===============================
"""
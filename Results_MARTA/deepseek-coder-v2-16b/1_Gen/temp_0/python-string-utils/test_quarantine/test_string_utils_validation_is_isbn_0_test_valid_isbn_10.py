
import pytest
from string_utils.validation import is_isbn

def test_valid_isbn_10():
    input_string = '037429685X'
    assert is_isbn(input_string) == True, "Expected valid ISBN-10 to return true"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_0_test_valid_isbn_10.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_isbn_10 ______________________________

    def test_valid_isbn_10():
        input_string = '037429685X'
>       assert is_isbn(input_string) == True, "Expected valid ISBN-10 to return true"
E       AssertionError: Expected valid ISBN-10 to return true
E       assert False == True
E        +  where False = is_isbn('037429685X')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_0_test_valid_isbn_10.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_0_test_valid_isbn_10.py::test_valid_isbn_10
============================== 1 failed in 0.03s ===============================

"""
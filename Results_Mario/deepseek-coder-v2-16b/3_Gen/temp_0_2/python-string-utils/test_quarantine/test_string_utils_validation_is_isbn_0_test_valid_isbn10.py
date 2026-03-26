
import pytest
from string_utils.validation import is_isbn, __ISBNChecker

def test_valid_isbn10():
    input_string = '0471606957'
    checker = __ISBNChecker(input_string, True)
    assert checker.is_isbn_10() is True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_0_test_valid_isbn10.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_isbn10 _______________________________

    def test_valid_isbn10():
        input_string = '0471606957'
        checker = __ISBNChecker(input_string, True)
>       assert checker.is_isbn_10() is True
E       assert False is True
E        +  where False = is_isbn_10()
E        +    where is_isbn_10 = <string_utils.validation.__ISBNChecker object at 0x1062b6170>.is_isbn_10

python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_0_test_valid_isbn10.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_0_test_valid_isbn10.py::test_valid_isbn10
============================== 1 failed in 0.02s ===============================
"""
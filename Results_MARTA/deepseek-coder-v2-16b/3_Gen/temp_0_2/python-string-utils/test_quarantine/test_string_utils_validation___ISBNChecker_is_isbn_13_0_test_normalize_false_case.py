
import pytest
from string_utils.validation import __ISBNChecker, InvalidInputError

def test_normalize_false_case():
    checker = __ISBNChecker('978-0-470-05902-9', normalize=False)
    assert checker.input_string == '978-0-470-05902-9'
    assert checker.is_isbn_13() is True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_0_test_normalize_false_case.py F [100%]

=================================== FAILURES ===================================
__________________________ test_normalize_false_case ___________________________

    def test_normalize_false_case():
        checker = __ISBNChecker('978-0-470-05902-9', normalize=False)
        assert checker.input_string == '978-0-470-05902-9'
>       assert checker.is_isbn_13() is True
E       assert False is True
E        +  where False = is_isbn_13()
E        +    where is_isbn_13 = <string_utils.validation.__ISBNChecker object at 0x105fa9d50>.is_isbn_13

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_0_test_normalize_false_case.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_0_test_normalize_false_case.py::test_normalize_false_case
============================== 1 failed in 0.03s ===============================
"""
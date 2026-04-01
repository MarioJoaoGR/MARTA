
import pytest
from string_utils.validation import __ISBNChecker, InvalidInputError

def test_valid_input_happy_path():
    checker = __ISBNChecker("9780470059029")
    assert checker.is_isbn_13() is True

    checker = __ISBNChecker("978-0-470-05902-9", normalize=False)
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

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_0_test_valid_input_happy_path.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_happy_path __________________________

    def test_valid_input_happy_path():
        checker = __ISBNChecker("9780470059029")
        assert checker.is_isbn_13() is True
    
        checker = __ISBNChecker("978-0-470-05902-9", normalize=False)
>       assert checker.is_isbn_13() is True
E       assert False is True
E        +  where False = is_isbn_13()
E        +    where is_isbn_13 = <string_utils.validation.__ISBNChecker object at 0x1060d93f0>.is_isbn_13

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_0_test_valid_input_happy_path.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_0_test_valid_input_happy_path.py::test_valid_input_happy_path
============================== 1 failed in 0.02s ===============================
"""
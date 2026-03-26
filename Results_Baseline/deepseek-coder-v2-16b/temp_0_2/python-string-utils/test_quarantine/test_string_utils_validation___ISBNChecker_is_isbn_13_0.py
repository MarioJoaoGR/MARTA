
import pytest
from string_utils.validation import __ISBNChecker

class InvalidInputError(Exception):
    pass

# Test cases for initializing an __ISBNChecker object with different inputs
def test_init_with_valid_isbn():
    checker = __ISBNChecker('978-0-13-235088-4')
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_0.py . [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
______________________ test_init_with_invalid_non_string _______________________

    def test_init_with_invalid_non_string():
        with pytest.raises(InvalidInputError):
>           __ISBNChecker(123456)

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_0.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <string_utils.validation.__ISBNChecker object at 0x102150310>
input_string = 123456, normalize = True

    def __init__(self, input_string: str, normalize: bool = True):
        if not is_string(input_string):
>           raise InvalidInputError(input_string)
E           string_utils.errors.InvalidInputError: Expected "str", received "int"

python-string-utils/string_utils/validation.py:45: InvalidInputError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_0.py::test_init_with_invalid_non_string
========================= 1 failed, 2 passed in 0.02s ==========================

"""
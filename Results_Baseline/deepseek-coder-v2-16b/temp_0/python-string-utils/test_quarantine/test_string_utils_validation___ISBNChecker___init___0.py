
import pytest
from string_utils.validation import __ISBNChecker

class InvalidInputError(Exception):
    pass

# Test cases for __ISBNChecker class
def test__init__valid_isbn():
    checker = __ISBNChecker("978-0-13-235088-4")
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___0.py . [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
__________________________ test__init__invalid_input ___________________________

    def test__init__invalid_input():
        with pytest.raises(InvalidInputError):
>           __ISBNChecker(12345)

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___0.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <string_utils.validation.__ISBNChecker object at 0x10700bcd0>
input_string = 12345, normalize = True

    def __init__(self, input_string: str, normalize: bool = True):
        if not is_string(input_string):
>           raise InvalidInputError(input_string)
E           string_utils.errors.InvalidInputError: Expected "str", received "int"

python-string-utils/string_utils/validation.py:45: InvalidInputError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___0.py::test__init__invalid_input
========================= 1 failed, 2 passed in 0.02s ==========================

"""

from string_utils.validation import is_isbn
import pytest

def test_none_input():
    assert not is_isbn(None)  # Test for None input

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_1_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
>       assert not is_isbn(None)  # Test for None input

python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_1_test_none_input.py:6: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
python-string-utils/string_utils/validation.py:656: in is_isbn
    checker = __ISBNChecker(input_string, normalize)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <string_utils.validation.__ISBNChecker object at 0x101f2cf10>
input_string = None, normalize = True

    def __init__(self, input_string: str, normalize: bool = True):
        if not is_string(input_string):
>           raise InvalidInputError(input_string)
E           string_utils.errors.InvalidInputError: Expected "str", received "NoneType"

python-string-utils/string_utils/validation.py:45: InvalidInputError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_1_test_none_input.py::test_none_input
============================== 1 failed in 0.03s ===============================

"""
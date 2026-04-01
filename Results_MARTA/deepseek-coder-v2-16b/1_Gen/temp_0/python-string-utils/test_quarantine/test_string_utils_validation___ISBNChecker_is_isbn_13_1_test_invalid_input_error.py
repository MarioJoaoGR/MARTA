
from string_utils.validation import __ISBNChecker, InvalidInputError

def test_invalid_input_error():
    try:
        checker = __ISBNChecker(123456)
    except InvalidInputError as e:
        assert str(e) == "123456 is not a valid string."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_1_test_invalid_input_error.py F [100%]

=================================== FAILURES ===================================
___________________________ test_invalid_input_error ___________________________

    def test_invalid_input_error():
        try:
>           checker = __ISBNChecker(123456)

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_1_test_invalid_input_error.py:6: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <string_utils.validation.__ISBNChecker object at 0x105f08f70>
input_string = 123456, normalize = True

    def __init__(self, input_string: str, normalize: bool = True):
        if not is_string(input_string):
>           raise InvalidInputError(input_string)
E           string_utils.errors.InvalidInputError: Expected "str", received "int"

python-string-utils/string_utils/validation.py:45: InvalidInputError

During handling of the above exception, another exception occurred:

    def test_invalid_input_error():
        try:
            checker = __ISBNChecker(123456)
        except InvalidInputError as e:
>           assert str(e) == "123456 is not a valid string."
E           assert 'Expected "st...eceived "int"' == '123456 is no...valid string.'
E             
E             - 123456 is not a valid string.
E             + Expected "str", received "int"

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_1_test_invalid_input_error.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_1_test_invalid_input_error.py::test_invalid_input_error
============================== 1 failed in 0.03s ===============================

"""
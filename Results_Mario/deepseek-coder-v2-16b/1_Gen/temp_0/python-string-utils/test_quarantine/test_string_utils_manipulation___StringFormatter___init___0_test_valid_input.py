
import pytest
from string_utils.manipulation import is_string
from __StringFormatter import InvalidInputError

class __StringFormatter:
    def __init__(self, input_string):
        if not is_string(input_string):
            raise InvalidInputError(input_string)
        self.input_string = input_string

def test_valid_input():
    formatter = __StringFormatter("valid string")
    assert formatter.input_string == "valid string"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___init___0_test_valid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___init___0_test_valid_input.py:4:0: E0401: Unable to import '__StringFormatter' (import-error)

"""
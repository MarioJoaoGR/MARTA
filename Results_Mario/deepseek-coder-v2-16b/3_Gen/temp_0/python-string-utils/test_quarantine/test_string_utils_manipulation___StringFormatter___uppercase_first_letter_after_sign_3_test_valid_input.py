
import re
from unittest.mock import patch
from string_utils.manipulation import is_string, InvalidInputError
from __StringFormatter import __StringFormatter

def test_valid_input():
    formatter = __StringFormatter("hello world")
    assert formatter.input_string == "hello world"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___uppercase_first_letter_after_sign_3_test_valid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___uppercase_first_letter_after_sign_3_test_valid_input.py:5:0: E0401: Unable to import '__StringFormatter' (import-error)


"""
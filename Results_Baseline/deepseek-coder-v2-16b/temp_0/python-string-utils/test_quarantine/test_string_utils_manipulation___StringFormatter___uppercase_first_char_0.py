
# Module: string_utils.manipulation
# string_utils.manipulation/test_string_formatter.py
from string_utils.manipulation import __StringFormatter
import pytest
from custom_exceptions import InvalidInputError  # Assuming this is the correct module for InvalidInputError

def test_valid_input():
    formatter = __StringFormatter("valid string")
    assert formatter.input_string == "valid string"

def test_invalid_input_type():
    with pytest.raises(InvalidInputError) as excinfo:
        __StringFormatter(12345)
    assert str(excinfo.value) == 'Expected "str", received "int"'

def test_format_method():
    formatter = __StringFormatter("hello world")
    formatted_string = formatter._StringFormatter__uppercase_first_char("hello world")
    assert formatted_string == "Hello World"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___uppercase_first_char_0
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___uppercase_first_char_0.py:6:0: E0401: Unable to import 'custom_exceptions' (import-error)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___uppercase_first_char_0.py:19:23: E1101: Instance of '__StringFormatter' has no '_StringFormatter__uppercase_first_char' member (no-member)

"""
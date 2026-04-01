
import pytest
from string_utils.manipulation import __StringFormatter

def test_uppercase_first_char():
    # Create an instance of __StringFormatter with a valid input string
    formatter = __StringFormatter("hello world")
    
    # Call the private method __uppercase_first_char directly on the instance
    result = formatter._StringFormatter__uppercase_first_char(formatter.input_string)
    
    # Assert that the result is what we expect (the first character of each word capitalized)
    assert result == "Hello World"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___uppercase_first_char_3_test_valid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___uppercase_first_char_3_test_valid_input.py:10:13: E1101: Instance of '__StringFormatter' has no '_StringFormatter__uppercase_first_char' member (no-member)


"""
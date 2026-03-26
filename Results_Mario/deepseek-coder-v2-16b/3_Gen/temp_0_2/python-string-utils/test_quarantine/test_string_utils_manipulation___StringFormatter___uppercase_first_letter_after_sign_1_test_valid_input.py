
from string_utils.manipulation import StringFormatter
import re
import pytest

def test_valid_input():
    # Arrange
    formatter = StringFormatter("hello world")
    
    # Act
    formatted_string = formatter.format_string()
    
    # Assert
    assert isinstance(formatted_string, str)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___uppercase_first_letter_after_sign_1_test_valid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___uppercase_first_letter_after_sign_1_test_valid_input.py:2:0: E0611: No name 'StringFormatter' in module 'string_utils.manipulation' (no-name-in-module)


"""
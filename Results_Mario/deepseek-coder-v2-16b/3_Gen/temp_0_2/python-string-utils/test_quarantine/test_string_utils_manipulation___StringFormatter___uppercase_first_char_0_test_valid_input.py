
import pytest
from string_utils.manipulation import __StringFormatter

def test_valid_input():
    # Arrange
    input_string = "hello world"
    expected_output = "Hello World"  # Assuming the method capitalizes the first character of each word
    
    # Act
    formatter = __StringFormatter(input_string)
    formatted_string = formatter.format_string()
    
    # Assert
    assert formatted_string == expected_output, f"Expected '{expected_output}', but got '{formatted_string}'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___uppercase_first_char_0_test_valid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___uppercase_first_char_0_test_valid_input.py:12:23: E1101: Instance of '__StringFormatter' has no 'format_string' member (no-member)


"""

# Module: string_utils.manipulation
import pytest
from string_utils.manipulation import __StringFormatter

# Test cases for __uppercase_first_letter_after_sign method in __StringFormatter class
def test_uppercase_first_letter_after_sign():
    # Create an instance of __StringFormatter with a valid input string
    formatter = __StringFormatter("hello world")
    
    # Define the regex match object for testing
    import re
    regex_match = re.match(0, "h", "ello world")
    
    # Call the method to be tested
    result = formatter.__uppercase_first_letter_after_sign(regex_match)
    
    # Assert that the result is as expected
    assert result == "hello World"

def test_uppercase_first_letter_after_sign_invalid():
    # Create an instance of __StringFormatter with a valid input string
    formatter = __StringFormatter("hello world")
    
    # Define the regex match object for testing (should raise an error)
    import re
    regex_match = re.match(0, "", "ello world")  # Empty match should raise an error
    
    # Call the method to be tested and expect a InvalidInputError
    with pytest.raises(InvalidInputError):
        formatter.__uppercase_first_letter_after_sign(regex_match)

def test_uppercase_first_letter_after_sign_no_change():
    # Create an instance of __StringFormatter with a valid input string
    formatter = __StringFormatter("hello world")
    
    # Define the regex match object for testing (should not change anything)
    import re
    regex_match = re.match(0, "w", "orld")  # No uppercase needed here
    
    # Call the method to be tested
    result = formatter.__uppercase_first_letter_after_sign(regex_match)
    
    # Assert that the result is as expected (no change)
    assert result == "hello world"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___uppercase_first_letter_after_sign_0
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___uppercase_first_letter_after_sign_0.py:30:23: E0602: Undefined variable 'InvalidInputError' (undefined-variable)

"""
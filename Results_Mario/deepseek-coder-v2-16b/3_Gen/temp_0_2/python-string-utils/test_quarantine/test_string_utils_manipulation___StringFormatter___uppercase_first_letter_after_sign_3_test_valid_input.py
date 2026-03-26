
import re
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_uppercase_first_letter_after_sign():
    # Create an instance of __StringFormatter with a sample input string
    formatter = __StringFormatter("hello-world")
    
    # Define the regex pattern to match the part after the sign (e.g., '-')
    regex_pattern = r'([a-zA-Z])-'  # This assumes we are looking for letters followed by a hyphen
    
    # Use re.sub to replace the matched pattern with the first letter uppercase and rest unchanged
    formatted_string = formatter._StringFormatter__uppercase_first_letter_after_sign(regex_pattern, "hello-world")
    
    # Assert that the result is as expected after the transformation
    assert formatted_string == "hello-World"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___uppercase_first_letter_after_sign_3_test_valid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___uppercase_first_letter_after_sign_3_test_valid_input.py:13:23: E1101: Instance of '__StringFormatter' has no '_StringFormatter__uppercase_first_letter_after_sign' member (no-member)


"""
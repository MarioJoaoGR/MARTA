
import re
from string_utils.manipulation import __StringFormatter

def test_valid_input():
    formatter = __StringFormatter("Hello World")
    regex_pattern = r"(\s+)(.*)(\s+)"
    match = re.match(regex_pattern, " Hello World ")
    
    # Call the private method using a mock or direct call since it's now part of the class
    formatted_string = formatter._StringFormatter__remove_internal_spaces(match)
    
    assert formatted_string == "HelloWorld", f"Expected 'HelloWorld', but got '{formatted_string}'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___remove_internal_spaces_0_test_valid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___remove_internal_spaces_0_test_valid_input.py:11:23: E1101: Instance of '__StringFormatter' has no '_StringFormatter__remove_internal_spaces' member (no-member)


"""
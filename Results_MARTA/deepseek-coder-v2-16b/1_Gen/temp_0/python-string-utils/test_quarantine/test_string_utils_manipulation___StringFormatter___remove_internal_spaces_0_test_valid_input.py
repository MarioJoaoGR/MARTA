
import pytest
from string_utils.manipulation import __StringFormatter

def test_valid_input():
    # Arrange
    formatter = __StringFormatter("valid string")
    
    # Act
    formatted_string = formatter._StringFormatter__remove_internal_spaces(r"(\s+)(.*)(\s+)")
    
    # Assert
    assert formatted_string == "valid string".replace(" ", "")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___remove_internal_spaces_0_test_valid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___remove_internal_spaces_0_test_valid_input.py:10:23: E1101: Instance of '__StringFormatter' has no '_StringFormatter__remove_internal_spaces' member (no-member)

"""
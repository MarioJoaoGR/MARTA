
import re
from unittest.mock import patch
from string_utils.manipulation import is_string, InvalidInputError
from string_formatter import __StringFormatter

def test_valid_input():
    # Arrange
    formatter = __StringFormatter("valid string")
    
    # Act and Assert
    assert isinstance(formatter.input_string, str)
    assert formatter.input_string == "valid string"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___remove_duplicates_1_test_valid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___remove_duplicates_1_test_valid_input.py:5:0: E0401: Unable to import 'string_formatter' (import-error)


"""
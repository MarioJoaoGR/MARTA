
import pytest
from string_utils.manipulation import booleanize
from custom_exceptions import InvalidInputError

def test_valid_input_true():
    # Test when input is 'true'
    assert booleanize('true') == True
    assert booleanize('YES') == True  # Case insensitive test
    assert booleanize('tRuE') == True  # Mixed case test

# Add a test for invalid input to ensure the function handles it correctly
def test_invalid_input():
    with pytest.raises(InvalidInputError):
        booleanize(123)  # Invalid type, should raise InvalidInputError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation_booleanize_0_test_valid_input_true
python-string-utils/Test4DT_tests/test_string_utils_manipulation_booleanize_0_test_valid_input_true.py:4:0: E0401: Unable to import 'custom_exceptions' (import-error)


"""
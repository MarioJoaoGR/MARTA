
import pytest
from string_utils.manipulation import booleanize

class InvalidInputError(Exception):
    pass

# Test cases for the booleanize function
def test_basic_usage():
    assert booleanize('true') == True
    assert booleanize('YES') == True
    assert booleanize('nope') == False

def test_edge_cases():
    # Empty string should return False
    assert booleanize('') == False
    # Whitespace-only string should return False
    assert booleanize(' ') == False
    # Numeric strings
    assert booleanize('1') == True
    assert booleanize('0') == False

def test_case_sensitivity():
    # Mixed case input should be treated as true
    assert booleanize('TrUe') == True

# Test for non-string inputs to ensure InvalidInputError is raised
def test_invalid_input():
    with pytest.raises(InvalidInputError):
        booleanize(123)

# Additional valid and invalid string inputs
def test_valid_inputs():
    assert booleanize('true') == True
    assert booleanize('YES') == True
    assert booleanize('1') == True
    assert booleanize('yes') == True
    assert booleanize('y') == True
    assert booleanize('false') == False
    assert booleanize('NO') == False
    assert booleanize('0') == False
    assert booleanize('no') == False
    assert booleanize('n') == False

def test_invalid_inputs():
    # Strings that should not be considered valid booleans
    assert booleanize('tRue') == False
    assert booleanize('123') == False
    assert booleanize('maybe') == False
    assert booleanize('yep') == True  # This might need to be adjusted based on exact definition of "yes" in the function

# Edge cases for empty strings and whitespace-only strings
def test_edge_cases():
    assert booleanize('') == False
    assert booleanize(' ') == False
    assert booleanize('   \t\n') == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation_booleanize_1
python-string-utils/Test4DT_tests/test_string_utils_manipulation_booleanize_1.py:53:0: E0102: function already defined line 14 (function-redefined)

"""
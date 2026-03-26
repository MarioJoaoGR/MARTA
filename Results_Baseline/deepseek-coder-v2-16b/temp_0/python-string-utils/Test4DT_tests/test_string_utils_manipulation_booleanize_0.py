
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

import pytest
from unittest.mock import patch
from string_utils.manipulation import booleanize, InvalidInputError

# Test valid inputs
def test_valid_inputs():
    assert booleanize('true') == True
    assert booleanize('YES') == True
    assert booleanize('1') == True
    assert booleanize('y') == True
    assert booleanize('false') == False
    assert booleanize('NO') == False
    assert booleanize('0') == False
    assert booleanize('n') == False

# Test edge cases
def test_edge_cases():
    # None input should raise InvalidInputError
    with pytest.raises(InvalidInputError):
        booleanize(None)
    
    # Empty string should return False
    assert booleanize('') == False
    
    # Non-string values should raise InvalidInputError
    with pytest.raises(InvalidInputError):
        booleanize(12345)

# Test invalid inputs
def test_invalid_inputs():
    # None input should raise InvalidInputError
    with pytest.raises(InvalidInputError):
        booleanize(None)
    
    # Non-string values should raise InvalidInputError
    with pytest.raises(InvalidInputError):
        booleanize(12345)

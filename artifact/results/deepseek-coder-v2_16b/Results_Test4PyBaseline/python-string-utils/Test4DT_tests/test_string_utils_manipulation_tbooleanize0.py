# Module: string_utils.manipulation
import pytest
from string_utils.manipulation import booleanize
from string_utils.errors import InvalidInputError

# Test case 1: Passing a string that should return True
def test_booleanize_true():
    assert booleanize('true') == True
    assert booleanize('YES') == True
    assert booleanize('yEs') == True

# Test case 2: Passing a string that should return False
def test_booleanize_false():
    assert booleanize('nope') == False
    assert booleanize('NO') == False
    assert booleanize('nonono') == False

# Test case 3: Passing an invalid input type to see the error handling in action
def test_booleanize_invalid_input():
    with pytest.raises(InvalidInputError):
        booleanize(12345)  # int is not a valid input type

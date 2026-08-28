
import pytest
from string_utils.manipulation import booleanize, InvalidInputError

# Test valid input 'true' returns True
def test_valid_true():
    input_string = 'true'
    assert booleanize(input_string) is True

# Test valid input 'YES' returns True
def test_valid_YES():
    input_string = 'YES'
    assert booleanize(input_string) is True

# Test valid input '1' returns True
def test_valid_1():
    input_string = '1'
    assert booleanize(input_string) is True

# Test valid input 'y' returns True
def test_valid_y():
    input_string = 'y'
    assert booleanize(input_string) is True

# Test invalid input that raises InvalidInputError
def test_invalid_case():
    input_string = 12345
    with pytest.raises(InvalidInputError):
        booleanize(input_string)

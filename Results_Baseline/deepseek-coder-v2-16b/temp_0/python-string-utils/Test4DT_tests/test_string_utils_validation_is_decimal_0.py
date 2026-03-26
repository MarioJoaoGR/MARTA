
import pytest
from string_utils.validation import is_decimal

# Test cases for the `is_decimal` function
def test_valid_decimal():
    assert is_decimal('42.0') == True, "Expected True for '42.0'"
    assert is_decimal('-123.45e6') == True, "Expected True for '-123.45e6'"
    assert is_decimal('+78.9') == True, "Expected True for '+78.9'"

def test_invalid_decimal():
    assert is_decimal('123') == False, "Expected False for '123'"
    assert is_decimal('abc') == False, "Expected False for 'abc'"

# Additional tests to cover edge cases and invalid inputs
def test_integer_not_decimal():
    assert is_decimal('42') == False, "Expected False for '42' (integer)"

def test_scientific_notation():
    assert is_decimal('-123.45e6') == True, "Expected True for '-123.45e6'"
    assert is_decimal('+78.9e-10') == False, "Expected False for '+78.9e-10'"

def test_invalid_scientific_notation():
    assert is_decimal('abcde') == False, "Expected False for 'abcde' (not a number in scientific notation)"

# Run the tests with pytest
if __name__ == "__main__":
    pytest.main()

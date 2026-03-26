# Module: string_utils.validation
import pytest
from string_utils.validation import is_isbn_13

# Test cases for the is_isbn_13 function
def test_valid_isbn_13():
    assert is_isbn_13('9780312498580') == True
    assert is_isbn_13('978-0312498580') == True

def test_invalid_isbn_13():
    assert is_isbn_13('978-0312498580', normalize=False) == False
    assert is_isbn_13('97803124985801') == False  # Invalid length
    assert is_isbn_13('invalid string') == False

def test_normalize_parameter():
    assert is_isbn_13('978-0312498580', normalize=True) == True
    assert is_isbn_13('978-0312498580', normalize=False) == False

if __name__ == "__main__":
    pytest.main()

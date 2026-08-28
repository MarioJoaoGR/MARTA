# Module: string_utils.validation
import pytest
from string_utils.validation import is_isbn_13

# Test cases for valid ISBN-13 numbers with default normalization
def test_valid_isbn_13():
    assert is_isbn_13('9780312498580') == True
    assert is_isbn_13('978-0312498580') == True

# Test cases for valid ISBN-13 numbers with normalization disabled
def test_valid_isbn_13_no_normalize():
    assert is_isbn_13('978-0312498580', normalize=False) == False
    assert is_isbn_13('9780312498580', normalize=False) == True  # Since normalization is disabled, this should pass

# Test cases for invalid ISBN-13 numbers
def test_invalid_isbn_13():
    assert is_isbn_13('978031249858') == False  # Incorrect length
    assert is_isbn_13('978-0312-49858-0') == True  # Valid but with extra hyphens, should pass due to normalization
    assert is_isbn_13('invalidinput') == False

# Test cases for non-string input
def test_non_string_input():
    with pytest.raises(TypeError):
        is_isbn_13(9780312498580)  # This should raise a TypeError since the input is not a string

# Module: string_utils.validation
import pytest
from string_utils.validation import is_isbn_13

# Test cases for valid ISBN-13 numbers
def test_valid_isbn_13():
    assert is_isbn_13('9780312498580') == True
    assert is_isbn_13('978-0312498580') == True

# Test cases for invalid ISBN-13 numbers with hyphens but should pass normalization
def test_invalid_isbn_13_with_hyphens():
    assert is_isbn_13('978-0312498580', normalize=False) == False

# Test cases for valid ISBN-13 numbers without hyphens
def test_valid_isbn_13_without_hyphens():
    assert is_isbn_13('9780312498580') == True

# Test cases for invalid ISBN-13 numbers without normalization
def test_invalid_isbn_13_without_normalization():
    assert is_isbn_13('978-0312498580', normalize=False) == False

# Edge case: empty string should return false
def test_empty_string():
    assert is_isbn_13('') == False

# Edge case: string with only hyphens should return false
def test_string_with_only_hyphens():
    assert is_isbn_13('---------') == False

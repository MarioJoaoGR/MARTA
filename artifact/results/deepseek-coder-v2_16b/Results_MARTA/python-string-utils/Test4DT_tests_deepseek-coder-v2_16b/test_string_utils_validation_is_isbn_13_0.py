
import pytest
from string_utils.validation import is_isbn_13

# Test valid normalized ISBN-13 number
def test_valid_normalized_isbn13():
    input_string = '9780312498580'
    result = is_isbn_13(input_string)
    assert result is True, f"Expected True for valid normalized ISBN-13 number '{input_string}', but got {result}"

# Test valid non-normalized ISBN-13 number with normalization enabled by default
def test_valid_non_normalized_isbn13():
    input_string = '978-0312498580'
    result = is_isbn_13(input_string)
    assert result is True, f"Expected True for valid non-normalized ISBN-13 number '{input_string}' with normalization enabled, but got {result}"

# Test valid non-normalized ISBN-13 number with normalization explicitly set to False
def test_valid_non_normalized_isbn13_with_normalize_false():
    input_string = '978-0312498580'
    result = is_isbn_13(input_string, normalize=False)
    assert result is False, f"Expected False for valid non-normalized ISBN-13 number '{input_string}' with normalization set to False, but got {result}"

# Test invalid ISBN number, normalization does not affect the result as it is a different format
def test_invalid_isbn():
    input_string = '978045145052'
    result = is_isbn_13(input_string)
    assert result is False, f"Expected False for invalid ISBN number '{input_string}', but got {result}"

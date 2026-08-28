
import pytest
from string_utils.validation import is_isbn_10

def test_valid_normalized_isbn_10():
    input_string = '1506715214'
    result = is_isbn_10(input_string)
    assert result == True, f"Expected True for valid normalized ISBN-10 '{input_string}', but got {result}"

def test_valid_non_normalized_isbn_10():
    input_string = '150-6715214'
    result = is_isbn_10(input_string)
    assert result == True, f"Expected True for valid non-normalized ISBN-10 '{input_string}', but got {result}"

def test_invalid_non_normalized_isbn_10():
    input_string = '150-6715214'
    result = is_isbn_10(input_string, normalize=False)
    assert result == False, f"Expected False for invalid non-normalized ISBN-10 '{input_string}', but got {result}"

def test_invalid_isbn_10():
    input_string = '123456789X'
    result = is_isbn_10(input_string)
    assert result == False, f"Expected False for invalid ISBN-10 '{input_string}', but got {result}"

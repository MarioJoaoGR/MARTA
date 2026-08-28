
import pytest
from string_utils.validation import is_string

def test_valid_string():
    assert is_string('hello') == True, "Expected 'hello' to be identified as a valid string."

def test_empty_string():
    assert is_string('') == True, "Expected an empty string to be identified as a valid string."

def test_non_string_types():
    non_string_values = [None, 123, [1, 2, 3], b'binary', 3.14]
    for value in non_string_values:
        assert is_string(value) == False, f"Expected {value!r} to be identified as a non-string."

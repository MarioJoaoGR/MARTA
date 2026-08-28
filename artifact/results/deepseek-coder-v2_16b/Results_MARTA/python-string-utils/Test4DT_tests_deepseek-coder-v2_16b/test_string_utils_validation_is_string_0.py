
import pytest
from string_utils.validation import is_string

def test_is_string_valid():
    assert is_string('hello') == True, "Expected 'hello' to be recognized as a string."

def test_is_string_invalid():
    assert is_string(12345) == False, "Expected 12345 to not be recognized as a string."

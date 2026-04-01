
import pytest
from string_utils.validation import is_pangram, is_full_string  # Assuming this is the correct module path

def test_valid_pangram():
    assert is_pangram('The quick brown fox jumps over the lazy dog') == True
    assert is_pangram('hello world') == False

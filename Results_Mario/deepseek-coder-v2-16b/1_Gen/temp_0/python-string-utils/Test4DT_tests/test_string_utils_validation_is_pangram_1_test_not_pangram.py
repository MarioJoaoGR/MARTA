
import pytest
from string_utils.validation import is_pangram

def test_not_pangram():
    # Test a non-pangram sentence
    assert not is_pangram('hello world')  # This should return False as 'hello world' does not contain all letters of the alphabet

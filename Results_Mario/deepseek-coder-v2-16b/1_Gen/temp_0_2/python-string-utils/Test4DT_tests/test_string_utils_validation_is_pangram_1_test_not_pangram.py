
import pytest
from string_utils.validation import is_pangram  # Assuming this is the correct import path for 'is_full_string'

def test_not_pangram():
    assert not is_pangram('hello world')
    assert not is_pangram('just a test string')
    assert not is_pangram('missing some letters')

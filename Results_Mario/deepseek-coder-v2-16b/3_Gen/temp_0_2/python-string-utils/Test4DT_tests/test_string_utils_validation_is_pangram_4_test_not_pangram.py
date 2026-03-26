
import pytest
from string_utils.validation import is_pangram  # Assuming this is the correct import path

def test_not_pangram():
    assert not is_pangram('hello world')
    assert not is_pangram('this is not a pangram')
    assert not is_pangram('missing some letters')

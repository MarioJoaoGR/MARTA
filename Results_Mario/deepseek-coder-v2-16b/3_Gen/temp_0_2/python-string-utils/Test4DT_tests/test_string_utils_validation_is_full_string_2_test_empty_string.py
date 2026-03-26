
import pytest
from string_utils.validation import is_full_string

def test_empty_string():
    assert not is_full_string('')
    assert not is_full_string(' ')
    assert is_full_string('hello')
    assert not is_full_string(None)

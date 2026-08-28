
import pytest
from string_utils.validation import is_full_string

def test_is_full_string_basic():
    assert is_full_string(None) == False
    assert is_full_string('') == False
    assert is_full_string(' ') == False
    assert is_full_string('hello') == True

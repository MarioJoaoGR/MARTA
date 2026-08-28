
import pytest
from string_utils.validation import is_isogram

def is_full_string(input_string: str) -> bool:
    return isinstance(input_string, str) and len(input_string.strip()) > 0

def test_valid_isogram():
    assert is_isogram('dermatoglyphics') == True
    assert is_isogram('hello') == False


def test_empty_string():
    assert not is_full_string('')
    assert not is_isogram('')

def test_whitespace_only():
    assert not is_full_string('     ')
    assert not is_isogram('     ')
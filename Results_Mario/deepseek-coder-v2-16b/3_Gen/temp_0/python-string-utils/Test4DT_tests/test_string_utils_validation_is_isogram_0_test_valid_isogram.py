
from string_utils.validation import is_isogram
import pytest

def test_valid_isogram():
    assert is_isogram('dermatoglyphics') == True
    assert is_isogram('hello') == False
    assert is_isogram(' ') == False

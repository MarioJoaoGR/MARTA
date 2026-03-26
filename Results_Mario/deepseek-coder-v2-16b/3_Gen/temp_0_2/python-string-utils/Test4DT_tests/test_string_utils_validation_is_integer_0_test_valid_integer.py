
import pytest
from string_utils.validation import is_integer

def test_valid_integer():
    assert is_integer('42') == True
    assert is_integer('-42') == True
    assert is_integer('+42') == True
    assert is_integer('0') == True
    assert is_integer('000') == True
    assert is_integer('0001') == True

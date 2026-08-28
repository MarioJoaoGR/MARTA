
import pytest
from string_utils.validation import is_integer

def test_positive_integer():
    assert is_integer('42') == True

def test_negative_integer():
    assert is_integer('-15') == True

def test_unsigned_integer():
    assert is_integer('+7') == True

def test_zero():
    assert is_integer('0') == True

def test_float_number():
    assert is_integer('42.0') == False


def test_non_numeric_string():
    assert is_integer('abc') == False

def test_string_with_spaces():
    assert is_integer(' 42 ') == False

def test_none_input():
    with pytest.raises(TypeError):
        is_integer(None)

def test_empty_string():
    assert is_integer('') == False
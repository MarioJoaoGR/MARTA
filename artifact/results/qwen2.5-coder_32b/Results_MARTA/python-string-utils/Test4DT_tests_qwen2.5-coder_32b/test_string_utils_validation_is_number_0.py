
import pytest
from string_utils.validation import is_number

def test_positive_integer():
    assert is_number('42') == True, "Failed on '42'"

def test_negative_integer():
    assert is_number('-5') == True, "Failed on '-5'"

def test_positive_float():
    assert is_number('19.99') == True, "Failed on '19.99'"

def test_negative_float():
    assert is_number('-3.14') == True, "Failed on '-3.14'"

def test_scientific_notation_positive_exponent():
    assert is_number('1e3') == True, "Failed on '1e3'"


def test_implied_leading_zero_float():
    assert is_number('.5') == True, "Failed on '.5'"

def test_multiple_numbers_with_space():
    assert is_number('1 2 3') == False, "Failed on '1 2 3'"

def test_invalid_string():
    assert is_number('abc') == False, "Failed on 'abc'"

def test_invalid_float_format():
    assert is_number('4.5.6') == False, "Failed on '4.5.6'"

def test_positive_scientific_notation_with_plus_sign():
    assert is_number('+1e3') == True, "Failed on '+1e3'"

def test_zero():
    assert is_number('0') == True, "Failed on '0'"

def test_negative_zero():
    assert is_number('-0') == True, "Failed on '-0'"

def test_positive_float_with_plus_sign():
    assert is_number('+3.14') == True, "Failed on '+3.14'"

def test_empty_string():
    assert is_number('') == False, "Failed on ''"
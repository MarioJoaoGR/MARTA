# Module: isort.sorting
import pytest

from isort.sorting import _atoi

# Test cases for _atoi function

def test_valid_numeric_string():
    assert _atoi("123") == 123

def test_invalid_numeric_string():
    assert _atoi("abc") == 'abc'

def test_empty_string():
    assert isinstance(_atoi(""), str)

def test_leading_zeros():
    assert _atoi("00123") == 123

def test_decimal_point():
    assert _atoi("123.45") == '123.45'

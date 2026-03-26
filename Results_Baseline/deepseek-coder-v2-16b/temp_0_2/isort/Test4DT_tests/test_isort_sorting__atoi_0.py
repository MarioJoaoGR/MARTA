# Module: isort.sorting
import pytest

from isort.sorting import _atoi


# Test case 1: Convert a string that represents an integer
def test_atoi_valid_integer():
    assert _atoi("123") == 123

# Test case 2: Leave a string unchanged if it does not represent an integer
def test_atoi_invalid_string():
    assert _atoi("abc") == 'abc'

# Test case 3: Handle an empty string by returning an empty string
def test_atoi_empty_string():
    assert _atoi("") == ''

# Test case 4: Leave a mixed string unchanged if it contains digits
def test_atoi_mixed_string():
    assert _atoi("123abc") == '123abc'

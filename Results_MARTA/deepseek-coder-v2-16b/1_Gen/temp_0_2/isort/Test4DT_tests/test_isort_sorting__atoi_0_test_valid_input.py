
import pytest
from isort.sorting import _atoi

def test_valid_input():
    assert _atoi("123") == 123
    assert _atoi("0") == 0
    assert _atoi("456789") == 456789
    assert _atoi("abc") == "abc"

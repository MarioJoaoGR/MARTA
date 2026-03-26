
import pytest
from isort.sorting import _atoi

def test_invalid_input():
    assert _atoi("abc") == "abc"

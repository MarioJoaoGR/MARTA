
import pytest
from flutes.iterator import drop

def test_valid_input():
    n = 3
    iterable = [1, 2, 3, 4, 5]
    expected = [4, 5]
    result = list(drop(n, iterable))
    assert result == expected

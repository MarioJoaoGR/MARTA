
import pytest
from flutes.iterator import drop
from typing import Iterable, Iterator, Type

def test_invalid_input():
    n = -1
    iterable = [1, 2, 3]
    with pytest.raises(ValueError) as excinfo:
        list(drop(n, iterable))
    assert str(excinfo.value) == '`n` should be non-negative'


import pytest
from flutes.iterator import chunk
from typing import List, Iterable

def test_invalid_n():
    iterable = range(10)
    n = -1
    with pytest.raises(ValueError):
        list(chunk(n, iterable))

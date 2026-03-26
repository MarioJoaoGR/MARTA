
import pytest
from flutes.iterator import chunk

def test_invalid_input():
    n = -1
    iterable = range(5)
    with pytest.raises(ValueError):
        list(chunk(n, iterable))


import pytest
from flutes.iterator import drop
from itertools import count

def test_invalid_input():
    n = 'a'
    iterable = count()
    with pytest.raises(TypeError):
        list(drop(n, iterable))

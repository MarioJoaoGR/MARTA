
import pytest
from flutes.iterator import drop

def test_drop():
    n = 0
    iterable = None
    with pytest.raises(TypeError):
        list(drop(n, iterable))

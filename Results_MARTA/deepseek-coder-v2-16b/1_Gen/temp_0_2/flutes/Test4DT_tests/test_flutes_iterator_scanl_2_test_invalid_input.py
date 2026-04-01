
import pytest
from flutes.iterator import scanl
from typing import Callable, Iterable, Iterator, Any

def test_invalid_input():
    with pytest.raises(TypeError):
        list(scanl(lambda x, y: x + y))  # Missing iterable argument should raise TypeError

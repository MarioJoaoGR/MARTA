
import pytest
from flutes.iterator import scanl
from typing import Callable, Iterable, Iterator

def test_edge_case_none():
    # Test when iterable is None
    with pytest.raises(TypeError):
        list(scanl(lambda acc, x: acc + x, None, 0))

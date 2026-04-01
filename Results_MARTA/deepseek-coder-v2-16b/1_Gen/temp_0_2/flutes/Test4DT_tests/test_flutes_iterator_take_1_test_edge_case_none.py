
import pytest
from flutes.iterator import take
from typing import Iterator, Iterable, TypeVar

T = TypeVar('T')

def test_edge_case_none():
    with pytest.raises(ValueError):
        list(take(-1, None))

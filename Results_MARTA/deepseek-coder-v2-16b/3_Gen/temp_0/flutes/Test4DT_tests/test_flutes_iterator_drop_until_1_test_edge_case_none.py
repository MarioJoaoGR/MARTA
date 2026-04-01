
import pytest
from flutes.iterator import drop_until
from typing import Callable, Iterable, Iterator, TypeVar

T = TypeVar('T')

def test_edge_case_none():
    with pytest.raises(TypeError):
        list(drop_until(lambda x: x > 5, None))

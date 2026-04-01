
import pytest
from flutes.iterator import drop_until
from typing import Callable, Iterable, Iterator, TypeVar

T = TypeVar('T')

def test_invalid_predicate():
    with pytest.raises(TypeError):
        list(drop_until("not a callable", range(10)))

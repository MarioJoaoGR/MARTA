
import pytest
from flutes.iterator import take
from typing import Iterator, Iterable, TypeVar

T = TypeVar('T')

def test_negative_n():
    with pytest.raises(ValueError):
        list(take(-1, range(10)))


import pytest
from flutes.iterator import take
from typing import Iterable, Iterator, TypeVar

T = TypeVar('T')

def test_negative_input():
    with pytest.raises(ValueError):
        list(take(-1, range(10)))

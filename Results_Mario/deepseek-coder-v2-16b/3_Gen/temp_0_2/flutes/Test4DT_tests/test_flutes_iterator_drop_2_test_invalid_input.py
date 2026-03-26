
import pytest
from flutes.iterator import drop
from typing import Iterable, Iterator, TypeVar

T = TypeVar('T')

def test_invalid_input():
    with pytest.raises(ValueError):
        list(drop(-1, range(10)))

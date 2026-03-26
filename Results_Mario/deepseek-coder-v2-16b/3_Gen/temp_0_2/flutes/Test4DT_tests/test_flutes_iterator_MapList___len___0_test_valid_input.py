
from flutes.iterator import MapList
import pytest
from typing import Callable, Sequence, TypeVar

T = TypeVar('T')
R = TypeVar('R')

def test_valid_input():
    a = [1, 2, 3, 4, 5]
    maplist_instance = MapList(lambda x: x * x, a)
    assert len(maplist_instance) == len(a)


import pytest
from flutes.iterator import MapList
from typing import Callable, Sequence, List

def test_maplist():
    a = [1, 2, 3, 4, 5]
    b = MapList(lambda x: x * x, a)
    assert len(b) == 5


import pytest
from flutes.iterator import MapList
from typing import Callable, Sequence, List

def test_maplist():
    a = []
    b = MapList(lambda x: x * x, a)
    assert len(b) == 0

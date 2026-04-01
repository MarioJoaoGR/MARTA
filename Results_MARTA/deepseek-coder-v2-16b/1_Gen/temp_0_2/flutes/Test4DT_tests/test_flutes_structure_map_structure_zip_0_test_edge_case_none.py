
import pytest
from flutes.structure import map_structure_zip
from typing import Callable, Sequence, Collection

def add(a, b):
    return a + b

def test_edge_case_none():
    with pytest.raises(TypeError):
        assert map_structure_zip(add, [None]) is None

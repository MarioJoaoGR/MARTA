
import pytest
from flutes.structure import map_structure, Collection
from typing import Callable, TypeVar

T = TypeVar('T')
R = TypeVar('R')

def test_invalid_input():
    with pytest.raises(TypeError):
        map_structure(lambda x: x ** 2, "not a collection")

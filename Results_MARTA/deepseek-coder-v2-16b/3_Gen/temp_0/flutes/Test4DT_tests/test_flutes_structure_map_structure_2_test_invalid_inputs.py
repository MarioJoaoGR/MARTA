
import pytest
from flutes.structure import map_structure
from typing import Callable, Collection, TypeVar

T = TypeVar('T')
R = TypeVar('R')

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test case for invalid input type (should raise TypeError)
        map_structure(lambda x: x**2, "not a collection")

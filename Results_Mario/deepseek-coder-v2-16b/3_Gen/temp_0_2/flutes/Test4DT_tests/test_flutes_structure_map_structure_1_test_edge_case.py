
import pytest
from typing import Callable, Collection, List, Tuple, Dict, Set
from flutes.structure import map_structure

# Assuming _NO_MAP_TYPES and _NO_MAP_INSTANCE_ATTR are defined in the module 'flutes.structure'
# from flutes.structure import _NO_MAP_TYPES, _NO_MAP_INSTANCE_ATTR

def test_map_structure():
    def square(x):
        return x ** 2

    # Test with list
    assert map_structure(square, [1, 2, 3]) == [1, 4, 9]
    
    # Test with tuple
    assert map_structure(square, (1, 2, 3)) == (1, 4, 9)
    
    # Test with dictionary
    assert map_structure(square, {'a': 1, 'b': 2}) == {'a': 1, 'b': 4}
    
    # Test with set
    assert map_structure(square, {1, 2, 3}) == {1, 4, 9}

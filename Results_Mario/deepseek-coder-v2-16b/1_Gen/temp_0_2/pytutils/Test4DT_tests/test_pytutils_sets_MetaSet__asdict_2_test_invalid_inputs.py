
import pytest
from pytutils.sets import MetaSet
import attr
import random
import copy

def test_invalid_inputs():
    meta_set = MetaSet()
    
    with pytest.raises(TypeError):
        # Test adding a non-hashable type (e.g., list)
        meta_set.add([1, 2, 3])
        
    with pytest.raises(TypeError):
        # Test adding a mutable type (e.g., dict)
        meta_set.add({'a': 1})

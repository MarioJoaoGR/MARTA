
import pytest
from pytutils.sets import MetaSet
import attr
import random

def test_invalid_inputs():
    meta_set = MetaSet()
    
    # Test adding non-hashable objects which should raise a TypeError
    with pytest.raises(TypeError):
        meta_set.add([1, 2, 3])  # List is not hashable
        meta_set.add({})         # Dictionary is not hashable
        meta_set.add((1,))       # Tuple is not hashable

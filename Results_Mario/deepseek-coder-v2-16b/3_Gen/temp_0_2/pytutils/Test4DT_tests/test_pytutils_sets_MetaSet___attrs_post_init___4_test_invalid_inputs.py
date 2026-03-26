
import pytest
from pytutils.sets import MetaSet
import random

@pytest.fixture
def meta_set():
    return MetaSet()

def test_invalid_inputs(meta_set):
    # Test that the _meta_func uses a callable and generates a unique identifier for each value when it's added.
    assert callable(meta_set._meta_func)
    
    # Add an invalid initial input (not iterable) to test the __attrs_post_init__ method
    meta_set._initial = 123
    with pytest.raises(TypeError):
        meta_set.__attrs_post_init__()
    
    # Add a valid initial input and check if it gets added correctly
    meta_set._initial = [4, 5, 6]
    meta_set.__attrs_post_init__()
    assert len(meta_set._store) == 3

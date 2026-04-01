
import pytest
from flutes.iterator import LazyList

def test_invalid_len():
    lazy_list = LazyList([1, 2, 3, 4])
    
    with pytest.raises(TypeError) as excinfo:
        len(lazy_list)
        
    assert str(excinfo.value) == "__len__ is not available before the iterable is depleted"

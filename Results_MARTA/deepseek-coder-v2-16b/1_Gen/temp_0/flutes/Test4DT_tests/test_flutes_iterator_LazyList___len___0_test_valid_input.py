
import pytest
from flutes.iterator import LazyList

def test_valid_input():
    lazy_list = LazyList([1, 2, 3, 4])
    
    # Initially, len should raise a TypeError
    with pytest.raises(TypeError):
        assert len(lazy_list)
    
    # Iterate over the list to exhaust it
    for item in lazy_list:
        pass
    
    # After exhausting the iterable, len should return the correct length
    assert len(lazy_list) == 4

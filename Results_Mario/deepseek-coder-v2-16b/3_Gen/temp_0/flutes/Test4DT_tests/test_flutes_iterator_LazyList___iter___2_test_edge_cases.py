
import pytest
from flutes.iterator import LazyList

def test_edge_cases():
    # Test None as iterable
    with pytest.raises(TypeError):
        lazy_list = LazyList(None)
    
    # Test empty list
    my_list = []
    lazy_list = LazyList(my_list)
    assert list(lazy_list) == []
    
    # Test boundary values (single element list)
    my_list = [1]
    lazy_list = LazyList(my_list)
    assert list(lazy_list) == [1]

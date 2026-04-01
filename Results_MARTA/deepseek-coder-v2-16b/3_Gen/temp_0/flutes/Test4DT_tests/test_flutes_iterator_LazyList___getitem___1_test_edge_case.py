
import pytest
from flutes.iterator import LazyList

def test_edge_case():
    lazy_list = LazyList([1, 2, 3, 4])
    
    # Test single index access
    assert lazy_list[0] == 1
    assert lazy_list[1] == 2
    assert lazy_list[2] == 3
    assert lazy_list[3] == 4
    
    # Test slice access
    assert list(lazy_list[0:4]) == [1, 2, 3, 4]
    assert list(lazy_list[0:2]) == [1, 2]
    assert list(lazy_list[2:4]) == [3, 4]
    
    # Test beyond the end of the list
    with pytest.raises(IndexError):
        lazy_list[4]

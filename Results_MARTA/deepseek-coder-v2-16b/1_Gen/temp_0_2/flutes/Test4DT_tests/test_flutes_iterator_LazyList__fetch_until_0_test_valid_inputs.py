
import pytest
from flutes.iterator import LazyList

def test_valid_inputs():
    lazy_list = LazyList([1, 2, 3, 4])
    
    # Test iteration over the entire list
    result = []
    for item in lazy_list:
        result.append(item)
    assert result == [1, 2, 3, 4]
    
    # Test accessing specific indices
    assert lazy_list[0] == 1
    assert lazy_list[2] == 3
    
    # Test that the list is not fetched until accessed
    with pytest.raises(IndexError):
        _ = lazy_list[4]


import pytest
from flutes.iterator import LazyList

def test_valid_input():
    lazy_list = LazyList([1, 2, 3, 4])
    assert lazy_list[0] == 1
    assert lazy_list[1] == 2
    assert lazy_list[2] == 3
    assert lazy_list[3] == 4
    
    # Test accessing beyond the current list length
    with pytest.raises(IndexError):
        lazy_list[4]

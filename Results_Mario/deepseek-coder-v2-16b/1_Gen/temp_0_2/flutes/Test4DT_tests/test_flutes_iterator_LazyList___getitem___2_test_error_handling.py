
import pytest
from flutes.iterator import LazyList

def test_lazylist_getitem_error_handling():
    # Test that accessing an out-of-range index raises IndexError
    lazy_list = LazyList([1, 2, 3])
    
    with pytest.raises(IndexError):
        _ = lazy_list[5]  # This should raise an IndexError because the list only has indices 0, 1, and 2.

    # Test that accessing a valid index does not raise an error
    item = lazy_list[1]  # This should return 2 as it is the second element in the list.
    assert item == 2

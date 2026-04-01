
import pytest
from flutes.iterator import LazyList

def test_lazylist_getitem_error_handling():
    # Test that accessing an index out of range raises IndexError
    lazy_list = LazyList([1, 2, 3])
    
    with pytest.raises(IndexError):
        _ = lazy_list[5]  # This should raise an IndexError because the list only has elements up to index 2

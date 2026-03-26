
import pytest
from flutes.iterator import LazyList

def test_error_handling():
    # Test that accessing an out-of-bounds index raises IndexError
    lazy_list = LazyList([1, 2, 3])
    
    with pytest.raises(IndexError):
        item = lazy_list[5]  # This should raise an IndexError because the list only has elements up to index 2


import pytest
from flutes.iterator import LazyList

def test_invalid_input():
    # Test that accessing an invalid index raises an IndexError
    lazy_list = LazyList([1, 2, 3])
    
    with pytest.raises(IndexError):
        _ = lazy_list[5]  # Accessing an index beyond the list length


import pytest
from flutes.iterator import LazyList

def test_invalid_index():
    lazy_list = LazyList([1, 2, 3, 4])
    
    # Test accessing an index beyond the current list bounds
    with pytest.raises(IndexError):
        item = lazy_list[5]  # This should raise IndexError because there are only 4 items in the list

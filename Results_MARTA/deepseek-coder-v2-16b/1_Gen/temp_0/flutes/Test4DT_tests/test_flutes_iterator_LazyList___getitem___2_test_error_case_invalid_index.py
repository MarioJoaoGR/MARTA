
import pytest
from flutes.iterator import LazyList

def test_error_case_invalid_index():
    lazy_list = LazyList([1, 2, 3])
    
    with pytest.raises(IndexError):
        element = lazy_list[10]  # This index is out of bounds

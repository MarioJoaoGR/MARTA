
import pytest
from flutes.iterator import LazyList

def test_error_handling():
    lazy_list = LazyList([1, 2, 3, 4])
    
    # Access elements to ensure they are fetched lazily
    with pytest.raises(TypeError):
        len(lazy_list)

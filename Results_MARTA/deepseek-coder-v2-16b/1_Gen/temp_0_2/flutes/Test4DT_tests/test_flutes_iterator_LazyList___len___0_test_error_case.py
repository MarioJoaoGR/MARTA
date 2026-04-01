
import pytest
from flutes.iterator import LazyList

def test_error_case():
    lazy_list = LazyList([1, 2, 3, 4])
    
    with pytest.raises(TypeError):
        len(lazy_list)

    # Consume the entire list to make __len__ available
    list(lazy_list)
    
    assert len(lazy_list) == 4

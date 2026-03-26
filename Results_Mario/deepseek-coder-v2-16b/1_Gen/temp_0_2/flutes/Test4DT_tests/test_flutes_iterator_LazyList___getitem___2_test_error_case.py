
import pytest
from flutes.iterator import LazyList

def test_error_case():
    lazy_list = LazyList([1, 2, 3, 4])
    
    with pytest.raises(IndexError):
        assert lazy_list[5] == 6  # This should raise an IndexError because there is no element at index 5

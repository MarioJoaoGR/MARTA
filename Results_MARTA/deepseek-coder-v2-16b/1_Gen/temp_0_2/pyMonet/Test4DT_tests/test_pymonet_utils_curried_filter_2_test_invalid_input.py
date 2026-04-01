
import pytest
from pymonet.utils import curried_filter

def test_invalid_input():
    def always_false(n):
        return False
    
    # Test with a collection that contains elements which will all fail the filterer function
    assert curried_filter(always_false, [1, 3, 5, 7]) == []
    
    # Test with an empty collection
    assert curried_filter(always_false, []) == []
    
    # Test with a non-iterable input (e.g., None)
    with pytest.raises(TypeError):
        curried_filter(always_false, None)

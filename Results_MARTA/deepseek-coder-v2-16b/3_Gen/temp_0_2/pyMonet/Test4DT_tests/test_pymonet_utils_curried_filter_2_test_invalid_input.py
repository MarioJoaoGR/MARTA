
import pytest
from pymonet.utils import curried_filter

def is_even(n):
    return n % 2 == 0

def test_invalid_input():
    # Test with a non-callable filterer function
    invalid_filterer = "not a callable"
    with pytest.raises(TypeError):
        curried_filter(invalid_filterer, [1, 2, 3, 4])
    
    # Test with an iterable that is not a list or another iterable type
    invalid_collection = 12345
    with pytest.raises(TypeError):
        curried_filter(is_even, invalid_collection)


import pytest
from pytutils.iters import accumulate
import operator

def test_edge_cases():
    # Test with empty list
    assert list(accumulate([])) == []
    
    # Test with None input
    with pytest.raises(TypeError):
        list(accumulate(None))
    
    # Test with a single element list
    assert list(accumulate([1])) == [1]
    
    # Test with a list of positive numbers
    assert list(accumulate([1, 2, 3, 4, 5])) == [1, 3, 6, 10, 15]
    
    # Test with a list of negative numbers
    assert list(accumulate([-1, -2, -3, -4, -5])) == [-1, -3, -6, -10, -15]
    
    # Test with a list of mixed positive and negative numbers
    assert list(accumulate([1, -2, 3, -4, 5])) == [1, -1, 2, -2, 3]

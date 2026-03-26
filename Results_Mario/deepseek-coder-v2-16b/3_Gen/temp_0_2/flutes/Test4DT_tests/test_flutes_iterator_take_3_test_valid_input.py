
import pytest
from flutes.iterator import take

def test_valid_input():
    # Test case 1: Take first 5 elements from a range of length 10
    result = list(take(5, range(10)))
    assert result == [0, 1, 2, 3, 4]
    
    # Test case 2: Take all elements from an iterable with fewer than n elements
    result = list(take(10, range(5)))
    assert result == [0, 1, 2, 3, 4]
    
    # Test case 3: Take zero elements
    result = list(take(0, range(10)))
    assert list(result) == []
    
    # Test case 4: Take negative number of elements (should raise ValueError)
    with pytest.raises(ValueError):
        list(take(-5, range(10)))

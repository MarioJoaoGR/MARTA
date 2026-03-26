
import pytest
from flutes.iterator import drop

def test_valid_input():
    # Test dropping zero elements
    assert list(drop(0, range(10))) == list(range(10))
    
    # Test dropping some elements
    assert list(drop(3, range(10))) == [3, 4, 5, 6, 7, 8, 9]
    
    # Test dropping more elements than available
    assert list(drop(10, range(10))) == []
    
    # Test with an empty iterable
    assert list(drop(0, [])) == []
    
    # Test with negative number (should raise ValueError)
    with pytest.raises(ValueError):
        list(drop(-1, range(10)))

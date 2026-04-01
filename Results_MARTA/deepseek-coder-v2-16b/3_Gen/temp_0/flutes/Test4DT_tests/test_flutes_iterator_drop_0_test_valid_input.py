
import pytest
from flutes.iterator import drop
from typing import Iterator, Iterable, TypeVar

T = TypeVar('T')

def test_valid_input():
    # Test dropping elements from a range
    result = list(drop(5, range(10)))
    assert result == [5, 6, 7, 8, 9]
    
    # Test dropping elements from a list
    result = list(drop(1, [10, 20, 30, 40]))
    assert result == [20, 30, 40]
    
    # Test dropping zero elements (should return the iterable as is)
    result = list(drop(0, [10, 20, 30, 40]))
    assert result == [10, 20, 30, 40]
    
    # Test dropping negative number of elements (should raise ValueError)
    with pytest.raises(ValueError):
        list(drop(-1, range(10)))


import pytest
from flutes.iterator import take
from typing import Iterable, Iterator, Type

def test_valid_input():
    # Test with a valid iterable and positive n
    result = list(take(5, range(10)))
    assert result == [0, 1, 2, 3, 4]
    
    # Test with an empty iterable
    result = list(take(5, []))
    assert result == []
    
    # Test with a shorter iterable than n
    result = list(take(5, [0, 1]))
    assert result == [0, 1]
    
    # Test with negative n, should raise ValueError
    with pytest.raises(ValueError):
        list(take(-1, range(10)))

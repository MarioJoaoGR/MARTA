
import pytest
from pymonet.maybe import Maybe

def test_edge_cases():
    # Test None value
    maybe_none = Maybe(value=None, is_nothing=True)
    assert maybe_none.is_nothing is True
    
    # Test empty string
    maybe_empty_string = Maybe(value="", is_nothing=False)
    assert maybe_empty_string.value == ""
    assert maybe_empty_string.is_nothing is False
    
    # Test zero value
    maybe_zero = Maybe(value=0, is_nothing=False)
    assert maybe_zero.value == 0
    assert maybe_zero.is_nothing is False
    
    # Test empty list
    maybe_empty_list = Maybe(value=[], is_nothing=False)
    assert maybe_empty_list.value == []
    assert maybe_empty_list.is_nothing is False
    
    # Test map function with None value
    def add_one(x):
        return x + 1 if x is not None else None
    
    mapped_maybe = maybe_none.map(add_one)
    assert mapped_maybe.is_nothing is True
    
    # Test map function with a valid value
    mapped_maybe = maybe_zero.map(add_one)
    assert mapped_maybe.value == 1
    assert mapped_maybe.is_nothing is False

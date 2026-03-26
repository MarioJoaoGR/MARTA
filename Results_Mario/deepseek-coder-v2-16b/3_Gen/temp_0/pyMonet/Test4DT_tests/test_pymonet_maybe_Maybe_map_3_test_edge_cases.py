
import pytest
from pymonet.maybe import Maybe

def test_edge_cases():
    # Test with None value
    maybe_none = Maybe(value=None, is_nothing=True)
    assert maybe_none.is_nothing is True
    
    # Test with empty string value
    maybe_empty_string = Maybe(value="", is_nothing=False)
    assert maybe_empty_string.value == ""
    
    # Test map function with None value
    mapped_maybe_none = maybe_none.map(lambda x: x * 2 if x is not None else None)
    assert mapped_maybe_none.is_nothing is True
    
    # Test map function with empty string value
    mapped_maybe_empty_string = maybe_empty_string.map(lambda x: x + " world")
    assert mapped_maybe_empty_string.value == " world"


import pytest
from pymonet.maybe import Maybe

def test_edge_cases():
    maybe_none_with_value = Maybe(None, False)
    maybe_empty = Maybe(None, True)
    
    # Test equality with None (not nothing)
    assert maybe_none_with_value == Maybe(None, False)
    
    # Test equality with None (nothing)
    assert maybe_none_with_value != Maybe(None, True)
    
    # Test equality with empty value (nothing)
    assert maybe_empty == Maybe(None, True)
    
    # Test equality with non-empty value (not nothing)
    assert maybe_none_with_value != Maybe(10, False)
    
    # Test equality with None and different is_nothing value
    assert maybe_none_with_value != Maybe(None, True)

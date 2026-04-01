
import pytest
from pymonet.monad_try import Try

def test_edge_cases():
    # Test with None value
    none_try = Try(None, True)
    assert none_try.value is None
    assert none_try.is_success is True
    
    # Test with empty list value
    empty_try = Try([], False)
    assert empty_try.value == []
    assert not empty_try.is_success

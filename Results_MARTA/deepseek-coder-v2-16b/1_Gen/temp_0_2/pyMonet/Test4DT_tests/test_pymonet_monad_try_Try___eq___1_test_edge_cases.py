
import pytest
from pymonet.monad_try import Try

def test_edge_cases():
    none_try = Try(None, True)
    empty_try = Try([], False)
    
    # Test None value
    assert none_try.value is None
    assert none_try.is_success is True
    
    # Test empty list value
    assert len(empty_try.value) == 0
    assert empty_try.is_success is False

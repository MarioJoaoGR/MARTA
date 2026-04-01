
import pytest
from pymonet.monad_try import Try

def test_edge_cases():
    # Test with None value
    none_try = Try(None, True)
    assert none_try.get_or_else("default") is None
    
    # Test with empty list value
    empty_list_try = Try([], True)
    assert empty_list_try.get_or_else("default") == []
    
    # Test with boundary values for is_success
    success_try = Try(42, True)
    assert success_try.get_or_else(0) == 42
    
    failure_try = Try("error", False)
    assert failure_try.get_or_else("default") == "default"

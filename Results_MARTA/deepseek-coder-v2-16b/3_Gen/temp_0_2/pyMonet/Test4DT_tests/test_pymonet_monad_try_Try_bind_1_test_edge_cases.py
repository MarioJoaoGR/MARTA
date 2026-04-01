
import pytest
from pymonet.monad_try import Try

def test_edge_cases():
    # Test with None value
    none_try = Try(None, False)
    assert none_try.value is None
    assert not none_try.is_success
    
    # Test with empty list (not strictly an edge case but a different type of failure)
    empty_list_try = Try([], False)
    assert empty_list_try.value == []
    assert not empty_list_try.is_success
    
    # Test bind function with None value
    def double(x): return Try(x * 2, True) if x is not None else Try(None, False)
    result = none_try.bind(double)
    assert result.value is None
    assert not result.is_success
    
    # Test bind function with empty list (should fail as well)
    def error_func(_): return Try(None, False)
    result_failure = empty_list_try.bind(error_func)
    assert result_failure.value == []
    assert not result_failure.is_success

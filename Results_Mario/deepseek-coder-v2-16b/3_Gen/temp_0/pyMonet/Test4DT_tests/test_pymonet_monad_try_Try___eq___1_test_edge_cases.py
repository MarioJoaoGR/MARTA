
import pytest
from pymonet.monad_try import Try

def test_edge_cases():
    # Test with None value
    none_try = Try(None, is_success=False)
    assert not none_try.is_success
    assert none_try.value is None

    # Test with empty list value
    empty_list_try = Try([], is_success=True)
    assert empty_list_try.is_success
    assert empty_list_try.value == []

    # Test with boundary values (e.g., minimum and maximum integer values)
    min_int_try = Try(float('-inf'), is_success=True)
    assert min_int_try.is_success
    assert min_int_try.value == float('-inf')

    max_int_try = Try(float('inf'), is_success=True)
    assert max_int_try.is_success
    assert max_int_try.value == float('inf')

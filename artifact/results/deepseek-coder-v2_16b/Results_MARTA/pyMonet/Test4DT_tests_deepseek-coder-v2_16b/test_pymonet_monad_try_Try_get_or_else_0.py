
import pytest
from pymonet.monad_try import Try

# Test scenarios
def test_valid_inputs():
    success_try = Try(10, True)
    assert success_try.value == 10
    assert success_try.is_success is True

def test_edge_cases():
    failure_try = Try(None, False)
    assert failure_try.value is None
    assert failure_try.is_success is False

    empty_list_try = Try([], False)
    assert len(empty_list_try.value) == 0
    assert empty_list_try.is_success is False

def test_invalid_inputs():
    try_with_error = Try('error', False)
    assert try_with_error.value == 'error'
    assert try_with_error.is_success is False


# Module: pymonet.monad_try
import pytest
from pymonet.monad_try import Try

# Test creating a failed Try object
def test_failed_init():
    failed_try = Try("Operation failed", is_success=False)
    assert not failed_try.is_success
    assert failed_try.value == "Operation failed"

# Test creating a successful Try object
def test_successful_init():
    successful_try = Try(42, is_success=True)
    assert successful_try.is_success
    assert successful_try.value == 42

# Test accessing the value from a successful Try object
def test_accessing_value_from_successful_try():
    successful_try = Try(42, is_success=True)
    if successful_try.is_success:
        assert successful_try.value == 42

# Test handling errors in a failed Try object
def test_handling_errors_in_failed_try():
    failed_try = Try("Operation failed", is_success=False)
    if not failed_try.is_success:
        assert failed_try.value == "Operation failed"

# Test using the bind method to chain operations safely
def test_bind_method():
    success_try = Try("success", True)
    
    def binder(val):
        return Try(val + " bound", True)
    
    result = success_try.bind(binder)
    assert result.is_success
    assert result.value == "success bound"

# Test handling a failed operation using bind
def test_handling_failed_operation_with_bind():
    failure_try = Try("failure", False)
    result = failure_try.bind(lambda x: Try(None, False))
    assert not result.is_success
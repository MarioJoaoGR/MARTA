
import pytest
from pymonet.monad_try import Try

# Test initialization of a successful Try object
def test_successful_init():
    try_obj = Try(42, is_success=True)
    assert try_obj.value == 42
    assert try_obj.is_success is True

# Test initialization of a failed Try object
def test_failed_init():
    try_obj = Try("Operation failed", is_success=False)
    assert try_obj.value == "Operation failed"
    assert try_obj.is_success is False

# Test get method with successful Try object
def test_get_successful():
    try_obj = Try(42, is_success=True)
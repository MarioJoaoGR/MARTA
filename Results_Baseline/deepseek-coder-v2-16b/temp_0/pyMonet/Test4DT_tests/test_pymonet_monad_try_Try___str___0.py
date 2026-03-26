# Module: pymonet.monad_try
import pytest
from pymonet.monad_try import Try

# Test creating a successful Try object
def test_successful_try():
    try_obj = Try(42, is_success=True)
    assert try_obj.value == 42
    assert try_obj.is_success is True

# Test creating a failed Try object
def test_failed_try():
    try_obj = Try("Operation failed", is_success=False)
    assert try_obj.value == "Operation failed"
    assert try_obj.is_success is False

# Test accessing the value from a successful Try object
def test_accessing_value_from_successful_try():
    try_obj = Try(42, is_success=True)
    if try_obj.is_success:
        assert try_obj.value == 42

# Test handling errors in a failed Try object
def test_handling_errors_in_failed_try():
    try_obj = Try("Operation failed", is_success=False)
    if not try_obj.is_success:
        assert try_obj.value == "Operation failed"

# Test the string representation of the Try object
def test_string_representation_of_try():
    try_obj = Try(42, is_success=True)
    expected_str = 'Try[value=42, is_success=True]'
    assert str(try_obj) == expected_str

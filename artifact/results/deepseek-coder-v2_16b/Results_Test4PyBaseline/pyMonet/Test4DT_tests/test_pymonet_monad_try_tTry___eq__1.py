
import pytest
from pymonet.monad_try import Try

# Test equality with another instance of Try for successful operations
def test_eq_successful():
    success1 = Try(42, True)
    success2 = Try(42, True)
    assert success1 == success2  # Both instances have the same value and is_success

# Test equality with another instance of Try for failed operations
def test_eq_failed():
    failure1 = Try("error", False)
    failure2 = Try("error", False)
    assert failure1 == failure2  # Both instances have the same value and is_success

# Test inequality with an instance of Try that has a different value for successful operations
def test_neq_value():
    success = Try(42, True)
    other_success = Try(100, True)
    assert success != other_success  # Different values but same is_success

# Test inequality with an instance of Try that has a different is_success for successful operations
def test_neq_is_success():
    success = Try(42, True)
    failure = Try(42, False)
    assert success != failure  # Same value but different is_success

# Test inequality with an instance of Try that has a different type
def test_neq_type():
    success = Try(42, True)
    other_type = "not a Try instance"
    assert success != other_type  # Different types should not be equal

# Test equality with the same instance
def test_eq_same_instance():
    success = Try(42, True)
    assert success == success  # An instance is always equal to itself

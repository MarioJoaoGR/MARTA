# Module: pytutils.memo
import pytest
from pytutils.memo import CachedException

# Test Case 1: Raising a cached exception directly from an instance
def test_raise_cached_exception():
    with pytest.raises(ValueError) as exc_info:
        raise CachedException(ValueError("An error occurred"))()
    assert str(exc_info.value) == "An error occurred"

# Test Case 2: Using the class directly in a try-except block
def test_use_class_in_try_except():
    with pytest.raises(ValueError) as exc_info:
        raise CachedException(ValueError("Another error happened"))()
    assert str(exc_info.value) == "Another error happened"

# Test Case 3: Creating and throwing an exception manually
def test_manual_exception_raising():
    cached_exception = CachedException(ValueError("A manual error"))
    with pytest.raises(ValueError) as exc_info:
        raise cached_exception()
    assert str(exc_info.value) == "A manual error"

# Test Case 4: Using different exception types
def test_different_exception_types():
    with pytest.raises(TypeError) as exc_info:
        raise CachedException(TypeError("A type error occurred"))()
    assert str(exc_info.value) == "A type error occurred"

# Module: pytutils.memo
import pytest
from pytutils.memo import CachedException

# Test cases for CachedException class
def test_cached_exception_initialization():
    """Test initialization of CachedException with a custom exception."""
    class CustomError(Exception):
        pass
    ex = CustomError("An error occurred")
    cached_exception = CachedException(ex)
    assert isinstance(cached_exception, CachedException)
    assert cached_exception.ex == ex

def test_throw_method():
    """Test the throw method of CachedException."""
    class CustomError(Exception):
        pass
    ex = CustomError("An error occurred")
    cached_exception = CachedException(ex)
    with pytest.raises(CustomError) as excinfo:
        cached_exception.throw()
    assert str(excinfo.value) == "An error occurred"

def test_throw_method_with_different_exception():
    """Test the throw method with a different exception type."""
    class DifferentError(Exception):
        pass
    ex = DifferentError("A different error occurred")
    cached_exception = CachedException(ex)
    with pytest.raises(DifferentError) as excinfo:
        cached_exception.throw()
    assert str(excinfo.value) == "A different error occurred"

def test_throw_method_with_standard_error():
    """Test the throw method raises an exception even if it's a standard Python exception."""
    with pytest.raises(ValueError) as excinfo:
        cached_exception = CachedException(ValueError("A standard error occurred"))
        cached_exception.throw()
    assert str(excinfo.value) == "A standard error occurred"

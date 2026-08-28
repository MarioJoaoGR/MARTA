
import pytest
from pymonet.monad_try import Try

# Test initialization with a successful operation
def test_init_successful():
    success = Try(42, True)
    assert success.value == 42
    assert success.is_success is True

# Test initialization with a failed operation
def test_init_failed():
    failure = Try("error", False)
    assert failure.value == "error"
    assert failure.is_success is False

# Test the map method for successful operations
def test_map_successful():
    success = Try(42, True)
    def square(x): return x * x
    success_squared = success.map(square)
    assert success_squared.value == 1764

# Test the bind method for successful operations
def test_bind_successful():
    success = Try(10, True)
    def add_ten(x): return x + 10
    result = success.bind(add_ten)
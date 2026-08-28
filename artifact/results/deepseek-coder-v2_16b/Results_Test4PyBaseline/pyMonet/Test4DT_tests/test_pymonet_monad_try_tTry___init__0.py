
import pytest
from pymonet.monad_try import Try

# Test initialization of a successful Try instance
def test_successful_init():
    try_instance = Try(42, True)
    assert try_instance.value == 42
    assert try_instance.is_success is True

# Test initialization of a failed Try instance
def test_failed_init():
    try_instance = Try("error", False)
    assert try_instance.value == "error"
    assert try_instance.is_success is False

# Test the map method to transform the value if successful
def test_map_method():
    success = Try(42, True)
    def square(x): return x * x
    transformed = success.map(square)
    assert transformed.value == 1764

# Test the bind method to apply a function that might fail
def test_bind_method():
    success = Try(10, True)
    def add_ten(x): return x + 10
    result = success.bind(add_ten)
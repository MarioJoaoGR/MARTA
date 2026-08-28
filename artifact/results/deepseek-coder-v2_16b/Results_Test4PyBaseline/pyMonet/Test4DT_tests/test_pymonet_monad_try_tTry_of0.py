
import pytest
from pymonet.monad_try import Try

# Test cases for the __init__ method
def test_init():
    success = Try(42, True)
    assert success.value == 42
    assert success.is_success is True
    
    failure = Try("error", False)
    assert failure.value == "error"
    assert failure.is_success is False

# Test cases for the of method
def test_of():
    def safe_function(x):
        return x / 0  # This will raise a ZeroDivisionError
    
    result = Try.of(safe_function, 1)
    assert isinstance(result.value, Exception)
    assert not result.is_success

# Test cases for the map method
def test_map():
    success = Try(42, True)
    
    def square(x): return x * x
    mapped_success = success.map(square)
    assert mapped_success.value == 1764
    assert mapped_success.is_success is True

# Test cases for the bind method
def test_bind():
    success = Try(42, True)
    
    def add_ten(x): return Try(x + 10, True)
    bound_result = success.bind(add_ten)
    assert bound_result.value == 52
    assert bound_result.is_success is True

# Test cases for the on_fail method
def test_on_fail():
    failure = Try("error", False)
    
    def print_error(val):
        assert val == "error"
    
    failure.on_fail(print_error)

# Test cases for the filter method
def test_filter():
    success = Try(42, True)
    
    def is_even(x): return x % 2 == 0
    filtered_success = success.filter(is_even)
    assert filtered_success.value == 42
    assert filtered_success.is_success is True

# Test cases for the get method
def test_get():
    try_instance = Try(10, True)
    assert try_instance.get() == 10

# Test cases for the get_or_else method
def test_get_or_else():
    try_default = Try("error", False)
    assert try_default.get_or_else(0) == 0

if __name__ == "__main__":
    pytest.main()


import pytest
from pymonet.monad_try import Try

# Test initialization with a successful value
def test_init_successful():
    try_instance = Try(42, True)
    assert try_instance.value == 42
    assert try_instance.is_success is True

# Test initialization with a failed value
def test_init_failed():
    try_instance = Try("error", False)
    assert try_instance.value == "error"
    assert try_instance.is_success is False

# Test bind method with a successful function
def test_bind_successful():
    success = Try(42, True)
    def add_ten(x): return Try(x + 10, True)
    result = success.bind(add_ten)
    assert result.value == 52

# Test bind method with a failed function
def test_bind_failed():
    failure = Try("error", False)
    def add_ten(x): return Try(x + 10, True)
    result = failure.bind(add_ten)
    assert result.value == "error"
    assert not result.is_success

# Test bind method with a function that returns another Try instance
def test_bind_nested():
    success = Try(42, True)
    def successful_try(x): return Try(x + 10, True)
    result = success.bind(successful_try)
    assert result.value == 52

# Test bind method with a function that raises an exception
def test_bind_exception():
    success = Try(42, True)
    def failing_function(x): raise ValueError("Test failure")
    try:
        result = success.bind(failing_function)
    except ValueError as e:
        assert str(e) == "Test failure"

# Test get_or_else method with a successful Try instance
def test_get_or_else():
    try_instance = Try(10, True)
    default_value = 0
    assert try_instance.get_or_else(default_value) == 10

# Test get_or_else method with a failed Try instance
def test_get_or_else_failed():
    failure = Try("error", False)
    default_value = "fallback"
    assert failure.get_or_else(default_value) == "fallback"

# Test on_success method with a successful Try instance
def test_on_success():
    success = Try(42, True)
    def print_value(val):
        assert val == 42
    success.on_success(print_value)

# Test on_fail method with a failed Try instance
def test_on_fail():
    failure = Try("error", False)
    def print_error(val):
        assert val == "error"
    failure.on_fail(print_error)

if __name__ == "__main__":
    pytest.main()

# Module: pymonet.monad_try
import pytest
from pymonet.monad_try import Try

# Test initialization of successful Try instance
def test_successful_init():
    success = Try(42, True)
    assert success.value == 42
    assert success.is_success is True

# Test initialization of failed Try instance
def test_failed_init():
    failure = Try("error", False)
    assert failure.value == "error"
    assert failure.is_success is False

# Test map method with a successful operation
def test_map_successful():
    success = Try(42, True)
    def square(x): return x * x
    success_squared = success.map(square)
    assert success_squared.value == 1764

# Test bind method with a successful operation
def test_bind_successful():
    success = Try(5, True)
    def add_ten(x): return Try(x + 10, True)
    result = success.bind(add_ten)
    assert result.value == 15

# Test on_fail method with a failed operation
def test_on_fail():
    failure = Try("error", False)
    def print_error(val):
        assert val == "error"
    failure.on_fail(print_error)

if __name__ == "__main__":
    pytest.main()

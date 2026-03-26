
# Module: pymonet.monad_try
# test_pymonet_monad_try.py
from pymonet.monad_try import Try
import pytest

# Test creating a successful Try instance
def test_successful_try():
    try_instance = Try(42, True)
    assert try_instance.value == 42
    assert try_instance.is_success is True

# Test creating a failed Try instance
def test_failed_try():
    try_failure = Try("example", False)
    assert try_failure.value == "example"
    assert try_failure.is_success is False

# Test using the map method to transform the value
def test_map_method():
    def square(x):
        return x * x
    
    try_instance = Try(3, True)
    mapped_try = try_instance.map(square)
    assert mapped_try.value == 9
    assert mapped_try.is_success is True

# Test using the bind method to chain operations
def test_bind_method():
    def square(x):
        if isinstance(x, int):
            return Try(x * x, True)
        else:
            return Try(None, False)
    
    try_instance = Try(3, True)
    result = try_instance.bind(square)
    assert result.value == 9
    assert result.is_success is True

# Test using the on_success method to handle success
def test_on_success():
    def print_success(x):
        print("Success:", x)
    
    try_instance = Try(42, True)
    try_instance.on_success(print_success)
    # The function just prints a message, so we don't need to assert anything here

# Test using the on_fail method to handle failure
def test_on_fail():
    def print_error(value):
        print("Error:", value)
    
    try_instance = Try("some error", False)
    try_instance.on_fail(print_error)
    # The function just prints a message, so we don't need to assert anything here

# Test using the filter method to apply a filter function
def test_filter_method():
    def is_even(n):
        return n % 2 == 0
    
    try_instance = Try(42, True)
    filtered_try = try_instance.filter(is_even)
    assert filtered_try.value == 42
    assert filtered_try.is_success is True

# Test using the get method to retrieve the value
def test_get_method():
    try_instance = Try(42, True)
    result = try_instance.get()
    assert result == 42

# Test using the get_or_else method to handle non-successful cases
def test_get_or_else_method():
    try_instance = Try("some value", True)
    result = try_instance.get_or_else(0)
    assert result == "some value"

# Test the string representation of the Try class
def test_str_representation():
    try_instance = Try(42, True)
    assert str(try_instance) == 'Try[value=42, is_success=True]'

if __name__ == "__main__":
    pytest.main()

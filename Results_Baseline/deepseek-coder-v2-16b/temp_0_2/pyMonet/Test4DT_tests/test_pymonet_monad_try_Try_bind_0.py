# Module: pymonet.monad_try
import pytest
from pymonet.monad_try import Try

# Test initialization with success status
def test_init_with_success():
    try_instance = Try(42, True)
    assert try_instance.value == 42
    assert try_instance.is_success is True

# Test initialization with failure status
def test_init_with_failure():
    try_failure = Try("example", False)
    assert try_failure.value == "example"
    assert try_failure.is_success is False

# Test bind method with successful binder function
def test_bind_successful():
    def square(x):
        return Try(x * x, True)
    
    try_instance = Try(3, True)
    result = try_instance.bind(square)
    assert result.value == 9
    assert result.is_success is True

# Test bind method with failing binder function
def test_bind_failure():
    def fail_function(x):
        return Try("error", False)
    
    try_failure = Try("example", False)
    result = try_failure.bind(fail_function)
    assert result.value == "example"
    assert result.is_success is False

# Test on_success method with a print function
def test_on_success():
    def print_success(x):
        print("Success:", x)
    
    try_instance = Try(42, True)
    try_instance.on_success(print_success)
    # This should not raise an error and the output will be captured by pytest's stdout capture

# Test on_fail method with a print function
def test_on_fail():
    def print_error(value):
        print("Error:", value)
    
    try_instance = Try("some error", False)
    try_instance.on_fail(print_error)
    # This should not raise an error and the output will be captured by pytest's stdout capture

# Test filter method with a even number check function
def test_filter():
    def is_even(n):
        return n % 2 == 0
    
    try_instance = Try(42, True)
    filtered_try = try_instance.filter(is_even)
    assert filtered_try.value == 42
    assert filtered_try.is_success is True

# Test get method with success status
def test_get():
    try_instance = Try(42, True)
    result = try_instance.get()
    assert result == 42

# Test get_or_else method with failure status
def test_get_or_else():
    try_instance = Try("example", False)
    result = try_instance.get_or_else(0)
    assert result == 0

if __name__ == "__main__":
    pytest.main()

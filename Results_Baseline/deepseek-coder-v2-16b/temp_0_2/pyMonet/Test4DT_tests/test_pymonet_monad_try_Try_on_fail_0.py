
import pytest
from pymonet.monad_try import Try

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

# Test using the `on_fail` method to call a fail callback
def test_on_fail():
    def print_error(value):
        assert value == "some error"
    try_instance = Try("some error", False)
    try_instance.on_fail(print_error)

# Test using the `map` method to transform the value
def test_map():
    def square(x):
        return x * x
    
    try_instance = Try(3, True)
    mapped_try = try_instance.map(square)
    assert mapped_try.value == 9

# Test using the `bind` method to chain operations
def test_bind():
    def square(x):
        return Try(x * x, True)
    
    try_instance = Try(3, True)
    result = try_instance.bind(square)
    assert result.value == 9

# Test using the `on_success` method to call a success callback
def test_on_success():
    def print_success(x):
        assert x == 42
    try_instance = Try(42, True)
    try_instance.on_success(print_success)

# Test using the `get` method to retrieve the value
def test_get():
    try_instance = Try(42, True)
    result = try_instance.get()
    assert result == 42

# Test using the `get_or_else` method to get the value or a default
def test_get_or_else():
    try_instance = Try(42, True)
    result = try_instance.get_or_else(0)
    assert result == 42

# Test using the `filter` method to apply a filter function
def test_filter():
    def is_even(n):
        return n % 2 == 0
    
    try_instance = Try(42, True)
    filtered_try = try_instance.filter(is_even)
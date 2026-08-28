
import pytest
from pymonet.monad_try import Try

# Test initialization with correct parameters
def test_valid_initialization():
    try_valid = Try(42, True)
    assert try_valid.value == 42
    assert try_valid.is_success is True

# Test initialization without required parameter 'is_success'
def test_invalid_initialization():
    with pytest.raises(TypeError):
        try_missing_params = Try(42)

# Test string representation of the Try object
def test_str_representation():
    try_valid = Try(42, True)
    assert str(try_valid) == 'Try[value=42, is_success=True]'

# Test mapping function on a successful Try object
def test_map_function():
    def double_value(x):
        return x * 2

    try_valid = Try(42, True)
    mapped_try = try_valid.map(double_value)
    assert mapped_try.get() == 84

# Test bind function with a successful Try object
def test_bind_function():
    def divide_by_two(x):
        return Try(x / 2, True) if x % 2 == 0 else Try(None, False)

    try_valid = Try(8, True)
    bound_try = try_valid.bind(divide_by_two)
    assert bound_try.get() == 4.0

# Test bind function with a failed Try object
def test_bind_function_failure():
    def divide_by_two(x):
        return Try(x / 2, True) if x % 2 == 0 else Try(None, False)

    try_invalid = Try(9, True)
    bound_try = try_invalid.bind(divide_by_two)
    assert not bound_try.is_success

# Test on_success callback with a successful Try object
def test_on_success_callback():
    def print_value(x):
        assert x == 42

    try_valid = Try(42, True)
    try_valid.on_success(print_value)

# Test on_fail callback with a failed Try object
def test_on_fail_callback():
    def print_error(x):
        assert x == "error"

    try_invalid = Try("error", False)
    try_invalid.on_fail(print_error)

# Test filter function with a successful Try object
def test_filter_function():
    def is_even(x):
        return x % 2 == 0

    try_valid = Try(8, True)
    filtered_try = try_valid.filter(is_even)
    assert filtered_try.get() == 8

# Test filter function with a failed Try object
def test_filter_function_failure():
    def is_even(x):
        return x % 2 == 0

    try_invalid = Try(9, True)
    filtered_try = try_invalid.filter(is_even)
    assert not filtered_try.is_success

# Test get method with a successful Try object
def test_get_method():
    try_valid = Try(42, True)
    assert try_valid.get() == 42

# Test get_or_else method with a failed Try object
def test_get_or_else_method():
    try_invalid = Try("error", False)
    assert try_invalid.get_or_else("default") == "default"

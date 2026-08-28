
import pytest
from pymonet.monad_try import Try

# Test valid initialization of Try class
def test_valid_init():
    try1 = Try(42, True)
    assert not try1.is_success is None
    assert try1.value == 42

# Test invalid initialization with wrong type for is_success

# Test the map method on a successful Try instance
def test_map_method_on_success():
    try1 = Try(42, True)
    def double(x):
        return x * 2
    mapped_try = try1.map(double)
    assert mapped_try.is_success is True
    assert mapped_try.value == 84

# Test the bind method on a successful Try instance
def test_bind_method_on_success():
    try1 = Try(42, True)
    def divide_by_two(x):
        if x % 2 == 0:
            return Try(x / 2, True)
        else:
            return Try(None, False)
    bound_try = try1.bind(divide_by_two)
    assert bound_try.is_success is True
    assert bound_try.value == 21.0

# Test the on_success method with a log function
def test_on_success_method():
    try1 = Try(42, True)
    def log_success(value):
        print(f"Success! The value is {value}")
    try1.on_success(log_success)

# Test the on_fail method with a log function
def test_on_fail_method():
    try2 = Try("error", False)
    def log_failure(value):
        print(f"Failure! The error is {value}")
    try2.on_fail(log_failure)

# Test the filter method on a successful Try instance
def test_filter_method():
    try1 = Try(42, True)
    def is_even(x):
        return x % 2 == 0
    filtered_try = try1.filter(is_even)
    assert filtered_try.is_success is True
    assert filtered_try.value == 42

# Test the get method on a successful Try instance
def test_get_method():
    try1 = Try(42, True)
    value = try1.get()
    assert value == 42

# Test the get_or_else method on a failed Try instance
def test_get_or_else_method():
    try2 = Try("error", False)
    default_value = try2.get_or_else("default")
    assert default_value == "default"
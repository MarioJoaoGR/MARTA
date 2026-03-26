# Module: pymonet.monad_try
import pytest
from pymonet.monad_try import Try

# Test initialization with value and success status
def test_init():
    try_instance = Try(42, True)
    assert try_instance.value == 42
    assert try_instance.is_success is True
    
    try_failure = Try("example", False)
    assert try_failure.value == "example"
    assert try_failure.is_success is False

# Test filter method with a valid filterer function
def test_filter_valid():
    def is_even(n):
        return n % 2 == 0
    
    try_instance = Try(42, True)
    filtered_try = try_instance.filter(is_even)
    assert filtered_try.value == 42
    assert filtered_try.is_success is True
    
    another_try = Try(13, True)
    filtered_another_try = another_try.filter(is_even)
    assert filtered_another_try.value == 13
    assert filtered_another_try.is_success is False

# Test filter method with an invalid filterer function
def test_filter_invalid():
    def is_odd(n):
        return n % 2 != 0
    
    try_instance = Try(42, True)
    filtered_try = try_instance.filter(is_odd)
    assert filtered_try.value == 42
    assert filtered_try.is_success is False

# Test filter method with a function that always returns True
def test_filter_always_true():
    try_instance = Try(42, True)
    filtered_try = try_instance.filter(lambda x: True)
    assert filtered_try.value == 42
    assert filtered_try.is_success is True

# Test filter method with a function that always returns False
def test_filter_always_false():
    try_instance = Try(42, True)
    filtered_try = try_instance.filter(lambda x: False)
    assert filtered_try.value == 42
    assert filtered_try.is_success is False

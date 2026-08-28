# Module: pymonet.monad_try
import pytest
from pymonet.monad_try import Try

# Test initialization of successful Try instance
def test_successful_init():
    try_instance = Try(42, True)
    assert try_instance.value == 42
    assert try_instance.is_success is True

# Test initialization of failed Try instance
def test_failed_init():
    try_instance = Try("error", False)
    assert try_instance.value == "error"
    assert try_instance.is_success is False

# Test map method with a successful Try instance
def test_map_successful():
    def square(x): return x * x
    success = Try(42, True)
    mapped_success = success.map(square)
    assert mapped_success.value == 1764
    assert mapped_success.is_success is True

# Test map method with a failed Try instance
def test_map_failed():
    def square(x): return x * x
    failure = Try("error", False)
    mapped_failure = failure.map(square)
    assert mapped_failure.value == "error"
    assert mapped_failure.is_success is False

# Test map method with a function that does not change the value
def test_map_identity():
    success = Try(42, True)
    identity_mapped_success = success.map(lambda x: x)
    assert identity_mapped_success.value == 42
    assert identity_mapped_success.is_success is True

# Test map method with a function that changes the value for both successful and failed Try instances
def test_map_function():
    def add_ten(x): return x + 10
    success = Try(42, True)
    mapped_success = success.map(add_ten)
    assert mapped_success.value == 52
    assert mapped_success.is_success is True

    failure = Try("error", False)
    mapped_failure = failure.map(add_ten)
    assert mapped_failure.value == "error"
    assert mapped_failure.is_success is False

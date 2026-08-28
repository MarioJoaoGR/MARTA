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

# Test filter method with a successful Try instance and a filterer function that returns True
def test_filter_successful():
    def is_positive(x): return x > 0
    success = Try(42, True)
    filtered_success = success.filter(is_positive)
    assert filtered_success.value == 42
    assert filtered_success.is_success is True

# Test filter method with a successful Try instance and a filterer function that returns False
def test_filter_failed():
    def is_negative(x): return x < 0
    success = Try(42, True)
    filtered_failure = success.filter(is_negative)
    assert filtered_failure.value == 42
    assert filtered_failure.is_success is False

# Test filter method with a failed Try instance
def test_filter_failed_init():
    failure = Try("error", False)
    filtered_failure = failure.filter(lambda x: True)
    assert filtered_failure.value == "error"
    assert filtered_failure.is_success is False

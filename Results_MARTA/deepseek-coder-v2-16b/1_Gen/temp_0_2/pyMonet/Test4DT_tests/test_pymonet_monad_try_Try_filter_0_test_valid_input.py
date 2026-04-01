
import pytest
from pymonet.monad_try import Try

def is_even(n):
    return n % 2 == 0

def test_valid_input():
    success = Try(4, True)
    filtered_success = success.filter(is_even)
    assert filtered_success.value == 4
    assert filtered_success.is_success is True
    
    failure = Try(5, True)
    filtered_failure = failure.filter(is_even)
    assert filtered_failure.value == 5
    assert filtered_failure.is_success is False


import pytest
from pymonet.monad_try import Try

def is_even(n):
    return n % 2 == 0

def test_invalid_input():
    failure = Try(5, True)
    filtered_failure = failure.filter(is_even)
    assert not filtered_failure.is_success
    assert filtered_failure.value == 5

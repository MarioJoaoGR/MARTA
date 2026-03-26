
import pytest
from pymonet.monad_try import Try

def is_even(n):
    return n % 2 == 0

def test_invalid_input():
    odd_try = Try(3, is_success=True)
    filtered_odd_try = odd_try.filter(is_even)
    assert not filtered_odd_try.is_success, "Expected filter method to return failed Try object for invalid input"


import pytest
from pymonet.monad_try import Try

def is_even(n):
    return n % 2 == 0

def test_valid_input():
    even_try = Try(4, is_success=True)
    filtered_even_try = even_try.filter(is_even)
    assert filtered_even_try.is_success is True

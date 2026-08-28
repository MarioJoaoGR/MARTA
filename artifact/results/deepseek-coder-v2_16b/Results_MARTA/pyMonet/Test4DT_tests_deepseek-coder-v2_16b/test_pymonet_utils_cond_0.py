
import pytest
from typing import Callable, List, Tuple
from pymonet.utils import cond

# Test case 1: Basic usage of cond function
def test_basic_usage():
    def is_even(n):
        return n % 2 == 0

    def double(n):
        return n * 2

    result = cond([
        (is_even, double),
        (lambda n: n > 5, lambda n: n * 3)
    ])(4)
    assert result == 8

# Test case 2: Using cond with different conditions and actions

# Test case 3: Using cond with a list of conditions and actions
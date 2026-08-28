
import pytest
from flutes.iterator import scanl
from typing import Callable, Iterable, Iterator
import operator

# Test 1: Basic usage with `operator.add` and an initial value of 0
def test_scanl_with_initial():
    result = list(scanl(operator.add, [1, 2, 3, 4], 0))
    assert result == [0, 1, 3, 6, 10]

# Test 2: Usage with a lambda function and a list of strings
def test_scanl_with_lambda():
    result = list(scanl(lambda s, x: x + s, ['a', 'b', 'c', 'd']))
    assert result == ['a', 'ba', 'cba', 'dcba']

# Test 3: Usage without an initial value
def test_scanl_without_initial():
    result = list(scanl(operator.add, [1, 2, 3, 4]))
    assert result == [1, 3, 6, 10]

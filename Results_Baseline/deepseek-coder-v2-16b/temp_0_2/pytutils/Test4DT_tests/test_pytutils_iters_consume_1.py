
import pytest
from itertools import count
import collections

# Import the function from its module
from pytutils.iters import consume

def test_consume_none():
    lst = [1, 2, 3, 4]
    it = iter(lst)
    with pytest.raises(StopIteration):
        consume(it)
        next(it)

def test_consume_specific_steps():
    lst = [1, 2, 3, 4]
    it = iter(lst)
    consume(it, n=2)
    assert next(it) == 3
    assert next(it) == 4

def test_consume_more_than_available():
    lst = [1, 2, 3, 4]
    it = iter(lst)
    consume(it, n=10)
    with pytest.raises(StopIteration):
        next(it)

def test_consume_zero_steps():
    lst = [1, 2, 3, 4]
    it = iter(lst)
    consume(it, n=0)
    assert next(it) == 1

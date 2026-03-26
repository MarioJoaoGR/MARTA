
# Module: pytutils.iters
import pytest
import itertools
import collections
from pytutils.iters import consume

# Test cases for consume function
def test_consume_default():
    lst = [1, 2, 3, 4]
    it = iter(lst)
    consume(it)
    assert next(it) == 1

def test_consume_specific_number():
    lst = [1, 2, 3, 4]
    it = iter(lst)
    consume(it, 2)
    assert next(it) == 3

def test_consume_custom_iterator():
    from itertools import islice, count
    lst = [1, 2, 3, 4]
    it = iter(lst)
    consume(it, 1)
    assert next(it) == 2

# Edge cases to consider:
def test_consume_none():
    with pytest.raises(TypeError):
        consume()

def test_consume_invalid_iterator():
    with pytest.raises(TypeError):
        consume("not an iterator")

def test_consume_negative_n():
    lst = [1, 2, 3, 4]
    it = iter(lst)
    with pytest.raises(StopIteration):
        consume(it, -1)

def test_consume_large_n():
    lst = [1, 2, 3, 4]
    it = iter(lst)
    consume(it, 10)
    assert next(it) is None  # Should reach the end and return None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_iters_consume_0
pytutils/Test4DT_tests/test_pytutils_iters_consume_0.py:31:8: E1120: No value for argument 'iterator' in function call (no-value-for-parameter)


"""
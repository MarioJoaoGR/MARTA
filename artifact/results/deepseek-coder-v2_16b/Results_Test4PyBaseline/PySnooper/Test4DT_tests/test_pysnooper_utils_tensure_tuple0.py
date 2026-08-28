
import pytest
from pysnooper.utils import ensure_tuple
from collections import abc as collections_abc
from six import string_types

# Test case 1: Passing a list to ensure_tuple
def test_ensure_tuple_list():
    result = ensure_tuple([1, 2, 3])
    assert isinstance(result, tuple), "Expected type is tuple"
    assert result == (1, 2, 3), "Expected output is (1, 2, 3)"

# Test case 2: Passing a string to ensure_tuple
def test_ensure_tuple_string():
    result = ensure_tuple("hello")
    assert isinstance(result, tuple), "Expected type is tuple"
    assert result == ('hello',), "Expected output is ('hello',)"

# Test case 3: Passing None to ensure_tuple
def test_ensure_tuple_none():
    result = ensure_tuple(None)
    assert isinstance(result, tuple), "Expected type is tuple"
    assert result == (None,), "Expected output is (None,)"

# Test case 4: Passing an integer to ensure_tuple
def test_ensure_tuple_integer():
    result = ensure_tuple(42)
    assert isinstance(result, tuple), "Expected type is tuple"
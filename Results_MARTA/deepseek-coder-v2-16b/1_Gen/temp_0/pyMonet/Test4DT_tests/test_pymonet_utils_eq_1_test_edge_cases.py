
import pytest
from pymonet.utils import eq

def test_eq():
    assert eq(5, 5) == True
    assert eq("hello", "world") == False
    assert eq(None, None) == True
    assert eq([1, 2], [1, 2]) == True
    assert eq([1, 2], [3, 4]) == False
    assert eq({"a": 1}, {"a": 1}) == True
    assert eq({"a": 1}, {"b": 2}) == False

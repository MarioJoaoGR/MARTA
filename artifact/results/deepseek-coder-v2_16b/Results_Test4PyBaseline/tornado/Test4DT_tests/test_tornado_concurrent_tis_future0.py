# Module: tornado.concurrent
import pytest
from typing import Any

# Assuming the module name is tornado.concurrent and we need to define the FUTURES class here itself
class FUTURES: pass

def is_future(x: Any) -> bool:
    return isinstance(x, FUTURES)

# Test cases for the function `is_future`
def test_is_future_with_instance():
    futures = FUTURES()
    assert is_future(futures) == True

def test_is_future_with_string():
    assert is_future("not a future") == False

def test_is_future_with_none():
    assert is_future(None) == False

def test_is_future_with_int():
    assert is_future(42) == False

def test_is_future_with_float():
    assert is_future(3.14) == False

def test_is_future_with_list():
    assert is_future([1, 2, 3]) == False

def test_is_future_with_dict():
    assert is_future({}) == False

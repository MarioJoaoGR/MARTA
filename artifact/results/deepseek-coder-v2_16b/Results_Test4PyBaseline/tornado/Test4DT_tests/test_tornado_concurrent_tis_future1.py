
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

# Additional test cases to cover uncovered lines and edge cases
def test_is_future_with_unknown_type():
    class UnknownType: pass
    unknown = UnknownType()
    assert is_future(unknown) == False

def test_is_future_with_future_subclass():
    class FutureSubclass(FUTURES): pass
    future_subclass = FutureSubclass()
    assert is_future(future_subclass) == True

def test_is_future_with_nonexistent_type():
    # Assuming a type that does not exist in the module
    class NonExistentType: pass
    nonexistent = NonExistentType()
    assert is_future(nonexistent) == False

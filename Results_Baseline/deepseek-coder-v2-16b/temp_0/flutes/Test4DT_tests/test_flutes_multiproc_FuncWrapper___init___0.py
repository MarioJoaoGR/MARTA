
import pytest
from flutes.multiproc import FuncWrapper
from typing import Callable, Iterable, Mapping, Any

# Define a sample function to wrap
def add_one(x):
    return x + 1

# Define another sample function to wrap
def multiply(a, b=1):
    return a * b

# Define a function that takes no arguments
def no_arguments():
    return "No args here!"

# Test cases for FuncWrapper class
@pytest.mark.parametrize("fn, args, kwds, expected", [
    (add_one, (2,), {}, 3),
    (no_arguments, (), {}, "No args here!"),
    (multiply, (4,), {'b': 5}, 20)
])
def test_funcwrapper(fn, args, kwds, expected):
    wrapper = FuncWrapper(fn, args, kwds)
    assert wrapper.fn(*args, **kwds) == expected

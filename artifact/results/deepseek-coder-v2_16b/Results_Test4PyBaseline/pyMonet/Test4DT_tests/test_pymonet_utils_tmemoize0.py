# Module: pymonet.utils
import pytest
from typing import Callable, List, Any
from pymonet.utils import memoize

# Define a simple function to be memoized
def add(x):
    print("Calculating...")
    return x + 1

# Memoize the function
memoized_add = memoize(add)

# Test that the memoized function calculates and returns the result for new arguments
def test_memoized_add():
    assert memoized_add(5) == 6
    # The second call should return the cached result since the argument is the same.
    assert memoized_add(5) == 6

# Define a function with multiple arguments to be memoized using a custom key function
def add_key(x, y):
    return x == y

memoized_add_with_key = memoize(add, key=add_key)

# Test that the memoized function calculates and returns the result for new arguments with a custom key function
def test_memoized_add_with_key():
    assert memoized_add_with_key(5) == 6
    # The second call should return the cached result since the argument is the same.
    assert memoized_add_with_key(5) == 6

# Define a function to be used in Lazy
def square(x):
    print("Calculating...")
    return x * x

# Create a Lazy instance with the function
class Lazy:
    def __init__(self, fn: Callable[[Any], Any]):
        self.fn = fn
        self.cache = None

    def __call__(self, *args):
        if self.cache is None:
            self.cache = self.fn(*args)
        return self.cache

# Test that the Lazy instance calculates and returns the result for new arguments
def test_lazy():
    lazy_square = Lazy(square)
    assert lazy_square(5) == 25
    # The second call should return the cached result since the argument is the same.
    assert lazy_square(5) == 25

# Create a Right instance with a value
class Right:
    def __init__(self, value):
        self.value = value

    def map(self, fn: Callable[[Any], Any]):
        return Right(fn(self.value))

# Test that the map method transforms the contained value
def test_right():
    right_instance = Right(10)
    mapped_right = right_instance.map(lambda x: x + 1)
    assert mapped_right.value == 11

# Create a Box with an integer value
class Box:
    def __init__(self, value):
        self.value = value

    def map(self, fn: Callable[[Any], Any]):
        return Box(fn(self.value))

    def bind(self, fn: Callable[[Any], Any]):
        return fn(self.value)

# Test that the map method transforms the contained value
def test_box():
    box = Box(42)
    mapped_box = box.map(lambda x: x + 1)
    assert mapped_box.value == 43

# Test that the bind method applies a transformation
def test_bind():
    box = Box(42)
    bound_box = box.bind(lambda x: x * 2)
    assert bound_box == 84

if __name__ == "__main__":
    pytest.main()

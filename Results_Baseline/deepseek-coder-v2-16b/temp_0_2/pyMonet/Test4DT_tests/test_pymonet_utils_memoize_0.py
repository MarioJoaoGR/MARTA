
import pytest
from typing import Callable, List, Any
from pymonet.utils import memoize

# Define a simple function to memoize
def add(x):
    return x + 1

# Memoize the function
memoized_add = memoize(add)

# Test cases for memoize function
def test_memoize_basic():
    assert memoized_add(2) == 3
    assert memoized_add(2) == 3  # Should return cached result

def test_memoize_different_argument():
    assert memoized_add(3) == 4
    assert memoized_add(3) == 4  # Should return cached result

# Define a function to be memoized
def square(x):
    return x * x

# Create a lazy instance with the memoized function
class Lazy:
    def __init__(self, fn):
        self.fn = memoize(fn)
    
    def fold(self):
        return lambda x: self.fn(x)

lazy_square = Lazy(square)

# Test cases for lazy evaluation
def test_lazy_evaluation():
    assert lazy_square.fold()(5) == 25
    assert lazy_square.fold()(5) == 25  # Should return cached result

# Define a simple fork function
class Task:
    def __init__(self, fn):
        self.fn = memoize(fn)
    
    def map(self, transform):
        return Task(lambda x: transform(self.fn(x)))
    
    def fork(self, reject, resolve):
        result = self.fn(42)
        if isinstance(result, Exception):
            return reject(result)
        else:
            return resolve(result)

# Test cases for Task class
def test_task_map():
    task = Task(lambda x: x * 2)
    new_task = task.map(lambda x: x * 2)
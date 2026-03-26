# Module: flutes.multiproc
import pytest
from multiprocessing import Queue
from typing import Iterator
import logging
from flutes.multiproc import _gather_fn  # Assuming the module name is correct and the function is imported correctly

# Define a sample callable function that yields results
def example_fn(x):
    yield x * 2
    yield x * 3

# Create a queue to hold the results
q = Queue()

# Call _gather_fn with the example function, queue, and an argument
result = _gather_fn(q, example_fn, 5)
print(f"Result: {result}")

def test_basic_usage():
    q = Queue()
    result = _gather_fn(q, example_fn, 5)
    assert result is True
    # Add assertions to check the contents of the queue if possible

def test_handling_exceptions():
    def problematic_fn(x):
        if x == 5:
            raise ValueError("Value error occurred!")
        yield x * 2
        yield x * 3
    
    q = Queue()
    try:
        result = _gather_fn(q, problematic_fn, 5)
    except ValueError as e:
        assert str(e) == "Value error occurred!"

def test_different_types():
    def example_fn(x):
        yield x * 2
        yield str(x) + " is a string"
    
    q = Queue()
    result = _gather_fn(q, example_fn, 5)
    assert result is True
    # Add assertions to check the contents of the queue if possible

def test_end_signature():
    def end_example_fn(x):
        yield x * 2
        yield x * 3
    
    q = Queue()
    result = _gather_fn(q, end_example_fn, 5)
    assert result is True
    # Add assertions to check the contents of the queue if possible

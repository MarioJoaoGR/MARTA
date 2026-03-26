
import pytest
from multiprocessing import Queue
from typing import Iterator, Optional, Callable, TypeVar
from flutes.multiproc import _gather_fn, END_SIGNATURE

# Define type variables for clarity in the function signature
T = TypeVar('T')
R = TypeVar('R')

def test_valid_inputs():
    # Mock functions and data to be used in the test
    def example_fn(x):
        yield x * 2
        yield x * 3
    
    q = Queue()
    
    # Call the function with valid inputs
    result = _gather_fn(q, example_fn, 5)
    
    # Check if the results are in the queue as expected
    assert q.get() == 10  # First item yielded by example_fn(5) is 10
    assert q.get() == 15  # Second item yielded by example_fn(5) is 15
    assert q.get() == END_SIGNATURE  # End of generation signal
    
    # Check the return value
    assert result is True


import pytest
from multiprocessing import Queue
from typing import Callable, Iterator, Optional, TypeVar
from unittest.mock import MagicMock, patch
from flutes.multiproc import _gather_fn, END_SIGNATURE

# Define type variables
R = TypeVar('R')
T = TypeVar('T')

@pytest.mark.parametrize("queue, fn, args, kwargs", [
    (Queue(), lambda x: iter([x*2]), (5,), {}),
    (Queue(), lambda x: iter([x*3]), (5,), {}),
])
def test_valid_inputs(queue, fn, args, kwargs):
    # Create a mock function that yields results
    def example_fn(x):
        yield x * 2
        yield x * 3
    
    # Call the _gather_fn with the mocked queue and function
    result = _gather_fn(queue, example_fn, *args, **kwargs)
    
    # Check if the results are in the queue
    assert queue.get() == (5*2)
    assert queue.get() == (5*3)
    assert queue.get() == END_SIGNATURE
    
    # Assert that the function returned True
    assert result is True

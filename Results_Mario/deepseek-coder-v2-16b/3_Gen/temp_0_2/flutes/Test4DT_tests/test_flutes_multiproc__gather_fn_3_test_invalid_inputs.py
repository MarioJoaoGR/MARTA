
import pytest
from multiprocessing import Queue
from flutes.multiproc import _gather_fn, END_SIGNATURE
from typing import Callable, Iterator, Optional, TypeVar

T = TypeVar('T')
R = TypeVar('R')

def test_invalid_inputs():
    queue = None  # This is the invalid input we are testing for.
    fn = lambda: iter([1, 2, 3])  # A dummy function to pass as an argument.
    
    with pytest.raises(AttributeError):
        _gather_fn(queue, fn)  # Passing None instead of a Queue should raise AttributeError due to the queue.put call on a NoneType object.

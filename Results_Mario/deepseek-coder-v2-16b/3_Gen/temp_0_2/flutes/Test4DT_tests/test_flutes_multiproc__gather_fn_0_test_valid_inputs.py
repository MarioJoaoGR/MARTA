
import pytest
import multiprocessing
from typing import Iterator, Optional, Callable, TypeVar, cast
from flutes.multiproc import _gather_fn, END_SIGNATURE

T = TypeVar('T')
R = TypeVar('R')

def generate_items(num: int) -> Iterator[str]:
    for i in range(num):
        yield f"item_{i}"

@pytest.mark.parametrize("num", [5, 10])
def test_valid_inputs(num):
    # Create a multiprocessing queue
    q = multiprocessing.Queue()
    
    # Call the function with the mock function and queue
    result = _gather_fn(q, generate_items, num)
    
    # Check that the results are in the queue
    for i in range(num):
        assert q.get() == f"item_{i}"
    
    # Check that the end signal is in the queue
    assert q.get() == END_SIGNATURE

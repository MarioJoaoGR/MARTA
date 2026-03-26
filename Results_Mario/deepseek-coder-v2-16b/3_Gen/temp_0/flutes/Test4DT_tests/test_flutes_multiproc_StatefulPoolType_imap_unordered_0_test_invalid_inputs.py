
import pytest
from multiprocessing import Pool, Queue
from typing import List, Any, Callable, Iterable, Mapping, Iterator
from flutes.multiproc import safe_pool  # Assuming this is a hypothetical module for stateful pool

class State:
    def __init__(self):
        self.queue = Queue()

    def process_item(self, item: int) -> int:
        return item * 2

# Mocking the safe_pool function to return a dummy pool instance for testing purposes
def mock_safe_pool(state_class):
    class DummyPool:
        def imap_unordered(self, fn, iterable, chunksize=1, args=(), kwds={}):
            if not callable(fn):
                raise ValueError("Function must be callable")
            return iter([fn(state_instance, item) for item in iterable])
    state_instance = state_class()
    return DummyPool()

# Applying the mock to the safe_pool function
safe_pool = mock_safe_pool  # type: ignore[assignment]

def test_invalid_inputs():
    stateful_pool = safe_pool(State)
    
    with pytest.raises(ValueError):
        results = list(stateful_pool.imap_unordered('not a function', range(10), chunksize=2))

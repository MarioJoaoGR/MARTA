
import pytest
from flutes.multiproc import StatefulPoolType, safe_pool
from multiprocessing import Pool, Queue
from typing import List, Any

class State:
    def __init__(self):
        self.queue = Queue()
    
    def process_item(self, item: int) -> int:
        # Example function to process each item in the iterable
        return item * 2

def test_error_case():
    with pytest.raises(TypeError):
        stateful_pool = StatefulPoolType(State)

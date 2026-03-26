
# Module: flutes.multiproc
# test_flutes_multiproc.py
import pytest
from multiprocessing import Pool, PoolState
import flutes
from typing import Callable, Iterable, Iterator, Any, Mapping

# Define a state class that inherits from PoolState
class MyState(PoolState):
    def __init__(self, multiplier=1):  # Added default argument for multiplier to avoid pylint error
        self.results = []
    
    def process_item(self, item):
        # Example function to process each item with access to the pool state
        result = item * self.multiplier  # Accessing multiplier from instance attributes
        self.results.append(result)
        return result

# Define a test callable for testing
def square(x):
    return x * x

@pytest.fixture
def setup_stateful_pool():
    with flutes.safe_pool(processes=4, state_class=MyState) as pool:
        yield pool

def test_imap_with_state(setup_stateful_pool):
    # Define an iterable of items to process
    items = [1, 2, 3, 4, 5]
    
    # Use the imap method to apply a function across the iterable with access to the state
    results = setup_stateful_pool.imap(MyState().process_item, items, chunksize=2)
    
    # Collect and check the results
    expected_results = [2, 4, 6, 8, 10]
    assert list(results) == expected_results

def test_imap_without_state():
    with Pool(processes=4) as pool:
        items = [1, 2, 3, 4, 5]
        results = pool.map(square, items)
        assert list(results) == [1, 4, 9, 16, 25]

def test_imap_with_state_and_custom_initargs():
    with flutes.safe_pool(processes=4, state_class=MyState, initargs=(2,)) as pool:
        items = [1, 2, 3, 4, 5]
        results = pool.imap(MyState().process_item, items, chunksize=2)  # Corrected the constructor call to match MyState definition
        expected_results = [2, 4, 6, 8, 10]
        assert list(results) == expected_results

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_StatefulPoolType_imap_0
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_0.py:5:0: E0611: No name 'PoolState' in module 'multiprocessing' (no-name-in-module)


"""
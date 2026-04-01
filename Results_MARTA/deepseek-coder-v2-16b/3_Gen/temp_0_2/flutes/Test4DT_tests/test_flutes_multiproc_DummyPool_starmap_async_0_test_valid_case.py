
import multiprocessing as mp
from typing import Optional, Callable, Iterable, Any, List, Tuple
from flutes.multiproc import DummyPool

def test_valid_case():
    # Create a DummyPool instance with single-threaded execution
    pool = DummyPool(processes=0)
    
    # Define a sample function to be mapped over an iterable of arguments
    def sample_func(x, y):
        return x + y
    
    # Define an iterable of arguments for the starmap method
    args_iterable = [(1, 2), (3, 4)]
    
    # Use the starmap method to apply the function over the iterable of arguments
    results = pool.starmap(sample_func, args_iterable)
    
    # Assert that the results are as expected
    assert results == [3, 7]


import pytest
from flutes.multiproc import DummyPool  # Correctly importing from the module 'flutes.multiproc'

def test_edge_cases():
    pool = DummyPool(processes=0)  # Create a single-threaded pool
    
    def square(x):
        return x * x
    
    results = list(pool.imap(square, [1, 2, 3]))  # Apply the function to an iterable
    
    assert results == [1, 4, 9]  # Check if the results are as expected

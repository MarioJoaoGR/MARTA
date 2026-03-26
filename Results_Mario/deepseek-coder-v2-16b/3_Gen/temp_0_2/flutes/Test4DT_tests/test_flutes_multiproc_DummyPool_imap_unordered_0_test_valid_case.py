
import pytest
from multiprocessing import Pool, TimeoutError
from flutes.multiproc import DummyPool

def test_valid_case():
    # Create a DummyPool instance with processes set to 0 for single-threaded execution
    pool = DummyPool(processes=0)
    
    # Define a function to be applied in the pool
    def square(x):
        return x * x
    
    # Test iterable with valid inputs
    results = list(pool.imap_unordered(square, [1, 2, 3]))
    
    # Expected output: [1, 4, 9]
    assert results == [1, 4, 9]

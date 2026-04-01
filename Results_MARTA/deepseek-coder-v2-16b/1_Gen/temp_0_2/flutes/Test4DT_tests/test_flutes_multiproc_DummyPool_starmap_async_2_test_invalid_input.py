
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

def test_invalid_input():
    pool = DummyPool(processes=0)  # Create a DummyPool with processes set to 0, which means single-threaded execution
    
    with pytest.raises(TypeError):
        # Test that passing an invalid input (a non-callable function) raises a TypeError
        result = pool.starmap_async([1, 2], "not_a_function")

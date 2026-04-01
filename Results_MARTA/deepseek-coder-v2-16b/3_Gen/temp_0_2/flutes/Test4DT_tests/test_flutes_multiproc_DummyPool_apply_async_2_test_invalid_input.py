
import pytest
from flutes.multiproc import DummyPool

def test_invalid_input():
    pool = DummyPool(processes=0)  # Create a DummyPool instance with single-threaded execution
    
    # Define an invalid function (None) to pass to apply_async
    fn = None
    
    # Use pytest.raises to check if the method call raises a TypeError
    with pytest.raises(TypeError):
        result = pool.apply_async(fn, args=(1, 2))

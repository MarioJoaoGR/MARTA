
import pytest
from flutes.multiproc import DummyPool

def test_invalid_input():
    pool = DummyPool(processes=0)  # Create a DummyPool instance with single-threaded execution
    
    with pytest.raises(TypeError):
        # Test that starmap raises TypeError when fn is not callable
        result = pool.starmap_async(None, [(1,)])  # Provide an invalid function (None) as the first argument

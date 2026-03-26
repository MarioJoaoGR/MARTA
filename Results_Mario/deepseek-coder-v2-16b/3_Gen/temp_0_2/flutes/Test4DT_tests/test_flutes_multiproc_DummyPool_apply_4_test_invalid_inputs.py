
import pytest
from flutes.multiproc import DummyPool

def test_invalid_inputs():
    pool = DummyPool(processes=0)  # Single-threaded execution for testing invalid inputs
    
    with pytest.raises(TypeError):
        result = pool.apply("not a callable", args=(1,))

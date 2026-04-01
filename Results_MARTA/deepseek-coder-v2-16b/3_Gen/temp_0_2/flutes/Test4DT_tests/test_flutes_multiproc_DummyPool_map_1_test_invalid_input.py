
import pytest
from flutes.multiproc import DummyPool

def test_invalid_input():
    pool = DummyPool(processes=0)  # Create a single-threaded pool
    
    with pytest.raises(TypeError):
        results = list(pool.map(lambda x: x * 2, [1, 2, 3], args=(42,)))  # Invalid usage of args


import pytest
from multiprocessing import Pool
from flutes.multiproc import PoolWrapper

def test_invalid_inputs():
    pool = PoolWrapper()
    
    # Test with None as the function argument
    with pytest.raises(TypeError):
        pool.map(None, [1, 2, 3])
        
    # Test with an integer as the function argument
    with pytest.raises(TypeError):
        pool.map(42, [1, 2, 3])
        
    # Test with a string as the function argument
    with pytest.raises(TypeError):
        pool.map("not_a_function", [1, 2, 3])

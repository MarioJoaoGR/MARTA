
import pytest
from flutes.multiproc import PoolWrapper

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test case 1: Invalid argument type for map method
        pool = PoolWrapper()
        list(pool.map("not a function", [1, 2, 3]))
    
    with pytest.raises(TypeError):
        # Test case 2: Invalid argument type for imap_unordered method
        pool = PoolWrapper()
        list(pool.imap_unordered("not an iterable", lambda x: x))

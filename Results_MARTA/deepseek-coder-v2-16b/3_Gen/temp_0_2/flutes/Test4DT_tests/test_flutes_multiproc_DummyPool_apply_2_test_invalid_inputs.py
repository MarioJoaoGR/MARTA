
import pytest
from flutes.multiproc import DummyPool

def test_invalid_inputs():
    pool = DummyPool(processes=0)  # Create a DummyPool instance with single-threaded execution
    
    def valid_function(x):
        return x * 2
    
    result = pool.apply(valid_function, args=(5,))
    assert result == 10
    
    invalid_functions = [None, 5, [], {}]  # Invalid function types to test for TypeError
    
    for func in invalid_functions:
        with pytest.raises(TypeError):
            pool.apply(func, args=(5,))  # Attempt to apply an invalid function type

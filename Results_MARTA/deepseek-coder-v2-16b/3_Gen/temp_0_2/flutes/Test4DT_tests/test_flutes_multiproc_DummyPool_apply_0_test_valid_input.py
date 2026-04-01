
import pytest
from flutes.multiproc import DummyPool

def test_valid_input():
    def example_function(x):
        return x * 2
    
    pool = DummyPool(processes=0)
    result = pool.apply(example_function, args=(5,))
    assert result == 10

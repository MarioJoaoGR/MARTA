
import pytest
from flutes.multiproc import DummyPool

def test_invalid_input():
    # Test that DummyPool raises a TypeError when given invalid input types
    
    with pytest.raises(TypeError):
        pool = DummyPool(processes=0)  # Valid processes value
        pool.map_async("not_a_function", [1, 2, 3])  # Invalid function type

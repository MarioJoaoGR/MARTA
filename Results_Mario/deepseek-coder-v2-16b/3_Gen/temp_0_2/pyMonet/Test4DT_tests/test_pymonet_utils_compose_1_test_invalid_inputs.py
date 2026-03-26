
import pytest
from pymonet.utils import compose
from functools import reduce

def test_invalid_inputs():
    # Test with None as value
    with pytest.raises(TypeError):
        compose(None, lambda x: x + 1)
    
    # Test with invalid function type (e.g., string)
    with pytest.raises(TypeError):
        compose(5, "not_a_function")
    
    # Test with None as a function
    with pytest.raises(TypeError):
        compose(5, lambda x: x + 1, None)

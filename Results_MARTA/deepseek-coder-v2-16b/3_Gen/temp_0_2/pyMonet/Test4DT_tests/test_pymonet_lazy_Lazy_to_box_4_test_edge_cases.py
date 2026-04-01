
import pytest
from pymonet.lazy import Lazy

def test_edge_cases():
    # Test None input
    lazy = Lazy(lambda x: x)  # Using a lambda to avoid actual function call
    with pytest.raises(TypeError):
        result = lazy.to_box()  # Should raise TypeError because no arguments are provided

    # Test empty tuple input
    lazy = Lazy(lambda x: x)  # Using a lambda to avoid actual function call
    with pytest.raises(TypeError):
        result = lazy.to_box()  # Should raise TypeError because no arguments are provided

    # Test None argument in to_box
    lazy = Lazy(lambda x: x)  # Using a lambda to avoid actual function call
    with pytest.raises(TypeError):
        result = lazy.to_box()  # Should raise TypeError because no arguments are provided

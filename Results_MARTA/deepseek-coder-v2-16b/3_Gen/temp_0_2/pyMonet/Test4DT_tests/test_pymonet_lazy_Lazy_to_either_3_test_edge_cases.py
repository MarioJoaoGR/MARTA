
import pytest
from pymonet.lazy import Lazy

def test_edge_cases():
    # Test None input
    lazy = Lazy(lambda x: x)
    with pytest.raises(TypeError):
        lazy.to_either()  # Should raise TypeError because no arguments are provided

    # Test empty input
    lazy = Lazy(lambda x: x)
    with pytest.raises(TypeError):
        lazy.to_either()  # Should raise TypeError because no arguments are provided

    # Test valid input
    lazy = Lazy(lambda x: x * x)
    result = lazy.to_either(5).value
    assert result == 25

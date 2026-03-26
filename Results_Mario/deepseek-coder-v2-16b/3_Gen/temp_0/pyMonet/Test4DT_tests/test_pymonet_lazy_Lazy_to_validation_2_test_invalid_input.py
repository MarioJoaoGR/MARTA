
import pytest
from pymonet.lazy import Lazy

def test_invalid_input():
    with pytest.raises(TypeError):
        lazy = Lazy(42)  # Passing an integer instead of a callable function
        lazy.to_validation()

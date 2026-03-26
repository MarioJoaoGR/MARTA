
import pytest
from pymonet.lazy import Lazy

def test_invalid_input():
    with pytest.raises(TypeError):
        # Providing invalid constructor function (non-callable)
        lazy = Lazy(42)  # Non-callable object to simulate invalid input
        lazy.to_either()  # Call to_either method should raise TypeError

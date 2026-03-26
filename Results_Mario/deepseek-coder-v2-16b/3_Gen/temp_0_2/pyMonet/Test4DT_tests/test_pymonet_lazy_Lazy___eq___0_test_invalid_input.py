
import pytest
from pymonet.lazy import Lazy

def test_invalid_input():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    
    # Test with an invalid input type (a string instead of a number)
    with pytest.raises(TypeError):
        lazy.constructor_fn("invalid")

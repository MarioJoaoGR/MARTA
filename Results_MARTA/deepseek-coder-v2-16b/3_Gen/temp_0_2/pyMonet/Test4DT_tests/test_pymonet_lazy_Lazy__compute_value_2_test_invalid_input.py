
import pytest
from pymonet.lazy import Lazy

def test_invalid_input():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    args = ('not a number',)
    
    with pytest.raises(TypeError):
        result = lazy._compute_value(*args)

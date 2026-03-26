
import pytest
from pymonet.lazy import Lazy

def test_invalid_input():
    def square(x):
        return x * x
    
    lazy = Lazy('not a function')  # Invalid function type
    args = ('not an argument',)  # Invalid arguments type
    
    with pytest.raises(TypeError):
        result = lazy._compute_value(*args)

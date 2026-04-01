
import pytest
from pymonet.lazy import Lazy

def test_invalid_case():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    invalid_input = 'string'
    
    with pytest.raises(TypeError):
        result = lazy.constructor_fn(invalid_input)

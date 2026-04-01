
import pytest
from pymonet.lazy import Lazy

def test_valid_inputs():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    assert lazy.get(5) == 25
    assert lazy.get() == 25
    either_value = lazy.to_either(5)
    assert either_value.value == 25


import pytest
from pymonet.lazy import Lazy

def test_valid_inputs():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    assert lazy.get(5) == 25
    assert lazy.to_box(5).value == 25

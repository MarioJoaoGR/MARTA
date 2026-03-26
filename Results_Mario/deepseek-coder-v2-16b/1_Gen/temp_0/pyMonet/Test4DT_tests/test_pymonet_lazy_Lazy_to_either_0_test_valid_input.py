
import pytest
from pymonet.lazy import Lazy

def test_valid_input():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    assert lazy.get(5) == 25

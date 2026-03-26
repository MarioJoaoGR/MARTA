
import pytest
from pymonet.lazy import Lazy

def test_valid_input():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    assert not lazy.is_evaluated  # Check that the function is not evaluated initially
    
    result = lazy._compute_value(5)  # Call _compute_value with valid arguments
    assert lazy.is_evaluated  # Check that the function has been evaluated
    assert result == 25  # Check the result of the computation

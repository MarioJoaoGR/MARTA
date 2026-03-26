
import pytest
from pymonet.lazy import Lazy

def test_valid_input():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    assert not lazy.is_evaluated  # Check that the function hasn't been evaluated yet
    result = lazy.get(5)           # Evaluate the function with an argument
    assert lazy.is_evaluated      # Check that the function has now been evaluated
    assert result == 25            # Check the result of the evaluation

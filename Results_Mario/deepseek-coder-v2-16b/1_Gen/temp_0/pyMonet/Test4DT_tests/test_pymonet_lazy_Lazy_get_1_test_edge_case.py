
import pytest
from pymonet.lazy import Lazy

def square(x):
    return x * x

def test_edge_case():
    # Initialize the Lazy object with the square function
    lazy = Lazy(square)
    
    # Test that calling get() without arguments evaluates the function correctly
    assert lazy.get(5) == 25, "Expected result of square(5) to be 25"


import pytest
from pymonet.lazy import Lazy

def test_edge_case():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    
    # First call to get should evaluate the function and store the result
    assert lazy.get(5) == 25
    
    # Subsequent calls to get should return the memoized value without re-evaluating the function
    assert lazy.get(5) == 25
    
    # Test to_maybe method
    maybe_lazy = lazy.to_maybe(5)
    assert maybe_lazy.value == 25

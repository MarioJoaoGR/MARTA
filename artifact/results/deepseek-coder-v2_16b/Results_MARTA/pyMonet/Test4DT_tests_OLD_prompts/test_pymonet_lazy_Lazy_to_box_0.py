
import pytest
from pymonet.lazy import Lazy

def test_valid_inputs():
    def expensive_computation():
        return sum(range(1000))
    
    lazy_object = Lazy(expensive_computation)
    assert not lazy_object.is_evaluated
    result = lazy_object.get()
    assert lazy_object.is_evaluated
    assert result == 499500

def test_edge_cases():
    def expensive_computation(data):
        return sum(data)
    
    # Test with None
    lazy_object = Lazy(lambda: None)
    assert not lazy_object.is_evaluated
    result = lazy_object.get()
    assert lazy_object.is_evaluated
    assert result is None

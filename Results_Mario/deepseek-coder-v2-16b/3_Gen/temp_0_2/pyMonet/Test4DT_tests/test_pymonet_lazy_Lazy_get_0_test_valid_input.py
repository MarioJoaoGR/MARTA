
import pytest
from pymonet.lazy import Lazy

def test_valid_input():
    def expensive_computation(x):
        return x * x
    
    lazy_value = Lazy(expensive_computation)
    assert not lazy_value.is_evaluated  # Initially False, since no value has been computed yet
    
    result = lazy_value.get(10)  # Computes the value using expensive_computation(10) and stores it in lazy_value.value
    assert lazy_value.is_evaluated  # Now True, as the value has been computed
    assert lazy_value.value == 100  # The result of the computation should be 100

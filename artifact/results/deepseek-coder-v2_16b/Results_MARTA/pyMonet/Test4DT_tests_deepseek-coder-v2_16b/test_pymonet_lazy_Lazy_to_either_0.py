
import pytest
from pymonet.lazy import Lazy

# Test valid input where Lazy is not nothing and has a valid value

# Test edge case where Lazy is empty (is_nothing is True)
def test_edge_case():
    def expensive_computation(data):
        return sum(data)
    
    lazy_object = Lazy(expensive_computation)
    with pytest.raises(AttributeError):
        result = lazy_object.fold([1, 2, 3])
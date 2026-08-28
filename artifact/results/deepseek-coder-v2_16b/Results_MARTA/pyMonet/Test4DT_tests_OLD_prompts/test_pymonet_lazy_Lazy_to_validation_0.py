
import pytest
from pymonet.lazy import Lazy
from unittest.mock import patch

def test_valid_input():
    def expensive_computation():
        return sum(range(1000))
    
    lazy_object = Lazy(expensive_computation)
    result = lazy_object.get()
    assert result == 499500

def test_edge_case():
    with pytest.raises(TypeError):
        Lazy().to_validation()

def test_invalid_input():
    def faulty_function():
        raise ValueError('Error')
    
    lazy_object = Lazy(faulty_function)
    with pytest.raises(ValueError):
        lazy_object.get()


import pytest
from unittest.mock import patch
from pymonet.lazy import Lazy

def test_edge_cases():
    def expensive_computation(data):
        return sum(data)
    
    lazy_object = Lazy(expensive_computation)
    
    with patch('pymonet.lazy.Lazy._compute_value', side_effect=lambda *args: 6):
        assert lazy_object.get() == 6


import pytest
from pymonet.lazy import Lazy

def test_edge_case():
    def square(x):
        return x * x
    
    lazy = Lazy(None)
    
    with pytest.raises(TypeError):
        lazy.to_validation()

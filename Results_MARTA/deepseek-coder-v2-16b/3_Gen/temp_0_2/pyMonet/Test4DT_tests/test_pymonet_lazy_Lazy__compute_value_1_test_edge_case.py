
import pytest
from pymonet.lazy import Lazy

def test_edge_case():
    # Arrange
    def square(x):
        return x * x
    
    lazy = Lazy(None)
    args = (5,)
    
    # Act & Assert
    with pytest.raises(TypeError):
        result = lazy._compute_value(*args)

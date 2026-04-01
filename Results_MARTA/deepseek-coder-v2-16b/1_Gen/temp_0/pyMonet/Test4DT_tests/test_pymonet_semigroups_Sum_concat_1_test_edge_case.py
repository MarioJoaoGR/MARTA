
import pytest
from pymonet.semigroups import Sum

def test_edge_case():
    # Test with None
    sum1 = Sum(0)
    sum2 = Sum(None)
    
    with pytest.raises(TypeError):
        result = sum1.concat(sum2)

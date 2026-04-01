
import pytest
from pymonet.semigroups import Semigroup

def test_edge_case():
    # Test with None
    s_none = Semigroup(None)
    assert s_none.value is None
    
    # Test with empty list
    s_empty = Semigroup([])
    assert s_empty.value == []
    
    # Test with boundary value (float('inf'))
    s_boundary = Semigroup(float('inf'))
    assert s_boundary.value == float('inf')


import pytest
from pymonet.semigroups import Semigroup

def test_edge_case():
    # Test with None
    s_none = Semigroup(None)
    assert s_none.value is None
    
    # Test with empty list
    s_empty_list = Semigroup([])
    assert s_empty_list.value == []
    
    # Additional boundary value test (e.g., an empty string, zero, etc.)
    s_zero = Semigroup(0)
    assert s_zero.value == 0

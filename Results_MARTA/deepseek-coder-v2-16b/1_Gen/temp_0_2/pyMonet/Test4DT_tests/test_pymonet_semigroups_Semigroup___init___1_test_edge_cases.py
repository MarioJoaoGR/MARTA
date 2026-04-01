
import pytest
from pymonet.semigroups import Semigroup

def test_edge_cases():
    # Test with None
    s_none = Semigroup(None)
    assert s_none.value is None
    
    # Test with empty list
    s_empty = Semigroup([])
    assert s_empty.value == []
    
    # Additional boundary value test (e.g., an empty string)
    s_boundary = Semigroup("")
    assert s_boundary.value == ""


import pytest
from pymonet.semigroups import Semigroup

def test_edge_cases():
    # Test with None
    s1 = Semigroup(None)
    assert s1.value is None
    
    # Test with empty list
    s2 = Semigroup([])
    assert s2.value == []
    
    # Additional boundary value test (e.g., zero, an empty string, etc.) can be added here if necessary


import pytest
from pymonet.semigroups import Semigroup

def test_edge_cases():
    # Test with None value
    s_none = Semigroup(None)
    assert s_none.value is None, "Expected value to be None"
    
    # Test with empty list value
    s_empty = Semigroup([])
    assert s_empty.value == [], "Expected value to be an empty list"

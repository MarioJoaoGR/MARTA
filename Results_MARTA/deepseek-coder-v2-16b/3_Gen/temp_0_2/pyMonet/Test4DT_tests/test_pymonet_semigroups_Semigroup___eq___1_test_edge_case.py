
import pytest
from pymonet.semigroups import Semigroup

def test_edge_case():
    # Test with None values
    s1 = Semigroup(None)
    s2 = Semigroup(None)
    assert s1 == s2, "Semigroups with None values should be equal"
    
    # Test with empty string values
    s3 = Semigroup('')
    s4 = Semigroup('')
    assert s3 == s4, "Semigroups with empty string values should be equal"


import pytest
from pymonet.semigroups import Semigroup

def test_edge_cases():
    # Test with None
    s1 = Semigroup(None)
    assert s1.value is None
    
    # Test with an empty list
    s2 = Semigroup([])
    assert s2.value == []
    
    # Test with a boundary value (e.g., 0 or an empty string)
    s3 = Semigroup(0)
    assert s3.value == 0
    
    s4 = Semigroup('')
    assert s4.value == ''

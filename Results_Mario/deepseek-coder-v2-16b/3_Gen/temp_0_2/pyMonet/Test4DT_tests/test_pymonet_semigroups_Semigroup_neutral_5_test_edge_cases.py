
import pytest
from pymonet.semigroups import Semigroup

def test_edge_cases():
    # Test None as a value
    s1 = Semigroup(None)
    assert s1.value is None
    
    # Test empty list as a value
    s2 = Semigroup([])
    assert s2.value == []
    
    # Test boundary values (e.g., 0, "", etc.)
    s3 = Semigroup(0)
    assert s3.value == 0
    
    s4 = Semigroup("")
    assert s4.value == ""

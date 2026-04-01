
import pytest
from pymonet.semigroups import Semigroup

def test_edge_cases():
    # Test with None
    s = Semigroup(None)
    assert s.value is None
    
    # Test with empty list
    s2 = Semigroup([])
    assert s2.value == []
    
    # Test with empty string
    s3 = Semigroup('')
    assert s3.value == ''

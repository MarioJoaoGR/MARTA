
import pytest
from pymonet.semigroups import Semigroup

def test_valid_inputs():
    s1 = Semigroup(5)
    s2 = Semigroup(5)
    s3 = Semigroup(10)
    
    assert s1 == s2, "s1 and s2 should be equal"
    assert not (s1 == s3), "s1 and s3 should not be equal"

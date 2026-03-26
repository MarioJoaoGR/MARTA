
import pytest
from pymonet.semigroups import Semigroup

def test_valid_case():
    s1 = Semigroup(5)
    s2 = Semigroup(5)
    
    assert s1 == s2

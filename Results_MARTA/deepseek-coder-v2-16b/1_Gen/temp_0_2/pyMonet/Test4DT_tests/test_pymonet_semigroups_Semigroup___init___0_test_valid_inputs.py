
import pytest
from pymonet.semigroups import Semigroup

def test_valid_inputs():
    s = Semigroup(5)
    s2 = Semigroup('hello')
    
    assert s.value == 5
    assert s2.value == 'hello'

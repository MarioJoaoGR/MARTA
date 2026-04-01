
import pytest
from pymonet.semigroups import Semigroup

def test_valid_input():
    s = Semigroup(5)
    assert s.value == 5
    
    s2 = Semigroup('hello')
    assert s2.value == 'hello'

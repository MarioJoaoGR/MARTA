
import pytest
from pymonet.semigroups import Semigroup

def test_valid_input():
    s = Semigroup(5)
    t = Semigroup('hello')
    
    assert s.value == 5
    assert t.value == 'hello'

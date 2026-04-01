
import pytest
from pymonet.semigroups import Semigroup

def test_valid_inputs():
    s = Semigroup(5)
    assert s.value == 5
    
    s = Semigroup("hello")
    assert s.value == "hello"

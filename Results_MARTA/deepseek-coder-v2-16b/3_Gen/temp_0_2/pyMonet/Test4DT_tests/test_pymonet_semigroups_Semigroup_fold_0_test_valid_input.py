
import pytest
from pymonet.semigroups import Semigroup

def test_valid_input():
    semigroup = Semigroup(5)
    
    def add_one(x):
        return x + 1
    
    result = semigroup.fold(add_one)
    assert result == 6, "Expected the fold operation to add one to the value"


import pytest
from pymonet.semigroups import Max

def test_valid_case_1():
    max_monoid = Max(0)
    another_max = Max(5)
    
    combined = max_monoid.concat(another_max)
    
    assert combined.value == 5

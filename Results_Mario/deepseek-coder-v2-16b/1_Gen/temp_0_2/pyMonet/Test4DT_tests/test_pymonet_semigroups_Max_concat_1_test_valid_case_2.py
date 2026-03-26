
import pytest
from pymonet.semigroups import Max

def test_valid_case_2():
    max_monoid = Max(-10)
    another_max = Max(5)
    
    combined = max_monoid.concat(another_max)
    
    assert combined.value == 5, "The combined value should be the largest of the two inputs."

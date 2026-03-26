
import pytest
from pymonet.semigroups import Max

def test_valid_case_1():
    max_monoid = Max(-float('inf'))
    another_max = Max(10)
    combined_max = max_monoid.concat(another_max)
    
    assert combined_max.value == 10, "Expected the value to be 10"

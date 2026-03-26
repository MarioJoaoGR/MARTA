
import pytest
from pymonet.semigroups import Min

def test_valid_case_1():
    min_instance = Min(5)
    other_min = Min(3)
    
    combined_min = min_instance.concat(other_min)
    
    assert combined_min.value == 3, "The combined value should be the smallest of the two instances."

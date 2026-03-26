
import pytest
from pymonet.semigroups import Min

def test_valid_case_1():
    min1 = Min(3.0)
    min2 = Min(4.5)
    
    combined_min = min1.concat(min2)
    
    assert combined_min.value == 3.0, "The smallest value should be returned"

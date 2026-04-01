
import pytest
from pymonet.semigroups import Min

def test_valid_case_2():
    min1 = Min(5.0)
    min2 = Min(5.0)
    
    combined_min = min1.concat(min2)
    
    assert combined_min.value == 5.0, "Expected the smallest value to be returned when both values are equal"

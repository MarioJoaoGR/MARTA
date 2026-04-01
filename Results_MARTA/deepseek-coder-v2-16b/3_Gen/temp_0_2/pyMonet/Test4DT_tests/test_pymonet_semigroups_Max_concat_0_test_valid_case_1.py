
import pytest
from pymonet.semigroups import Max

def test_valid_case_1():
    max1 = Max(5)
    max2 = Max(3)
    
    combined_max = max1.concat(max2)
    assert combined_max.value == 5

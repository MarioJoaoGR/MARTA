
import pytest
from pymonet.semigroups import Max  # Correctly specify the path to the module and class

def test_valid_case_2():
    max1 = Max(-5)
    max2 = Max(3)
    combined_max = max1.concat(max2)
    assert combined_max.value == 3
    
    another_max = Max(0)
    result = another_max.concat(combined_max)
    assert result.value == 3

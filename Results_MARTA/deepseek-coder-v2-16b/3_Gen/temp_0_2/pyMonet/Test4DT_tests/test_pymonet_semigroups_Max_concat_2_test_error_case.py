
import pytest
from pymonet.semigroups import Max

def test_concat():
    max1 = Max(-5)
    max2 = Max(3)
    combined_max = max1.concat(max2)  # The value of combined_max will be 3
    assert combined_max.value == 3
    
    another_max = Max(0)
    result = another_max.concat(combined_max)  # The value of result will still be 3, as it is the maximum between 0 and 3
    assert result.value == 3

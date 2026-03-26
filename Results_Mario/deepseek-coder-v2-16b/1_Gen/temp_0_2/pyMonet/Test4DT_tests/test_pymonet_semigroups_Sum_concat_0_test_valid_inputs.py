
import pytest
from pymonet.semigroups import Sum

def test_valid_inputs():
    sum1 = Sum(3)
    sum2 = Sum(4)
    
    result = sum1.concat(sum2)
    
    assert result.value == 7, "The concatenated value should be the sum of the two initial values."

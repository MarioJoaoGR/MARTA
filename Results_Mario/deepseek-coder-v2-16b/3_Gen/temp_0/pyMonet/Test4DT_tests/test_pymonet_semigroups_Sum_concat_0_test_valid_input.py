
import pytest
from pymonet.semigroups import Sum  # Assuming the correct module path is used

def test_valid_input():
    sum1 = Sum(3)
    sum2 = Sum(5)
    result = sum1.concat(sum2)
    assert result.value == 8

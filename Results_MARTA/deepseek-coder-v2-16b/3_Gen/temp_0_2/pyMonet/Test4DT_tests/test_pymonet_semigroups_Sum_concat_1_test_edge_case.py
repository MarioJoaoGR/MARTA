
import pytest
from pymonet.semigroups import Sum  # Assuming the module is correctly imported as 'pymonet'

def test_edge_case():
    sum1 = Sum(0)  # Instantiating with an integer 0
    sum2 = Sum(0)  # Instantiating with another integer 0
    result = sum1.concat(sum2)  # Adding the two sums together
    assert result.value == 0, f"Expected value: 0, but got {result.value}"

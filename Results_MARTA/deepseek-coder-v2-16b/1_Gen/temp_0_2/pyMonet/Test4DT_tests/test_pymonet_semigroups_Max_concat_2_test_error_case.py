
import pytest
from pymonet.semigroups import Max  # Assuming Max is in a submodule named semigroups

def test_error_case():
    max1 = Max(3)
    max2 = Max(7)
    
    combined = max1.concat(max2)
    
    assert combined.value == 7, "The combined value should be the larger of the two inputs."

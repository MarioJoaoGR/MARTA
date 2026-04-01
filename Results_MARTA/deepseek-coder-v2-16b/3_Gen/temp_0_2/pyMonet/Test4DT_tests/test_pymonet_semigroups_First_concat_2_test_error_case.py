
import pytest
from pymonet.semigroups import First  # Assuming this is the correct import path

def test_error_case():
    first1 = First(1)
    first2 = First(2)
    
    combined_first = first1.concat(first2)
    
    assert combined_first.value == 1, "Expected the value to be the same as the original instance"

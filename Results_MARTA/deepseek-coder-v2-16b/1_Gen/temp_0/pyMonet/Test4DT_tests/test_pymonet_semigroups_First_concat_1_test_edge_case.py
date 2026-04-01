
import pytest
from pymonet.semigroups import First

def test_edge_case():
    # Create two instances of First with different values
    first1 = First(1)
    first2 = First(2)
    
    # Combine the two instances using the concat method
    combined_first = first1.concat(first2)
    
    # Assert that the combined instance has the same value as the first one
    assert combined_first.value == 1

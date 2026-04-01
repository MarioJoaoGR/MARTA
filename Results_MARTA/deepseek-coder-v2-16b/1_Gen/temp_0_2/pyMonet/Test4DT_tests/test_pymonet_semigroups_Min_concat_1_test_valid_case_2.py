
import pytest
from pymonet.semigroups import Min, Semigroup

def test_valid_case_2():
    # Create an instance of Min with a specific value
    min_instance = Min(3)
    
    # Create another instance of Min with a different value
    other_min = Min(5)
    
    # Concatenate the two instances
    combined_min = min_instance.concat(other_min)
    
    # Assert that the concatenated result has the smallest value
    assert combined_min.value == 3

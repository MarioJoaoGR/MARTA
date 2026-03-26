
import pytest
from pymonet.semigroups import One

def test_error_case_type_mismatch():
    # Create an instance of One with True value
    one1 = One(True)
    
    # Create an instance of One with False value
    one2 = One(False)
    
    # Concatenate the two instances and check the result
    combined = one1.concat(one2)
    assert combined.value is True
    
    # Create another instance of One with False value
    another_one = One(False)
    
    # Concatenate with a False value and check the result
    combined_again = one2.concat(another_one)
    assert combined_again.value is False

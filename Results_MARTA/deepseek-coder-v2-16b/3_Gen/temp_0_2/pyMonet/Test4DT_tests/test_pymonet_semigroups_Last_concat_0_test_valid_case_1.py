
import pytest
from pymonet.semigroups import Last  # Assuming this is the correct module path

def test_valid_case_1():
    # Create two instances of Last with different values
    last1 = Last(10)
    last2 = Last(20)
    
    # Combine the two instances
    combined_last = last1.concat(last2)
    
    # Assert that the value of the combined instance is the latest value (20)
    assert combined_last.value == 20

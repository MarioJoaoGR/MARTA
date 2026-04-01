
import pytest
from pymonet.semigroups import First

def test_valid_input():
    # Create an instance of First with a valid value
    first_instance = First(5)
    
    # Check the string representation of the instance
    assert str(first_instance) == 'Fist[value=5]'

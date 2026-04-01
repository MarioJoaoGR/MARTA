
import pytest
from pymonet.semigroups import Last  # Assuming the correct import path is known or inferred from context

def test_valid_inputs():
    l1 = Last(5)
    assert l1.value == 5
    
    l2 = Last("hello")
    combined = l1.concat(l2)
    assert combined.value == "hello"
    
    # Adding another test to ensure the value is updated correctly with each concat
    l3 = Last(10)
    combined_again = combined.concat(l3)
    assert combined_again.value == 10

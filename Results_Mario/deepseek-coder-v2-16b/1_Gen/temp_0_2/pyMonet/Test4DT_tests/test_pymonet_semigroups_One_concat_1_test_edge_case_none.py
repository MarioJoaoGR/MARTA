
import pytest
from pymonet.semigroups import One

def test_edge_case_none():
    # Setup
    one1 = One(None)
    one2 = One(False)
    
    # Function call
    combined_one = one1.concat(one2)
    
    # Assertion
    assert combined_one.value is False

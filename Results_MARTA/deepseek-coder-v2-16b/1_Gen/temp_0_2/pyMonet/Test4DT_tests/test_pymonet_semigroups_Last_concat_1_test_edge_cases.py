
import pytest
from pymonet.semigroups import Last  # Assuming this is the correct module path

def test_last_concat():
    l1 = Last(5)
    l2 = Last("hello")
    
    combined = l1.concat(l2)
    
    assert combined.value == "hello"

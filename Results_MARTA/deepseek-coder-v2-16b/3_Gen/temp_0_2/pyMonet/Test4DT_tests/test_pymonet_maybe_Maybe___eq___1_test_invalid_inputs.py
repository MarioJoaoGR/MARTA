
import pytest
from pymonet.maybe import Maybe

def test_invalid_inputs():
    # Test equality with invalid inputs (non-Maybe objects)
    maybe = Maybe(value=42, is_nothing=False)
    
    assert not maybe == 1  # Comparing with an integer
    assert not maybe == "string"  # Comparing with a string
    assert not maybe == None  # Comparing with None
    assert not maybe == []  # Comparing with a list
    assert not maybe == {}  # Comparing with a dictionary

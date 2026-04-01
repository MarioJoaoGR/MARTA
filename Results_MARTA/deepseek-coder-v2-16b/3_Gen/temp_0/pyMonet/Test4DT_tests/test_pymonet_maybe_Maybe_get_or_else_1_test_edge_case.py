
import pytest
from pymonet.maybe import Maybe

def test_edge_case():
    # Test edge cases with None and empty values
    nothing = Maybe(value=None, is_nothing=True)
    assert nothing.get_or_else(0) == 0
    
    some = Maybe(value="Hello", is_nothing=False)
    assert some.get_or_else("World") == "Hello"

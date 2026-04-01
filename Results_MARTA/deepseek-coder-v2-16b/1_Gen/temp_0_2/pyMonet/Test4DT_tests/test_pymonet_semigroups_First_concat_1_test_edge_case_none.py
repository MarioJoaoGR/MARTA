
import pytest
from pymonet.semigroups import First

def test_edge_case_none():
    # Create an instance of First with a value of None
    f1 = First(None)
    
    # Try to concat another First instance (should not change the value)
    result = f1.concat(First("hello"))
    
    # Assert that the result is still None, as per the Monoid's behavior
    assert result.value == None

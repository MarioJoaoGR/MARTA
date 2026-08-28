
# Module: pymonet.semigroups
import pytest
from pymonet.semigroups import One

# Test initialization with different values
def test_initialization():
    one1 = One(False)
    assert one1.value == False
    
    one2 = One(True)
    assert one2.value == True
    
    # Initialize with a falsy value (0, "", [])
    one3 = One(0)
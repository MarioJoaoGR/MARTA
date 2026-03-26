
import pytest
from pymonet.semigroups import First

def test_edge_case_none():
    f1 = First(None)
    f2 = First(None)
    
    combined = f1.concat(f2)
    assert combined.value is None

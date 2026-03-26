
import pytest
from pymonet.semigroups import All

def test_valid_case_true_true():
    a = All(True)
    b = All(True)
    
    result = a.concat(b)
    
    assert result.value is True

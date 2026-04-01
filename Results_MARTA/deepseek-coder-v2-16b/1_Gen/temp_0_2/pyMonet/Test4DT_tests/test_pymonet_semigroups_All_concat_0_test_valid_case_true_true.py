
import pytest
from pymonet.semigroups import All

def test_valid_case_true_true():
    all_true = All(True)
    other_true = All(True)
    
    combined = all_true.concat(other_true)
    
    assert combined.value is True

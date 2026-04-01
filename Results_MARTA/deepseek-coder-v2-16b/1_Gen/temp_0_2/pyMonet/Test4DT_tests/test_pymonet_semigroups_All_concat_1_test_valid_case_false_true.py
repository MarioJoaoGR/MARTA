
import pytest
from pymonet.semigroups import All

def test_valid_case_false_true():
    all_false = All(False)
    other_true = All(True)
    
    combined = all_false.concat(other_true)
    assert combined.value == False

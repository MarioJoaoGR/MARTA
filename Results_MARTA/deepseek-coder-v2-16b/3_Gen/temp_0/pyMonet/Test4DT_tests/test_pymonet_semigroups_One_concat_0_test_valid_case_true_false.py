
import pytest
from pymonet.semigroups import One

def test_valid_case_true_false():
    one1 = One(True)
    one2 = One(False)
    
    combined = one1.concat(one2)
    assert combined.value is True
    
    another_one = One(False)
    combined_again = one2.concat(another_one)
    assert combined_again.value is False

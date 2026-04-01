
import pytest
from pymonet.semigroups import One

def test_valid_case_true_and_false():
    one1 = One(True)
    one2 = One(False)
    
    combined_one = one1.concat(one2)
    assert combined_one.value is True

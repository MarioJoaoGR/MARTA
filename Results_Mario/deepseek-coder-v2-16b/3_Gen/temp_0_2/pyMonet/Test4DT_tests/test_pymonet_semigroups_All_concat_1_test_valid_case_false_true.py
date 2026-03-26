
import pytest
from pymonet.semigroups import All

def test_valid_case_false_true():
    a = All(False)  # Initial value is False
    b = All(True)   # Another instance with initial value True
    
    result1 = a.concat(b)  # Combine a (False) with b (True)
    assert result1.value == False  # Expected result should be False
    
    result2 = b.concat(a)  # Combine b (True) with a (False)
    assert result2.value == False  # Expected result should be False

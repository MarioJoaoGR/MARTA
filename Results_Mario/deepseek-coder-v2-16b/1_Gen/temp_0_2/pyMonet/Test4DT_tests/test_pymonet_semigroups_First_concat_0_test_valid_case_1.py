
import pytest
from pymonet.semigroups import First  # Assuming this is the correct module path

def test_valid_case_1():
    f1 = First(1)
    f2 = First("hello")
    
    result = f1.concat(f2)
    
    assert isinstance(result, First)
    assert result.value == 1  # The value should remain the same as in f1

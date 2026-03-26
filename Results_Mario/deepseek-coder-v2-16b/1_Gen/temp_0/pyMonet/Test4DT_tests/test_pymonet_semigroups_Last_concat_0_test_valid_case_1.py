
import pytest
from pymonet.semigroups import Last

def test_valid_case_1():
    last1 = Last(10)
    last2 = Last('hello')
    
    combined_last = last1.concat(last2)
    
    assert combined_last.value == 'hello'

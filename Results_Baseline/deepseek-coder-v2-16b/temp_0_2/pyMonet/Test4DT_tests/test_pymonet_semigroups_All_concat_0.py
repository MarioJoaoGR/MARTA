
# Test case  

# Test case  
# Module: pymonet.semigroups
import pytest
from pymonet.semigroups import All

# Test initialization of All class with True and False values
def test_all_initialization():
    all_true = All(True)
    assert all_true.value is True
    
    all_false = All(False)
    assert all_false.value is False

# Test concatenation of All objects
def test_concatenation():
    all1 = All(True)
    all2 = All(False)
    combined_all = all1.concat(all2)
    assert combined_all.value is False
    
    another_all = All(True)
    combined_with_true = another_all.concat(All(True))
    assert combined_with_true.value is True

# Test concatenation with different types (should not affect the result)
def test_concatenation_different_types():
    all_int = All(1)  # Coerced to True because non-zero integer is considered True
    all_str = All("hello")  # Coerced to True because non-empty string is considered True
    combined_all = all_int.concat(all_str)
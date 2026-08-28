
import pytest
from pymonet.semigroups import One

# Test initialization with different values
def test_initialization():
    one1 = One(False)
    assert one1.value == False
    
    one2 = One(True)
    assert one2.value == True
    
    # Initialize with a falsy value (0, "", [])
    one3 = One(0)
    assert one3.value == 0

# Test concatenation with itself
def test_concat_with_itself():
    one1 = One(False)
    result = one1.concat(one1)
    assert result.value == False
    
    one2 = One(True)
    result = one2.concat(one2)
    assert result.value == True
    
    # Initialize with a truthy value (non-zero, non-empty string, list)
    one3 = One(1)
    result = one3.concat(one3)
    assert result.value == 1

# Test concatenation with another semigroup instance
def test_concat_with_another_instance():
    one1 = One(False)
    other = One(True)
    result = one1.concat(other)
    assert result.value == True
    
    # Initialize with a truthy value (non-zero, non-empty string, list)
    one2 = One(1)
    other = One(False)
    result = one2.concat(other)
    assert result.value == 1
    
    # Initialize with another falsy value
    one3 = One(0)
    other = One(True)
    result = one3.concat(other)
    assert result.value == True

# Test concatenation with a neutral element (All(False))
def test_concat_with_neutral_element():
    all_false = One(False)
    result = all_false.concat(One(True))
# Module: pymonet.semigroups
import pytest
from pymonet.semigroups import Min

# Test cases for the Min class
def test_min_initialization():
    min_instance = Min(5)
    assert min_instance.value == 5
    
    another_min_instance = Min(3.2)
    assert another_min_instance.value == 3.2

# Test case for the neutral element
def test_neutral_element():
    neutral_min = Min(float('inf'))
    assert neutral_min.concat(Min(10)).value == 10
    assert neutral_min.concat(Min(float('inf'))).value == float('inf')

# Test case for the concat method
def test_concat():
    min_instance = Min(5)
    another_min_instance = Min(3.2)
    
    combined_min = min_instance.concat(another_min_instance)
    assert combined_min.value == 3.2
    
    larger_min_instance = Min(10)
    combined_with_larger = min_instance.concat(larger_min_instance)
    assert combined_with_larger.value == 5

# Test case for the concat method with infinity neutral element
def test_concat_with_neutral_element():
    neutral_min = Min(float('inf'))
    another_min = Min(10)
    
    combined_result = neutral_min.concat(another_min)
    assert combined_result.value == 10

# Test case for the concat method with equal values
def test_concat_with_equal_values():
    min_instance = Min(5)
    another_min_instance = Min(5)
    
    combined_min = min_instance.concat(another_min_instance)
    assert combined_min.value == 5

# Test case for the concat method with negative values
def test_concat_with_negative_values():
    neg_min_instance = Min(-10)
    another_neg_min_instance = Min(-20)
    
    combined_neg_min = neg_min_instance.concat(another_neg_min_instance)
    assert combined_neg_min.value == -20

# Test case for the concat method with zero value
def test_concat_with_zero():
    min_instance = Min(0)
    another_min_instance = Min(-1)
    
    combined_min = min_instance.concat(another_min_instance)
    assert combined_min.value == -1

# Test case for the concat method with large values
def test_concat_with_large_values():
    large_min_instance = Min(float('inf'))
    another_large_min_instance = Min(float('inf'))
    
    combined_large_min = large_min_instance.concat(another_large_min_instance)
    assert combined_large_min.value == float('inf')

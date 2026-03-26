
# Module: pymonet.semigroups
import pytest
from pymonet.semigroups import Sum

# Test initialization of Sum class
def test_sum_initialization():
    sum1 = Sum(3)
    assert sum1.value == 3, "Initialization with value 3 should set the value to 3"
    
    sum2 = Sum(5)
    assert sum2.value == 5, "Initialization with value 5 should set the value to 5"

# Test concatenation of two Sum objects
def test_sum_concat():
    sum1 = Sum(3)
    sum2 = Sum(5)
    result = sum1.concat(sum2)
    assert result.value == 8, "Concatenation of 3 and 5 should result in a value of 8"
    
    # Additional test to ensure concatenation works with different values
    sum3 = Sum(7)
    sum4 = Sum(10)
    result2 = sum3.concat(sum4)
    assert result2.value == 17, "Concatenation of 7 and 10 should result in a value of 17"

# Test concatenation with neutral element (Sum object initialized with neutral_element)
def test_sum_concat_neutral():
    neutral = Sum(Sum.neutral_element)
    sum5 = Sum(3)
    result_with_neutral = sum5.concat(neutral)
    assert result_with_neutral.value == 3, "Concatenation with neutral element should return the original value"
    
    # Additional test to ensure concatenation works correctly when one of the operands is the neutral element
    result_with_neutral2 = neutral.concat(sum5)
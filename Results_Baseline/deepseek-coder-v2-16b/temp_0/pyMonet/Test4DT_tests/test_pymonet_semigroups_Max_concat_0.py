
import pytest
from pymonet.semigroups import Max

# Test cases for the Max class and its concat method
def test_max_concat():
    # Create two instances of Max with different values
    max1 = Max(5)
    max2 = Max(10)
    
    # Concatenate them and check if the result is correct
    combined_max = max1.concat(max2)
    assert combined_max.value == 10, "Expected the largest value to be taken"

def test_max_concat_with_negative_values():
    # Create two instances of Max with negative values
    max1 = Max(-5)
    max2 = Max(-10)
    
    # Concatenate them and check if the result is correct
    combined_max = max1.concat(max2)
    assert combined_max.value == -5, "Expected the largest value to be taken"

def test_max_concat_with_same_values():
    # Create two instances of Max with the same values
    max1 = Max(10)
    max2 = Max(10)
    
    # Concatenate them and check if the result is correct
    combined_max = max1.concat(max2)
    assert combined_max.value == 10, "Expected the largest value to be taken"

def test_max_concat_with_neutral_element():
    # Create an instance of Max with a neutral element
    max_neutral = Max(-float('inf'))
    
    # Concatenate it with another instance and check if the result is correct
    combined_max = max_neutral.concat(Max(10))
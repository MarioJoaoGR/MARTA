# Module: pymonet.semigroups
import pytest
from pymonet.semigroups import Min

# Test cases for the Min class
def test_min_concat():
    # Instantiating two Min instances with different values
    min1 = Min(3.0)
    min2 = Min(4.5)
    
    # Combining the two instances
    combined_min = min1.concat(min2)
    
    # Asserting that the combined value is the smallest of the two
    assert combined_min.value == 3.0

def test_min_concat_with_neutral_element():
    # Instantiating a Min instance with a value
    min1 = Min(5.0)
    
    # Combining with the neutral element (positive infinity)
    neutral_min = min1.concat(Min(float('inf')))
    
    # Asserting that the combined value remains unchanged
    assert neutral_min.value == 5.0

def test_min_concat_with_same_values():
    # Instantiating two Min instances with the same values
    min1 = Min(6.0)
    min2 = Min(6.0)
    
    # Combining the two instances
    combined_min = min1.concat(min2)
    
    # Asserting that the combined value is one of the original values (either can be chosen)
    assert combined_min.value in [6.0, float('inf')]  # Assuming concat returns either value if they are equal

def test_min_concat_with_negative_values():
    # Instantiating two Min instances with negative values
    min1 = Min(-3.0)
    min2 = Min(-4.5)
    
    # Combining the two instances
    combined_min = min1.concat(min2)
    
    # Asserting that the combined value is the smallest of the two negative values
    assert combined_min.value == -4.5

def test_min_concat_with_mixed_values():
    # Instantiating a Min instance with a positive value and another with a negative value
    min1 = Min(3.0)
    min2 = Min(-4.5)
    
    # Combining the two instances
    combined_min = min1.concat(min2)
    
    # Asserting that the combined value is the smallest of the mixed values
    assert combined_min.value == -4.5

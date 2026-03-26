
import pytest
from string_utils.generation import roman_range

def test_invalid_inputs():
    with pytest.raises(ValueError):
        list(roman_range(-1))  # Invalid stop value
    
    with pytest.raises(ValueError):
        list(roman_range(stop=-1, start=5))  # Invalid start value
    
    with pytest.raises(ValueError):
        list(roman_range(stop=5, start=1, step="invalid"))  # Invalid step value
    
    with pytest.raises(OverflowError):
        list(roman_range(start=3, stop=2))  # Step leads to no iteration

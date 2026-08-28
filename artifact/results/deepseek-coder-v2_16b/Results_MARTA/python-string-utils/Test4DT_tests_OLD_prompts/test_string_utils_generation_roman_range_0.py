
import pytest
from string_utils.generation import roman_range

# Test valid configuration
def test_valid_configuration():
    with pytest.raises(OverflowError):
        list(roman_range(start=1, stop=7, step=-1))  # This should raise OverflowError

# Test invalid start value
def test_invalid_start_value():
    with pytest.raises(ValueError):
        list(roman_range(start=0, stop=7, step=1))  # Invalid start value

# Test invalid stop value
def test_invalid_stop_value():
    with pytest.raises(ValueError):
        list(roman_range(start=1, stop=4000, step=1))  # Invalid stop value

# Test invalid step value
def test_invalid_step_value():
    with pytest.raises(ValueError):
        list(roman_range(start=1, stop=7, step=0))  # Invalid step value

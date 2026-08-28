# Module: ansible.utils.helpers
import pytest
from ansible.utils.helpers import pct_to_int

# Test cases for converting percentage to integer
def test_pct_to_int_percentage():
    assert pct_to_int("50%", 200) == 100
    assert pct_to_int("30%", 300) == 90

# Test cases for converting direct integer value
def test_pct_to_int_integer():
    assert pct_to_int(15, 100) == 15

# Test cases for handling invalid input (non-string with percent sign)
def test_pct_to_int_invalid_input():
    with pytest.raises(ValueError):
        pct_to_int("not a percentage", 200)

# Test cases for converting to integer with custom minimum value
def test_pct_to_int_min_value():
    assert pct_to_int("30%", 300, min_value=5) == 90
    assert pct_to_int(15, 100, min_value=5) == 5

# Additional test cases to cover edge cases and potential failures
def test_pct_to_int_edge_cases():
    # Test with percentage value that results in exactly the minimum value
    assert pct_to_int("1%", 100, min_value=2) == 2
    
    # Test with zero percentage value
    assert pct_to_int("0%", 100) == 0

# Negative test cases to ensure function behaves as expected for incorrect inputs
def test_pct_to_int_negative():
    # Ensure the function does not accept non-string percent values
    with pytest.raises(ValueError):
        pct_to_int("30", 300)
    
    # Ensure the function raises an error for invalid percentage formats
    with pytest.raises(ValueError):
        pct_to_int("thirty%", 300)

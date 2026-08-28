
import pytest
from ansible.utils.helpers import pct_to_int

# Test scenario 1: Valid case with integer input
def test_valid_case_integer_input():
    value = 50
    num_items = 200
    result = pct_to_int(value, num_items)
    assert result == 100

# Test scenario 2: Valid case with percentage string input
def test_valid_case_percentage_input():
    value = '30%'
    num_items = 300
    result = pct_to_int(value, num_items)
    assert result == 90

# Test scenario 3: Edge case with minimum value specified
def test_edge_case_minimum_value():
    value = 15
    num_items = 100
    min_value = 5
    result = pct_to_int(value, num_items, min_value)
    assert result == 5

# Test scenario 4: Error case with invalid input type
def test_error_case_invalid_input():
    value = 'not a number'
    num_items = 200
    with pytest.raises(ValueError):
        pct_to_int(value, num_items)


import pytest
from unittest.mock import patch

# Function to be tested
def curried_filter(filterer, collection):
    return [item for item in collection if filterer(item)]

# Test scenarios
def test_valid_input():
    def is_even(n):
        return n % 2 == 0
    
    result = curried_filter(is_even, [1, 2, 3, 4])
    assert result == [2, 4]

def test_edge_case_empty_list():
    result = curried_filter(None, [])
    assert result == []

def test_invalid_input():
    def non_callable():
        return 'not callable'
    
    with pytest.raises(TypeError):
        curried_filter(non_callable, [1, 2, 3, 4])


import pytest
from unittest.mock import patch
from flutils.objutils import is_list_like

# Test valid inputs that should return True for list-like behavior
def test_valid_inputs():
    with patch('flutils.objutils._LIST_LIKE', [list, tuple, set]):
        assert is_list_like([1, 2, 3]) == True
        assert is_list_like((1, 2, 3)) == True
        assert is_list_like({1, 2, 3}) == True

# Test edge cases including None, empty lists, and boundary values
def test_edge_cases():
    with patch('flutils.objutils._LIST_LIKE', [list, tuple, set]):
        assert is_list_like(None) == False
        assert is_list_like([]) == True  # Empty list is considered list-like
        assert is_list_like(()) == True  # Empty tuple is considered list-like
        assert is_list_like(set()) == True  # Empty set is considered list-like

# Test invalid inputs that should return False for list-like behavior
def test_invalid_inputs():
    with patch('flutils.objutils._LIST_LIKE', [list, tuple, set]):
        assert is_list_like("hello") == False
        assert is_list_like(123) == False
        assert is_list_like(True) == False

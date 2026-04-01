
import pytest
from unittest.mock import MagicMock
from pymonet.lazy import Lazy

def test_valid_input():
    # Create a mock function and instance of Lazy
    mock_fn = MagicMock()
    lazy_instance = Lazy(mock_fn)
    
    # Mock the fold method to return a specific value
    expected_value = "expected_result"
    lazy_instance.fold = MagicMock(return_value=expected_value)
    
    # Create another instance of Lazy with the same mock function
    other_lazy_instance = Lazy(mock_fn)
    other_lazy_instance.fold = MagicMock(return_value=expected_value)
    
    # Check if both instances are equal
    assert lazy_instance == other_lazy_instance

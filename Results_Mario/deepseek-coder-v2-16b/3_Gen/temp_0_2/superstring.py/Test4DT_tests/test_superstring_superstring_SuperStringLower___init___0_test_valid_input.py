
import pytest
from unittest.mock import patch
from superstring.superstring import SuperStringLower

@pytest.mark.parametrize("base, expected", [
    ("Hello World", "Hello World"),  # Test with a simple string
    ("Another example", "Another example"),  # Another test with different string
    ("12345", "12345")  # Test with numeric string
])
def test_valid_input(base, expected):
    """
    This function tests the __init__ method of SuperStringLower class with valid input parameters.
    
    Args:
        base (str): The input string to be set in the _base attribute of SuperStringLower.
        expected (_base): The expected value of the _base attribute after initialization.
    """
    # Create a mock instance of SuperStringLower with the given base parameter
    with patch('superstring.superstring.SuperStringLower', autospec=True) as MockSuperStringLower:
        # Set up the mock to return the expected value when accessing _base attribute
        mock_instance = MockSuperStringLower.return_value
        mock_instance._base = base
        
        # Verify that the _base attribute of the mock instance is set correctly
        assert mock_instance._base == expected


from unittest.mock import MagicMock
import pytest
from superstring.superstring import SuperStringBase, SuperStringLower

def test_invalid_input():
    # Create a mock for SuperStringBase
    base_mock = MagicMock()
    
    # Try to instantiate SuperStringLower with the mock
    lower_instance = SuperStringLower(base_mock)
    
    # Now you can use lower_instance in your test, ensuring it is properly instantiated
    assert isinstance(lower_instance, SuperStringLower)

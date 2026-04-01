
import pytest
from unittest.mock import MagicMock
from superstring.superstring import SuperStringSubstring

def test_character_at_0_edge_cases():
    # Create a mock for SuperStringBase
    base = MagicMock()
    base.character_at = MagicMock(return_value='H')
    
    # Create an instance of SuperStringSubstring
    substr = SuperStringSubstring(base, 0, 13)
    
    # Test the character at index 0
    assert substr.character_at(0) == 'H'

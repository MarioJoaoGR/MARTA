
import pytest
from unittest.mock import MagicMock
from superstring.superstring import SuperStringUpper  # Assuming this is the module path for SuperStringUpper

def test_character_at_edge_case():
    # Create a mock instance of SuperStringBase
    base = MagicMock()
    
    # Set up the mock to return a character at index 0 when character_at is called
    base.character_at.return_value = "H"
    
    # Instantiate SuperStringUpper with the mocked base
    upper_case_extractor = SuperStringUpper(base)
    
    # Call the method under test
    result = upper_case_extractor.character_at(0)
    
    # Assert that the character at index 0 is "H" in uppercase
    assert result == "H"

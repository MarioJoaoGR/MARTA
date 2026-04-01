
import pytest
from unittest.mock import MagicMock
from superstring.superstring import SuperStringUpper  # Assuming this is the correct module path

def test_edge_case():
    base_string = MagicMock()
    base_string.character_at = lambda index: "H" if index == 0 else ""
    
    upper_instance = SuperStringUpper(base_string)
    assert upper_instance.character_at(0) == "H"

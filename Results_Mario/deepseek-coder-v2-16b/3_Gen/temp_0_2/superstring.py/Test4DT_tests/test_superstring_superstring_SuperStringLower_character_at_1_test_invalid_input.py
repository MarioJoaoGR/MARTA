
import pytest
from unittest.mock import MagicMock
from superstring.superstring import SuperStringBase, SuperStringLower

def test_invalid_input():
    # Mocking SuperStringBase to avoid creating an actual instance during testing
    base_string = MagicMock()
    base_string.character_at = MagicMock(side_effect=IndexError("Invalid index"))
    
    with pytest.raises(IndexError):
        lower_instance = SuperStringLower(base_string)
        lower_instance.character_at(10)  # Attempt to access an invalid index

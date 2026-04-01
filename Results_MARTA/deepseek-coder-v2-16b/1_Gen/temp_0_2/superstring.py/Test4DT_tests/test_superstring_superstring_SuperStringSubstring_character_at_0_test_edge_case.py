
import pytest
from unittest.mock import MagicMock
from superstring.superstring import SuperStringBase  # Assuming this is the correct module path

# Assuming the class definition in the module looks something like this:
class SuperStringSubstring:
    def __init__(self, base, start_index, end_index):
        self._base = base
        self._start_index = start_index
        self._end_index = end_index

    def character_at(self, index):
        return self._base.character_at(self._start_index + index)

# Test case for the edge case where index is 0
def test_character_at_edge_case():
    # Create a mock SuperStringBase instance
    base = MagicMock()
    base.character_at = MagicMock(return_value='H')
    
    # Instantiate the SuperStringSubstring with the mocked base
    substring = SuperStringSubstring(base, 0, 1)
    
    # Call the character_at method with index 0
    result = substring.character_at(0)
    
    # Assert that the character at index 0 is 'H'
    assert result == 'H'
    
    # Optionally, you can add more assertions to ensure other conditions are met
    base.character_at.assert_called_with(0)

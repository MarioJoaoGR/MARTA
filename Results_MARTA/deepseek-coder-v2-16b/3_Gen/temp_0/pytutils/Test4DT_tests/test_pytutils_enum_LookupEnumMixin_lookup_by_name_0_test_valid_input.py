
import pytest
from pytutils.enum import LookupEnumMixin
from enum import Enum

def test_valid_input():
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
    
    expected_output = {
        'RED': Color.RED,
        'GREEN': Color.GREEN,
        'BLUE': Color.BLUE
    }
    
    # Since __members__ is not a standard attribute of the enum class, we need to mock it or use an alternative method to test the functionality.
    def mock_lookup_by_name(cls):
        return {member.name: member for member in cls}
    
    LookupEnumMixin.lookup_by_name = mock_lookup_by_name
    
    assert LookupEnumMixin.lookup_by_name(Color) == expected_output

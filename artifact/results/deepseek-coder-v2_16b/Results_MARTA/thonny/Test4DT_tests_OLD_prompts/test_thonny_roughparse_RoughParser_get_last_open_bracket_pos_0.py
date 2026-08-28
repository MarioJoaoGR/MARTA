
import pytest
from unittest.mock import patch
from thonny.roughparse import RoughParser

# Test for get_last_open_bracket_pos method
def test_RoughParser_get_last_open_bracket_pos_basic():
    # Create an instance of RoughParser with default settings
    parser = RoughParser(indent_width=4, tabwidth=4)
    
    # Mock the behavior of _study2 to always return None (no brackets found)
    with patch.object(RoughParser, '_study2', return_value=None):
        # Call get_last_open_bracket_pos and assert it returns None
        assert parser.get_last_open_bracket_pos() is None

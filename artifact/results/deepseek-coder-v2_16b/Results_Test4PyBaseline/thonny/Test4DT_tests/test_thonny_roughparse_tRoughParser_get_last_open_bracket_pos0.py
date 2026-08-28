
import pytest
from thonny.roughparse import RoughParser

# Test initialization of RoughParser with default values
def test_roughparser_initialization():
    parser = RoughParser(indent_width=4, tabwidth=4)
    assert parser.indent_width == 4
    assert parser.tabwidth == 4

# Test get_last_open_bracket_pos method with no open brackets in an empty string
def test_get_last_open_bracket_pos_empty_string():
    parser = RoughParser(indent_width=4, tabwidth=4)
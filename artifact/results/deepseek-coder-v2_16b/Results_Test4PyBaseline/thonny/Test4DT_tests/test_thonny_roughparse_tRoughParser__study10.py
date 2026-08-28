
import pytest
from thonny.roughparse import RoughParser, C_BACKSLASH, C_NONE

# Test initialization with typical values for indent_width and tabwidth
def test_RoughParser_init_typical():
    parser = RoughParser(indent_width=4, tabwidth=4)
    assert parser.indent_width == 4
    assert parser.tabwidth == 4

# Test initialization with different values for indent_width and tabwidth
def test_RoughParser_init_different():
    parser = RoughParser(indent_width=2, tabwidth=8)
    assert parser.indent_width == 2
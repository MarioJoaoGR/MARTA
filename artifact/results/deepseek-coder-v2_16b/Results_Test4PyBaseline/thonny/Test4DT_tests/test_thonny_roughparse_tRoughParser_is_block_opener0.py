
import pytest
from thonny.roughparse import RoughParser

# Test initialization with specific indentation and tab width settings
def test_init():
    parser = RoughParser(indent_width=4, tabwidth=4)
    assert parser.indent_width == 4
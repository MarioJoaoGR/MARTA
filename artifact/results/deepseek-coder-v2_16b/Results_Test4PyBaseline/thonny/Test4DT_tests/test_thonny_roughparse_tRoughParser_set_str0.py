
import pytest
from thonny.roughparse import RoughParser

# Test initialization with indent width and tab width
def test_initialization():
    parser = RoughParser(indent_width=4, tabwidth=4)
    assert parser.indent_width == 4
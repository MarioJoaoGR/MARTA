
# Module: thonny.roughparse
import pytest
from thonny.roughparse import RoughParser

# Test initialization with specific indent width and tab width
def test_roughparser_initialization():
    parser = RoughParser(indent_width=4, tabwidth=4)
    assert parser.indent_width == 4
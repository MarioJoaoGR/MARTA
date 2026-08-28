
import pytest
from thonny.roughparse import RoughParser

# Test initialization of RoughParser with default values
def test_RoughParser_initialization():
    parser = RoughParser(indent_width=4, tabwidth=4)
    assert parser.indent_width == 4
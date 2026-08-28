
import pytest
from thonny.roughparse import RoughParser

def test_valid_init():
    parser = RoughParser(indent_width=4, tabwidth=4)
    assert parser.indent_width == 4
    assert parser.tabwidth == 4




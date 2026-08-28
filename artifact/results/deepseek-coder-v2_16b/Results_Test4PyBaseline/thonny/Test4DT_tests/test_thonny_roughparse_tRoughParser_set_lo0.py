
# Module: thonny.roughparse
import pytest
from thonny.roughparse import RoughParser

# Test initialization with default values
def test_init_default():
    parser = RoughParser(indent_width=4, tabwidth=4)
    assert parser.indent_width == 4
    assert parser.tabwidth == 4

# Test initialization with different values
def test_init_different_values():
    parser = RoughParser(indent_width=2, tabwidth=8)
    assert parser.indent_width == 2
    assert parser.tabwidth == 8

# Test set_lo method with lo = 0
def test_set_lo_zero():
    parser = RoughParser(indent_width=4, tabwidth=4)
    parser.str = "test string"
    parser.set_lo(lo=0)
    assert parser.str == "test string"

# Test set_lo method with lo > 0 and previous character is newline
def test_set_lo_positive_with_newline():
    parser = RoughParser(indent_width=4, tabwidth=4)
    parser.str = "\ntest string"
    parser.set_lo(lo=1)
    assert parser.str == "test string"

# Test set_lo method with lo > 0 and previous character is not newline
def test_set_lo_positive_without_newline():
    parser = RoughParser(indent_width=4, tabwidth=4)
    parser.str = "test\nstring"
    parser.set_lo(lo=5)
    assert parser.str == "string"

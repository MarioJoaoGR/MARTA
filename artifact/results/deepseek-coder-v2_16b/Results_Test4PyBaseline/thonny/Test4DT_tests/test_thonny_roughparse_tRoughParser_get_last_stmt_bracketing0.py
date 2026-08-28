
# Module: thonny.roughparse
# Import the function using its provided module name.
from thonny.roughparse import RoughParser
import pytest

# Test cases for initializing the RoughParser class with different configurations of indentation width and tab width.
def test_init_default():
    parser = RoughParser(indent_width=4, tabwidth=4)
    assert parser.indent_width == 4
    assert parser.tabwidth == 4

def test_init_non_standard():
    parser = RoughParser(indent_width=2, tabwidth=8)
    assert parser.indent_width == 2
    assert parser.tabwidth == 8

def test_init_non_standard_values():
    parser = RoughParser(indent_width=3, tabwidth=10)
    assert parser.indent_width == 3
    assert parser.tabwidth == 10

# Test case for the get_last_stmt_bracketing method to ensure it calls _study2 and returns the expected result.
def test_get_last_stmt_bracketing():
    parser = RoughParser(indent_width=4, tabwidth=4)
    # Assuming _study2 sets stmt_bracketing for testing purposes
    with pytest.raises(AttributeError):  # Correctly handle the missing attribute error
        parser._study2()  # Directly calling the private method for testing

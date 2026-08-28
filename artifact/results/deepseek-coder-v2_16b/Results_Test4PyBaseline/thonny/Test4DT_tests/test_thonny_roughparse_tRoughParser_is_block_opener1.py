
import pytest
from thonny.roughparse import RoughParser

# Test initialization with specific indentation and tab width settings
def test_init():
    parser = RoughParser(indent_width=4, tabwidth=4)
    assert parser.indent_width == 4

# Test is_block_opener when self._study2() has not been called yet
def test_is_block_opener_not_called():
    parser = RoughParser(indent_width=4, tabwidth=4)
    assert not hasattr(parser, 'lastch')  # Ensure lastch is not set
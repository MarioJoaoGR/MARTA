
import pytest
from blib2to3.pgen2.tokenize import Untokenizer, Coord

# Test initialization of the Untokenizer class
def test_untokenizer_initialization():
    untokenizer = Untokenizer()
    assert untokenizer is not None
    assert untokenizer.tokens == []
    assert untokenizer.prev_row == 1
    assert untokenizer.prev_col == 0

# Test adding whitespace between tokens
def test_add_whitespace():
    untokenizer = Untokenizer()
    untokenizer.tokens = ['Hello', 'world']
    untokenizer.prev_row = 1
    untokenizer.prev_col = 0
    untokenizer.add_whitespace((1, 5))
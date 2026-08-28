
import pytest
from blib2to3.pgen2.tokenize import Untokenizer

# Test initialization of Untokenizer
def test_Untokenizer_initialization():
    untokenizer = Untokenizer()
    assert untokenizer.tokens == []
    assert untokenizer.prev_row == 1
    assert untokenizer.prev_col == 0

# Test adding whitespace at a valid position

# Test adding whitespace at an invalid position (should fail)